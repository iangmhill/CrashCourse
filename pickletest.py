import cPickle as pickle
from datastructures import User

user1 = User('ihill','crashcourse','Ian Hill','2017','E:C',0,0,0,0)
user2 = User('mkeene','crashcourse','Maire Keene','2017','UD',0,0,0,0)
user3 = User('mborges','crashcourse','Mafalda Borges','2017','UD',0,0,0,0)
user4 = User ('hpelletier','crashcourse','Haley Pelletier','2017','UD',0,0,0,0)
user5= User ('sgrimshaw1','crashcourse','Susie Grimshaw', '2017','UD',0,0,0,0)
users = [user1,user2,user3, user4, user5]

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
    print(user.last_updated)
    
with open('ihill.usr', 'wb') as output:
    print('Writing File')
    pickle.dump(user1, output, -1)