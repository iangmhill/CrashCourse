import sys
import os
import shutil
os.chdir('..')
os.chdir('tftpy')
sys.path.insert(0, os.getcwd())
from TftpServerCustom import TftpServer
os.chdir('..')
sys.path.insert(0, os.getcwd())
from datastructures import Semester, User
import threading
from datetime import date, datetime
import cPickle as pickle
from socket import socket, SOCK_DGRAM, AF_INET
os.chdir('Server')
sys.path.insert(0, os.getcwd())

class Controller(object):
    def __init__(self):
        self.running = True
        current_year = date.today().year
        if 1 <= date.today().month <= 6:
            current_season = 's'
        else:
            current_season = 'f'
        self.current_semester = Semester(current_year,current_season)
        self.semesters = [self.current_semester]
        for sem in range(7):
            if self.semesters[-1].season == 's':
                self.semesters.append(Semester(self.semesters[-1].year,'f'))
            else:
                self.semesters.append(Semester(self.semesters[-1].year + 1,'s'))
        self.distribution = {}
    
    def get_ipaddress(self):
        s = socket(AF_INET,SOCK_DGRAM)
        s.connect(('google.com',0))
        return s.getsockname()[0]
        
    def CommandThread(self):
        while self.running:
            k = raw_input(">>> ")
            if k == "x":
                print("running = False")
                self.running = False
            elif k == "ls":
                print(os.getcwd())
                for file in os.listdir(os.getcwd()):
                    print(file)
                
    def ServerThread(self):
        print(self.get_ipaddress())
        server = TftpServer(os.getcwd(),None,self.get_ipaddress(),5301,5)
        while self.running:
            for n in range(12):
                if self.running:
                    server.listen()
                else:
                    break
            try:
                self.merge()
                self.generate_statistics()
            except:
                pass
                
        print("Beginning shutdown")
        server.stop() 
        
    def generate_statistics(self):
        self.distribution = {k:{} for k in self.semesters}
        for cwdfile in os.listdir(os.getcwd()):
            if cwdfile[-4:] == ".usr":
                with open(cwdfile, 'rb') as userfile:
                    user = pickle.load(userfile)
                    for sem_dist in self.distribution:
                        for sem_cour in user.courses:
                            if sem_dist == sem_cour:
                                for code in user.courses[sem_cour]:
                                    if code in self.distribution[sem_dist]:
                                        self.distribution[sem_dist][code] += 1
                                    else:
                                        self.distribution[sem_dist][code] = 1
        with open("stats.sts", 'wb') as statsfile:
            pickle.dump(datetime.now(),statsfile,-1)
            pickle.dump(self.distribution, statsfile, -1)
        return True

    def merge(self):
        for cwdfile in os.listdir(os.getcwd()):
            if cwdfile[-5:] == "1.usr":
                os.remove(cwdfile[:-5] + '.usr')
                shutil.copyfile(cwdfile, cwdfile[:-5] + '.usr')
                os.remove(cwdfile)
                
    
    def run(self):
            t1 = threading.Thread(target=self.CommandThread)
            t2 = threading.Thread(target=self.ServerThread)
            t1.start()
            t2.start()

if __name__ == '__main__':
    ops = Controller()
    ops.run()


           
