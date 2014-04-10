from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class DragCourseButton(BoxLayout,Button):
	def __init__(self, **kwargs):
		super(DragCourseButton, self).__init__(**kwargs)
		self.text=''

		boxes=BoxLayout(orientation='vertical')
		
		grid1=GridLayout(cols=2, size_hint=())
		grid1.add_widget(Label(text='Professor'))
		grid1.add_widget(Label(text='Course Code'))
		
		grid2=GridLayout(cols=2)
		grid2.add_widget(ToggleButton(text='Will Take Pass/Fail'))
		grid2.add_widget(Button(text='More...'))

		boxes.add_widget(Label(text='Course Name'))
		boxes.add_widget(grid1)
		boxes.add_widget(grid2)

		
		self.add_widget(boxes)
		#self.size=(300,300)

	
		

class TestApp(App):

    def build(self):
    	things=Button()
    	button=DragCourseButton()
    	things.add_widget(button)
        return button
if __name__=='__main__':   
	TestApp().run()