#!/usr/bin/bash
# Author: Pranay Bomma
# to push terraform on all the folders
clear

cat <<- TERRA
    ###################
    1. terraform init
    2. terraform plan
    3. terraform apply
    4. Exit
    ################### 
TERRA
echo " "
echo -n "What you wnat to do ?? : "
read _comments
clear

echo " "
cat <<- FORM
    ###################
    1. Commit on Prd
    2. Commit on SPrd
    3. Exit
    ###################    
FORM
echo " On which Envirnoment ?? : "
echo -n "enter the command: "
read _OPTION


case "$_comments" in

    1) comment=$"terraform init"
       ;;
    2) comment=$"terraform plan"
       ;;
    3) comment=$"terraform apply --auto-approve"
       ;;
    4) exit
       ;;
esac


case "$_OPTION" in

    1) cd tfsawsprod ; for d in ./*/*/ ; do (cd "$d" && echo "  " && echo "########## Pushing on "$(pwd | grep -o '[^/]\+$')"###############" && $comment && sleep 4 && break); done
       ;;
    2) ./connectivity.bash
       ;;
    3) exit
       ;;
esac