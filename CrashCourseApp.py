# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:41:40 2014

@author: hpelletier
"""

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader, StripLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.clock import Clock
from FileManager import FileManager
from Course_Item import Course_Item


fm = FileManager()
catalog = fm.load_courses()  

class StartUpScreen(Screen):
    def __init__(self,**kwargs):        
        super(StartUpScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.image = Image(source='logo1.png',allow_stretch=False,keep_ratio=True)
        Clock.schedule_once(self.transition,5)        
                
        self.add_widget(self.image)
                             
    def transition(self,instance):            
        sm.current = 'login'
        
class LogInScreen(BoxLayout,Screen):
    def __init__(self,**kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.username = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.username.add_widget(Label())
        self.username.add_widget(Label(text='Username:'))
        self.u_entry = TextInput(multiline = False)
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
        self.buttons.add_widget(Button(text = 'New User?',on_press = self.new_user_function))
        self.buttons.add_widget(Button(text = 'Log In',on_press = self.enter_function))
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
        sm.current = 'newuser'
        
    def enter_function(self,instance):
        if self.u_entry.text != 'Username' and self.p_entry.text != 'Password':
            self.space4.text = 'Username and password incorrect. Please try again.'
        elif self.u_entry.text != 'Username':
            self.space4.text = 'Username incorrect. Please try again.'
        elif self.p_entry.text != 'Password':
            self.space4.text = 'Password incorrect. Please try again.'        
        else:
            sm.current = 'tabs'
        
        
class NewUserScreen(BoxLayout,Screen):
    def __init__(self,**kwargs):
        super(NewUserScreen, self).__init__(**kwargs)        
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
        sm.current = 'login'
        
    def enter_function(self,instance):
        #add self.u_entry.text to file
        #add self.p_entry.text to file
        sm.current = 'tabs'
        
        
class TabsPanel(TabbedPanel):
    def __init__(self,**kwargs):
        super(TabsPanel, self).__init__(**kwargs)

        self.strip_image = 'strip_logo2.png'
        self.tab1 = TabbedPanelHeader(text='Dashboard')
        self.tab1.content = Dashboard()
        self.tab2 = TabbedPanelHeader(text='Catalog')
        self.tab2.content = Catalog()
        self.tab3 = TabbedPanelHeader(text='Planner')
        self.tab3.content = Planner()
        self.tab4 = TabbedPanelHeader(text='Schedule')
        self.tab4.content = Schedule()        
        
        self.add_widget(self.tab1)
        self.add_widget(self.tab2)
        self.add_widget(self.tab3)
        self.add_widget(self.tab4)
        
        
class Dashboard(GridLayout):
    def __init__(self,**kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.cols = 2
        self.one = Label(text='one')
        self.two = Label(text = 'two')
        self.three = Label(text='three')
        self.four = Label(text = 'four') 
        
        self.add_widget(self.one)
        self.add_widget(self.two)
        self.add_widget(self.three)
        self.add_widget(self.four)
        
        
class Catalog(BoxLayout):
    def __init__(self,**kwargs):
        super(Catalog, self).__init__(**kwargs)       

        self.orientation = 'vertical'

        self.search_bar = BoxLayout(size_hint=(1.0,0.05))        
        self.search_bar.add_widget(Button(text='Search',size_hint=(0.25,1.0),on_press=self.name_search))
        self.search_text = (TextInput(multiline=False,size_hint=(0.75,1.0)))
        self.search_bar.add_widget(self.search_text)

        self.filter_bar = BoxLayout(size_hint=(1.0,0.05))        
        self.AHSE = ToggleButton(text='AHSE',size_hint=(0.1875,1.0))
        self.ENGR = ToggleButton(text='ENGR',size_hint=(0.1875,1.0))
        self.MTH = ToggleButton(text='MTH',size_hint=(0.1875,1.0))
        self.SCI = ToggleButton(text='SCI',size_hint=(0.1875,1.0))
        self.filter_bar.add_widget(Button(text='Filter',size_hint=(0.25,1.0),on_press=self.filter_search))
        self.filter_bar.add_widget(self.AHSE)
        self.filter_bar.add_widget(self.ENGR)
        self.filter_bar.add_widget(self.MTH)
        self.filter_bar.add_widget(self.SCI)

        self.scrollview = ScrollView(size_hint=(1.0,0.9),size=(400,400))
        self.courses = GridLayout(cols=4,spacing=5,size_hint_y=None)
        self.courses.bind(minimum_height=self.courses.setter('height'))
        for course in catalog:
            course_item = Course_Item(size_hint_y=None,height=200)
            course_item.title.text = course.name                    
            self.courses.add_widget(course_item)
        self.scrollview.add_widget(self.courses)
                        
        self.add_widget(self.search_bar)
        self.add_widget(self.filter_bar)
        self.add_widget(self.scrollview)

    def name_search(self,instance):
        query = self.search_text.text.lower()
        for course_item in self.courses.children:
            if query == "":
                for course_item in self.courses.children:
                    course_item.title.color = (1,1,1,1)
            if query == course_item.title.text.lower():
                course_item.title.color = (0.1,0.6,0.8,1.0)

    def filter_search(self,instance):
        if self.AHSE.state == 'normal' and self.ENGR.state == 'normal' and self.MTH.state == 'normal' and self.SCI.state == 'normal':
            for course_item in self.courses.children:
                course_item.title.color = (1,1,1,1)                
        if self.AHSE.state == 'down':
            for course in catalog:
                if course.credits['AHSE'] > 0:
                    for course_item in self.courses.children:
                        if course_item.title.text == course.name:                            
                            course_item.title.color = (0.1,0.6,0.8,1.0)
        if self.ENGR.state == 'down':
            for course in catalog:
                if course.credits['ENGR'] > 0:
                    for course_item in self.courses.children:
                        if course_item.title.text == course.name:                            
                            course_item.title.color = (0.1,0.6,0.8,1.0)
        if self.MTH.state == 'down':
            for course in catalog:
                if course.credits['MTH'] > 0:
                    for course_item in self.courses.children:
                        if course_item.title.text == course.name:                            
                            course_item.title.color = (0.1,0.6,0.8,1.0)
        if self.SCI.state == 'down':
            for course in catalog:
                if course.credits['SCI'] > 0:
                    for course_item in self.courses.children:
                        if course_item.title.text == course.name:                            
                            course_item.title.color = (0.1,0.6,0.8,1.0)

               
class Planner(GridLayout):
    def __init__(self,**kwargs):
        super(Planner, self).__init__(**kwargs)

        self.cols = 2
        self.one = Label(text='one')
        self.two = Label(text = 'two')
        self.three = Label(text='three')
        self.four = Label(text = 'four') 
        
        self.add_widget(self.one)
        self.add_widget(self.two)
        self.add_widget(self.three)
        self.add_widget(self.four)
        
        
class Schedule(BoxLayout):
    def __init__(self,**kwargs):
        super(Schedule, self).__init__(**kwargs)

        self.mon = Label(text= 'Mon')
        self.tue = Label(text= 'Tue')
        self.wed = Label(text=' Wed')
        self.thu = Label(text= 'Thu')
        self.fri = Label(text=' Fri')       
        
        self.add_widget(self.mon)
        self.add_widget(self.tue)
        self.add_widget(self.wed)
        self.add_widget(self.thu)
        self.add_widget(self.fri)
        
    
class TabsScreen(Screen):
    def __init__(self,**kwargs):
        super(TabsScreen, self).__init__(**kwargs)        
        self.add_widget(TabsPanel(do_default_tab=False))
        
    
sm = ScreenManager(transition = WipeTransition())
#sm.add_widget(StartUpScreen(name='startup'))
#sm.add_widget(LogInScreen(name='login'))
#sm.add_widget(NewUserScreen(name='newuser'))
sm.add_widget(TabsScreen(name='tabs'))


class CrashCourseApp(App):   
    def build(self):                
        return sm   


if __name__ == '__main__':
    CrashCourseApp().run()