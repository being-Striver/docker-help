#use the alpine-slim image of nginx as base image
FROM nginx:alpine-slim 

#OCI labels
LABEL org.opencontainers.image.authors="Sudhanshu Bhagat"
LABEL org.opencontainers.image.description="This is a simple Dockerfile to demonstrate how to add a file from a URL in a Dockerfile"

#using github repository to download files

# syntax=docker/dockerfile:1.0.0-experimental

#here ADD will not work as our docker version is not compatible with ADD

# Install git
RUN apk add --no-cache git
# ADD
RUN git clone --depth 1 --branch v1.0.0 https://github.com/being-Striver/docker-add-fetch-url-demo.git /tmp/repo \
    && cp -r /tmp/repo/docs /usr/share/nginx/html/ \
    && rm -rf /tmp/repo

EXPOSE 80