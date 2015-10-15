#############################
# network_containers.sh
# Emmanuel Shiferaw
# Davis Gossage
# Commands for configuring quagga on docker taken from:
# http://anton-baranov.blogspot.com/2015/03/using-quagga-with-docker-containers.html
############################

bash -c "curl https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework" > pipework

sudo ./pipework br0 R1
sudo ./pipework br0 R2
