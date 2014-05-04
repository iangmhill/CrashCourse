from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class CourseButton(BoxLayout, Button):
	def __init__(self, **kwargs):
		super(CourseButton, self).__init__(**kwargs)
		#self.text=''
		self.orientation='vertical'
		# self.padding=10
		# self.spacing=10

		grid1=GridLayout(cols=2, size_hint=(1,.25))
		grid1.add_widget(Label(text='Professor'))
		grid1.add_widget(Label(text='Course Type'))
		
		grid2=GridLayout(cols=2, size_hint=(1, .25), padding=5, spacing=2)
		grid2.add_widget(ToggleButton(text='Pass/Fail'))
		grid2.add_widget(Button(text='More...'))

		self.add_widget(Label(text='Course Name', size_hint=(1, .4), font_size= 24))
		self.add_widget(grid1)
		self.add_widget(grid2)

#Slighty more nested-but-i-know-it-works verson
		# boxes=BoxLayout(orientation='vertical', padding = '20', spacing='10')
		
		# grid1=GridLayout(cols=2, size_hint=(1,.3))
		# grid1.add_widget(Label(text='Professor'))
		# grid1.add_widget(Label(text='Course Code'))
		
		# grid2=GridLayout(cols=2, size_hint=(1, .2), padding='20', spacing='10')
		# grid2.add_widget(ToggleButton(text='Will Take Pass/Fail'))
		# grid2.add_widget(Button(text='More...'))

		# boxes.add_widget(Label(text='Course Name', size_hint=(1, .5), font_size= 24))
		# boxes.add_widget(grid1)
		# boxes.add_widget(grid2)

		
		# self.add_widget(boxes)
		

	
		

class TestApp(App):

    def build(self):
    	button=CourseButton()
        return button

if __name__=='__main__':   
	TestApp().run()