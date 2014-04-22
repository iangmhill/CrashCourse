from FileManager import FileManager
from NetworkManager import NetworkManager
from datastructures import User


global fm
fm = FileManager()
global nm
nm = NetworkManager()
global catalog
catalog = []
global profs
profs = []
global user
user = User('noone','crashcourse','No One',2017,'E:C',{'ENGR':100, 'AHSE':1000,'MTH':2,'SCI':2},[],"")

