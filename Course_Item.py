
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class Course_Item(BoxLayout):
	def __init__(self,course,**kwargs):
		super(Course_Item, self).__init__(**kwargs)
		self.course = course

		self.orientation='vertical'

		self.title = (Label(text=course.name, size_hint=(1.0,0.85)))

		self.options = BoxLayout(size_hint=(1.0,0.15)) 
		self.add_button = Button(text='Add to Planner',on_press=self.add_to_planner)
		self.details_button = Button(text='Details',on_press=self.pop_up)		
		self.options.add_widget(self.add_button)
		self.options.add_widget(self.details_button)

		ahse = str(self.course.credits['AHSE'])
		engr = str(self.course.credits['ENGR'])
		mth = str(self.course.credits['MTH'])
		sci = str(self.course.credits['SCI'])
		if self.course.PNR == True:
			pnorec = 'Yes'
		else:
			pnorec = 'No'

		content = GridLayout(cols=1)
		desc = Label(text=self.course.description,size_hint=(1.0,0.6))
		info_1 = BoxLayout(size_hint=(1.0,0.2))
		info_2 = BoxLayout(size_hint=(1.0,0.2))
		code = Label(text='Course Code:  ' + str(self.course.code))
		prof = Label(text='Professor:  ' + self.course.prof)
		rcre = Label(text='Real Credits:  ' + self.course.real_credits)
		preq = Label(text='Pre-Reqs:  ' + str(self.course.pre_req))	
		cred = Label(text='AHSE: '+ahse+'   '+'ENGR: '+engr+'   '+'MTH: '+mth+'   '+'SCI: '+sci)
		pnr = Label(text='Pass/No Record-able:  ' + pnorec)

		info_1.add_widget(prof)
		info_1.add_widget(cred)
		info_1.add_widget(pnr)
		info_2.add_widget(preq)	
		info_2.add_widget(rcre)
		info_2.add_widget(code)		

		content.add_widget(desc)
		content.add_widget(info_1)
		content.add_widget(info_2)

		self.popup = Popup(title=self.course.name,content=content,size_hint=(None,None),size=(750,500))				

		self.add_widget(self.title)            
		self.add_widget(self.options)

	def add_to_planner(self,instance):
		#there might be a better way to do this but i have yet to find one
		for child in self.parent.parent.parent.parent.parent.parent.children:			
			child.tab3.content.add_Icon(self.course.name)								
				
	def pop_up(self,instance):	
		self.popup.open()