#!/bin/bash
# Author: Pranay Bomma
clear
echo -n "Please select your option:"

cat <<- PRANAY

    1. Convert wildcard mask to "/" notation [rename the file with m that needs to be converted]
    2. Convert "/" notation to wildcard mask [rename the file with m that needs to be converted]
    3. Conver FQDN's to IP [insert the FQDN's in f.txt]
    4. Conver IP to FQDN [insert the IP's in f.txt]
    5. HOST UP/DOWN
    6. Checking live hosts in a subnet
    7. Exit

PRANAY

read _OPTION

case "$_OPTION" in

    1) python IOSTOEOS.py
       ;;
    2) python NXOSTOEOS.py
       ;;
    3) python Name-IP.py
       ;;
    4) python Ip-host.py
       ;;
    5) ./live.bash
       ;;   
    6) ./Subnet2.bash
       ;;       
    7) exit
       ;;
 
esac
