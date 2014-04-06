import sys
sys.path.insert(0, '/home/ihill/Documents/CrashCourse/tftpy')
from TftpServer import TftpServer
sys.path.insert(0, '/home/ihill/Documents/CrashCourse')

server = TftpServer('/home/ihill/Documents/CrashCourse')
server.listen('127.0.0.1',5281,5)
