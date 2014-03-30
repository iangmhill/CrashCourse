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

class Requirements(object):
    def __init__(self,courses):
        self.courses = courses
    def iscompleted(self,student_courses):
        pass
class Time(object):
    def __init__(self,
class Schedule (object):
    def __init__(self):
        self.courses = []
        
ModSim=Course(1111, 'ModSim', JTownsend, {'ENGR':0, 'AHSE':0, 'MTH':2, 'SCI':2} , 4, 'Fall', 'Morning1', 'Modeling things yay MatLab', 'none', True)     