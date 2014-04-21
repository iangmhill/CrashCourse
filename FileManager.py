import os
import sys
import cPickle as pickle
from datastructures import Course, Professor, Time, Semester, User
import datetime

class FileManager(object):
    """Crash course object to handle the loading and saving of course, professor, and user data"""
    def __init__(self):
        pass
        
    def load_courses(self):
        """
        load_courses opens the courses.csv files and loads each course in the 
        file one by one and initializes a new course object for each line of
        data. The course objects are appended to the variable catalog which
        is a list of all course objects. This catalog is returned.
        """
        if not os.path.isfile('courses.csv'):
            return None
        catalog = []
        with open('courses.csv', 'r') as courses:
            lines = courses.readlines()
            for line in lines:
                c = line.split("/")
                try:
                    code = c[0]   #Course code as integer e.g. 1100
                    name = c[1]        #Course name as string e.g. "Modeling and Simulation"
                    keyw = eval(c[2])  #Course keywords as list of strings e.g. ["modsim","modeling", ...] 
                    prof = c[3]        #Course professor as string e.g. "Jessica Townsend"
                    cred = eval(c[4])  #Course credits as dictionary e.g. {"ENGR":4, ... }
                    rcre = c[5]        #Real credits as integer e.g. 4
                    seme = eval(c[6])  #semester held as list of lists i.e. [[year,semester], ...] e.g. [[2014,'f'], ... ]
                    time = eval(c[7])  #time of day held as list of lists i.e. [[day,hour,minutes,duration], ...] e.g. [['m',13,30,100],['r',13,30,100]]
                    desc = c[8]        #description as string
                    prer = eval(c[9])  #Prerequisites as list of integer course codes e.g. [1100,1200, ...]
                    pnre = eval(c[10])  #Pass/norecordable as boolean
                except:
                    print("Load error on the following line:")
                    print(line)
                    return False
                else:
                    #generate time objects from time list
                    TIMES = []
                    for t in time:
                        TIMES.append(Time(t[0],t[1],t[2],t[3]))
                    #generate semester objects from seme list
                    SEMESTERS = []
                    for s in seme:
                        SEMESTERS.append(Semester(s[0],s[1]))
                    input_course = Course(code,name,keyw,prof,cred,rcre,SEMESTERS,TIMES,desc,prer,pnre)
                    catalog.append(input_course)
        return catalog

    def load_profs(self):
        faculty = []
        with open('profs.csv', 'r') as profs:
            lines = profs.readlines()
            for line in lines:
                c = line.split("/")
                try:
                    name = c[0]        #Prof name as string e.g. "Jessica Townsend"
                    subj = c[1]        #Prof subject as string e.g. "Thermodynamics"
                    cour = eval(c[2])  #courses taught as list of course codes e.g. [1100,1200, ...]
                    styl = c[3]        #Prof style as string
                except:
                    print("Load error on the following line:")
                    print(line)
                    return False
                else:
                    input_prof = Professor(name,subj,cour,styl)
                    faculty.append(input_prof)
        return faculty

    def load_stats(self):
        with open('stats.sts', 'rb') as statsfile:
            last_updated = pickle.load(statsfile)
            distribution = pickle.load(statsfile)
        return last_updated,distribution

    def load_user(self,username,password):
        with open('user.usr', 'rb') as userfile:
            try:
                user = pickle.load(userfile)
            except:
                print("User file does not exist")
                return False
            else:
                if username == user.username and password == user.password:
                    return user
                else:
                    return None


    def save_user(self,user):
        with open('user.usr', 'wb') as userfile:
            pickle.dump(user, userfile, -1)





filemanager = FileManager()
catalog = filemanager.load_courses()
for course in catalog:
    print(course.keywords)
# last_updated,distribution = filemanager.load_stats()
# print(last_updated)
# for k in distribution:
#     print(str(k) + str(distribution[k]))
