#############################
# setup_install.sh
# Emmanuel Shiferaw
# Davis Gossage

# Run this first.
############################

sudo apt-get install apt-transport-https
sudo echo "deb https://apt.dockerproject.org/repo ubuntu-precise main" > /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get purge lxc-docker*

sudo apt-get install docker-engine
sudo docker run hello-world
