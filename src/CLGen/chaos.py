#!/bin/python
#chaosgen.py
#Emmanuel Shiferaw
#Davis Gossage
# CS514: Computer Networks and Distributed Systems

# Contains classes used to destroy

import datetime
import random

class ChaosLemur:

    def __init__(self, num_routers):
        self.event_list = [] # (event, time)
        self.num_routers = num_routers

    ###
    # Take down Node
    ###
    def takeDownNode(self, num):
        tdCommand = "sudo docker stop quag%s" % (num)
        os.system(tdCommand)
       
        failure_event = ChaosLemurEvent("Failure", datetime.datetime.now()) 
        self.event_list.append(failure_event)

    ###
    # Reverse all failures
    ###
    def reverseFailures(self):
        
        for event in self.event_list:
            # TODO: Implement
            if event.event_type == "Failure":
                recover_command = "sudo docker start quag%s" % (event.num)
                os.system(recover_command)
                print "Reversing failure for node %s" % (event.num)

    ###
    # Take down RANDOM node
    ###
    def takeDownRandomNode(self):
        
        node_to_fail = random.randint(0, self.num_routers)
        self.takeDownNode(node_to_fail)

class ChaosLemurEvent:

    def __init__(self, typ, time, number):
        self.event_type = typ
        self.time = time
        self.num = number



