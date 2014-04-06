from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from DragableButton2 import DragableButton  # import to get auto register
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

kv = '''
GridLayout:
    cols: 3
    GridLayout:
        cols: 2
        rows:2
        GridLayout:
            id: PassNoRecord
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
            id: Soph1
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
            id: awwGrades
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
            id: SuiteDraw
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
      
    GridLayout:
        id: Semesters
        cols:2
        rows:2
       
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
            bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
            droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
            drag_opacity: .5 
        DragableButton:
            text: 'HowStack?'
            bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
            droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
            drag_opacity: .5
        DragableButton:
            text: 'HowStack?'
            bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
            droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
            drag_opacity: .5
        DragableButton:
            text: 'HowStack?'
            bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
            droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
            drag_opacity: .5
        DragableButton:
            text: 'HowStack?'
            bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
            droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
            drag_opacity: .5
        DragableButton:
            text: 'HowStack?'
            bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
            droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
            drag_opacity: .5
        DragableButton:
            text: 'HowStack?'
            bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
            droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
            drag_opacity: .5
'''


class MyPaintApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    MyPaintApp().run()