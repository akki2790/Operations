#ping a range of ips with the python subprocess module

import subprocess

for ping in range(2,15):
    address = '192.168.2.'+ str(ping)
    res=subprocess.call(['ping ', '-c ','3 ' ,address])
    if res==0:
        print "ping to " + address + " was a success."
    elif res==2:
        print "no response from the address " + address
    else:
        print 'ping to ' + address + ' failed!'

        
