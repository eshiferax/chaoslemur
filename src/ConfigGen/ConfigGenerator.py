#!/bin/python
#ConfigGenerator.py
#Emmanuel Shiferaw
#Davis Gossage

import subprocess
import json

###
# Given desired number of routers and topology, will generate
# bgpd.conf quagga BGP configuration files and place them in specific location
# Should create separate directory, "context" for each bgpd.conf file, with its own Dockerfile, etc

# num_routers - desired # of routers in network
# topology - desired layout of nodes
# path - location to save new bgpd.conf files
###
def generateConfigs(num_routers, topology, path):

    ## Get docker network inspection info on default 'bridge' docker network
    inspectProc = subprocess.Popen(["sudo", "docker", "network", "inspect", "bridge"], stdout=subprocess.PIPE)
    (inspectResponse, err) = inspectProc.communicate()
    
    ## TODO: Extract subnet/gateway from JSON response

    ## TODO: Build bgpd.conf string for each router, save

    print inspectResponse

generateConfigs(1,2)
