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

    # Get portion of conf template listing router IP, neighbo
    with open ("bgpd.conf.template", "r") as tfile:
        bgpd_template = tfile.readlines()
        router_portion = bgpd_template[13:19]

    ## Get docker network inspection info on default 'bridge' docker network
    inspectProc = subprocess.Popen(["sudo", "docker", "network", "inspect", "bridge"], stdout=subprocess.PIPE)
    (inspectResponse, err) = inspectProc.communicate()
    
    ## Extract subnet/gateway from JSON response
    jsonResp = json.loads(inspectResponse)[0]
    subnet = jsonResp["IPAM"]["Config"][0]["Subnet"]

    ## TODO: Build bgpd.conf string for each router, save
    all_configs = []
    for rt in range(1, num_routers+1):
        curr_conf = buildConf(num_routers, rt)   
        all_configs.append(curr_conf)
  
    print router_portion
    print "Subnet: " + subnet

###
#
###
def buildConf(num, curr):
   

###
# Return simple
###
def neighborString(subnet, no):
    return "neighbor " + subnet[:-1] + str(no)



generateConfigs(1,2,".")
