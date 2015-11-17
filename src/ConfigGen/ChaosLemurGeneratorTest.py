#!/bin/python
#ChaosLemurGeneratorTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaosgen as cg

class ChaosLemurConfigTest(unittest.TestCase):
    
    def testNeighborString(self):
        self.assertEqual(cg.ChaosLemurGenerator.neighborString("172.17.0.0", 2), "neighbor 172.17.0.2")
    
    # Negative test for now
    def testBuildConf(self):
        self.assertEqual(cg.ChaosLemurGenerator.buildConf(4,2, "172.17.0.0"), "neighbor 172.17.0.1\nneighbor 172.17.0.3\nneighbor 172.17.0.4")            

if __name__ == '__main__':
    unittest.main()
