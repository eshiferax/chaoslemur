#!/bin/python
#ImageGenerator.py
#Emmanuel Shiferaw
#Davis Gossage

import subprocess
import json
from docker import Client

###
cli = Client(base_url='unix://var/run/docker.sock')


###
# Given path to 'top' of directory tree containing X contexts/config files, generate
# X docker images

# path - locationf 
###
def generateImages(path):

    ## TODO: Get all directories at path

    ## TODO: Loop through directories, building image for each



###
# Given list of images generated, make one container for each image
###
def generateContainers(images):

~                    
