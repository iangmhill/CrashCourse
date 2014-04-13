from DragableButton3 import DragableButton
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#Found a way to make the drag and drop work without having to use those weak-refs in kv called 'id'

class TestApp(App):
	"""docstring for TestApp"""
	def build(self):
		main=BoxLayout()
		source=StackLayout(orientation='tb-rl')
		#source.add_widget(Label(text='Source Widget'))
		dest=StackLayout(orientation='bt-lr')
		#dest.add_widget(Label(text='Destination Widget'))
		for i in range(3):
			btn=DragableButton(size=(150,150))
			btn.add_bound_zone(source)
			btn.add_bound_zone(dest)
			btn.add_droppable_zone(dest)
			source.add_widget(btn)
		main.add_widget(dest)
		main.add_widget(source)

		return main

if __name__=='__main__':
	TestApp().run()

