#!/bin/python
#chaosgen.py
#Emmanuel Shiferaw
#Davis Gossage
# CS514: Computer Networks and Distributed Systems

# Contains classes used to destroy

import datetime

class ChaosLemur:

    def __init__(self):
        self.failure_event_list = [] # (event, time)

    ###
    # Take down Node
    ###
    def takeDownNode(self, num):
        tdCommand = "sudo docker stop quag%s" % (num)
        os.system(tdCommand)
        self.failure_event_list.append((num, datetime.datetimenow()))

    ###
    # Reverse all failures
    ###
    def reverseFailures(self):
        
        for event in self.failure_event_list:
            # TODO: Implement
            print "Reversing failure: "




class ChaosLemurEvent:

    def __init__(self, typ, time):
        self.event_type = typ
        self.time = time



