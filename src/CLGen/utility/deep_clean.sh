#!/bin/bash
# Emmanuel Shiferaw
# Davis Gossage

##Stop, remove ALL existing containers
# NOTE: may take a bit of time
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)

