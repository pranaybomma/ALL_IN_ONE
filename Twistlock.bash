#!/usr/bin/bash
# Author: Pranay Bomma

cat <<- Twist
    ###################
    1. Please grep the details of region/clustername before stating the process
    2. Exit
    ################### 
Twist
echo " "
echo -n "Continue or Exit ?? : "
read _comments
clear
case "$_comments" in

    1) echo -n "Enter Region: "; read _region; echo -n "Enter clustername: "; read _cluster; echo -n "Enter profilename: "; read _profile;
       echo -n "Please insert the URL:"; read _OPTION; echo $_OPTION > temp.txt; wget $_OPTION;
       d=$(awk -F . '{print$3}' temp.txt | grep -P twist.* -o); rm temp.txt; mkdir $d; echo -n "########Extracting directory########"; echo" "; tar xvzf $d.tar.gz -C $d;
       export KUBECONFIG=~/.kube/$_cluster;
       (aws eks update-kubeconfig --kubeconfig ~/.kube/$_cluster --name $_cluster --region $_region --profile $_profile); cd $d;
       (linux/twistcli console export kubernetes --service-type LoadBalancer); sed -i '0,/^---$/d' twistlock_console.yaml; sed -i 's/8083/443/g' twistlock_console.yaml;
       sed -i '/^.*- name: mgmt-http$/{N;d;}' twistlock_console.yaml; sed -i '/^.*- name: MANAGEMENT_PORT_HTTP$/{N;d;}' twistlock_console.yaml; 
       sed -i '16 i\  annotations:\n    service.beta.kubernetes.io/aws-load-balancer-internal: 0.0.0.0/0' twistlock_console.yaml; kubectl create -f twistlock_console.yaml -n twistlock;
       ##wget $_OPTION;
       #echo -n "########creating directory########";
       #echo " ";
       #mkdir $d;
       #echo -n "########Extracting directory########";
       #echo " ";
       #tar xvzf $d.tar.gz -C $d;

       ;;
    2) exit
       ;;
esac
