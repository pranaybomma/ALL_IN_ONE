#!/bin/bash
# Author: Pranay Bomma
##
echo -n " Entern the subnet with / notation : "
read _SUBNET

## invoking the python script with subnet info:
python Subnet2.py "$_SUBNET"

for _name in `cat f.txt`
do
    echo "$_name"
    _RESULT="$(ping -t 1 -c 1 $_name | grep received | awk '{print $7}')"
    #echo $_RESULT
    if [ $_RESULT == 100.0% ]
    then 
        echo "DOWN"
        echo " "    
    else 
        echo "UP"    
        echo " "
    fi
  
done
echo "Checking Accomplished"  
rm f.txt