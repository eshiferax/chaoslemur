#!/bin/python
#ChaosLemurGeneratorTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaosgen as cg

class ChaosLemurConfigGeneratorTest(unittest.TestCase):
    
    def testNeighborString(self):
        self.assertEqual(cg.ChaosLemurConfigGenerator.neighborString("172.17.0.0", 2), "neighbor 172.17.0.2")
    
    def testBuildTopologyPortionMesh(self):
        self.assertEqual(cg.ChaosLemurConfigGenerator.buildTopologyPortionMesh(4,2, "172.17.0.0"), "neighbor 172.17.0.1\nneighbor 172.17.0.3\nneighbor 172.17.0.4")            

    def testGenerateConfigs(self):
        config_gen = cg.ChaosLemurConfigGenerator(4, "mesh")
        config_gen.generateConfigs()

if __name__ == '__main__':
    unittest.main()
