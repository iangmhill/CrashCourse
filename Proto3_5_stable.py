from DragableButton3 import DragableButton
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from NoKvId import Semester
from kivy.clock import Clock

catalog=['ModCon','ModSim','DesNat','AHS Found.','OIE','MODRWM']
semesters=['FL 2013', 'SP 2014','FL 2014','SP 2015','FL 2015','SP 2016','FL 2016','SP 2017']

class DragTab(BoxLayout):
	def __init__(self,**kwargs):
		super(DragTab,self).__init__(**kwargs)
		#Base Layer is a BoxLayout
		#right-hand column is StackLayout, lefthand is a vertical box layout
		self.Scrollhome=StackLayout(orientation='tb-rl', size_hint=(.3,1))
		#self.Scrollhome.add_widget(Button(text='hi'))
		self.lefthand=BoxLayout(orientation='vertical', size_hint=(.7,1))
		#within lefthand, stats and a series of semesters
		self.Planner=GridLayout(size_hint=(1,.9),rows=2, cols=4, spacing=3)

		self.slot1=Semester(text=str(semesters[0]))
		self.Planner.add_widget(self.slot1)
		self.slot2=Semester(text=str(semesters[2]))
		self.Planner.add_widget(self.slot2)
		self.slot3=Semester(text=str(semesters[4]))
		self.Planner.add_widget(self.slot3)
		self.slot4=Semester(text=str(semesters[6]))
		self.Planner.add_widget(self.slot4)
		self.slot5=Semester(text=str(semesters[1]))
		self.Planner.add_widget(self.slot5)
		self.slot6=Semester(text=str(semesters[3]))
		self.Planner.add_widget(self.slot6)
		self.slot7=Semester(text=str(semesters[5]))
		self.Planner.add_widget(self.slot7)
		self.slot8=Semester(text=str(semesters[7]))
		self.Planner.add_widget(self.slot8)

		self.lefthand.add_widget(self.Planner)

		self.stats_widget=BoxLayout(size_hint=(1, .1))
		self.recycle=Button(size_hint=(.25, 1), text= 'Recycle \n Course')
		self.stats=Label(size_hint=(.75,1),text= 'We can display statistics here', color=(1,1,1,.3))
		self.stats_widget.add_widget(self.recycle)
		self.stats_widget.add_widget(self.stats)
		self.lefthand.add_widget(self.stats_widget)
		
		#Now stuff it all in
		self.add_widget(self.lefthand)
		self.add_widget(self.Scrollhome)

		# for course in catalog:
		# 	self.add_Icon(course)

		# if len(self.lefthand.children)>=2:
		Clock.schedule_interval(self.update_stats_widget, .1)
		

	def add_Icon(self, course):
		Icon=DragableButton(course=course, text=course.name,size=(100,100),
                              droppable_zone_objects=[],
                              bound_zone_objects=[],
                              kill_zone_objects=[],
                              drag_opacity=.5,
                              remove_on_drag=True)
		# Icon.text_size=self.size
		Icon.bound_zone_objects.append(self.Planner)
		Icon.bound_zone_objects.append(self.Scrollhome)
		Icon.bound_zone_objects.append(self.recycle)
		
		Icon.droppable_zone_objects.append(self.slot1.coursehouse)
		Icon.droppable_zone_objects.append(self.slot2.coursehouse)
		Icon.droppable_zone_objects.append(self.slot3.coursehouse)
		Icon.droppable_zone_objects.append(self.slot4.coursehouse)
		Icon.droppable_zone_objects.append(self.slot5.coursehouse)
		Icon.droppable_zone_objects.append(self.slot6.coursehouse)
		Icon.droppable_zone_objects.append(self.slot7.coursehouse)
		Icon.droppable_zone_objects.append(self.slot8.coursehouse)
		
		Icon.droppable_zone_objects.append(self.Scrollhome)

		Icon.kill_zone_objects.append(self.recycle)

		self.Scrollhome.add_widget(Icon)

	def update_stats_widget(self, dt):
		count=0
		Fixed=False
		for child in self.lefthand.children[:]:
			if child.height> 300:
				for semester_block in child.children[:]:
					for semester_element in semester_block.children[:]:
						if semester_element.height>100:
							for course in semester_element.children[:]:
								count+=1
		for child in self.lefthand.children[:]:
			if child.height>300:
				Fixed=True
		if Fixed:
			for child in self.lefthand.children[:]:
				if child.height< 300:
					for grandchild in child.children[:]:
						if grandchild.width> 300:
							child.remove_widget(grandchild)
							stats=Label(size_hint=(1,1),text= 'Your schedule includes: ' + str(count)+' courses', color=(1,1,1,1))
							child.add_widget(stats)
						
						

class DemoApp2(App):
	"""docstring for TestApp"""
	def build(self):
		
		return DragTab()

if __name__=='__main__':
	DemoApp2().run()