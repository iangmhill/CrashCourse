from datetime import datetime
class User(object):
    """User objects will store information about each 
    individual user and save information from each session"""

    def __init__(self, username,password,name,grad_year,major,starting_credits,courses,notes):
        self.username = username            #as string e.g. "ihill"
        self.password = password            #as string e.g. "crashcourse1"
        self.last_updated = datetime.now()  #as datetime object
        self.name = name                    #as string e.g. "Ian Hill"
        self.grad_year = grad_year          #as int e.g. 2017
        self.major = major                  #as string e.g. "E:C"
        self.credits = starting_credits     #as dictinary e.g. {'ENGR':0, 'AHSE':0,'MTH':2,'SCI':2}
        self.courses = courses              #as list of course codes e.g. [1000,1200, ...]
        self.notes = notes                  #as string e.g. "I want to take SoftDes because..."
        
    def __str__(self):
        return self.name
  	
    def getCredits(self):
       pass
  
class Professor(object):
    """Professor objects store information about professors 
    that has been downloaded from the server"""

    def __init__(self, name, subject, courses,style):
        self.name = name                   #as string "Mark Somerville"
        self.subject = subject             #as string "Professor of Electrical Engineering and Physics"
        self.courses=courses               #as list of course codes e.g. [1000,1200, ...]
        self.style = style                 #as string e.g. "Cool!"
  
class Course(object):
    """Course objects store information about courses
    that has been downloaded from the server"""

    def __init__(self,code, name, prof, credits, real_credits, semester, time, description, pre_req, PNR):
        self.code = code                  #as int e.g. 1111
        self.name = name                  #as string e.g. "Modeling and Simulation"
        self.prof = prof                  #as string e.g. "Mark Somerville"
        self.credits = credits            #as dictionary i.e. { category : numberofcredits , etc...} 
                                          #e.g. {'ENGR':0, 'AHSE':0,'MTH':2,'SCI':2}
        self.real_credits = real_credits  #as int e.g. 4
        self.semester = semester          #as list of Semester object
        self.time = time                  #as list of Time objects
        self.description = description    #as string e.g. "MATLAB and stuff. YAY"
        self.pre_req = pre_req            #as list of course codes e.g. [1000,1200, ...]
        self.PNR = PNR                    #as boolean e.g. True

    def __str__(self):
        return self.name

class Requirements(object):
    """Requirements objects store a list of course codes as integers that can 
    be compared to the list of course codes of a user to determine if 
    requirements have been met"""

    def __init__(self,courses):
        self.courses = courses  #as list e.g. [1000,2000, ...]
    def iscompleted(self,student_courses):
        pass                    #work in progress

class Time(object):
    """Time objects store the day (as char), hour (as int), 
    minute (as int), and duration (as in in minutes) of a
    class period of a course"""

    def __init__(self,day,hours,minutes,duration):
        self.day = day            #as char e.g. 'm'
        self.hours = hours        #as int e.g. 13
        self.minutes = minutes    #as int e.g. 30
        self.duration = duration  #as int e.g. 100

class Semester(object):
    """Semester objects store information about a semester
    for data organization purposes and comparison"""

    def __init__(self,year,season):
        self.year = year      #as integer e.g. 2017
        self.season = season  #as char e.g. 'f' or 's'
    def __str__(self):
        return "[" + str(self.year) + "," + self.season + "]"
    def __eq__(self,other):
        return self.year == other.year and self.season == other.season

class Schedule (object):
    def __init__(self):
        self.courses = []
        
#ModSim=Course(1111, 'ModSim', JTownsend, {'ENGR':0, 'AHSE':0, 'MTH':2, 'SCI':2} , 4, 'Fall', 'Morning1', 'Modeling things yay MatLab', 'none', True)     