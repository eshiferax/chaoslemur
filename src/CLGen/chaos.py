#!/bin/python
#chaosgen.py
#Emmanuel Shiferaw
#Davis Gossage
# CS514: Computer Networks and Distributed Systems

# Contains classes used to destroy and recover nodes and links in ChaosLemur,
# as well as observe network state of any node

import subprocess
import datetime
import random
import os
import chaosgen as cg

class ChaosLemur:

    def __init__(self):
        self.event_list = [] # (event, time)
        self.names = []
        namesProc = subprocess.Popen("sudo docker ps | awk '{print $14}' | sed '/^\s*$/d'", stdout=subprocess.PIPE, shell=True)
        (names, err) = namesProc.communicate()
        self.names = names.splitlines()
        self.names.reverse()
        self.num_routers = len(self.names)

    ###
    # Take down Node
    ###
    def takeDownNode(self, num):
        name_rt = self.names[num]
        tdCommand = "sudo docker stop %s" % (name_rt)
        os.system(tdCommand)
        
        failure_event = ChaosLemurEvent("Node Failure %s" % (num), datetime.datetime.now(), num) 
        self.event_list.append(failure_event)

    ###
    # Take down link
    ###
    def takeDownLink(self, rt1, rt2):
        rt_name = self.names[rt_1]
        rt2_address = cg.ChaosLemurConfigGenerator.addressString("172.17.0.0", rt2)
        show_ip_route_command = "sudo docker exec -i %s sh -c 'echo \"neighbor %s shutdown\" | vtysh'" % (rt_name, rt2_address)
        os.system(show_ip_route_command)

        failure_event = ChaosLemurEvent("Link Failure %s and %s" % (rt1, rt2), datetime.datetime.now(), (rt1, rt2))
        print "Link Failure %s and %s" % (rt1, rt2)

    ###
    # Reverse all failures
    ###
    def reverseFailures(self):
        
        for event in self.event_list:
            if "Failure" in event.event_type:
                recover_command = "sudo docker start " + self.names[event.num]
                os.system(recover_command)
                print "Reversing failure for node %s" % (event.num)
        
        recovery_event = ChaosLemurEvent("Full Recovery", datetime.datetime.now(), 0)
        self.event_list.append(recovery_event)

    ###
    # Take down RANDOM node. Return ID of node failed.
    ###
    def takeDownRandomNode(self):
        
        node_to_fail = random.randint(0, self.num_routers - 1)
        self.takeDownNode(node_to_fail)
        return node_to_fail

    ###
    # Take down RANDOM link. Return ID of link failed.
    ###
    def takeDownRandomLink(self):
        link_to_fail_node1 = random.randint(0, self.num_routers - 1)
        link_to_fail_node2 = range(0,self.num_routers).remove(link_to_fail_node1)[random.randint(0, num_routers-2)]
        self.takeDownLink(link_to_fail_node1, link_to_fail_node2)
        return (link_to_fail_node1, link_to_fail_node2)
    ###
    # Display prefixes loaded for router X
    ###
    def showIPRoute(self, rt_num):
        rt_name = self.names[rt_num]
        show_ip_route_command = "sudo docker exec -i %s sh -c 'echo \"show ip route\" | vtysh'" % (rt_name)
        os.system(show_ip_route_command)
    
    ###
    # Display prefixes loaded for ANY router that is still running
    ###
    def showAliveIPRoute(self, dead_one):
        rt_num = random.randint(0, len(self.names)-1)
        while rt_num == dead_one:
            rt_num = random.randint(0, len(self.names)-1)
        self.showIPRoute(rt_num)
     
    ###
    # Attach to specific router
    ###
    def attachTo(self, rt_num):
        rt_name = self.names[rt_num]
        attach_command= "sudo docker attach %s" % (rt_name)
        os.system(attach_command)
        
class ChaosLemurEvent:

    def __init__(self, typ, time, number):
        self.event_type = typ
        self.time = time
        self.num = number



