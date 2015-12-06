#!/bin/python
#ChaosLemurConfigGeneratorTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaos as cl
import sys
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class ChaosLemurTest(unittest.TestCase):

    def testGetSubnets(self):
        running_CL = cl.ChaosLemur()
        running_CL.showIPRoute(2)

if __name__ == '__main__':
    unittest.main()

