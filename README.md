# ChaosLemur
Injecting failures into BGP.

Inspired by [Chaos Engineering](http://principlesofchaos.org) from Netflix and [SDN ChaosMonkey](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p371.pdf). 

Uses [Quagga](http://www.nongnu.org/quagga/) for building virtual network, [Docker](http://docker.com) for running separate virtual BGP routers/ASes on containers.

## How to Build/Run
  * This system was tested on a VM running Bitnami's Ubuntu base image, provided by Duke's [Innovation Co-Lab](https://colab.duke.edu/).
  * Many ChaosLemur scripts require root access, and have been tested primarily with `sudo`. 
  * To install dependencies (docker), run `sudo sh install/cl_install.sh`.
  * To run the pre-defined test setting up a ChaosLemur experiment with 4 routers in a mesh topology,
    run `sudo python src/CLGen/CL_MeshUniformTest.py`.
  * All the other pre-defined tests are python scripts following the same convention: CL_HubPareto.py, CL_MeshLognormal.py, etc.
  * After running one of the pre-defined tests, you can get the names of all running containers by running `sh src/CLGen/utility/running_container_names.sh`
  * You can then log into the vtysh console of any router with: `sudo docker attach $NAME `, where $NAME is any from the list obtained from the previous instruction.
  * You can also simply run `sudo python LogInToRouter.py $NUM`, where $NUM is the index of the router (running from 0 to the total number of routers minus 1).
  * You can show the table of prefixes on any router (current state of knowledge) with the src/CLGen/ShowIPRoute.py script. It takes in as an argument the 'index' of the router whose information is being requested. This index is simply the position of the router's name in the list returned by the aformentioned running_container_names script.
  * To run a test that takes down a router, displays the routing table of another (still alive) router, and reverses it (brings back node), run `sudo python src/CLGen/ChaosLemurTest.py.`
  * To run a test that simply takes down a random router, run `sudo python src/CLGen/TakeDownNodeTest.py`

## Current Progress
  * Scripts for configuring and running docker containers with quagga, able to speak BGP to each other.
  * Ability to input desired number of routers, distribution pattern/paremeters for number of networks initially advertised, and desired network topology (choice of mesh/hub).
  * API methods to introduce single-node failures and reverse them. (Taking down individual routers).
  * API method to report BGP routing table of routers.
  * API method for link failures (NOT FUNCTIONAL - vtysh does not accept "neighbor *peer* shutdown" command).

## Planned Features
* Parsing, interpretation of full BGP logs.


# Acknowledgements
* Used [docker-quagga](https://github.com/ewindisch/docker-quagga) as a starting point for a Docker image that would work well with Quagga.

