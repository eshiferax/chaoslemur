#!/bin/bash
# Automated setup of ubuntu docker environment for ChaosLemur
# Emmanuel Shiferaw
# Davis Gossage

###
# install pipework, lxterminal
###
sudo bash -c "curl https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework > /usr/local/bin/pipework"
PATH=$PATH:/usr/local/bin/pipework
sudo apt-get install lxterminal

###
# build Docker image from
###
sudo docker build -t quagga .
