install_docker () {

    locale-gen en_GB.UTF-8
    sudo apt-get update -q \
        && sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
        && echo 'deb https://apt.dockerproject.org/repo ubuntu-xenial main' | sudo tee /etc/apt/sources.list.d/docker.list \
        && sudo apt-get update -q \
        && sudo apt-get install -q -y \
        docker-engine \
        linux-image-extra-$(uname -r) \
        linux-image-extra-virtual \
        apt-transport-https \
        ca-certificates

    curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-compose-$(uname -s)-$(uname -m)" | sudo tee /usr/local/bin/docker-compose > /dev/null
    sudo chmod +x /usr/local/bin/docker-compose
    sudo usermod -aG docker $USER
}

sudo locale-gen en_GB.UTF-8

sudo apt-get update \
    && sudo apt-get install -y \
    mpd \
    mpc


install_docker
