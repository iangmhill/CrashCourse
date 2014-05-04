from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.button import Button

class RootWidget(BoxLayout):
	"""docstring for ClassName"""
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		self.add_widget(Button(text='btn 1'))
		cb= CustomBtn()
		cb.bind(pressed=self.btn_pressed)
		self.add_widget(cb)
		self.add_widget(Button(text='btn 2'))
	def btn_pressed(self,instance,pos):
		print ('pos: printed from root widget: {pos}'.format(pos=pos))

class CustomBtn(Widget):
	"""docstring for CustomBtn"""
	pressed= ListProperty([0,0])

	def on_touch_down(self, touch):
		if self.collide_point(*touch.pos):
			self.pressed=touch.pos
			return True
		return super(CustomBtn,self).on_touch_down(touch)	
	def on_pressed(self, instance, pos):
		print ('pressed at {pos}'.format(pos=pos))	

class TestApp(App):
	"""docstring for TestApp"""
	def build(self):
		return RootWidget()

if __name__=='__main__':
	TestApp().run()
		