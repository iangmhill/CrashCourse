# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 13:26:09 2014

@author: maire
"""
#No Kivy String Needed!!!!!
#OMG!!!!

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

class LoginScreen(GridLayout):
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.cols=2
		self.add_widget(Label(text='User Name'))
		self.username=TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text='Password?'))
		self.password=TextInput(password=True, multiline=False)
		self.add_widget(self.password)

	def print_password(self):
		print(self.password)

class TestApp(App):

    def build(self):
    	login=LoginScreen()
    	Clock.schedule_interval(login.print_password(), 5.0)
        return login

if __name__=='__main__':   
	TestApp().run()