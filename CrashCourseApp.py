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
from kivy.uix.dropdown import DropDown
from Proto3_5_stable import DragTab
from datastructures import User
#from dashNoKv import Dashboard


favorite_courses = []
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
    def __init__(self,sm,user,fm,nm,catalog,**kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        self.sm = sm
        self.user = user
        self.fm = fm
        self.nm = nm
        self.catalog = catalog
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
        self.add_widget(self.space4)
        
    def new_user_function(self,instance):
        self.sm.current = 'newuser'
        
    def enter_function(self,instance):
        self.space4.text = 'Connecting...'
        result = self.nm.update(self.u_entry.text,self.p_entry.text)
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
            self.fm.load_courses()
            self.user = self.fm.load_user()
            self.catalog = self.fm.load_courses()
            self.space4.text = 'All systems go!'
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
    def __init__(self,user,**kwargs):
        super(Dashboard, self).__init__(**kwargs)
        self.user = user
        self.cols = 2
        
        self.info = GridLayout (rows=5)
        self.info.add_widget(Label(text='Your Information'))
        grad_dropdown = DropDown()
        for x in ('2014','2015','2016','2017'):
            btn = Button(text=x, size_hint_y=None, height=20)
            # Underneath attaches the text of the button to the variable btn.text
            btn.bind(on_release=lambda btn: grad_dropdown.select(btn.text))
            grad_dropdown.add_widget(btn)
        mainbutton_gradYear = Button(text='Grad Year', size_hint_y=None, height=25)
        mainbutton_gradYear.bind(on_release=grad_dropdown.open)
        grad_dropdown.bind(on_select=lambda instance, x: setattr(mainbutton_gradYear, 'text', x))
        self.info.add_widget (mainbutton_gradYear)
        
        maj_dropdown = DropDown()
        for x in ('ECE','MechE','RoboE','E:Design','E:C','Sys:E','E:MatSci'):
            btn = Button(text=x, size_hint_y=None, height=20)
            # Underneath attaches the text of the button to the variable btn.text
            btn.bind(on_release=lambda btn: maj_dropdown.select(btn.text))
            maj_dropdown.add_widget(btn)
        mainbutton_major = Button(text='Major', size_hint_y=None, height=25)
        mainbutton_major.bind(on_release=maj_dropdown.open)
        maj_dropdown.bind(on_select=lambda instance, x: setattr(mainbutton_major, 'text', x))
        self.info.add_widget (mainbutton_major)
        self.info.add_widget(Label())
        self.info.add_widget(Label())        
        
        self.reminders = GridLayout (rows=5)
        self.reminders.add_widget(Label(text='Reminders'))
        self.reminders.add_widget(Button(text='Email Loretta Lynn about 22 Credits', size_hint_y=None, height = 25))
        self.reminders.add_widget(Label())
        self.reminders.add_widget(Label())        
        
        self.stats = BoxLayout (orientation='vertical')
        self.information = GridLayout (cols = 2, size_hint = (1,.7))
        self.information.add_widget (Label(text='Graduate:' + ' Yes!'))
        self.credits=GridLayout (cols=2, row=2)
        self.credits.add_widget (Label(text = 'AHS: ' + '12'))
        self.credits.add_widget (Label(text = 'ENGR: ' + '12'))
        self.credits.add_widget (Label(text = 'MTH: ' + '12'))
        self.credits.add_widget (Label(text = 'SCI: ' + '12'))
        
        self.information.add_widget (self.credits)
        
        self.stats.add_widget (Label (text = 'Statistics', size_hint =(1,.3)))
        self.stats.add_widget (self.information)
        
        
        self.notes = GridLayout(cols=1)
        self.n_entry = TextInput(text=self.user.notes, multiline=True)
        self.notes.add_widget(self.n_entry)
        
        
        self.add_widget(self.info)
        self.add_widget(self.reminders)
        self.add_widget(self.stats)
        self.add_widget(self.notes)
        
        
class Catalog(BoxLayout):
    def __init__(self,catalog,**kwargs):
        super(Catalog, self).__init__(**kwargs)
        self.catalog = catalog

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
        for course_object in self.catalog:
            course_item = Course_Item(course=course_object,size_hint=(0.245,None),height=200)                             
            self.courses.add_widget(course_item)
        self.scrollview.add_widget(self.courses)
                        
        self.add_widget(self.search_bar)
        self.add_widget(self.filter_bar)
        self.add_widget(self.scrollview)

        Clock.schedule_interval(self.update_favorites,0.1)
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

    def update_favorites(self,instance):        
        for course_item in self.courses.children:
            if course_item.favorite.state == 'normal' and course_item.course in favorite_courses:
                favorite_courses.remove(course_item.course)
            if course_item.favorite.state == 'down' and course_item.course not in favorite_courses:
                favorite_courses.append(course_item.course)                
        

class Planner(DragTab):
    def __init__(self,**kwargs):
        super(Planner, self).__init__(**kwargs)

        self.favorites = []        
        Clock.schedule_interval(self.update_favorites,0.1) 
        
    def update_favorites(self,instance):
        if len(favorite_courses) == len(self.favorites):
            return
        if len(favorite_courses) < len(self.favorites):
            self.favorites = []
            self.Scrollhome.clear_widgets()           
        for course in favorite_courses:
            if course not in self.favorites:
                self.favorites.append(course)
                self.add_Icon(course)
        
        
class Schedule(BoxLayout):
    def __init__(self,**kwargs):
        super(Schedule, self).__init__(**kwargs)

        self.mon = Label(text= 'Mon')
        self.tue = Label(text= 'Tue')
        self.wed = Label(text= 'Wed')
        self.thu = Label(text= 'Thu')
        self.fri = Label(text= 'Fri')       
        
        self.add_widget(self.mon)
        self.add_widget(self.tue)
        self.add_widget(self.wed)
        self.add_widget(self.thu)
        self.add_widget(self.fri)

        
class TabsPanel(TabbedPanel):
    def __init__(self,user,fm,catalog,**kwargs):
        super(TabsPanel, self).__init__(**kwargs)
        self.user = user
        self.fm = fm
        self.catalog = catalog

        self.strip_image = 'strip_logo2.png'
        self.tab1 = TabbedPanelHeader(text='Dashboard')
        self.tab1.content = Dashboard(self.user)
        self.tab2 = TabbedPanelHeader(text='Catalog')
        self.tab2.content = Catalog(self.catalog)
        self.tab3 = TabbedPanelHeader(text='Planner')
        self.tab3.content = Planner()
        self.tab4 = TabbedPanelHeader(text='Schedule')
        self.tab4.content = Schedule()        
        
        self.add_widget(self.tab1)
        self.add_widget(self.tab2)
        self.add_widget(self.tab3)
        self.add_widget(self.tab4)
        
    
class TabsScreen(Screen):
    def __init__(self,user,fm,catalog,**kwargs):
        super(TabsScreen, self).__init__(**kwargs)  
        self.user = user   
        self.fm = fm   
        self.catalog = catalog
        self.add_widget(TabsPanel(self.user,self.fm,self.catalog,do_default_tab=False))
        
    
class CrashCourseApp(App):
    def build(self):
        fm = FileManager()
        nm = NetworkManager()
        catalog = []
        profs = []
        user = User('noone','crashcourse','No One',2017,'E:C',{'ENGR':0, 'AHSE':0,'MTH':2,'SCI':2},[],"")
        sm = ScreenManager(transition = WipeTransition())
        sm.add_widget(StartUpScreen(sm,name='startup'))
        sm.add_widget(LogInScreen(sm,user,fm,nm,catalog,name='login'))
        sm.add_widget(NewUserScreen(sm,name='newuser'))
        sm.add_widget(TabsScreen(user,fm,catalog,name='tabs'))
        return sm


if __name__ == '__main__':
    CrashCourseApp().run()