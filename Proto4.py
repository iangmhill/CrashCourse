from DragableButton3 import DragableButton
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.uix.button import Button

catalog=['ModCon','ModSim','DesNat']
class Semester(BoxLayout):
	"""docstring for Semester"""
	def __init__(self, **kwargs):
		super(Semester, self).__init__(**kwargs)
		self.main=BoxLayout()

		self.Me=Button(text='A Special Semester', size_hint=(1,.1))
		self.coursehouse=StackLayout(size_hint=(1,.9), orientation='tb-lr')

		self.main.add_widget(self.Me)
		self.main.add_widget(self.coursehouse)

		self.add_widget(Button(text='me!'))
		#self.add_widget(self.coursehouse)

		

class DragTab(BoxLayout):
	def __init__(self,**kwargs):
		super(DragTab,self).__init__(**kwargs)
		#Base Layer
		self.base=BoxLayout()
		#right-hand column is X, lefthand is a vertical box layout
		self.Scrollhome=StackLayout(orientation='tb-lr', size_hint=(.3,1))
		self.Scrollhome.add_widget(Button(text='hi'))
		self.lefthand=BoxLayout(orientation='vertical', size_hint=(.7,1))
		#within lefthand, stats and a series of semesters
		self.Planner=GridLayout(size_hint=(1,.9),rows=2, cols=4)

		self.Planner.add_widget(Semester(size_hint=(1,1)))

		self.Planner.add_widget(Button(text='A Semester'))
		self.Planner.add_widget(Button(text='A Semester'))
		self.Planner.add_widget(Button(text='A Semester'))
		self.Planner.add_widget(Button(text='A Semester'))

		self.lefthand.add_widget(self.Planner)
		self.lefthand.add_widget(Button(size_hint=(1,.1),text= 'We can display statistics here'))
		

		self.base.add_widget(self.lefthand)
		self.base.add_widget(self.Scrollhome)
		


		self.add_widget(self.base)

	def add_Icon(self, display):
		Icon=DragableButton(text=display,size=(100,100),
                              droppable_zone_objects=[],
                              bound_zone_objects=[],
                              drag_opacity=.5,
                              remove_on_drag=True)
		Icon.droppable_zone_objects.append(self.lefthand)
		Icon.bound_zone_objects.append(self.lefthand)
		Icon.bound_zone_objects.append(self.Scrollhome)
		self.Scrollhome.add_widget(Icon)

class Semester(GridLayout):
	def __init__(self,**kwargs):
		super(Semester,self).__init__(**kwargs)
		self.rows=3
		self.cols=2


class DemoApp2(App):
	"""docstring for TestApp"""
	def build(self):
		
		return DragTab()

if __name__=='__main__':
	DemoApp2().run()