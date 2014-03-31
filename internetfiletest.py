
import urllib
import urllib2
import cPickle as pickle


class User(object):
    def __init__(self, username,password,name,grad_year,major,transfer_ENGR,transfer_AHSE,transfer_MTH,transfer_SCI):
        self.username = username
        self.password = password
        self.name = name
        self.grad_year = grad_year
        self.major = major
        self.ENGR = transfer_ENGR
        self.AHSE = transfer_AHSE
        self.MTH = transfer_MTH
        self.SCI = transfer_SCI
        self.courses = []
    def __str__(self):
        return self.name

def check_internet():
    try:
        response=urllib2.urlopen('http://www.google.com',None,timeout=1)
        print "you are connected"
        return True
    except urllib2.URLError as err:
        print "you are disconnected"


if check_internet():
    urllib.urlretrieve("http://students.olin.edu/2017/ihill/test.occ", "fromInternet.occ")
    with open('fromInternet.occ', 'rb') as data:
        print('Loading File')
        number_of_users = pickle.load(data)
        print('Number of users = ' + str(number_of_users))
        new_users = []

        for n in range(number_of_users):
            new_users.append(pickle.load(data))

        for user in new_users:
            print(user)