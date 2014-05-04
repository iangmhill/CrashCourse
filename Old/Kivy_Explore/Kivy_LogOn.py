# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 00:07:22 2014

@author: maire
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class LoginScreen(Widget):
    pass
    
    
class LogonApp(App):
    def build(self):
        screen=LoginScreen()
        return screen
        
LogonApp().run()