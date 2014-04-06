import datetime
class User(object):
    def __init__(self, username,password,name,grad_year,major,transfer_ENGR,transfer_AHSE,transfer_MTH,transfer_SCI,courses):
        self.username = username
        self.password = password
        self.last_updated = datetime.datetime.now()
        self.name = name
        self.grad_year = grad_year
        self.major = major
        self.ENGR = transfer_ENGR
        self.AHSE = transfer_AHSE
        self.MTH = transfer_MTH
        self.SCI = transfer_SCI
        self.courses = courses #as dictionary
        
    def __str__(self):
        return self.name
  	
    def getCredits(self):
       return self.ENGR + self.AHSE + self.MTH + self.SCI
  
class Professor(object):
    def __init__(self, name, subject, courses,style):
        self.name = name
        self.subject = subject
        self.courses=courses
        self.style = style
  
class Course(object):
    def __init__(self,code, name, prof, credits, real_credits, semester, time, description, pre_req, PNR):
        self.code = code
        self.name = name
        self.prof = prof
        self.credits = credits # { category : numberofcredits , etc...}
        self.real_credits = real_credits
        self.semester = semester
        self.time = time
        self.description = description
        self.pre_req = pre_req
        self.PNR = PNR

    def __str__(self):
        return self.name

class Requirements(object):
    def __init__(self,courses):
        self.courses = courses
    def iscompleted(self,student_courses):
        pass

class Time(object):
    def __init__(self,day,hours,minutes,duration):
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.duration = duration

class Semester(object):
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