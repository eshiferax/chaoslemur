#!/bin/python
#chaosgen.py
#Emmanuel Shiferaw
#Davis Gossage
# CS514: Computer Networks and Distributed Systems

# Contains classes used to set up the ChaosLemur environment for experiments to be run


import subprocess
import json
import datetime
import os
# import docker-py

class ChaosLemurConfigGenerator:
    
    def __init__(self, num_routers, topology):
        self.num_routers = num_routers
        self.topology = topology
        
        self.bgpd_template = []
        self.subnet = ""
        self.loadTemplate() 
    
    
    def recycle(self, num_routers, topology):
        self.num_routers = num_routers
        self.topology = topology   
    
    ###
    # Load bgpd.conf.template file from fs, extract portion describing self/neighbors
    ###
    def loadTemplate(self):
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
    def generateConfigsAndReturnContext(self):

        ## Get docker network inspection info on default 'bridge' docker network
        inspectProc = subprocess.Popen(["sudo", "docker", "network", "inspect", "bridge"], stdout=subprocess.PIPE)
        (inspectResponse, err) = inspectProc.communicate()

        ## Extract subnet/gateway from JSON response
        jsonResp = json.loads(inspectResponse)[0]
        self.subnet = jsonResp["IPAM"]["Config"][0]["Subnet"]
        print "Subnet: " + self.subnet
        ## TODO: Build bgpd.conf string for each router, save
        all_configs = []
        for rt in range(1, self.num_routers+1):
            # topology_to_method
            curr_conf = ChaosLemurConfigGenerator.buildTopologyPortionMesh(self.num_routers, rt, self.subnet[:-3])
            all_configs.append((rt, curr_conf))
        bgpd_confs = self.__makeConfigs(all_configs)
        context = self.__makeContext(bgpd_confs)

    
    ###
    #
    ###
    def __makeContext(self, bgpd_confs):
        root_dir_name = ChaosLemurConfigGenerator.addTimeStamp("_ChaosLemurContext")
        if not os.path.exists(root_dir_name):
            os.makedirs(root_dir_name)
        
        contextGen = ChaosLemurContextGenerator(bgpd_confs, root_dir_name)
        contextGen.buildContext()
        
        return root_dir_name

    ###
    # Given list of neighbor-listing portions that contain topology info,
    # builds 4 full bgpd.conf files (as lists of lines) , returns list of those lists
    ###
    def __makeConfigs(self, list_of_portions):
        all_bgpd = []
        start_line = 15
        network_line = 14
        router_line = 13
        for tupl in list_of_portions:
            router_statement = "router bgp " + self.subnet[:-4] + str(tupl[0]) + "\n"
            cf_portion = tupl[1]
            end_line = start_line + len(cf_portion) + 1
            bgpd = self.bgpd_template[:]
            bgpd[router_line] = router_statement
            bgpd[start_line:end_line] = cf_portion
            bgpd[network_line] = "network " + self.subnet + "\n"
            all_bgpd.append(bgpd)

        return all_bgpd



    ###
    # Build bgpd.conf file from template for specific router number, given total number
    # For "Full Mesh" configuration
    ###
    @staticmethod
    def buildTopologyPortionMesh(num, curr, subnet):
        all_except_me = range(1, num+1)
        all_except_me.remove(curr)
        neighbor_portion = [ChaosLemurConfigGenerator.neighborString(subnet, neighbor) for neighbor in all_except_me]        
        return neighbor_portion

    ###
    # Build bgpd.conf file from template for specific router number, given total number
    # For "Hub" configuration
    ###
    @staticmethod
    def buildTopologyPortionHub(num, curr, subnet, hub_num):
        ##TODO: Implement
        if(curr == hub_num):
            all_except_me = range(1, num+1)
            all_except_me.remove(curr)
            neighbor_portion = [ChaosLemurConfigGenerator.neighborString(subnet, neighbor) for neighbor in all_except_me]
        else:
            neighbor_portion = ChaosLemurConfigGenerator.neighborString(subnet, hub_num)
        return neighbor_portion
    ###
    # Add timestamp to any name
    ###
    @staticmethod
    def addTimeStamp(name):
        FORMAT = '%Y%m%d%H%M%S'
        datestring = datetime.datetime.now().strftime(FORMAT)
        new_name = '%s_%s' % (name, datestring)
        return new_name

    ###
    # Return simple "neighbor IP" string for given router number
    ###
    @staticmethod
    def neighborString(subnet, no):
        return "neighbor " + subnet[:-1] + str(no) + "\n"


class ChaosLemurContextGenerator:

    def __init__(self, configs, root):
        self.bgpd_list = configs
        self.root_path = root

    def buildContext(self):
        for bgpd_conf in self.bgpd_list:
            print "Conf: " + str(self.bgpd_list.index(bgpd_conf))
            self.copyInFiles(bgpd_conf, self.bgpd_list.index(bgpd_conf))
        
        
        
    def copyInFiles(self, bgpd_conf, no):
        this_container_dir = "router%s" % (no)
        this_container_path = self.root_path + "/" + this_container_dir
        if not os.path.exists(this_container_path):
            os.makedirs(this_container_path)
        copyDockerfileCommand = "cp Dockerfile.template %s/%s/Dockerfile" % (self.root_path, this_container_dir)
        bgpd_file_loc = "%s/%s/bgpd.conf" % (self.root_path, this_container_dir)
        bgpd_file = open(bgpd_file_loc, "w")
        bgpd_file.writelines(bgpd_conf)
        bgpd_file.close()    






























