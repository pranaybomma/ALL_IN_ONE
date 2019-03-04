#!/usr/bin/python
# Author: Pranay Bomma
#License: GPLv3


with open(r'm', 'r') as infile, \
     open(r'm1', 'w') as outfile:
    data = infile.read()
    data = data.replace(" 0.255.255.255", "/8")
    data = data.replace(" 0.127.255.255", "/9")
    data = data.replace(" 0.63.255.255", "/10")
    data = data.replace(" 0.31.255.255", "/11")
    data = data.replace(" 0.15.255.255", "/12")
    data = data.replace(" 0.7.255.255", "/13")
    data = data.replace(" 0.3.255.255", "/14")
    data = data.replace(" 0.1.255.255", "/15")
    data = data.replace(" 0.0.255.255", "/16")
    data = data.replace(" 0.0.127.255", "/17")
    data = data.replace(" 0.0.63.255", "/18")
    data = data.replace(" 0.0.31.255", "/19")
    data = data.replace(" 0.0.15.255", "/20")
    data = data.replace(" 0.0.7.255", "/21")
    data = data.replace(" 0.0.3.255", "/22")
    data = data.replace(" 0.0.1.255", "/23")
    data = data.replace(" 0.0.0.255", "/24")
    data = data.replace(" 0.0.0.127", "/25")
    data = data.replace(" 0.0.0.63", "/26")
    data = data.replace(" 0.0.0.31", "/27")
    data = data.replace(" 0.0.0.15", "/28")
    data = data.replace(" 0.0.0.7", "/29")
    data = data.replace(" 0.0.0.3", "/30")
    data = data.replace(" 0.0.0.1", "/31")
    data = data.replace(" 0.0.0.0", "/32")
    outfile.write(data)

