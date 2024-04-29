FROM alpine:latest

RUN apk update && apk upgrade 
RUN apk add tree git curl coreutils make gnupg tzdata maven docker-cli bash openjdk17 diffutils

# python + ckan dependnecies
ARG PYTHON_VERSION=3.10.14

RUN apk add \
    wget \
    gcc \
    make \
    zlib-dev \
    libffi-dev \
    openssl-dev \
    musl-dev

RUN cd /opt \
    && wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \                                              
    && tar xzf Python-${PYTHON_VERSION}.tgz

RUN cd /opt/Python-${PYTHON_VERSION} \ 
    && ./configure --prefix=/usr --enable-optimizations --with-ensurepip=install \
    && make install \
    && rm /opt/Python-${PYTHON_VERSION}.tgz /opt/Python-${PYTHON_VERSION} -rf

RUN apk add --no-cache \
    postgresql-dev \
    linux-headers \
    gcc \
    g++ \
    autoconf \
    automake \
    libtool \
    patch \
    musl-dev \
    pcre-dev \
    pcre \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    gettext \
    postgresql-client \
    libmagic \
    libxslt \
    libxml2 \
    apache2-utils
    
RUN adduser --disabled-password --home /home/developer developer
RUN addgroup developer root
    
WORKDIR /workspace

USER developer