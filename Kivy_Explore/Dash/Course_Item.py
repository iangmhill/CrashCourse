
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class Course_Item(BoxLayout):
	def __init__(self,course,**kwargs):
		super(Course_Item, self).__init__(**kwargs)
		self.course = course

		self.orientation='vertical'

		self.title = (Label(text=course.name, size_hint=(1.0,0.85)))

		self.options = BoxLayout(size_hint=(1.0,0.15)) 
		self.favorite = ToggleButton(text='Favorite')
		self.details = Button(text='Details',on_press=self.pop_up)		
		self.options.add_widget(self.favorite)
		self.options.add_widget(self.details)

		self.popup = Popup(title=self.course.name,content=Label(text=self.course.description),size_hint=(None,None),size=(750,500))				

		self.add_widget(self.title)            
		self.add_widget(self.options)

	def pop_up(self,instance):	
		self.popup.open()

