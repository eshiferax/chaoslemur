#!/bin/python
#ChaosLemurConfigGeneratorTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaosgen as cg
import sys
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class ChaosLemurConfigGeneratorTest(unittest.TestCase):
    
    def testNeighborString(self):
        self.assertEqual(cg.ChaosLemurConfigGenerator.neighborString("172.17.0.0", 2, 7675), "neighbor 172.17.0.2 remote-as 7675\n")
    
    def testBuildTopologyPortionMesh(self):
        self.assertEqual(cg.ChaosLemurConfigGenerator.buildTopologyPortionMesh(4,2, "172.17.0.0"), ["neighbor 172.17.0.2 remote-as 7675\n", "neighbor 172.17.0.4 remote-as 7675\n", "neighbor 172.17.0.5 remote-as 7675\n"])            

    def testGetSubnets(self):
        req_list = cg.ChaosLemurConfigGenerator.getSubnets(6)
        self.assertEqual(6, len(req_list))

if __name__ == '__main__':
    unittest.main()
