import sys
sys.path.insert(0, '/home/ihill/Documents/CrashCourse/tftpy')
from TftpServer import TftpServer
sys.path.insert(0, '/home/ihill/Documents/CrashCourse/Server')

server = TftpServer('/home/ihill/Documents/CrashCourse/Server')
server.listen('127.0.0.1',5281,5)

def generate_statistics():
    pass