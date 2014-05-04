from networkmanager import NetworkManager
from filemanager import FileManager

fmanager=FileManager()
catalog=fmanager.load_courses()
faculty=fmanager.load_profs()
user=fmanager.load_user(username, password)