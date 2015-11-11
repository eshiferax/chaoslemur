#!/bin/python
#ChaosLemurGeneratorTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaosgen as cg

class ChaosLemurConfigTest(unittest.TestCase):
    
    def testNeighborString(self):
        self.assertEqual(cg.ChaosLemurGenerator.neighborString("127.17.0.0", 2), "neighbor 172.17.0.2")

if __name__ == '__main__':
    unittest.main()
