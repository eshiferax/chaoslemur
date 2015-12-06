#!/bin/bash
# Emmanuel Shiferaw
# Davis Gossage

# Get just the names of running docker containers
sudo docker ps | awk '{print $14}' | sed '/^\s*$/d'
