#############################
# prepare_images.sh
# Emmanuel Shiferaw
# Davis Gossage
# Commands for configuring quagga on docker taken from:
# http://anton-baranov.blogspot.com/2015/03/using-quagga-with-docker-containers.html
############################

#get images from remote
sudo docker pull gliderlabs/alpine
sudo docker images gliderlabs/alpine

git clone http://github.com/spacedog/docker-quagga
cd docker-quagga
cat Dockerfile

sudo docker pull abaranov/quagga

