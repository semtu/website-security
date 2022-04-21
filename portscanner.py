import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer=input('Enter a remote host to scan: ')
try:
    remoteServerIP=socket.gethostbyname(remoteServer)
except socket.gaierror:
    print('Connect to the Internet')

print('-'*60)
print('Please wait, scanning remote host',remoteServerIP)
print('-'*60)

t1=datetime.now()

try:
    for port in range(1,1025):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP,port))
        if result==0:
            print(f'Port {port}: Open')
        sock.close()

except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

t2=datetime.now()
total=t2-t1
print(f'Scanning Completed in: {total}')