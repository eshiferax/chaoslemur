# ChaosLemur
Injecting failures into BGP.

Inspired by [Chaos Engineering](http://principlesofchaos.org) from Netflix and [SDN ChaosMonkey](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p371.pdf). 

Uses [Quagga](http://www.nongnu.org/quagga/) for building virtual network, [Docker](http://docker.com) for running separate virtual BGP routers/ASes on containers.

## How to Build/Run
  * Stay tuned.

## updates

 * (11/2) - switched over to using ubuntu images and a different script structure to get everything ready to be networked. Still
	    using pipework - next step is to add a piece in the 'setup.sh' script to get the container IDs of the new containers
            and give them to 'startquagga.sh', which will use them as arguments for pipework.
            THEN need to write scripts that will run on each container, to install/set up quagga for BGP. This includes abstracting
            the BGP configuration out (luckily quagga does that as bgpd.conf file) to allow for diff topologies. Need to think of way
            to cleanly automate the different 'experiments'.
            THEN need to add Quagga (maybe as git sub-module, if we do end up having to edit source)  and get to work on failure injection.

 * (11/3) - Docker built-in [advanced networking](http://blog.docker.com/2015/11/docker-1-9-production-ready-swarm-multi-host-networking/) is now
            production ready and in Docker 1.9!!! So I don't think pipework is necessary anymore, but we'll see. The current
            Dockerfile and setup_containers.sh script work to prepare the host environment, build image from file, and start one container. 

 * (11/8) - Started writing a script to make different BGP configuration files for Quagga. These configuration files will define our topologies 
            (and we will need to have a different one for each container) , so we need a way to generate them, given a desired topology and number
            of routers. Also, in order to create x different docker images corresponding to each BGP configuration file, will need to generate Dockerfiles
            programmatically alongside the config files. This will require us to change the setup_containers.sh build process a bit (perhaps transitioning
            fully to [docker-py](https://docker-py.readthedocs.org/en/latest/) for the whole process (outside setting up dependencies, etc). 

## Current Progress
  * Scripts for configuring and running docker containers with quagga, able to speak BGP to each other.

## Planned Features
* API will be added to Quagga's BGP implementation to introduce single-node and single-link failures.
* System will be built for causing these failures in a controlled way (scheduling, timing, etc.)
* 'Failure response' logging/analysis system that measures time until BGP convergence and other metrics immediately after failures
* Allow user to build initial "Experiment Plan" for failures that will be introduced to BGP network, and then have them continuously updated


