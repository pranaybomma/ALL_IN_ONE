#!/usr/bin/python
# Author: Pranay Bomma
#License: GPLv3


with open(r'm', 'r') as infile, \
     open(r'm1', 'w') as outfile:
    data = infile.read()
    data = data.replace("/8", " 0.255.255.255")
    data = data.replace("/9", " 0.127.255.255")
    data = data.replace("/10", " 0.63.255.255")
    data = data.replace("/11", " 0.31.255.255")
    data = data.replace("/12", " 0.15.255.255")
    data = data.replace("/13", " 0.7.255.255")
    data = data.replace("/14", " 0.3.255.255")
    data = data.replace("/15", " 0.1.255.255")
    data = data.replace("/16", " 0.0.255.255")
    data = data.replace("/17", " 0.0.127.255")
    data = data.replace("/18", " 0.0.63.255")
    data = data.replace("/19", " 0.0.31.255")
    data = data.replace("/20", " 0.0.15.255")
    data = data.replace("/21", " 0.0.7.255")
    data = data.replace("/22", " 0.0.3.255")
    data = data.replace("/23", " 0.0.1.255")
    data = data.replace("/24", " 0.0.0.255")
    data = data.replace("/25", " 0.0.0.127")
    data = data.replace("/26", " 0.0.0.63")
    data = data.replace("/27", " 0.0.0.31")
    data = data.replace("/28", " 0.0.0.15")
    data = data.replace("/29", " 0.0.0.7")
    data = data.replace("/30", " 0.0.0.3")
    data = data.replace("/31", " 0.0.0.1")
    data = data.replace("/32", " 0.0.0.0")
    outfile.write(data)