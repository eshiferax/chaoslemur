#############################
# build_and_run_containers.sh
# Emmanuel Shiferaw
# Davis Gossage
# Commands for configuring quagga on docker taken from:
# http://anton-baranov.blogspot.com/2015/03/using-quagga-with-docker-containers.html
############################

#Build volumes for containers
mkdir -p ~/volumes/quagga/R1
mkdir -p ~/volumes/quagga/R2

sudo setfacl -R -m u:100:rwx ~/volumes/quagga
sudo setfacl -R -m:g:101:rwx ~/volumes/quagga

#Set up quagga configurations for each container
echo "hostname R1\npassword zebra" > ~/volumes/quagga/R1/bgpd.conf
echo "hostname R1\npassword zebra" > ~/volumes/quagga/R1/zebra.conf
echo "hostname R2\npassword zebra" > ~/volumes/quagga/R2/bgpd.conf
echo "hostname R2\npassword zebra" > ~/volumes/quagga/R2/zebra.conf

#Run containers
sudo docker run -P --hostname=R1 --name=R1 -d -v ~/volumes/quagga/R1:/etc/quagga abaranov/quagga

sudo docker run -P --hostname=R2 --name=R2 -d -v ~/volumes/quagga/R2:/etc/quagga abaranov/quagga


