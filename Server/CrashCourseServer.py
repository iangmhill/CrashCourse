import sys
import os
import shutil
import datetime
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
        self.filepath = os.getcwd()
        self.running = True
        self.working_file = ""
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
        self.t1 = threading.Thread(target=self.ServerThread)
        self.t2 = threading.Thread(target=self.CommandThread)
        self.ip = self.get_ipaddress()
        self.port = 5304
        self.log = ""
        try:
            sys.path.insert(0,"//stuweb/WEB/Students/2017/ihill")
            os.chdir("//stuweb/WEB/Students/2017/ihill")
            print(os.getcwd())
            with open('ServerAddress.txt', 'w') as ip:
                ip.write(self.ip + "\n" + str(self.port))
            sys.path.insert(0,self.filepath)
            os.chdir(self.filepath)
            print("IP address posted to stuweb")
        except:
            sys.path.insert(0,self.filepath)
            os.chdir(self.filepath)
            print("IP address failed to post")



    
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
            elif k == "merge":
                self.merge()
                print("Merge Complete")
            elif k == "log":
                print(self.log)
                
    def ServerThread(self):
        server = TftpServer(os.getcwd(),None,self.ip,self.port,5)
        print("Server started: " + self.get_ipaddress() + ":" + str(self.port))
        while self.running:
            for n in range(5):
                if self.running:
                    server.listen()
                    if server.working_file != self.working_file:
                        self.log += str(datetime.now()) + ' ' + server.working_file + '\n'
                        self.working_file = server.working_file
                else:
                    break
            try:
                self.merge()
                self.log += str(datetime.now()) + ' Merge completed\n'
                self.generate_statistics()
                self.log += str(datetime.now()) + ' Statistics generated\n'
                with open('ServerLog.txt','w') as log:
                    log.write(self.log)
            except:
                pass
                
        print("Beginning shutdown")
        server.stop()
        #self.t2.join()
        
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
            self.t1.start()
            self.t2.start()

if __name__ == '__main__':
    ops = Controller()
    ops.run()


           
