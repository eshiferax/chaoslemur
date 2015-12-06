#!/bin/python
#CL_MeshUniformTest.py
#Emmanuel Shiferaw
#Davis Gossage

import os
import unittest
import chaosgen as cg
import sys
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class CLMeshParetoTest(unittest.TestCase):

    def testGenerateConfigsAndReturnContextMeshPareto(self):
        config_gen = cg.ChaosLemurConfigGenerator(4, "mesh", "pareto",2.3)
        config_gen.generateConfigsAndReturnContext()

if __name__ == '__main__':
    unittest.main()
