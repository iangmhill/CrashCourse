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
		FreshColor=[0.2,0.65,0.8,0.85]
		SophColor=[0.2,0.65,0.8,0.75]
		JuniColor=[0.2,0.65,0.8,0.6]
		SeniColor=[0.2,0.65,0.8,0.45]

		self.courses = StackLayout(spacing=5,size_hint_y=None,orientation='tb-rl',size_hint=(0.3,1))		
		
		self.lefthand=BoxLayout(orientation='vertical', size_hint=(.7,1))
		self.Planner=GridLayout(size_hint=(1,.85),rows=2, cols=4, spacing=3)

		self.slot1=Semester(text="Fall "+ str(all_globals.user.grad_year-4), color=FreshColor)
		self.slot2=Semester(text="Fall "+ str(all_globals.user.grad_year-3), color=SophColor)
		self.slot3=Semester(text="Fall "+ str(all_globals.user.grad_year-2), color=JuniColor)
		self.slot4=Semester(text="Fall "+ str(all_globals.user.grad_year-1), color=SeniColor)
		self.slot5=Semester(text="Spring "+ str(all_globals.user.grad_year-3), color=FreshColor)
		self.slot6=Semester(text="Spring "+ str(all_globals.user.grad_year-2), color=SophColor)
		self.slot7=Semester(text="Spring "+ str(all_globals.user.grad_year-1), color=JuniColor)
		self.slot8=Semester(text="Spring "+ str(all_globals.user.grad_year), color=SeniColor)

		self.slots=[self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6, self.slot7, self.slot8]
		
		for sem_obj in self.slots:
			self.Planner.add_widget(sem_obj)

		self.lefthand.add_widget(self.Planner)

		self.stats_widget=BoxLayout(size_hint=(1, .15))
		self.recycle=Button(size_hint=(.2, 1),background_normal='recycle.png',background_down='recycle.png')#,text= 'Recycle \n Course')
		self.stats=Label(size_hint=(1,1),color=(1,1,1,.3))
		self.stats_widget.add_widget(self.recycle)
		self.stats_widget.add_widget(self.stats)
		self.lefthand.add_widget(self.stats_widget)

		#Now stuff it all in
		self.add_widget(self.lefthand)
		self.add_widget(self.courses)

		Clock.schedule_interval(self.update_stats_widget, .1)


	def add_Icon(self,course):

		Icon=DragableButton(course=course,text=course.keywords[0],height=100,size_hint_y=None,
							  droppable_zone_objects=[],
							  bound_zone_objects=[],
							  kill_zone_objects=[],
							  drag_opacity=.5,
							  remove_on_drag=True)
		
		Icon.bound_zone_objects.append(self.Planner)
		Icon.bound_zone_objects.append(self.courses)
		Icon.bound_zone_objects.append(self.recycle)

		for sem in self.slots:
			Icon.add_droppable_zone(sem.coursehouse)

		Icon.droppable_zone_objects.append(self.courses)

		Icon.kill_zone_objects.append(self.recycle)

		self.courses.add_widget(Icon)

	def update_stats_widget(self, dt):		
		# When the user gets pre-credits as an attribute, we can stop writing over 
		# Fixed=False
		all_globals.user.credits['AHSE'] = 0#course.course.pre_credits['AHSE']												
		all_globals.user.credits['ENGR'] = 0#course.course.pre_credits['ENGR']													
		all_globals.user.credits['MTH'] = 0#course.course.pre_credits['MTH']													
		all_globals.user.credits['SCI'] = 0#course.course.pre_credits['SCI']
		all_globals.user.courses=[]
		for semester_obj in self.slots:
			for icon in semester_obj.coursehouse.children[:]:
				all_globals.user.courses.append(icon.course.code)
				all_globals.user.credits['AHSE'] += icon.course.credits['AHSE']												
				all_globals.user.credits['ENGR'] += icon.course.credits['ENGR']													
				all_globals.user.credits['MTH'] += icon.course.credits['MTH']													
				all_globals.user.credits['SCI'] += icon.course.credits['SCI']
		
		self.stats_widget.remove_widget(self.stats)
		self.stats=Label(size_hint=(1,1),text='AHSE:  '+str(all_globals.user.credits['AHSE'])+'  '+'ENGR:  '+str(all_globals.user.credits['ENGR'])+'  '+'MTH:  '+str(all_globals.user.credits['MTH'])+'  '+'SCI:  '+str(all_globals.user.credits['SCI'])+'  ',color=(1,1,1,1))
		print all_globals.user.courses
		self.stats_widget.add_widget(self.stats)

		for sem in self.slots:
			sem.Me.clear_widgets()

		adjust=4
		for sem in self.slots[0:4]:
			sem.Me.add_widget(Label(text="Fall "+ str(all_globals.user.grad_year-adjust)))
			adjust-=1
		adjust=3
		for sem in self.slots[4:]:
			sem.Me.add_widget(Label(text="Spring "+ str(all_globals.user.grad_year-adjust)))
			adjust-=1

		# self.slot1.Me.add_widget(Label(text="Fall "+ str(all_globals.user.grad_year-4))
		# self.slot2.Me.add_widget(Label(text="Fall "+ str(all_globals.user.grad_year-3))
		# self.slot3.Me.add_widget(Label(text="Fall "+ str(all_globals.user.grad_year-2))
		# self.slot4.Me.add_widget(Label(text="Fall "+ str(all_globals.user.grad_year-1))
		# self.slot5.Me.add_widget(Label(text="Spring "+ str(all_globals.user.grad_year-3))
		# self.slot6.Me.add_widget(Label(text="Spring "+ str(all_globals.user.grad_year-2))
		# self.slot7.Me.add_widget(Label(text="Spring "+ str(all_globals.user.grad_year-1))
		# self.slot8.Me.add_widget(Label(text="Spring "+ str(all_globals.user.grad_year))

		


class DemoApp2(App):
	"""docstring for TestApp"""
	def build(self):

		return DragTab()

if __name__=='__main__':	
	DemoApp2().run()