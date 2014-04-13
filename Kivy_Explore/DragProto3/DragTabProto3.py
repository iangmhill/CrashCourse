from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from DragableButton3 import DragableButton  # import to get auto register
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class Semester(Widget):
    pass

class Stats(Widget):
    pass

class Source(Widget):
    pass

class DragTab(Widget):   
    pass

class DragScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(DragScreen(name='dragscreen'))

class MyDragApp(App):
    def build(self):       
        return sm       

if __name__ == '__main__':
    MyDragApp().run()