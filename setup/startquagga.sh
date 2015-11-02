#!/bin/bash

# AJ NOURI: cciethebeginning.wordpress.com
# Email: ajn.bin@gmail.com

# $1 = Image tag
# $2 = Container name

function networking(){
   # $1 : The 1st argument passed to the function, container ID.
   # Configure additional interfaces on the container:
   # - host bridge to  which the interfaces is connected
   # - container interface IP
   # - gateway: the last configured gateway is used
   echo "Container networking... \n"
   while true; do
       read -p 'Continue? [Yy] [Nn]' NET
       case $NET in
       [Yy]* ) break;;
       [Nn]* ) exit;;
       esac
   done
   while true; do
       read -p 'Host bridge interface => ' BR
       read -p 'Container: interface (a new one) connected to host bridge => ' INT
       read -p 'Container: interface IP => ' IP
       read -p 'Container: interface IP mask => ' MASK
       read -p 'Container: interface next-hop IP (GNS3) => ' NH
       if sudo pipework $BR -i $INT $1 $IP/$MASK@$NH ; then
        sudo echo "command: >> sudo pipework $BR -i $INT $1 $IP/$MASK@$NH << successfully executed."
    else
        echo "pipework error!" 1>&2
    fi
       read -p 'Would you like to continue with network configuration? [Yy] [Nn]  ' CONT
       case $CONT in
            [Yy]* ) ;;
            [Nn]* ) exit;;
            * ) echo "Please answer yes [Yy]* or no [Nn]*";;
            esac
    done
   }

if [ "$#" -ne 2 ]
then
    echo "Usage: `basename $0` {image_tag} {container_name}" ;exit 2
fi

INAME=$1
CNAME=$2
IID="$(sudo docker images | grep $INAME | awk '{ print $3; }')"
RCID="$(sudo docker ps -a | grep $CNAME | grep Up | awk '{ print $1; }')"
CID="$(sudo docker ps -a | grep $CNAME | grep Exited | awk '{ print $1; }')"

if [[ $RCID ]]
then
    while true; do
        echo "There is a running container with the same name, $CNAME :CID= $RCID"
        read -p 'Would you like to [E]xit it, [D]elete it, [A]ttach a console or [S]kip? [Ee]/[Dd]/[Aa]/[Ss]  ' RESP
        case "$RESP" in
        [Ee]* ) sudo docker stop $RCID;exit;;
        [Ss]* ) networking $CID; exit;;
        [Dd]* ) sudo docker stop $RCID; sudo docker rm $RCID; exit;;
        [Aa]* ) lxterminal -e "sudo docker attach $RCID";exit;;
        * ) echo "Please answer yes [Yy]* or no [Nn]*";;
        esac
    done
fi

if [[ $CID  ]]
then
    echo "Container ID: $CID"
    while true; do
        echo "There is a stopped container with the same name, $CNAME :CID= $CID"
        read -p 'Would you like to [R]un it or [D]elete it or [S]kip? [Rr]/[Dd]/[Ss]  ' RESP
        case $RESP in
        [Rr]* ) sudo docker start $CID;lxterminal -e "sudo docker attach $CNAME"; sleep 2;networking $CID; break;;
        [Dd]* ) sudo docker stop $CID; sudo docker rm $CID; exit;;
        [Ss]* ) exit;;
        * ) echo "Please answer yes [Yy]* or no [Nn]*";;
        esac
    done
else
    echo "Spawning a new container"
    lxterminal -e "sudo docker run -t -i --privileged=true --name $CNAME $IID /bin/bash"
    sleep 2
    CID="$(sudo docker ps | grep $CNAME | awk '{ print $1; }')"
    networking $CID
fi
