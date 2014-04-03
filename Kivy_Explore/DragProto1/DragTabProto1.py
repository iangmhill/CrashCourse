from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import DragableButton  # import to get auto register

kv = '''
GridLayout:
    cols: 3
    GridLayout:
        cols:2
        rows:2
        canvas:
            Color:
                rgba: 0,1,1,.5
            Rectangle:
                pos: self.pos
                size: self.size
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,0
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,.1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,.2
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,.3
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
      
    GridLayout:
        id: Semesters
        cols:2
        rows:2
        canvas:
            Color:
                rgba: 0,1,1,.4
            Rectangle:
                pos: self.pos
                size: self.size
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,.5
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,.6
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,.7
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
        GridLayout:
            cols: 2
            rows: 3
            canvas:
                Color:
                    rgba: 1,1,0,.8
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
            Label:
                text:'Frosh'
    StackLayout:
                
        id: Courses
        orientation: 'tb-rl'
        
        DragableButton:
            text: 'Drag me 3'
            bound_zone_objects: [Courses, Semesters]
            droppable_zone_objects: [Semesters]
            drag_opacity: .5
            drop_func: app.greet
    
'''


class MyPaintApp(App):
    def build(self):
        return Builder.load_string(kv)

    def greet(self):
        print "Dragging done!!!"

if __name__ == '__main__':
    MyPaintApp().run()