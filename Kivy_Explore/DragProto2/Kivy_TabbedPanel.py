from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from DragableButton2 import DragableButton 

Builder.load_string("""

<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Go to Settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'            

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'See the Pretty Tabs'
            on_press: root.manager.current = 'tabs'
        Button:
            text: 'Back to Menu'
            on_press: root.manager.current = 'menu'



<TabsPanel>:
    size_hint: 1, 1
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False
   
    TabbedPanelItem:
        text: 'Dis tab'   
        FloatLayout:            
            Slider:
                size_hint: (.25,.5)
                pos_hint: {'x':0,'y':.3}
                size:(100,44)
                min: -80
                max: 80
                value: 25
                orientation: 'vertical'
            Spinner:
                size_hint: (.25,.1)
                pos_hint: {'x':.3,'y':.5}
                pos:(300,20)
                size:(100,44)            
                text: 'text'
                values: ['value1','value2']
            TextInput:
                size_hint: (.25,.5)
                pos_hint: {'x':.7,'y':.3}
                pos:(600,20)                
                text: 'Text entry yeahhhh'  
                
    TabbedPanelItem:
        text: 'Dat tab'
        StackLayout:            
            Button:
                text: 'Button that does nothing'
                width: 200
                size_hint: (None,0.15)
            ToggleButton:
                text: 'This is a toggle button'
                width: 200
                size_hint: (None,0.15)            
                group: 'group1'
            CheckBox:     
                
    TabbedPanelItem:
        text: 'Dat other tab'
        RstDocument:
            text: '\\n'.join(("Hello world", "-----------", "You are in dat other tab."))    
            
    TabbedPanelItem:
        text: 'Drag'
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
                    text: 'DesNat'
                    bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
                    droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
                    drag_opacity: .5 
                DragableButton:
                    text: 'ModSim '
                    bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
                    droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
                    drag_opacity: .5
                DragableButton:
                    text: 'ModCon'
                    bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
                    droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
                    drag_opacity: .5
                DragableButton:
                    text: 'Rwm'
                    bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
                    droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
                    drag_opacity: .5
                DragableButton:
                    text: 'Linearity 1'
                    bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
                    droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
                    drag_opacity: .5
                DragableButton:
                    text: 'Linearity 2'
                    bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
                    droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
                    drag_opacity: .5
                DragableButton:
                    text: 'POE'
                    bound_zone_objects: [Courses, Semesters, PassNoRecord, Soph1, awwGrades, SuiteDraw]
                    droppable_zone_objects: [Semesters, PassNoRecord, Soph1, awwGrades,SuiteDraw]
                    drag_opacity: .5

<TabsScreen>:
    TabsPanel:


""")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TabsPanel(TabbedPanel):
    pass

class TabsScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(TabsScreen(name='tabs'))

class TabbedPanelApp(App):
    def build(self):
        return sm
        
if __name__ == '__main__':
    TabbedPanelApp().run()