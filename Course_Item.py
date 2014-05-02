from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class Course_Item(BoxLayout):
	"""A Course Item and associated Pop-Up to be shown in the Catalog Tab"""
	def __init__(self,course,**kwargs):
		super(Course_Item, self).__init__(**kwargs)
		self.course = course  #Every course item has an associated course object

		## COURSE ITEM CONTENT ##		
		self.orientation='vertical'

		# Title #
		self.title = (Label(text=course.keywords[0], size_hint=(1.0,0.85)))

		# Buttons #
		self.options = BoxLayout(size_hint=(1.0,0.15)) 
		self.add_button = Button(text='Add to Planner',on_press=self.add_to_planner, size_hint=(.66,1))
		self.details_button = Button(text='Details',on_press=self.open_pop_up, size_hint=(.34,1))		
		self.options.add_widget(self.add_button)
		self.options.add_widget(self.details_button)

		# Add Widgets to Course Item #
		self.add_widget(self.title)            
		self.add_widget(self.options)


		## POPUP CONTENT ##
		content = GridLayout(cols=1)

		if self.course.PNR == True:
			pnorec = 'Yes'
		else:
			pnorec = 'No'

		# Only displays a course's non-zero credits #
		ahse = ''
		engr = ''
		mth = ''
		sci = ''
		if self.course.credits['AHSE'] != 0:
			ahse = str(self.course.credits['AHSE']) + ' AHSE  '
		if self.course.credits['ENGR'] != 0:
			engr = str(self.course.credits['ENGR']) + ' ENGR  '
		if self.course.credits['MTH'] != 0:
			mth = str(self.course.credits['MTH']) + ' MTH  '
		if self.course.credits['SCI'] != 0:
			sci = str(self.course.credits['SCI']) + ' SCI'

		# Description #
		desc = Label(text=self.course.description,size_hint=(1.0,0.55))

		# Line one of information #
		info_1 = BoxLayout(size_hint=(1.0,0.2))	
		prof = Label(text='Professor:  ' + self.course.prof)
		cred = Label(text='Credits:  '+ahse+engr+mth+sci)
		pnr = Label(text='Pass/No Credit-able:  ' + pnorec)			
		info_1.add_widget(prof)
		info_1.add_widget(cred)
		info_1.add_widget(pnr)	

		# Line two of Information #
		info_2 = BoxLayout(size_hint=(1.0,0.2))
		preq = Label(text='Pre-Reqs:  ' + str(self.course.pre_req))
		rcre = Label(text='Feels Like:  ' + self.course.real_credits + ' Credits')
		code = Label(text='Course Code:  ' + str(self.course.code))
		info_2.add_widget(preq)	
		info_2.add_widget(rcre)
		info_2.add_widget(code)

		# Close Button #
		close = BoxLayout(size_hint=(1.0,0.05))
		empty_space = Label(size_hint = (0.9,1.0))	
		close_button = Button(text='Close',size_hint=(0.1,1.0),on_press=self.close_pop_up)
		close.add_widget(empty_space)
		close.add_widget(close_button)

		# Add Widgets to PopUp #
		content.add_widget(desc)
		content.add_widget(info_1)
		content.add_widget(info_2)
		content.add_widget(close)

		# Add PopUp to Course Item #
		self.popup = Popup(title=self.course.name,content=content,size_hint=(None,None),size=(750,500))


	def add_to_planner(self,instance):
		"""Adds an equivalent course item to the Planner tab"""
		for child in self.parent.parent.parent.parent.parent.parent.children:			
			child.tab3.content.add_Icon(self.course)
				
	def open_pop_up(self,instance):	
		self.popup.open()

	def close_pop_up(self,instance):
		self.popup.dismiss()