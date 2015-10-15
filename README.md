# ChaosLemur
Injecting failures into BGP.

Inspired by [Chaos Engineering](http://principlesofchaos.org) from Netflix and [SDN ChaosMonkey](http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p371.pdf). 

Uses [Quagga](http://www.nongnu.org/quagga/) for building virtual network, [Docker](http://docker.com) for running separate virtual BGP routers/ASes on containers.

## How to Build/Run
  * As this is still an extremely early-stage project, we don't have any instructions yet. Stay tuned.

## Current Features
  * Scripts for configuring and running docker containers with quagga, able to speak BGP to each other.

## Future Features
* API will be added to Quagga's BGP implementation to introduce single-node and single-link failures.
* System will be built for causing these failures in a controlled way (scheduling, timing, etc.)
* 'Failure response' logging/analysis system that measures time until BGP convergence and other metrics immediately after failures
* Allow user to build initial "Experiment Plan" for failures that will be introduced to BGP network, and then have them continuously updated


