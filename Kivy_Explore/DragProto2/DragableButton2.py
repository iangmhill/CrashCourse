from DragNDropWidget2 import DragNDropWidget
from kivy.uix.button import Button


class DragableButton(Button, DragNDropWidget):
    '''
    classdocs
    '''
    def __init__(self, **kw):
        '''
        Constructor
        '''
        #Button.__init__(self, **kw)
        super(DragableButton, self).__init__(**kw)
        self.size_hint = (None, None)

    def __deepcopy__(self, dumb):
        return DragableButton(text=self.text,
                              droppable_zone_objects=self.droppable_zone_objects,
                              bound_zone_objects=self.bound_zone_objects,
                              drag_opacity=self.drag_opacity,
                              remove_on_drag=self.remove_on_drag)