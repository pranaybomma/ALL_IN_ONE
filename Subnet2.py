# Author: Pranay Bomma
from netaddr import *
import pprint
from os import walk
import sys, csv

inc = 1
#Host = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5", "192.168.1.6"]
ConfigFile = open('f.txt', 'w')
input = sys.argv[1]

#Network = raw_input("Enter the Network address without notation:")
#Notaion = raw_input("Please input the notation with /:")
#Networks = IPNetwork(Network+Notaion)
Networks = IPNetwork(input)
print "checking live hosts in " + str(Networks) + "\n"
Host = list(Networks)
#print Host
Total_number_hosts = len(Networks)




for i in range(1,Total_number_hosts - 1):
	ConfigFile.write(str(Host[i]) + "\n")