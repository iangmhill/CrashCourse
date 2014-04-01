import os
import sys
sys.path.insert(0, '/home/ihill/Documents/CrashCourse/tftpy')
from TftpClient import TftpClient
sys.path.insert(0, '/home/ihill/Documents/CrashCourse')
import urllib2
import cPickle as pickle
from datastructures import User


class Network(object):
    def __init__():
        client = TftpClient('127.0.0.1',5281)
        
    def check_internet():
    try:
        response=urllib2.urlopen('http://www.google.com',None,timeout=1)
        print "you are connected"
        return True
    except urllib2.URLError as err:
        print "you are disconnected"
        return False
        
    def update(username,password):
        if check_internet():
            try:
                client.download( username + '.usr', 'login.usr')
            except:
                print("User does not exist")
                return -1
            else:
                with open('login.usr', 'rb') as userfile:
                    print('Loading User')
                    User = pickle.load(userfile)
                    if password != User.password:
                        print("Incorrect password")
                        os.remove('login.usr')
                        return -2
                    else:
                        os.rename('login.usr','user.usr')
                        try:
                            client.download('courses.csv', 'courses.csv')
                            client.download('profs.csv','profs.csv')
                        except:
                            print("Network error when downloading new content")
                            return -3
                        else:
                            return True
                            
