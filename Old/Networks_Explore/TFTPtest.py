import sys
sys.path.insert(0, '/home/ihill/Documents/CrashCourse/tftpy')
from TftpClient import TftpClient
sys.path.insert(0, '/home/ihill/Documents/CrashCourse')

tftp_client = TftpClient('127.0.0.1',5281)
tftp_client.download('test.occ','new.occ')