import sys
import cPickle
from datastructures import Course

class FileManager(object):
    """Crash course object to handle the loading and saving of course, professor, and user data"""
    def __init__(self):
        self.catalog = self.load_courses()
        if self.catalog != False: print(self.catalog[0].time[0])
        
    def load_courses(self):
        """
        load_courses opens the courses.csv files and loads each course in the 
        file one by one and initializes a new course object for each line of
        data. The course objects are appended to the variable catalog which
        is a list of all course objects. This catalog is returned.
        """
        catalog = []
        with open('courses.csv') as courses:
            lines = courses.readlines()
            for line in lines:
                c = line.split("/")
                try:
                    code = int(c[0])   #Course code as integer e.g. 1100
                    name = c[1]        #Course name as string e.g. "Modeling and Simulation" 
                    prof = c[2]        #Course professor as string e.g. "Jessica Townsend"
                    cred = eval(c[3])  #Course credits as dictionary e.g. {"ENGR":4, ... }
                    rcre = c[4]        #Real credits as integer e.g. 4
                    seme = eval(c[5])  #semester held as list of lists i.e. [[year,semester], ...] e.g. [[2014,'f'], ... ]
                    time = eval(c[6])  #time of day held as list of lists i.e. [[day,hour,minutes,duration], ...] e.g. [['m',13,30,100],['r',13,30,100]]
                    desc = c[7]        #description as string
                    prer = eval(c[8])  #Prerequisites as list of integer course codes e.g. [1100,1200, ...]
                    pnre = eval(c[9])  #Pass/norecordable as boolean
                except:
                    print("Load error on the following line:")
                    print(line)
                    return False
                else:
                    input_course = Course(code,name,prof,cred,rcre,seme,time,desc,prer,pnre)
                    catalog.append(input_course)
        return catalog

    def load_profs(self):
        pass

filemanager = FileManager()
print("Still returned")