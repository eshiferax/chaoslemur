#!/bin/bash

# setup.sh
# Automated setup of ubuntu docker environment for ChaosLemur
# Emmanuel Shiferaw
# Davis Gossage

##Stop, remove ALL existing containers
# NOTE: may take a bit of time
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docer ps -aq)

###
# install pipework, lxterminal
###
sudo bash -c "curl https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework > /usr/local/bin/pipework"
PATH=$PATH:/usr/local/bin/pipework
sudo apt-get install lxterminal

## 
# generate key for ssh into containers
##
echo -e  'y\n'|ssh-keygen -q -t rsa -N "" -f ./id_rsa

###
# build Docker image from Dockerfile
###
sudo docker build -t quagga .


###
# Run containers
###
