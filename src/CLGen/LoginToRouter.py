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

def showIPRoute():
    running_CL = cl.ChaosLemur()
    running_CL.attachTo(int(sys.argv[1]))

showIPRoute()
