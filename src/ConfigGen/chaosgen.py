#!/bin/python
#ChaosLemurGenerator.py
#Emmanuel Shiferaw
#Davis Gossage

import subprocess
import json
# import docker-py
class ChaosLemurGenerator:
    
    def __init__(self, num_routers, topology):
        self.num_routers = num_routers
        self.topology = topology
  
    ###
    # Given desired number of routers and topology, will generate
    # bgpd.conf quagga BGP configuration files and place them in specific location
    # Should create separate directory, "context" for each bgpd.conf file, with its own Dockerfile, etc

    # num_routers - desired # of routers in network
    # topology - desired layout of nodes
    # path - location to save new bgpd.conf files
    ###
    def generateConfigs(path):

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
        for rt in range(1, self.num_routers+1):
            curr_conf = buildConf(self.num_routers, rt)
            all_configs.append(curr_conf)

        print router_portion
        print "Subnet: " + subnet

    ###
    # Build bgpd.conf file from template for specific router number, given total number
    ###
    @staticmethod
    def buildConf(num, curr):
        ##TODO: Implement
        return

    ###
    # Return simple "neighbor IP" string for given router number
    ###
    @staticmethod
    def neighborString(subnet, no):
        return "neighbor " + subnet[:-1] + str(no)
