# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:41:40 2014

@author: hpelletier
"""
import os
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader, StripLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.clock import Clock
from FileManager import FileManager
from NetworkManager import NetworkManager
from Course_Item import Course_Item
from Proto5 import DragTab
from datastructures import User
import all_globals
#from dashNoKv import Dashboard

#fm = FileManager()
#user = fm.load_user('ihill','crashcourse')
#user.credits = {'
#fm.save_user(user)

search_temp_list = [] 

class StartUpScreen(Screen):
    def __init__(self,sm,**kwargs):   
        self.sm = sm
        super(StartUpScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.image = Image(source='logo1.png',allow_stretch=False,keep_ratio=True)
        Clock.schedule_once(self.transition,3)        
                
        self.add_widget(self.image)
                             
    def transition(self,instance):            
        self.sm.current = 'login'
        
class LogInScreen(BoxLayout,Screen):
    def __init__(self,sm,**kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        self.sm = sm

        self.orientation = 'vertical'

        self.username = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.username.add_widget(Label())
        self.username.add_widget(Label(text='Username:'))
        self.u_entry = TextInput(multiline=False)
        self.username.add_widget(self.u_entry)
        self.username.add_widget(Label())
        
        self.password = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.password.add_widget(Label())
        self.password.add_widget(Label(text='Password:'))  
        self.p_entry = TextInput(multiline=False,password=True)
        self.password.add_widget(self.p_entry)
        self.password.add_widget(Label())

        self.buttons = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.buttons.add_widget(Label())
        self.buttons.add_widget(Button(text='New User?',on_press=self.new_user_function))
        self.buttons.add_widget(Button(text='Log In',on_press=self.enter_function))
        self.buttons.add_widget(Label())
        
        self.offline = GridLayout (cols = 3, size_hint = (1.0,0.05))
        self.offline.add_widget(Label())
        self.offline_button = ToggleButton(text = 'Offline Mode')
        self.offline.add_widget(self.offline_button)
        self.offline.add_widget(Label())
            
        self.logo = Image(source='logo1.png',size_hint=(1.0,0.35))
        self.space1 = Label(size_hint=(1.0,0.175))
        self.space2 = Label(size_hint=(1.0,0.1))
        self.space3 = Label(size_hint=(1.0,0.05))
        self.space4 = Label(size_hint=(1.0,0.175))

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
        if self.offline_button.state == 'normal':
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

        else:
            print all_globals.user.name
            new_user = all_globals.fm.load_user(self.u_entry.text,self.p_entry.text)
            print new_user.name 

            all_globals.user = all_globals.fm.load_user(self.u_entry.text,self.p_entry.text)
            print all_globals.user.name
            print all_globals.user.credits['AHSE']
            #all_globals.user.credits={'ENGR':100,'AHSE':1000,'MTH':2,'SCI':2}
            all_globals.catalog = all_globals.fm.load_courses()
            if all_globals.catalog == None:
                self.space4.text = 'Login failed. No courses.csv file.'
            elif all_globals.user == None:
                self.space4.text = 'Login failed. Incorrect username or password for local user.'
            else:
                self.space4.text = 'Starting in Offline Mode.'
                self.sm.current = 'tabs'
        
        
class NewUserScreen(BoxLayout,Screen):
    def __init__(self,sm,**kwargs):
        super(NewUserScreen, self).__init__(**kwargs)
        self.sm = sm       
        self.orientation = 'vertical'    

        self.username = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.username.add_widget(Label())
        self.username.add_widget(Label(text='Please enter a username:'))
        self.u_entry = TextInput(multiline=False)
        self.username.add_widget(self.u_entry)
        self.username.add_widget(Label())
        
        self.password = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.password.add_widget(Label())
        self.password.add_widget(Label(text='Please enter a password:'))        
        self.p_entry = TextInput(multiline=False,password=True)
        self.password.add_widget(self.p_entry)
        self.password.add_widget(Label())

        self.buttons = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.buttons.add_widget(Label())
        self.buttons.add_widget(Button(text = 'Back',on_press = self.back_function))
        self.buttons.add_widget(Button(text = 'Create Account',on_press = self.enter_function))
        self.buttons.add_widget(Label())
            
        self.logo = Image(source='logo1.png',size_hint=(1.0,0.35))
        self.space1 = Label(size_hint=(1.0,0.175))
        self.space2 = Label(size_hint=(1.0,0.1))
        self.space3 = Label(size_hint=(1.0,0.05))        
        self.warning = Label(text='*WARNING*  Once you choose a username and password, they CAN NOT be changed!',size_hint=(1.0,0.175))
                        
        self.add_widget(self.space1)
        self.add_widget(self.logo)
        self.add_widget(self.space2)
        self.add_widget(self.username)       
        self.add_widget(self.password)
        self.add_widget(self.space3)
        self.add_widget(self.buttons)
        self.add_widget(self.warning)
        
    def back_function(self,instance):
        self.sm.current = 'login'

        
    def enter_function(self,instance):
        #add self.u_entry.text to file
        #add self.p_entry.text to file
        self.sm.current = 'tabs'        
      
        
class Dashboard(GridLayout):
    def __init__(self,**kwargs):
        super(Dashboard, self).__init__(**kwargs)

        ahse_cred = 0
        engr_cred = 0
        mth_cred = 0
        sci_cred = 0
        will_grad = 'No'

        self.cols = 2
        
        self.info = GridLayout(rows=5)
        self.info.add_widget(Label(text='Your Information',size_hint=(1.0,0.1)))
       
        self.years = BoxLayout(size_hint=(1.0,0.1))
        self.majors = BoxLayout(orientation='vertical',size_hint=(1.0,0.8))

        self.year1 = ToggleButton(text=str(2014),group='year')        
        self.year2 = ToggleButton(text=str(2015),group='year')   
        self.year3 = ToggleButton(text=str(2016),group='year')   
        self.year4 = ToggleButton(text=str(2017),group='year')
        self.years.add_widget(self.year1)
        self.years.add_widget(self.year2)   
        self.years.add_widget(self.year3)   
        self.years.add_widget(self.year4)
        self.info.add_widget(self.years) 
   
        self.ece = ToggleButton(text='ECE',group='major')
        self.meche = ToggleButton(text='Mech:E',group='major')
        self.roboe = ToggleButton(text='Robo:E',group='major')
        self.bioe = ToggleButton(text='Bio:E',group='major')
        self.edesign = ToggleButton(text='E:Design',group='major')
        self.ec = ToggleButton(text='E:C',group='major')
        self.syse = ToggleButton(text='E:Sys',group='major')
        self.ematsci = ToggleButton(text='E:MatSci',group='major')
        self.other = ToggleButton(text='Other',group='major')    
        self.majors.add_widget(self.ece)
        self.majors.add_widget(self.meche)
        self.majors.add_widget(self.roboe)
        self.majors.add_widget(self.bioe)
        self.majors.add_widget(self.edesign)
        self.majors.add_widget(self.ec)
        self.majors.add_widget(self.syse)
        self.majors.add_widget(self.ematsci)
        self.majors.add_widget(self.other)
        self.info.add_widget(self.majors)         
        
        self.reminders = GridLayout (rows=5)
        self.reminders.add_widget(Label(text='Reminders', size_hint=(1, .3)))
        self.reminders.add_widget(Label(text='Email Loretta Dinnon about 22 Credits', size_hint_y=None, height = 25))
        self.reminders.add_widget(Label())
        self.reminders.add_widget(Label())        
        
        self.stats = BoxLayout (orientation='vertical')
        self.information = GridLayout (cols = 2, size_hint = (1,.85))

        self.information.add_widget (Label(text='Graduate:' + will_grad))

        self.credits=GridLayout (cols=2, row=2)
        self.credits.add_widget (Label(text = 'AHSE: ' + str(ahse_cred)))
        self.credits.add_widget (Label(text = 'ENGR: ' + str(engr_cred)))
        self.credits.add_widget (Label(text = 'MTH: ' + str(mth_cred)))
        self.credits.add_widget (Label(text = 'SCI: ' + str(sci_cred)))
        
        self.information.add_widget (self.credits)
        
        self.stats.add_widget (Label (text = 'Statistics', size_hint =(1,.15)))
        self.stats.add_widget (self.information)        
        
        self.notes = GridLayout(cols=1)
        self.n_entry = TextInput(text=all_globals.user.notes, multiline=True)
        self.notes.add_widget(self.n_entry)
        
        self.add_widget(self.info)
        self.add_widget(self.reminders)
        self.add_widget(self.stats)
        self.add_widget(self.notes)

        Clock.schedule_interval(self.update_stats,0.1)

    def update_stats(self,instance):        
        ahse_cred = all_globals.user.credits['AHSE']         
        engr_cred = all_globals.user.credits['ENGR']
        mth_cred = all_globals.user.credits['MTH']
        sci_cred = all_globals.user.credits['SCI']
        if all_globals.user.credits['AHSE']+all_globals.user.credits['ENGR']+all_globals.user.credits['MTH']+all_globals.user.credits['SCI'] > 128:
            will_grad = 'Yes'
        else:
            will_grad = 'No'

        self.information.clear_widgets()
        self.information.add_widget (Label(text='Graduate: ' + will_grad))
        self.credits.clear_widgets()
        self.information.add_widget(self.credits)
        self.credits.add_widget (Label(text = 'AHSE: ' + str(ahse_cred)))
        self.credits.add_widget (Label(text = 'ENGR: ' + str(engr_cred)))
        self.credits.add_widget (Label(text = 'MTH: ' + str(mth_cred)))
        self.credits.add_widget (Label(text = 'SCI: ' + str(sci_cred)))

        if self.year1.state == 'down':
            all_globals.user.grad_year = int(self.year1.text)
        if self.year2.state == 'down':
            all_globals.user.grad_year = int(self.year2.text)
        if self.year3.state == 'down':
            all_globals.user.grad_year = int(self.year3.text)
        if self.year4.state == 'down':
            all_globals.user.grad_year = int(self.year4.text)
   
class Catalog(BoxLayout):
    def __init__(self,**kwargs):
        super(Catalog, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.search_bar = BoxLayout(size_hint=(1.0,0.05))        
        self.search_bar.add_widget(Label(text='Search',size_hint=(0.25,1.0)))
        self.search_text = (TextInput(multiline=False))
        self.search_bar.add_widget(self.search_text)

        self.filter_bar = BoxLayout(size_hint=(1.0,0.05))        
        self.AHSE = ToggleButton(text='AHSE',size_hint=(0.25,1.0))
        self.ENGR = ToggleButton(text='ENGR',size_hint=(0.25,1.0))
        self.MTH = ToggleButton(text='MTH',size_hint=(0.25,1.0))
        self.SCI = ToggleButton(text='SCI',size_hint=(0.25,1.0))        
        self.filter_bar.add_widget(self.AHSE)
        self.filter_bar.add_widget(self.ENGR)
        self.filter_bar.add_widget(self.MTH)
        self.filter_bar.add_widget(self.SCI)

        self.scrollview = ScrollView(size_hint=(1.0,0.9),size=(400,400))
        self.courses = StackLayout(spacing=5,size_hint_y=None)
        self.courses.bind(minimum_height=self.courses.setter('height'))

        self.scrollview.add_widget(self.courses)
                        
        self.add_widget(self.search_bar)
        self.add_widget(self.filter_bar)
        self.add_widget(self.scrollview)

        Clock.schedule_interval(self.search_function,0.1)    

    def search_function(self,instance):
        query = self.search_text.text.lower()        
        searched_items = []
        filtered_items = []

        #fills up the temp list the first time the function is called (copy of list of all courses)
        if len(search_temp_list) == 0:
            for course_item in self.courses.children:
                search_temp_list.append(course_item)       
        
        #if the query is not empty, does term search
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
    def __init__(self,**kwargs):
        super(Planner, self).__init__(**kwargs)

        
class TabsPanel(TabbedPanel):
    def __init__(self,**kwargs):
        super(TabsPanel, self).__init__(**kwargs)
        self.last_tab = None

        self.strip_image = 'strip_logo2.png'
        self.tab1 = TabbedPanelHeader(text='Dashboard')
        self.tab1.content = Dashboard()
        self.tab2 = TabbedPanelHeader(text='Catalog')
        self.tab2.content = Catalog()
        self.tab3 = TabbedPanelHeader(text='Planner')
        self.tab3.content = Planner()

        self.add_widget(self.tab1)
        self.add_widget(self.tab2)
        self.add_widget(self.tab3)     
        
        Clock.schedule_interval(self.populate,1)

    def populate(self,instance):
        
        if self.current_tab != self.last_tab and self.current_tab == self.tab2:
            self.tab2.content.courses.clear_widgets()
            print("changed to tab 2")
            for course_object in all_globals.catalog:
                course_item = Course_Item(course=course_object,size_hint=(0.245,None),height=200)
                self.tab2.content.courses.add_widget(course_item)

        self.last_tab = self.current_tab
    
class TabsScreen(Screen):
    def __init__(self,**kwargs):
        super(TabsScreen, self).__init__(**kwargs)  
        self.add_widget(TabsPanel(do_default_tab=False))
        
    
class CrashCourseApp(App):
    def build(self):
        sm = ScreenManager(transition = WipeTransition())
        sm.add_widget(StartUpScreen(sm,name='startup'))
        sm.add_widget(LogInScreen(sm,name='login'))
        sm.add_widget(NewUserScreen(sm,name='newuser'))
        sm.add_widget(TabsScreen(name='tabs'))
        return sm


if __name__ == '__main__': 
    CrashCourseApp().run()