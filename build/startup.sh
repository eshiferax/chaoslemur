# add docker's source to apt-get sources
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D;

sudo echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list;

sudo apt-get update;

sudo apt-get purge lxc-docker*;

# now ready to install

sudo apt-get install docker-engine;
