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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.clock import Clock

class StartUpScreen(Screen):
    def __init__(self,**kwargs):        
        super(StartUpScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.image = Image(source='logo1.png',allow_stretch=False,keep_ratio=True)
        Clock.schedule_once(self.transition,5)        
                
        self.add_widget(self.image)
                             
    def transition(self,instance):            
        sm.current = 'login'
        
class LogInScreen(GridLayout,Screen):
    def __init__(self,**kwargs):
        super(LogInScreen, self).__init__(**kwargs)
        self.cols = 2
        self.username = Label(text='Username')
        self.u_entry = TextInput(multiline=False)
        self.password = Label(text='Password')
        self.p_entry = TextInput(multiline=False,password=True)
        self.back = Button(text = 'New User',on_press = self.new_user_function)
        self.enter = Button(text = 'Enter',on_press = self.enter_function)  
        
        self.add_widget(self.username)
        self.add_widget(self.u_entry)
        self.add_widget(self.password)
        self.add_widget(self.p_entry)        
        self.add_widget(self.back)
        self.add_widget(self.enter)
        
    def new_user_function(self,instance):
        sm.current = 'newuser'
        
    def enter_function(self,instance):
        sm.current = 'tabs'    
        
        
class NewUserScreen(GridLayout,Screen):
    def __init__(self,**kwargs):
        super(NewUserScreen, self).__init__(**kwargs)
        
        self.cols = 2
        self.username = Label(text='Please enter a username.')
        self.u_entry = TextInput(multiline=False)
        self.password = Label(text='Please enter a password.')
        self.p_entry = TextInput(multiline=False,password=True)
        self.back = Button(text = 'Back',on_press = self.back_function)
        self.enter = Button(text = 'Enter',on_press = self.enter_function)       
        
        self.add_widget(self.username)
        self.add_widget(self.u_entry)
        self.add_widget(self.password)
        self.add_widget(self.p_entry)
        self.add_widget(self.back)
        self.add_widget(self.enter)
        
    def back_function(self,instance):
        sm.current = 'login'
        
    def enter_function(self,instance):
        sm.current = 'tabs'
        
        
class TabsPanel(TabbedPanel):
    def __init__(self,**kwargs):
        super(TabsPanel, self).__init__(**kwargs)        
        self.tab1 = TabbedPanelHeader(text='Dashboard',strip_image='logo1.png')
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
        self.one = Button(text='one')
        self.two = Button(text = 'two')
        self.three = Button(text='three')
        self.four = Button(text = 'four') 
        
        self.add_widget(self.one)
        self.add_widget(self.two)
        self.add_widget(self.three)
        self.add_widget(self.four)
        
        
class Catalog(BoxLayout):
    def __init__(self,**kwargs):
        super(Catalog, self).__init__(**kwargs)  
        self.orientation = 'vertical'
        self.search = TextInput(text='Search for a course.',multiline = False,size_hint=(1.0,0.1))
                
        self.courses = GridLayout(cols=2,size_hint=(1.0,0.9))
        self.courses.add_widget(Button(text='one'))
        self.courses.add_widget(Button(text = 'two'))
        self.courses.add_widget(Button(text='three'))
        self.courses.add_widget(Button(text = 'four'))
                
        self.add_widget(self.search)
        self.add_widget(self.courses)
        
               
class Planner(GridLayout):
    def __init__(self,**kwargs):
        super(Planner, self).__init__(**kwargs)
        self.cols = 2
        self.one = Button(text='one')
        self.two = Button(text = 'two')
        self.three = Button(text='three')
        self.four = Button(text = 'four') 
        
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
sm.add_widget(StartUpScreen(name='startup'))
sm.add_widget(LogInScreen(name='login'))
sm.add_widget(NewUserScreen(name='newuser'))
sm.add_widget(TabsScreen(name='tabs'))

    
class CrashCourseApp(App):   
    def build(self):                
        return sm
        

if __name__ == '__main__':
    CrashCourseApp().run()