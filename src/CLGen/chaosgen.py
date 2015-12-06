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
import random
# import docker-py



class ChaosLemurConfigGenerator:
      
    DEFAULT_AS = 7675
    def __init__(self, num_routers, topology, net_distrib, dist_param_1=1, dist_param_2=10):
        # Take input for choice of "distribution" of number of networks
        self.num_routers = num_routers
        self.topology = topology
        self.distribution = net_distrib
        self.param1 = dist_param_1
        self.param2 = dist_param_2
        
        self.bgpd_template = []
        self.subnet = ""
        self.subnet_amounts = [0 for i in range(1,num_routers+1)]
        self.loadTemplate() 
        self.calculateDistributions()  
    
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
    # Given distribution pattern specified, calculate number of subnets initially loaded into each router.
    ###
    def calculateDistributions(self):
        
        for i in range(0, self.num_routers):
            if(self.distribution == "uniform"):
                dval = random.randint(self.param1, self.param2)
            elif self.distribution == "lognormal":
                dval = int(random.lognormvariate(self.param1, self.param2))
            elif self.distribution == "pareto":
                dval = int(random.paretovariate(self.param1))
            if dval > 20:
                dval = 20
            elif dval < 1:
                dval = 1
            self.subnet_amounts[i] = int(dval)
        print self.subnet_amounts


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
        # print "Subnet: " + self.subnet
        
        ## Build bgpd.conf string for each router, save
        all_configs = []
        for rt in range(1, self.num_routers+1):
            # topology_to_method
            if self.topology == "mesh":
                curr_conf = ChaosLemurConfigGenerator.buildTopologyPortionMesh(self.num_routers, rt, self.subnet[:-3])
            elif self.topology == "hub":
                curr_conf = ChaosLemurConfigGenerator.buildTopologyPortionHub(self.num_routers, rt, self.subnet[:-3], 2)
            all_configs.append((rt, curr_conf))
        bgpd_confs = self.__makeConfigs(all_configs)
        context = self.__makeContext(bgpd_confs)
        
    
    ###
    #
    ###
    def __makeContext(self, bgpd_confs):
        root_dir_name = ChaosLemurConfigGenerator.addTimeStamp("_ChaosLemur_" + self.topology + "_" + self.distribution)
        if not os.path.exists(root_dir_name):
            os.makedirs(root_dir_name)
        
        contextGen = ChaosLemurContextGenerator(bgpd_confs, root_dir_name)
        contextGen.buildContext()
        contextGen.buildContainers()
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
            ind = list_of_portions.index(tupl)
            num_subnets = self.subnet_amounts[ind]
            start_line = network_line + num_subnets
            
            router_statement = "bgp router-id " + self.subnet[:-4] + str(tupl[0]+1) + "\n"
            cf_portion = tupl[1]
                          
            end_line = start_line + len(cf_portion) + 1
            bgpd = self.bgpd_template[:]
            # insert blank lines equal to amount of subnets
            bgpd = bgpd[:network_line] + ["network BLANK" for i in range(0,num_subnets)] + bgpd[start_line:]

            bgpd[router_line] = router_statement
            bgpd[start_line:end_line] = cf_portion
            bgpd[network_line:start_line] = [("network " + subnet) for subnet in ChaosLemurConfigGenerator.getSubnets(num_subnets)]
            #bgpd[network_line] = "network " + self.subnet + "\n"
            
            all_bgpd.append(bgpd)

        return all_bgpd



    ###
    # Build bgpd.conf file from template for specific router number, given total number
    # For "Full Mesh" configuration
    ###
    @staticmethod
    def buildTopologyPortionMesh(num, curr, subnet):
        all_except_me = range(2, num+2)
        all_except_me.remove(curr+1)
        neighbor_portion = [ChaosLemurConfigGenerator.neighborString(subnet, neighbor, ChaosLemurConfigGenerator.DEFAULT_AS) for neighbor in all_except_me]        
        return neighbor_portion

    ###
    # Build bgpd.conf file from template for specific router number, given total number
    # For "Hub" configuration
    ###
    @staticmethod
    def buildTopologyPortionHub(num, curr, subnet, hub_num):
        
        if(curr == hub_num):
            all_except_me = range(2, num+2)
            all_except_me.remove(curr+1)
            neighbor_portion = [ChaosLemurConfigGenerator.neighborString(subnet, neighbor, ChaosLemurConfigGenerator.DEFAULT_AS) for neighbor in all_except_me]
        else:
            neighbor_portion = ChaosLemurConfigGenerator.neighborString(subnet, hub_num, ChaosLemurConfigGenerator.DEFAULT_AS)
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
    def neighborString(subnet, no, remote_as):
        return "neighbor " + subnet[:-1] + str(no) + " remote-as " +  str(remote_as) + "\n"

    ###
    # Return X random prefixes from subnets.txt pool
    ###
    @staticmethod
    def getSubnets(num):
        # Get pool to choose from
        with open ("subnets.txt", "r") as tfile:
            all_nets  = tfile.readlines()
  
        to_return = []
        while len(to_return) < num:
            to_return.append(all_nets[random.randint(0,len(all_nets)-1)])

        return to_return

class ChaosLemurContextGenerator:

    def __init__(self, configs, root):
        self.bgpd_list = configs
        self.root_path = root
        self.failure_event_list = [] # (event, time)
 
    def buildContext(self):
        for bgpd_conf in self.bgpd_list:
            print "Conf: " + str(self.bgpd_list.index(bgpd_conf))
            self.copyInFiles(bgpd_conf, self.bgpd_list.index(bgpd_conf))
        
        
        
    def copyInFiles(self, bgpd_conf, no):
        this_container_dir = "router%s" % (no)
        this_container_path = self.root_path + "/" + this_container_dir
        if not os.path.exists(this_container_path):
            os.makedirs(this_container_path)
        
        osCommands = []
        copyQuaggaInitCommand = "cp quagga-init %s/%s/" % (self.root_path, this_container_dir); osCommands.append(copyQuaggaInitCommand); 
        copyDockerfileCommand = "cp Dockerfile.template %s/%s/Dockerfile" % (self.root_path, this_container_dir); osCommands.append(copyDockerfileCommand);
        copyZebraCommand = "cp zebra.conf %s/%s/zebra.conf" % (self.root_path, this_container_dir); osCommands.append(copyZebraCommand);
        copyVtyshCommand = "cp vtysh.conf %s/%s/vtysh.conf" % (self.root_path, this_container_dir); osCommands.append(copyVtyshCommand);
        # copyIdRSACommand = "sudo cp id_rsa* %s/%s/" % (self.root_path, this_container_dir); osCommands.append(copyIdRSACommand);
        # copyQuaggaSHCommand = "cp quagga.sh %s/%s/" % (self.root_path, this_container_dir); osCommands.append(copyQuaggaSHCommand);
        bgpd_file_loc = "%s/%s/bgpd.conf" % (self.root_path, this_container_dir)
        bgpd_file = open(bgpd_file_loc, "w")
        bgpd_file.writelines(bgpd_conf)
        bgpd_file.close() 
        
        for command in osCommands:
            os.system(command);

    ###
    # Build and run all generated containers
    ###
    def buildContainers(self):
        for bgpd_conf in self.bgpd_list:
            i = self.bgpd_list.index(bgpd_conf)
            this_dir = "%s/router%s" % (self.root_path, i)
            buildCommand = "sudo docker build -t quag%s %s" % (i, this_dir)
            runCommand = "sudo docker run --privileged -it -d quag%s" % (i)
            os.system(buildCommand)
            os.system(runCommand)
        
        #getNodeNamesCommand = "sudo docker ps | awk '{print $14}' | sed '/^\s*$/d'"
    






















