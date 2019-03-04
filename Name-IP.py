# Author: Pranay Bomma
#!/usr/bin/python
import sys
import socket

#p = sys.argv[1]

data_dict = {}

f = open('f.txt','r')
iplist = []
for line in f.readlines():
        line = line.strip()
#       print line
        try:
                ip = socket.gethostbyname(line)
#                print ip
                print line + " " + ip
                iplist.append(ip)
#               print ip
        except:
                print "cannot resolve host :- " + line
                pass
for ip in iplist:
      print ip
f.close()


#ACTUAL
#!/usr/bin/python
#import sys
#import socket#

#p = sys.argv[1]#

#data_dict = {}#

#f = open(p,'r')
#iplist = []
#for line in f.readlines():
#        line = line.strip()
##       print line
#        try:
#                ip = socket.gethostbyaddr(line)[0]
#                print line + " ------>>>> " + ip
#                iplist.append(ip)
##               print ip
#        except:
#                print "cannot resolve host :- " + line
#                pass
#for ip in iplist:
#        print ip
#f.close()