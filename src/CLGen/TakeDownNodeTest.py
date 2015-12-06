#!/bin/python
#TakeDownNodeTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaos as cl
import sys
import os
import time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class ChaosLemurTest(unittest.TestCase):

    def testTakeDownRandomNode(self):
        print "\nTaking down node %s..\n" % (node_taken_down) 
        running_CL = cl.ChaosLemur()
        node_taken_down = running_CL.takeDownRandomNode()
        time.sleep(2)
        print "Table after takedown... \n"
        time.sleep(1)
        running_CL.showAliveIPRoute(node_taken_down)

if __name__ == '__main__':
    unittest.main()

