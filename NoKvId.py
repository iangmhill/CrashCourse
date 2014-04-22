from DragableButton3 import DragableButton
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.button import Button

#Found a way to make the drag and drop work without having to use those weak-refs in kv called 'id'
class Semester(StackLayout):
	def __init__(self, text, **kwargs):
		super(Semester,self).__init__(**kwargs)
		self.text=text
		#self.color= color
		orientation='tb-lr'
		with self.canvas:
			Color(0, 0, 1., .2)
			self.rect=Rectangle(pos=self.pos, size=self.size)
		self.bind(pos=self.update_rect)
		self.bind(size=self.update_rect)

		self.Me=BoxLayout(size_hint=(1,.1))
		self.Me.add_widget(Label(text=self.text))
		self.coursehouse=GridLayout(size_hint=(1,.9), rows=6, cols=1)

		self.add_widget(self.Me)
		self.add_widget(self.coursehouse)

		#self.coursecount=0
		#self.bind(coursecount=self.update_count)

	def update_rect(self,*args):
		self.rect.pos=self.pos
		self.rect.size=self.size
		# Line(color=(1,1,1,1),rectangle=(self.pos[0], self.pos[1], self.width, self.height), width=3)
		# self.rows=3
		# self.cols=2
		#self.size_hint=(.25,.5)
	#def update_count(self, *args):
		

class TestApp(App):
	"""docstring for TestApp"""
	def build(self):
		main=BoxLayout()
		source=GridLayout(rows=5, size_hint=(1,1))
		#source.add_widget(Label(text='Source Widget'))
		dest=StackLayout(orientation='tb-lr')
		#dest.add_widget(Label(text='Destination Widget'))
		semester1=Semester()
		#semester1.add_widget(Label(text='1'))
		dest.add_widget(semester1)
		semester2=Semester()
		#semester2.add_widget(Label(text='2'))
		dest.add_widget(semester2)

		# semester3=GridLayout(rows=3, cols=2)
		# dest.add_widget(semester3)
		# semester4=GridLayout(rows=3, cols=2)
		# dest.add_widget(semester4)

		for i in range(6):
			btn=DragableButton(size=(100,100), text=str(i))
			btn.add_bound_zone(source)
			btn.add_droppable_zone(source)
			btn.add_bound_zone(semester1)
			btn.add_droppable_zone(semester1)
			btn.add_bound_zone(semester2)
			btn.add_droppable_zone(semester2)

			# btn.add_bound_zone(semester3)
			# btn.add_droppable_zone(semester3)
			# btn.add_bound_zone(semester4)
			# btn.add_droppable_zone(semester4)
			#btn.add_bound_zone(dest)
			#btn.add_droppable_zone(dest)
			source.add_widget(btn)
		
		main.add_widget(dest)
		main.add_widget(source)

		return Semester()

if __name__=='__main__':
	TestApp().run()

