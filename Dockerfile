FROM jupyter/datascience-notebook:latest

RUN apt update && apt upgrade

COPY . /app/

WORKDIR /app

RUN pip install -r requirments.txt