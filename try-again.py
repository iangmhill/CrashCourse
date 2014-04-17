# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 20:18:45 2014

@author: susie
"""

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
from Course_Item import Course_Item
from kivy.uix.dropdown import DropDown
from Proto3_5 import DragTab


fm = FileManager()
catalog = fm.load_courses()
user = fm.load_user('ihill','crashcourse')


favorite_courses = []
search_temp_list = [] 

class StartUpScreen(Screen):
    def __init__(self,**kwargs):        
        super(StartUpScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.image = Image(source='logo1.png',allow_stretch=False,keep_ratio=True)
        Clock.schedule_once(self.transition,3)        
                
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
        #self.tab2 = TabbedPanelHeader(text='Catalog')
        #self.tab2.content = Catalog()
        #self.tab3 = TabbedPanelHeader(text='Planner')
        #self.tab3.content = Planner()
        #self.tab4 = TabbedPanelHeader(text='Schedule')
        #self.tab4.content = Schedule()        
        
        self.add_widget(self.tab1)
        #self.add_widget(self.tab2)
        #self.add_widget(self.tab3)
        #self.add_widget(self.tab4)

class Dashboard(GridLayout):
    def __init__(self,**kwargs):
        super(Dashboard, self).__init__(**kwargs)
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
        self.n_entry = TextInput(text=user.notes, multiline=True)
        self.notes.add_widget(self.n_entry)
        
        
        self.add_widget(self.info)
        self.add_widget(self.reminders)
        self.add_widget(self.stats)
        self.add_widget(self.notes)
        
        


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