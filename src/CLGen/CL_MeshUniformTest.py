#!/bin/python
#CL_MeshUniformTest.py
#Emmanuel Shiferaw
#Davis Gossage

import unittest
import chaosgen as cg
import sys
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class CLMeshUniformTest(unittest.TestCase):

    def testGenerateConfigsAndReturnContextMesh(self):
        config_gen = cg.ChaosLemurConfigGenerator(4, "mesh", "uniform")
        config_gen.generateConfigsAndReturnContext()

if __name__ == '__main__':
    unittest.main()
