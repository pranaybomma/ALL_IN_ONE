#!/bin/bash
# Author: Pranay Bomma
for _name in `cat f.txt`
do
    echo "$_name"
    _RESULT="$(ping -t 1 -c 1 $_name | grep received | awk '{print $7}')"
    echo $_RESULT
    if [ $_RESULT == 100.0% ]
    then 
        echo "DOWN"
    else 
        echo "UP"    
    echo " "
    fi
done

