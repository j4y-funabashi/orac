sudo locale-gen en_GB.UTF-8

cp resources/.bashrc ~/.bashrc

sudo apt-get update \
    && sudo apt-get install -y \
    git \
    python3-pip \
    weechat \
    python3-dev \
    libssl-dev \
    libffi-dev

sudo pip3 install virtualenvwrapper
source ~/.bashrc

# mkvirtualenv -p `which python3` errbot-ve
