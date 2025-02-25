#define a build time arguemnt for nginx version
ARG NGNIX_VERSION=1.27

#using nginx:1.26-alipine-slim image as base image
FROM ngnix:${NGNIX_VERSION}-alpine-slim

# OCI Labels
LABEL org.opencontainers.image.authors="Kalyan Reddy Daida"
LABEL org.opencontainers.image.title="Demo: Using ARG Instruction"
LABEL org.opencontainers.image.description="A Dockerfile demo illustrating the ARG instruction"
LABEL org.opencontainers.image.version="1.0"


#copy index.html to the nginx html directory
COPY index.html /usr/share/nginx/html/