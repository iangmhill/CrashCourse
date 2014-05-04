from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty



#I commented out the server things cause I wasn't sure if we needed them or not. I also commented it out in the orkiv.kv file. 

class AccountDetailsForm(AnchorLayout):
    #server_box = ObjectProperty()
    username_box = ObjectProperty()
    password_box = ObjectProperty()
    def login(self):
        #Use the things in the print statements below to access the information in the server, username, and password boxes after login is pressed
        #print(self.server_box.text)
        print(self.username_box.text)
        print(self.password_box.text)

class Orkiv1(App):
    pass
 
Orkiv1().run()

