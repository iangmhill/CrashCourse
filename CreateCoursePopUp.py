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
from datastructures import Course
from TabTextInput import TabTextInput
import all_globals


class Build_Course(Popup):
    def __init__(self,sm,**kwargs):
        super(Build_Course,self).__init__(**kwargs)
        self.sm = sm        

        self.title = 'Make Your Own Course'
        self.size = (750,500)
        self.size_hint = (None,None)    
        self.content = GridLayout(cols=1)

        ## Name of Course Entry ##
        self.ncourse = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.ncourse.add_widget(Label())
        self.ncourse.add_widget(Label(text='Name of Course:'))
        self.ncourse_entry = TabTextInput(multiline=False)
        self.ncourse.add_widget(self.ncourse_entry)
        self.ncourse.add_widget(Label())
        
        ## Credit Entry ##
        #AHSE#
        self.ahse = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.ahse.add_widget(Label())
        self.ahse.add_widget(Label(text='AHSE:'))
        self.ahse_entry = TabTextInput(multiline=False)
        self.ahse.add_widget(self.ahse_entry)
        self.ahse.add_widget(Label())
        #ENGR#
        self.engr = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.engr.add_widget(Label())
        self.engr.add_widget(Label(text='ENGR:'))
        self.engr_entry = TabTextInput(multiline=False)
        self.engr.add_widget(self.engr_entry)
        self.engr.add_widget(Label())
        #MTH#
        self.mth = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.mth.add_widget(Label())
        self.mth.add_widget(Label(text='MTH:'))
        self.mth_entry = TabTextInput(multiline=False)
        self.mth.add_widget(self.mth_entry)
        self.mth.add_widget(Label())
        #SCI#
        self.sci = GridLayout(cols=4,size_hint=(1.0,0.05))
        self.sci.add_widget(Label())
        self.sci.add_widget(Label(text='SCI:'))
        self.sci_entry = TabTextInput(multiline=False)
        self.sci.add_widget(self.sci_entry)
        self.sci.add_widget(Label())

        ## Allow for Tabbing ##
        self.ncourse_entry.set_next(self.ahse_entry)
        self.ahse_entry.set_next(self.engr_entry)
        self.engr_entry.set_next(self.mth_entry)
        self.mth_entry.set_next(self.sci_entry)
        self.sci_entry.set_next(self.ncourse_entry)
        
        ## Create Course Button ##           
        self.create = GridLayout (cols = 3, size_hint = (1.0,0.05))
        self.create.add_widget(Label())
        self.create_button = Button(text = 'Add to Planner',on_press=self.create_course)
        self.create.add_widget(self.create_button)
        self.create.add_widget(Label())

        ## Close Button ##
        self.close = BoxLayout(size_hint=(1.0,0.05))
        empty_space = Label(size_hint=(0.9,1.0))
        self.close_button = Button(text='Close',size_hint=(0.1,1.0),on_press=self.close_pop_up)
        self.close.add_widget(empty_space)
        self.close.add_widget(self.close_button)
        
        ## Empty Space ##
        self.space1 = Label(size_hint=(1.0,0.175))
        self.space2 = Label(size_hint=(1.0,0.1))
        self.space3 = Label(size_hint=(1.0,0.05))
        self.space4 = Label(size_hint=(1.0,0.125))       

        ## Add widgets to Popup ##
        self.content.add_widget(self.space1) 
        self.content.add_widget(self.ncourse)               
        self.content.add_widget(self.space2)
        self.content.add_widget(self.ahse)
        self.content.add_widget(self.engr)
        self.content.add_widget(self.mth)
        self.content.add_widget(self.sci)
        self.content.add_widget(self.space3)
        self.content.add_widget(self.create)
        self.content.add_widget(self.space4)
        self.content.add_widget(self.close)       
    
    def create_course(self,instance):
        """Adds course to planner tab only if credit entries are integers"""
        try:            
            ahse = int(self.ahse_entry.text)
            engr = int(self.engr_entry.text)
            mth = int(self.mth_entry.text)
            sci = int(self.sci_entry.text)

            self.space4.text = 'Added to Planner!'
            new_course = Course(None,self.ncourse_entry.text,[self.ncourse_entry.text],None,{'AHSE':ahse,'ENGR':engr,'MTH':mth,'SCI':sci},None,None,None,None,None,None)           
            if len(self.sm.tabs.tabspanel.tab3.content.courses.children) <= 9:
                self.sm.tabs.tabspanel.tab3.content.add_Icon(new_course)
            else:
                self.space4.text = 'Your planner has too many courses, you eager beaver! \n Move some into your semesters before adding more.'
            
        except:            
            self.space4.text = 'Please enter integer values for course credits (zero if not applicable).'


    def open_pop_up(self,instance):
        self.ahse_entry.text=''
        self.engr_entry.text=''
        self.mth_entry.text=''
        self.sci_entry.text=''
        self.ncourse_entry.text=''
        self.space4.text=''
        self.open()

    def close_pop_up(self,instance):
        self.dismiss()