kv='''
<DragTab>:
	canvas:
		Color: 1,1,1,.2
			rectangle: 
				pos: self.pos
				size: self.size

'''

class DragTab(Widget):
	def __init__(**kwargs):
		super(DragTab,self).__init__(**kwargs)
		 for course in catalog:
