from DragableButton3 import DragableButton
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from NoKvId import Semester
from kivy.clock import Clock
import all_globals


class DragTab(BoxLayout):
	def __init__(self,**kwargs):
		super(DragTab,self).__init__(**kwargs)
		#Base Layer is a BoxLayout
		#right-hand column is StackLayout, lefthand is a vertical box layout		
		
		self.courses = StackLayout(spacing=5,size_hint_y=None,orientation='tb-rl',size_hint=(0.3,1))		
		
		self.lefthand=BoxLayout(orientation='vertical', size_hint=(.7,1))
		self.Planner=GridLayout(size_hint=(1,.85),rows=2, cols=4, spacing=3)

		self.slot1=Semester(text="Fall "+ str(all_globals.user.grad_year-4))
		self.Planner.add_widget(self.slot1)
		self.slot2=Semester(text="Fall "+ str(all_globals.user.grad_year-3))
		self.Planner.add_widget(self.slot2)
		self.slot3=Semester(text="Fall "+ str(all_globals.user.grad_year-2))
		self.Planner.add_widget(self.slot3)
		self.slot4=Semester(text="Fall "+ str(all_globals.user.grad_year-1))
		self.Planner.add_widget(self.slot4)
		self.slot5=Semester(text="Spring "+ str(all_globals.user.grad_year-3))
		self.Planner.add_widget(self.slot5)
		self.slot6=Semester(text="Spring "+ str(all_globals.user.grad_year-2))
		self.Planner.add_widget(self.slot6)
		self.slot7=Semester(text="Spring "+ str(all_globals.user.grad_year-1))
		self.Planner.add_widget(self.slot7)
		self.slot8=Semester(text="Spring "+ str(all_globals.user.grad_year))
		self.Planner.add_widget(self.slot8)

		self.lefthand.add_widget(self.Planner)

		self.stats_widget=BoxLayout(size_hint=(1, .15))
		self.recycle=Button(size_hint=(.2, 1),background_normal='recycle.png',background_down='recycle.png')#,text= 'Recycle \n Course')
		self.stats=Label(size_hint=(.8,1),color=(1,1,1,.3))
		self.stats_widget.add_widget(self.recycle)
		self.stats_widget.add_widget(self.stats)
		self.lefthand.add_widget(self.stats_widget)

		#Now stuff it all in
		self.add_widget(self.lefthand)
		self.add_widget(self.courses)

		# if len(self.lefthand.children)>=2:
		Clock.schedule_interval(self.update_stats_widget, .1)


	def add_Icon(self,course):

		Icon=DragableButton(course=course,text=course.keywords[0],height=100,size_hint_y=None,
							  droppable_zone_objects=[],
							  bound_zone_objects=[],
							  kill_zone_objects=[],
							  drag_opacity=.5,
							  remove_on_drag=True)
		# Icon.text_size=self.size
		Icon.bound_zone_objects.append(self.Planner)
		Icon.bound_zone_objects.append(self.courses)
		Icon.bound_zone_objects.append(self.recycle)

		Icon.droppable_zone_objects.append(self.slot1.coursehouse)
		Icon.droppable_zone_objects.append(self.slot2.coursehouse)
		Icon.droppable_zone_objects.append(self.slot3.coursehouse)
		Icon.droppable_zone_objects.append(self.slot4.coursehouse)
		Icon.droppable_zone_objects.append(self.slot5.coursehouse)
		Icon.droppable_zone_objects.append(self.slot6.coursehouse)
		Icon.droppable_zone_objects.append(self.slot7.coursehouse)
		Icon.droppable_zone_objects.append(self.slot8.coursehouse)

		Icon.droppable_zone_objects.append(self.courses)

		Icon.kill_zone_objects.append(self.recycle)

		self.courses.add_widget(Icon)

	def update_stats_widget(self, dt):		
		# DON'T REWRITE OVER THE USER INFORMATION WITH THE STUPID DUMMY DATA!!!!!!
		Fixed=False
		all_globals.user.credits['AHSE'] = 0#course.course.pre_credits['AHSE']												
		all_globals.user.credits['ENGR'] = 0#course.course.pre_credits['ENGR']													
		all_globals.user.credits['MTH'] = 0#course.course.pre_credits['MTH']													
		all_globals.user.credits['SCI'] = 0#course.course.pre_credits['SCI']
		all_globals.user.courses=[]
		for child in self.lefthand.children[:]:
			if child.height> 300:
				for semester_block in child.children[:]:
					for semester_element in semester_block.children[:]:
						if semester_element.height>100:
							for course in semester_element.children[:]:
								all_globals.user.courses.append(course.course.code)
								all_globals.user.credits['AHSE'] += course.course.credits['AHSE']												
								all_globals.user.credits['ENGR'] += course.course.credits['ENGR']													
								all_globals.user.credits['MTH'] += course.course.credits['MTH']													
								all_globals.user.credits['SCI'] += course.course.credits['SCI']
																			
		for child in self.lefthand.children[:]:
			if child.height>300:
				Fixed=True
		if Fixed:
			for child in self.lefthand.children[:]:
				if child.height< 300:
					for grandchild in child.children[:]:
						if grandchild.width> 300:
							child.remove_widget(grandchild)

							stats=Label(size_hint=(1,1),text='AHSE:  '+str(all_globals.user.credits['AHSE'])+'  '+'ENGR:  '+str(all_globals.user.credits['ENGR'])+'  '+'MTH:  '+str(all_globals.user.credits['MTH'])+'  '+'SCI:  '+str(all_globals.user.credits['SCI'])+'  ',color=(1,1,1,1))
							print all_globals.user.courses
							child.add_widget(stats)


class DemoApp2(App):
	"""docstring for TestApp"""
	def build(self):

		return DragTab()

if __name__=='__main__':	
	DemoApp2().run()