import os
import sys
sys.path.insert(0, '/home/ihill/Documents/CrashCourse/tftpy')
from TftpClient import TftpClient
sys.path.insert(0, '/home/ihill/Documents/CrashCourse')
import urllib2
import cPickle as pickle
from datastructures import User


class NetworkManager(object):
    def __init__(self):
        self.client = TftpClient('127.0.0.1',5281)
        
    def check_internet(self):
        try:
            response=urllib2.urlopen('http://www.google.com',None,timeout=1)
            print "Connected to the Internet"
            return True
        except urllib2.URLError as err:
            print "Disconnected from the Internet"
            return False
            
    def create_user(self,username):
        if self.check_internet():
            try:
                self.client.download( username + '.usr', 'temp.usr')
                print("User already exists")
                return -1
            except:
                print("User does not exist on server \nCreating file")
                os.rename('user.usr',username + '.usr')
                self.client.upload(username + '.usr', username + '.usr')
                os.rename(username + '.usr','user.usr')
                print("Done")
            
        
    def update(self,username,password):
        if self.check_internet():
            
            
            if os.path.isfile('temp.usr') and os.path.isfile('user.usr'):
                with open('temp.usr','rb') as temp:
                    online_user = pickle.load(temp)
                with open('user.usr','rb') as local:
                    local_user = pickle.load(local)
            else:
                print("User does not exist on client")
                return -2
            print("Checking if user file is up-to-date")
            if local_user.username != online_user.username or online_user.last_updated > local_user.last_updated:
                """ server version of user is newer than local version """
                os.remove('user.usr')
                os.rename('temp.usr','user.usr')
            elif local_user.username == online_user.username and local_user.last_updated >= online_user.last_updated:
                """ local version of user is newer than server version """
                os.remove('temp.usr')
            
            with open('user.usr','rb') as userfile:
                    user = pickle.load(userfile)
                    userfile.close()
            if password != user.password:
                print("Incorrect password")
                return -3
            else:
                print("Correct password")
                try:
                    self.client.download('courses.csv', 'courses_client.csv')
                    print("Downloaded course information")
                    self.client.download('profs.csv','profs_client.csv')
                    print("Downloaded professor information")
                    self.client.upload('user.usr', username + '.usr')
                    print("Uploaded user information")
                except:
                    print("Network error when downloading new content")
                    return -4
                else:
                    print("Update complete")
                    return True
if __name__ == '__main__':
    network = NetworkManager()
    network.create_user('mkeene')