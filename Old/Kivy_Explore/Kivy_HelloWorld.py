# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 13:26:09 2014

@author: maire
"""

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')
        
TestApp().run()