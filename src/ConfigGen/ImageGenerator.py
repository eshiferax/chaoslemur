#!/bin/python
#ImageGenerator.py
#Emmanuel Shiferaw
#Davis Gossage

import subprocess
import json
from docker import Client
import os

###
cli = Client(base_url='unix://var/run/docker.sock')


###
# Given path to 'top' of directory tree containing X contexts/config files, generate
# X docker images

# path - locationf 
###
def generateImages(path):

    ## TODO: Get all directories at path
    #lsProc = subprocess.Popen("ls", stdout=subprocess.PIPE)
    #(lsResponse, err) = lsProc.communicate()
    allDirs = os.listdir(path)

    imageList = []
    ## TODO: Loop through directories, building image for each
    for dir in allDirs:
        currResponse = cli.build(path + dir)


###
# Given list of images generated, make one container for each image
###
def generateContainers(images):

                    
