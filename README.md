# ChaosLemur
Injecting failures into BGP.

Inspired by [Chaos Engineering](http://principlesofchaos.org) from Netflix and [SDN ChaosMonkey](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p371.pdf). 

Uses [Quagga](http://www.nongnu.org/quagga/) for building virtual network, [Docker](http://docker.com) for running separate virtual BGP routers/ASes on containers.

## How to Build/Run
  * To install all dependencies, run cl_install.sh
  * To run the pre-defined test setting up a ChaosLemur experiment with 4 routers in a mesh topology,
    run "sudo python src/CLGen/ChaosLemurConfigGenerator.py".


## Current Progress
  * Scripts for configuring and running docker containers with quagga, able to speak BGP to each other.
  * API to introduce single-node failures and reverse them. (Taking down individual routers).
  * Logging of BGP 

## Planned Features
* API for link failures.
* Parsing, interpretation of BGP logs for measuring "response" to failures.
* Allow user to build initial "Experiment Plan" for failures that will be introduced to BGP network, and then have them continuously updated.


