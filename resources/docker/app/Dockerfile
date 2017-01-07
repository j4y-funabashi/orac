FROM resin/rpi-raspbian:jessie

WORKDIR /root/
RUN apt-get -q update && \
    apt-get -qy install python-dev python-pip python-smbus python-psutil gcc make && \
    pip install spidev && \
    pip install dot3k && \
    apt-get -qy remove python-dev gcc make && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qy clean all

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY ../.. /usr/src/app
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

