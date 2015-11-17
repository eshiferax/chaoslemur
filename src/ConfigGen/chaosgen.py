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
        
        self.bgpd_template = []
        self.subnet = ""
        loadTemplate() 
       
    ###
    # Load bgpd.conf.template file from fs, extract portion describing self/neighbors
    ###
    def loadTemplate():
        # Get portion of conf template listing router IP, neighbor
        with open ("bgpd.conf.template", "r") as tfile:
            self.bgpd_template = tfile.readlines()
            # self.router_portion = bgpd_template[13:19]

    ###
    # Given desired number of routers and topology, will generate
    # bgpd.conf quagga BGP configuration files and place them in specific location
    # Should create separate directory, "context" for each bgpd.conf file, with its own Dockerfile, etc

    # path - location to save new bgpd.conf files
    ###
    def generateConfigs(path):

        ## Get docker network inspection info on default 'bridge' docker network
        inspectProc = subprocess.Popen(["sudo", "docker", "network", "inspect", "bridge"], stdout=subprocess.PIPE)
        (inspectResponse, err) = inspectProc.communicate()

        ## Extract subnet/gateway from JSON response
        jsonResp = json.loads(inspectResponse)[0]
        self.subnet = jsonResp["IPAM"]["Config"][0]["Subnet"]

        ## TODO: Build bgpd.conf string for each router, save
        all_configs = []
        for rt in range(1, self.num_routers+1):
            # topology_to_method
            curr_conf = buildTopologyPortionMesh(self.num_routers, rt, self.subnet)
            all_configs.append(curr_conf)

        saveConfigs(all_configs, path)
        print router_portion
        print "Subnet: " + self.subnet

    ###
    # Given list of neighbor-listing portions that contain topology info,
    # builds 4 full
    ###
    def __saveConfigs(list_of_configs, path):
    



    ###
    # Build bgpd.conf file from template for specific router number, given total number
    # For "Full Mesh" configuration
    ###
    @staticmethod
    def buildTopologyPortionMesh(num, curr, subnet):
        all_except_me = range(1, num+1)
        all_except_me.remove(curr)
        neighbor_portion = [ChaosLemurGenerator.neighborString(subnet, neighbor) for neighbor in all_except_me]        

        return "\n".join(neighbor_portion)

    ###
    # Build bgpd.conf file from template for specific router number, given total number
    # For "Hub" configuration
    ###
    @staticmethod
    def buildTopologyPortionHub(num, curr, subnet, hub_num):
        ##TODO: Implement


    ###
    # Return simple "neighbor IP" string for given router number
    ###
    @staticmethod
    def neighborString(subnet, no):
        return "neighbor " + subnet[:-1] + str(no)

