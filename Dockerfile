FROM ubuntu:latest

RUN apt-get update && apt upgrade -y && \
    apt-get install -y python3
RUN apt install -y python3-pip  
copy . .
RUN pip3 install -r requirments.txt