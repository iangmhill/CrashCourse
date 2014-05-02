from kivy.uix.textinput import TextInput


"""Credit to dgel on StackOverflow for this code:
http://stackoverflow.com/questions/12037379/tab-enter-and-other-keystrokes-handling-in-kivys-textinput-widgets"""


class TabTextInput(TextInput):

    def __init__(self, *args, **kwargs):
        self.next = kwargs.pop('next', None)
        super(TabTextInput, self).__init__(*args, **kwargs)

    def set_next(self, next):
        self.next = next

    def _keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        if key in (9, 13) and self.next is not None:
            self.next.focus = True
            self.next.select_all()
        else:
            super(TabTextInput, self)._keyboard_on_key_down(window, keycode, text, modifiers)