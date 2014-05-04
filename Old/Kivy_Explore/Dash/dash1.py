from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen


kv = '''
GridLayout:
    cols:2
    rows:2
    canvas:
        Color:
            rgba: 0,1,1,.5
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: 'Your Information'
    Label:
        text: 'Reminders'
    Label:
        text: 'Statistics'
    Label:
        text: 'Notes'
        TextInput:
            #size_hint: (.25,.5)
            size: (200,200)
            #pos_hint: {'x':.7,'y':.3}
            pos:(550,20)                
            text: 'Enter Notes Here'  
    
'''


class MyPaintApp(App):
    def build(self):
        return Builder.load_string(kv)

    def greet(self):
        pass

if __name__ == '__main__':
    MyPaintApp().run()