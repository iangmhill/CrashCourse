import datetime
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import XMPPError
from sleekxmpp.jid import InvalidJID
from kivy.uix.textinput import TextInput
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import escape_markup
from kivy.core.audio import SoundLoader


class AccountDetailsForm(AnchorLayout):
    server_box = ObjectProperty()
    username_box = ObjectProperty()
    password_box = ObjectProperty()
    def login(self):
        print ("Click the Button")
        print(self.server_box.text)
        print(self.username_box.text)
        print(self.password_box.text)

class Orkiv1(App):
    pass
 
Orkiv1().run()

