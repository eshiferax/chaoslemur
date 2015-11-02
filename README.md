# ChaosLemur
Injecting failures into BGP.

Inspired by [Chaos Engineering](http://principlesofchaos.org) from Netflix and [SDN ChaosMonkey](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p371.pdf). 

Uses [Quagga](http://www.nongnu.org/quagga/) for building virtual network, [Docker](http://docker.com) for running separate virtual BGP routers/ASes on containers.

## How to Build/Run
  * As this is still an extremely early-stage project, we don't have any instructions yet. Stay tuned.

## updates

 * (11/2) - switched over to using ubuntu images and a different script structure to get everything ready to be networked. Still
	    using pipework - next step is to add a piece in the 'setup.sh' script to get the container IDs of the new containers
            and give them to 'startquagga.sh', which will use them as arguments for pipework.

## Current Features
  * Scripts for configuring and running docker containers with quagga, able to speak BGP to each other.

## Future Features
* API will be added to Quagga's BGP implementation to introduce single-node and single-link failures.
* System will be built for causing these failures in a controlled way (scheduling, timing, etc.)
* 'Failure response' logging/analysis system that measures time until BGP convergence and other metrics immediately after failures
* Allow user to build initial "Experiment Plan" for failures that will be introduced to BGP network, and then have them continuously updated


