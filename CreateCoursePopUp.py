# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:17:07 2014

@author: mafaldaborges
"""


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivy.clock import Clock

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput


class Build_Course(BoxLayout):
    def __init__(self,**kwargs):
        super(Build_Course,self).__init__(**kwargs)
        
        #content2 = TextInput(text='FISH')
        content3 = GridLayout(cols=1)
        
        self.ahse = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.ahse.add_widget(Label())
        self.ahse.add_widget(Label(text='AHSE:'))
        self.ahse_entry = TextInput(multiline=False)
        self.ahse.add_widget(self.ahse_entry)
        self.ahse.add_widget(Label())
        
        self.engr = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.engr.add_widget(Label())
        self.engr.add_widget(Label(text='ENGR:'))
        self.engr_entry = TextInput(multiline=False)
        self.engr.add_widget(self.engr_entry)
        self.engr.add_widget(Label())
        
        self.mth = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.mth.add_widget(Label())
        self.mth.add_widget(Label(text='MTH:'))
        self.mth_entry = TextInput(multiline=False)
        self.mth.add_widget(self.mth_entry)
        self.mth.add_widget(Label())
        
        self.sci = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.sci.add_widget(Label())
        self.sci.add_widget(Label(text='SCI:'))
        self.sci_entry = TextInput(multiline=False)
        self.sci.add_widget(self.sci_entry)
        self.sci.add_widget(Label())
        
        self.ncourse = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.ncourse.add_widget(Label())
        self.ncourse.add_widget(Label(text='Name of Course:'))
        self.ncourse_entry = TextInput(multiline=False)
        self.ncourse.add_widget(self.ncourse_entry)
        self.ncourse.add_widget(Label())        
        
        
        
        self.offline = GridLayout (cols = 3, size_hint = (1.0,0.05))
        self.offline.add_widget(Label())
        self.offline_button = Button(text = 'Create Course')
        self.offline.add_widget(self.offline_button)
        self.offline.add_widget(Label())
            
        self.space1 = Label(size_hint=(1.0,0.175))
        self.space2 = Label(size_hint=(1.0,0.1))
        self.space3 = Label(size_hint=(1.0,0.05))
        self.space4 = Label(size_hint=(1.0,0.175))

        content3.add_widget(self.space1) 
        content3.add_widget(self.ncourse)               
        content3.add_widget(self.space2)
        content3.add_widget(self.ahse)
        content3.add_widget(self.engr)
        content3.add_widget(self.mth)
        content3.add_widget(self.sci)
        content3.add_widget(self.space3)
        content3.add_widget(self.offline)
        content3.add_widget(self.space4)       
    
        
        self.popup = Popup(title = 'Make Your Own Course', content = content3,size_hint = (None,None),size = (750,500))
        #self.details_button = Button(text='Details',on_press=self.open_pop_up, size_hint=(.34,1))  
        #self.add_widget(self.details_button)   
    
    
    def open_pop_up(self,instance):
        self.popup.open()
    def close_pop_up(self,instance):
        self.popup.dismiss()

# class DemoApp3(App):
# 	"""docstring for TestApp"""
# 	def build(self):

# 		return Build_Course()

# if __name__=='__main__':	
# 	DemoApp3().run()