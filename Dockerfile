FROM postgres:latest
RUN  cd /opt
ADD  mkdir mytask
CMD  apt-get update -y && apt-get install wget -y
