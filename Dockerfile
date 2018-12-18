FROM ubuntu:18.04
RUN apt-get update && apt-get -y install \
        python3 \
        python3-flask \
        python3-flask-login \
        python3-setuptools \
        python3-dev \
        vim \
        git \
        software-properties-common \
        build-essential \
        debhelper \
        devscripts \
        equivs \
        python-minimal
