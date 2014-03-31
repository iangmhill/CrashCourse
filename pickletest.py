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

user1 = User('ihill','crashcourse','Ian Hill','2017','E:C',0,0,0,0)
user2 = User('mkeene','crashcourse','Maire Keene','2017','UD',0,0,0,0)
user3 = User('mborges','crashcourse','Mafalda Borges','2017','UD',0,0,0,0)
users = [user1,user2,user3]

with open('test.occ', 'wb') as output:
    print('Writing File')
    pickle.dump(len(users), output, -1)
    for user in users:
        pickle.dump(user, output, -1)
        print(user)



with open('test.occ', 'rb') as input:
    print('Loading File')
    number_of_users = pickle.load(input)
    print('Number of users = ' + str(number_of_users))
    new_users = []

    for n in range(number_of_users):
        new_users.append(pickle.load(input))

for user in new_users:
    print(user)