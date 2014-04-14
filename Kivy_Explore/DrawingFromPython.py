from kivy.uix.widget import Widget
from kivy.app import App
from kivy.graphics import Rectangle
#Not sure where to import Rectangle from

class MyWidget1(Widget):
	"""docstring for MyWidget1"""
	def __init__(self, **kwargs):
		super(MyWidget1, self).__init__(**kwargs)
		with self.canvas:
			self.rect=Rectangle(pos=self.pos, size=self.size)
		self.bind(pos=self.update_rect)
		self.bind(size=self.update_rect)
	def update_rect(self,*args):
		self.rect.pos=self.pos
		self.rect.size=self.size

class TestApp(App):
	"""docstring for TestApp"""
	def build(self):
		return MyWidget1()

if __name__=='__main__':
	TestApp().run()
