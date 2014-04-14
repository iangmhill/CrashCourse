
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button


class Course_Item(BoxLayout):
	def __init__(self,**kwargs):
		super(Course_Item, self).__init__(**kwargs)
		self.orientation='vertical'

		self.title = (Label(size_hint=(1.0,0.85)))

		self.options = BoxLayout(size_hint=(1.0,0.15)) 
		self.favorite = ToggleButton(text='Add to Favorites')
		self.description = Button(text='Course Details')
		self.options.add_widget(self.favorite)
		self.options.add_widget(self.description)

		self.add_widget(self.title)            
		self.add_widget(self.options)           
