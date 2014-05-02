# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:41:40 2014

@author: ihill, mborges, mkeene, hpelletier, sgrimshaw
"""
import os
import kivy
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader, StripLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.clock import Clock
from FileManager import FileManager
from NetworkManager import NetworkManager
from Course_Item import Course_Item
from Proto5_NoScroll import DragTab
from datastructures import User
from CreateCoursePopUp import Build_Course
from TabTextInput import TabTextInput
import all_globals


#new_user = User('hpelletier','crashcourse','Haley Pelletier',2017,'E:C',{'AHSE':0,'ENGR':0,'MTH':0,'SCI':0},[],'')
#all_globals.fm.save_user(new_user)

## Removes the multi-touch red dots ##
kivy.config.Config.set ('input', 'mouse', 'mouse,disable_multitouch')

search_temp_list = [] 


class StartUpScreen(Screen):
    """Screen that displays the logo for 3 seconds upon startup"""
    def __init__(self,sm,**kwargs):       
        super(StartUpScreen, self).__init__(**kwargs)
        self.sm = sm
        self.orientation = 'vertical'

        self.image = Image(source='logo1.png',allow_stretch=False,keep_ratio=True)
        Clock.schedule_once(self.transition,3)        
                
        self.add_widget(self.image)
                             
    def transition(self,instance):            
        self.sm.current = 'login'

        
class LogInScreen(BoxLayout,Screen):
    """Screen for user log-in"""   
    def __init__(self,sm,**kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        self.sm = sm
        self.orientation = 'vertical'

        ## Username ##
        self.username = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.username.add_widget(Label())
        self.username.add_widget(Label(text='Username:'))
        self.u_entry = TabTextInput(multiline=False)
        self.username.add_widget(self.u_entry)
        self.username.add_widget(Label())       
        
        ## Password ##
        self.password = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.password.add_widget(Label())
        self.password.add_widget(Label(text='Password:'))  
        self.p_entry = TabTextInput(multiline=False,password=True)
        self.password.add_widget(self.p_entry)
        self.password.add_widget(Label())

        ## Allow for Tabbing ##
        self.u_entry.set_next(self.p_entry)
        self.p_entry.set_next(self.u_entry)

        ## New User / Log In Buttons ##
        self.buttons = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.buttons.add_widget(Label())
        self.buttons.add_widget(Button(text='New User?',on_press=self.new_user_function))
        self.buttons.add_widget(Button(text='Log In',on_press=self.enter_function))
        self.buttons.add_widget(Label())

        ## Offline ##       
        self.offline = BoxLayout(size_hint = (1.0,0.05))        
        self.offline_label = Label(text='Offline Mode',size_hint=(0.15,1.0))
        self.offline_check = CheckBox(active=False,size_hint=(0.05,1.0))        
        self.offline.add_widget(Label(size_hint=(0.4,1.0)))
        self.offline.add_widget(self.offline_label)
        self.offline.add_widget(self.offline_check)
        self.offline.add_widget(Label(size_hint=(0.4,1.0)))
        
        ## Logo and Empy Space ##
        self.logo = Image(source='logo1.png',size_hint=(1.0,0.3))
        self.space1 = Label(size_hint=(1.0,0.175))
        self.space2 = Label(size_hint=(1.0,0.1))
        self.space3 = Label(size_hint=(1.0,0.05))
        self.space4 = Label(size_hint=(1.0,0.175))

        ## Add Widgets to Tab ##
        self.add_widget(self.space1)                
        self.add_widget(self.logo)
        self.add_widget(self.space2)
        self.add_widget(self.username)       
        self.add_widget(self.password)
        self.add_widget(self.space3)
        self.add_widget(self.buttons)
        self.add_widget(self.offline)
        self.add_widget(self.space4)
        
    def new_user_function(self,instance):
        self.sm.current = 'newuser'
        
    def enter_function(self,instance):
        """Determines if the user is able to log in and loads information for online or offline use"""
        ## Online Log-In: ##   
        if self.offline_check.active == False:
            self.space4.text = 'Connecting...'
            result = all_globals.nm.update(self.u_entry.text,self.p_entry.text)
            if result == 0:
                self.space4.text = 'No internet connection.'
                return
            elif result == -1:
                self.space4.text = 'User does not exist on server. Please create new user'
                return
            elif result == -3:
                self.space4.text = 'Connecting to server. Incorrect password.'
                return
            elif result == -4:
                self.space4.text = 'Lost internet connection while downloading new content.'
                return
            elif result == -5:
                self.space4.text = 'Lost internet connection while syncing user information.'
                return
            elif result == True:
                all_globals.user = all_globals.fm.load_user(self.u_entry.text,self.p_entry.text)                
                if all_globals.user != None:
                    all_globals.catalog = all_globals.fm.load_courses()
                    self.space4.text = 'All systems go!'
                    self.sm.current = 'tabs'
                else:
                    self.space4.text = 'Login failed. Incorrect username or password.'

        ## Offline Log-In: ##
        else:            
            all_globals.user = all_globals.fm.load_user(self.u_entry.text,self.p_entry.text)
            #print all_globals.user.name
            #print all_globals.user.credits['AHSE']            
            all_globals.catalog = all_globals.fm.load_courses()
            if all_globals.catalog == None:
                self.space4.text = 'Login failed. No courses.csv file.'
            elif all_globals.user == None:
                self.space4.text = 'Login failed. Incorrect username or password for local user.'
            else:
                self.space4.text = 'Starting in Offline Mode.'
                self.sm.current = 'tabs'
        
        
class NewUserScreen(BoxLayout,Screen):
    """Screen for new user creation"""
    def __init__(self,sm,**kwargs):
        super(NewUserScreen, self).__init__(**kwargs)
        self.sm = sm       
        self.orientation = 'vertical'    

        ## Username ##
        self.username = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.username.add_widget(Label())
        self.username.add_widget(Label(text='Please enter a username:'))
        self.u_entry = TabTextInput(multiline=False)
        self.username.add_widget(self.u_entry)
        self.username.add_widget(Label())
        
        ## Password ##
        self.password = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.password.add_widget(Label())
        self.password.add_widget(Label(text='Please enter a password:'))        
        self.p_entry = TabTextInput(multiline=False,password=True)
        self.password.add_widget(self.p_entry)
        self.password.add_widget(Label())

        ## Full Name ##
        self.fullname = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.fullname.add_widget(Label())
        self.fullname.add_widget(Label(text='Please enter your full name:'))        
        self.fullname_entry = TabTextInput(multiline=False)
        self.fullname.add_widget(self.fullname_entry)
        self.fullname.add_widget(Label())

        ## Allow for Tabbing ##
        self.u_entry.set_next(self.p_entry)
        self.p_entry.set_next(self.fullname_entry)
        self.fullname_entry.set_next(self.u_entry)

        ## Back / Create Account Buttons ##
        self.buttons = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.buttons.add_widget(Label())
        self.buttons.add_widget(Button(text = 'Back',on_press = self.back_function))
        self.buttons.add_widget(Button(text = 'Create Account',on_press = self.enter_function))
        self.buttons.add_widget(Label())
        
        ## Logo, Warning, and Empty Space ##    
        self.logo = Image(source='logo1.png',size_hint=(1.0,0.3))
        self.space1 = Label(size_hint=(1.0,0.175))
        self.space2 = Label(size_hint=(1.0,0.1))
        self.space3 = Label(size_hint=(1.0,0.05))        
        self.warning = Label(text='*WARNING*  Once you choose a username and password, they CAN NOT be changed!',size_hint=(1.0,0.175))
        
        ## Add Widgets to Tab ##
        self.add_widget(self.space1)
        self.add_widget(self.logo)
        self.add_widget(self.space2)
        self.add_widget(self.username)       
        self.add_widget(self.password)
        self.add_widget(self.fullname)
        self.add_widget(self.space3)
        self.add_widget(self.buttons)
        self.add_widget(self.warning)
        
    def back_function(self,instance):
        self.sm.current = 'login'
        
    def enter_function(self,instance):
        #TODO: create new user file with self.u_entry.text and self.p_entry.text and self.fullname_entry.text
        all_globals.user = User(self.u_entry.text,self.p_entry.text,self.fullname_entry.text,2017,'ECE',{'AHSE':0,'ENGR':0,'MTH':0,'SCI':0},None,'')
        try:
            all_globals.fm.save_user(all_globals.user)
            all_globals.nm.create_user(all_globals.user.username)
            self.sm.current = 'tabs'    
        except:
            self.warning.text = "User creation failed. Check your internet connection."
        else:
            self.warning.text = "User creation successful. Downloading the lastest course information."
            result = all_globals.nm.update(self.u_entry.text,self.p_entry.text)
            if result == True:
                all_globals.user = all_globals.fm.load_user(self.u_entry.text,self.p_entry.text)                
                if all_globals.user != None:
                    all_globals.catalog = all_globals.fm.load_courses()
                    self.warning.text = 'Download successful!'
                    self.sm.current = 'tabs'
                else:
                    self.warning.text = 'Download failed. Check your internet connection.'     
        
class Dashboard(BoxLayout):
    """Home tab that displays user statistics"""
    def __init__(self,**kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.ahse_cred = all_globals.user.credits['AHSE']         
        self.engr_cred = all_globals.user.credits['ENGR']
        self.mth_cred = all_globals.user.credits['MTH']
        self.sci_cred = all_globals.user.credits['SCI']
        ahse_req = 0
        engr_req = 0
        mth_req = 0
        sci_req = 0
        will_grad = 'No'

        ## USER INFORMATION HALF ##
        self.info = GridLayout(rows=5,size_hint=(0.475,1.0))

        # User's Name #
        self.display_name = Label(text=all_globals.user.name,size_hint=(1.0,0.05))

        # Grad Year #
        self.years = BoxLayout(size_hint=(1.0,0.15))

        year1 = BoxLayout(size_hint=(0.2,1.0))
        self.year1_check=CheckBox(active=False,group='year',size_hint=(0.1,1.0))
        self.year1_label = Label(text=str(2014),size_hint=(0.9,1.0))
        year1.add_widget(self.year1_label)
        year1.add_widget(self.year1_check)
        year2 = BoxLayout(size_hint=(0.2,1.0))
        self.year2_check=CheckBox(active=False,group='year',size_hint=(0.1,1.0))
        self.year2_label = Label(text=str(2015),size_hint=(0.9,1.0))
        year2.add_widget(self.year2_label)
        year2.add_widget(self.year2_check)
        year3 = BoxLayout(size_hint=(0.2,1.0))
        self.year3_check=CheckBox(active=False,group='year',size_hint=(0.1,1.0))
        self.year3_label = Label(text=str(2016),size_hint=(0.9,1.0))
        year3.add_widget(self.year3_label)
        year3.add_widget(self.year3_check)
        year4 = BoxLayout(size_hint=(0.2,1.0))
        self.year4_check=CheckBox(active=False,group='year',size_hint=(0.1,1.0))
        self.year4_label = Label(text=str(2017),size_hint=(0.9,1.0))
        year4.add_widget(self.year4_label)
        year4.add_widget(self.year4_check)

        self.years.add_widget(Label(size_hint=(0.1,1.0)))
        radio_buttons1=[year1,year2,year3,year4]        
        for button in radio_buttons1:
            self.years.add_widget(button)
        self.years.add_widget(Label(size_hint=(0.1,1.0)))
         
        # Major #  
        self.majors = GridLayout(cols=1,size_hint=(1.0,0.7))

        self.column1 = GridLayout(rows=5)
        ece = BoxLayout()
        self.ece_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.ece_label = Label(text='ECE',size_hint=(0.8,1.0))
        ece.add_widget(self.ece_label)
        ece.add_widget(self.ece_check)
        meche = BoxLayout()       
        self.meche_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.meche_label = Label(text='MechE',size_hint=(0.8,1.0))
        meche.add_widget(self.meche_label)
        meche.add_widget(self.meche_check)
        roboe = BoxLayout()       
        self.roboe_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.roboe_label = Label(text='E:Robo',size_hint=(0.8,1.0))
        roboe.add_widget(self.roboe_label)
        roboe.add_widget(self.roboe_check)
        bioe = BoxLayout()       
        self.bioe_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.bioe_label = Label(text='E:Bio',size_hint=(0.8,1.0))
        bioe.add_widget(self.bioe_label)
        bioe.add_widget(self.bioe_check)

        self.column2 = GridLayout(rows=5)
        designe = BoxLayout()       
        self.designe_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.designe_label = Label(text='E:Design',size_hint=(0.8,1.0))
        designe.add_widget(self.designe_label)
        designe.add_widget(self.designe_check)
        ec = BoxLayout()       
        self.ec_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.ec_label = Label(text='E:C',size_hint=(0.8,1.0))
        ec.add_widget(self.ec_label)
        ec.add_widget(self.ec_check)
        syse= BoxLayout()       
        self.syse_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.syse_label = Label(text='E:Sys',size_hint=(0.8,1.0))
        syse.add_widget(self.syse_label)
        syse.add_widget(self.syse_check)
        matscie = BoxLayout()       
        self.matscie_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.matscie_label = Label(text='E:MatSci',size_hint=(0.8,1.0))
        matscie.add_widget(self.matscie_label)
        matscie.add_widget(self.matscie_check)

        other = BoxLayout()
        self.other_check = CheckBox(active=False,group='majors',size_hint=(0.2,1.0))
        self.other_label = Label(text='Other',size_hint=(0.8,1.0))
        other.add_widget(self.other_label)
        other.add_widget(self.other_check)

        options=[ece, meche, roboe, bioe] 
        for choice in options:
            self.column1.add_widget(choice)
        self.majors.add_widget(self.column1)

        options=[designe, ec, syse, matscie, other]
        for choice in options:
            self.column2.add_widget(choice)
        self.majors.add_widget(self.column2)

        # Add Widgets to User Information Half #       
        self.info.add_widget(Label(text='Graduation Year & Major',font_size = 17,size_hint=(1.0,0.1)))
        self.info.add_widget(self.display_name)
        self.info.add_widget(self.years)
        self.info.add_widget(self.majors)
        

        ## BUFFER ##
        self.buffer = Label(size_hint=(0.05,1.0))         
        

        ## STATS AND NOTES HALF ##
        self.stats_and_notes = BoxLayout(orientation='vertical',size_hint=(0.475,1.0))

        # STATS QUADRANT # 
        self.stats = BoxLayout(orientation='vertical',size_hint=(1.0,0.5))
        # Stats #
        self.information = GridLayout(rows = 3, size_hint = (1,.75))
        self.grad = Label(text='Enough credits to graduate?:  ' + will_grad,size_hint=(1.0,0.15))        
        self.credits = GridLayout(cols=2,rows=2,size_hint=(1.0,0.7))        
        self.credits.add_widget(Label(text = 'AHSE: '+str(self.ahse_cred)+' / '+str(ahse_req)))        
        self.credits.add_widget(Label(text = 'ENGR: '+str(self.engr_cred)+' / '+str(engr_req)))        
        self.credits.add_widget(Label(text = 'MTH: '+str(self.mth_cred)+' / '+str(mth_req)))   
        self.credits.add_widget(Label(text = 'SCI: '+str(self.sci_cred)+' / '+str(sci_req)))
        buffer2 = Label(size_hint=(1.0,0.15))   
        self.information.add_widget(self.credits)
        self.information.add_widget(self.grad)      
        self.information.add_widget(buffer2)
        # Export and Save Buttons #
        self.options_bar = BoxLayout(size_hint=(1.0,0.1))        
        self.export_button = Button(text='Export to Spreadsheet',on_press=self.export_user_info)
        self.save_button = Button(text='Save User Information',on_press=self.save_user_info)
        self.options_bar.add_widget(self.export_button)
        self.options_bar.add_widget(self.save_button)
        # Add Widgets to Quadrant #
        self.stats.add_widget(self.options_bar)
        self.stats.add_widget(Label(text = 'Stats',font_size = 17,size_hint =(1,.15)))
        self.stats.add_widget(self.information)
        
        # NOTES QUADRANT #        
        self.notes = GridLayout(cols=1,size_hint =(1.0,0.5))
        self.n_label = Label(text='Notes',font_size = 17,size_hint = (1.0,0.15))        
        self.n_entry = TextInput(text=all_globals.user.notes,multiline=True,padding=15,size_hint=(1.0,0.85))              
        self.notes.add_widget(self.n_label)      
        self.notes.add_widget(self.n_entry)

        # Add Stats and Notes to Half #
        self.stats_and_notes.add_widget(self.stats)
        self.stats_and_notes.add_widget(self.notes)


        ## Add Halves to Home Tab ##
        self.add_widget(self.info)
        self.add_widget(self.buffer)
        self.add_widget(self.stats_and_notes)       

        Clock.schedule_interval(self.update_stats,0.1)

    def update_stats(self,instance):
        """Updates the information displayed on the Home tab and saves info to the user file"""      

        ahse_cred = all_globals.user.credits['AHSE']         
        engr_cred = all_globals.user.credits['ENGR']
        mth_cred = all_globals.user.credits['MTH']
        sci_cred = all_globals.user.credits['SCI']
        ahse_req = 0
        engr_req = 0
        mth_req = 0
        sci_req = 0             

        ## Determine required credits to be displayed based on chosen major and add major to user file ##
        if self.ece_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.ece_label.text
        if self.meche_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.meche_label.text
        if self.roboe_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.roboe_label.text
        if self.bioe_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.bioe_label.text
        if self.designe_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.designe_label.text
        if self.ec_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.ec_label.text
        if self.syse_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.syse_label.text
        if self.matscie_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.matscie_label.text
        if self.other_check.active == True:
            ahse_req = 28
            engr_req = 28
            mth_req = 28
            sci_req = 28
            all_globals.user.major = self.other_label.text

        ## Determine if user has enough credits to graduate ##
        if ahse_cred >= ahse_req and engr_cred >= engr_req and mth_cred >= mth_req and sci_cred >= sci_req:
            will_grad = 'Yes'
        else:
            will_grad = 'No' 

        ## Update the displayed credits & name ##
        self.grad.clear_widgets()
        self.grad = Label(text='Enough credits to graduate?:  ' + will_grad)
        self.credits.clear_widgets()
        self.credits.add_widget (Label(text = 'AHSE: '+str(ahse_cred)+' / '+str(ahse_req)))
        self.credits.add_widget (Label(text = 'ENGR: '+str(engr_cred)+' / '+str(engr_req)))
        self.credits.add_widget (Label(text = 'MTH: '+str(mth_cred)+' / '+str(mth_req)))
        self.credits.add_widget (Label(text = 'SCI: '+str(sci_cred)+' / '+str(sci_req)))
        self.display_name.text = all_globals.user.name
       
        ## Add grad year to user file ##
        if self.year1_check.active == True:
            all_globals.user.grad_year = int(self.year1_label.text)
        if self.year2_check.active == True:
            all_globals.user.grad_year = int(self.year2_label.text)
        if self.year3_check.active == True:
            all_globals.user.grad_year = int(self.year3_label.text)
        if self.year4_check.active == True:
            all_globals.user.grad_year = int(self.year4_label.text)

        ## Add notes to user file ##
        all_globals.user.notes=self.n_entry.text       

    def save_user_info(self,instance):
        #print 'User info saved!'
        all_globals.fm.save_user(all_globals.user)

    def export_user_info(self,instance):
        #print 'User info exported!'
        all_globals.fm.export_user(all_globals.user)
   

class Catalog(BoxLayout):
    """Tab that displays available courses and allows user to search for, see details about, and add courses to planner tab"""
    def __init__(self,sm,**kwargs):
        super(Catalog,self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.sm = sm

        ## Search Bar ##
        self.search_bar = BoxLayout(size_hint=(1.0,0.05))
        self.search_text = TextInput(multiline=False,size_hint =(0.6,1.0))
        self.create_course_popup = Build_Course(self.sm)
        self.create_course_button = Button(text='Create a Course',size_hint=(0.2,1.0),on_press=self.create_course_popup.open_pop_up)        
        self.search_bar.add_widget(Label(text='Search',size_hint=(0.2,1.0)))
        self.search_bar.add_widget(self.search_text)
        self.search_bar.add_widget(self.create_course_button)

        ## Filter Buttons ##
        self.filter_bar = BoxLayout(size_hint=(1.0,0.05))        
        self.AHSE = ToggleButton(text='AHSE',size_hint=(0.25,1.0))
        self.ENGR = ToggleButton(text='ENGR',size_hint=(0.25,1.0))
        self.MTH = ToggleButton(text='MTH',size_hint=(0.25,1.0))
        self.SCI = ToggleButton(text='SCI',size_hint=(0.25,1.0))        
        self.filter_bar.add_widget(self.AHSE)
        self.filter_bar.add_widget(self.ENGR)
        self.filter_bar.add_widget(self.MTH)
        self.filter_bar.add_widget(self.SCI)

        ## Scrollview of Courses ##
        self.scrollview = ScrollView(size_hint=(1.0,0.9),size=(400,400),scroll_timeout=5)
        self.courses = StackLayout(spacing=5,size_hint_y=None)
        self.courses.bind(minimum_height=self.courses.setter('height'))
        self.scrollview.add_widget(self.courses)
        
        ## Add Widgets to Tab ##
        self.add_widget(self.search_bar)
        self.add_widget(self.filter_bar)
        self.add_widget(self.scrollview)

        Clock.schedule_interval(self.search_function,0.1)    

    def search_function(self,instance):
        """Allows user to search for courses by name, keyword, professor, or course code and filter courses by type"""
        query = self.search_text.text.lower()        
        searched_items = []
        filtered_items = []

        #fills up the temp list the first time the function is called (copy of list of all courses)
        if len(search_temp_list) == 0:
            for course_item in self.courses.children:
                search_temp_list.append(course_item)       
        
        #if the query is not empty, does term search first
        if query != "":                      
            for course_item in search_temp_list:                            
                if query == course_item.course.name.lower() or query == course_item.course.code or query == course_item.course.prof.lower():
                    searched_items.append(course_item)
                for keyword in course_item.course.keywords:
                    if query == keyword.lower():                        
                        searched_items.append(course_item)

        #if the query is empty, searched courses = all courses
        else:
            searched_items = search_temp_list
        
        #if none of the buttons are down, keep all searched courses
        if self.AHSE.state == 'normal' and self.ENGR.state == 'normal' and self.MTH.state == 'normal' and self.SCI.state == 'normal':
            filtered_items = searched_items

        #if a button is down, shows only courses in that category (holding multiple buttons shows more courses)
        else:                                
            if self.AHSE.state == 'down':
                for course_item in searched_items:                   
                    if course_item.course.credits['AHSE'] > 0:                                                  
                        filtered_items.append(course_item)
            if self.ENGR.state == 'down': 
                for course_item in searched_items:                      
                    if course_item.course.credits['ENGR'] > 0 and course_item not in filtered_items:                                                  
                        filtered_items.append(course_item)
            if self.MTH.state == 'down':                          
                for course_item in searched_items:
                    if course_item.course.credits['MTH'] > 0 and course_item not in filtered_items:                                                 
                        filtered_items.append(course_item)
            if self.SCI.state == 'down':
                for course_item in searched_items:                   
                    if course_item.course.credits['SCI'] > 0 and course_item not in filtered_items:                                             
                        filtered_items.append(course_item)

        if len(self.courses.children) != len(filtered_items):
            self.courses.clear_widgets()
            for course_item in filtered_items:
                self.courses.add_widget(course_item) 


class Planner(DragTab):
    """Tab that allows user to arrange courses in semesters and plan their four years at Olin"""
    def __init__(self,**kwargs):
        super(Planner, self).__init__(**kwargs)

        
class TabsPanel(TabbedPanel):
    """Panel that holds the tab widgets"""
    def __init__(self,sm,**kwargs):
        super(TabsPanel, self).__init__(**kwargs)
        self.sm = sm
        self.last_tab = None

        self.strip_image = 'strip_logo2.png'  #Logo in the top right of the tabs

        ## Define the Tabs ##
        self.tab1 = TabbedPanelHeader(text='Home')
        self.tab1.content = Dashboard()
        self.tab2 = TabbedPanelHeader(text='Catalog')
        self.tab2.content = Catalog(self.sm)
        self.tab3 = TabbedPanelHeader(text='Planner')
        self.tab3.content = Planner()

        ## Add the Tabs to the Panel ##
        self.add_widget(self.tab1)
        self.add_widget(self.tab2)
        self.add_widget(self.tab3)
        
        Clock.schedule_interval(self.load,0.5)

    def load(self,instance):
        """Fills the App with Information from the user file and loads the courses"""
        ## Loads the Courses into Catalog Tab ##
        if self.current_tab != self.last_tab and self.current_tab == self.tab2:
            self.tab2.content.courses.clear_widgets()            
            for course_object in all_globals.catalog:
                course_item = Course_Item(course=course_object,size_hint=(0.245,None),height=200)
                self.tab2.content.courses.add_widget(course_item) 

        # Loads User Information into the Home Tab ##
        if self.current_tab != self.last_tab and self.current_tab == self.tab1: 

            # Loads Notes #           
            self.tab1.content.n_entry.text = all_globals.user.notes
 
            # Loads Credits #
            self.tab1.content.ahse_cred = all_globals.user.credits['AHSE']
            self.tab1.content.engr_cred = all_globals.user.credits['ENGR']
            self.tab1.content.mth_cred = all_globals.user.credits['MTH']
            self.tab1.content.sci_cred = all_globals.user.credits['SCI']
            
            # Loads Grad Year #
            if str(all_globals.user.grad_year) == '2014':
                self.tab1.content.year1_check.active = True
            if str(all_globals.user.grad_year) == '2015':
                self.tab1.content.year2_check.active = True
            if str(all_globals.user.grad_year) == '2016':
                self.tab1.content.year3_check.active = True
            if str(all_globals.user.grad_year) == '2017':
                self.tab1.content.year4_check.active = True
 
            # Loads Major #
            if str(all_globals.user.major) == 'ECE':
                self.tab1.content.ece_check.active = True
            if str(all_globals.user.major) == 'Meche':
                self.tab1.content.meche_check.active = True
            if str(all_globals.user.major) == 'E:Robo':
                self.tab1.content.roboe_check.active = True
            if str(all_globals.user.major) == 'E:Design':
                self.tab1.content.designe_check.active = True
            if str(all_globals.user.major) == 'E:C':
                self.tab1.content.ec_check.active = True
            if str(all_globals.user.major) == 'E:Sys':
                self.tab1.content.syse_check.active = True
            if str(all_globals.user.major) == 'E:Bio':
                self.tab1.content.bioe_check.active = True
            if str(all_globals.user.major) == 'E:Matsci':
                self.tab1.content.matscie_check.active = True
            if str(all_globals.user.major) == 'Other':
                self.tab1.content.other_check.active = True

        ##Loads User info on Planner Tab
        self.tab3.content.Load_Users_Plan()

        self.last_tab = self.current_tab

class TabsScreen(Screen):
    """Screen that holds the Tabs Panel"""
    def __init__(self,sm,**kwargs):
        super(TabsScreen, self).__init__(**kwargs)
        self.sm = sm
        self.tabspanel = TabsPanel(sm,do_default_tab=False)
        self.add_widget(self.tabspanel)
        
    
class CrashCourseApp(App):
    """The entire CrashCourse app"""
    def build(self):
        """Builds the app when the app is run"""
        ## Define the screen manager (base of the app) ##
        sm = ScreenManager(transition = WipeTransition())

        ## Add screens to the screen manager ##
        sm.startup=StartUpScreen(sm,name='startup')
        sm.add_widget(sm.startup)
        sm.login=LogInScreen(sm,name='login')
        sm.add_widget(sm.login)
        sm.newuser=NewUserScreen(sm,name='newuser')
        sm.add_widget(sm.newuser)
        sm.tabs=TabsScreen(sm,name='tabs')
        sm.add_widget(sm.tabs)

        return sm


if __name__ == '__main__':
    CrashCourseApp().run()