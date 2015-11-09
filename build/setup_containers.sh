#!/bin/bash

# setup.sh
# Automated setup of ubuntu docker environment for ChaosLemur
# Emmanuel Shiferaw
# Davis Gossage

##Stop, remove ALL existing containers
# NOTE: may take a bit of time
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)

###
# install pip, docker-py
###
sudo apt-get install python-setuptools
sudo easy_install docker-py

###
# install lxterminal
###
# Uncomment below if GUI needed
# sudo apt-get install lxterminal

## 
# generate key for ssh into containers
##
echo -e  'y\n'|ssh-keygen -q -t rsa -N "" -f ./id_rsa

###
# build Docker image from Dockerfile
### TRANSITIONING TO python script
#sudo docker build -t quagga .


###
# Run containers
###
