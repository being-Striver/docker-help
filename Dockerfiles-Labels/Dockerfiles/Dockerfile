# Use nginx:alpine-slim as base docker image.
FROM nginx:alpine-slim

# Custom label
LABEL maintainer="Sudhanshu Bhagat"
LABEL version= "v1"
LABEL description="This is a custom image for nginx server"
LABEL release-date="2025-21-02"

# OCI(open container initiatives) label
LABEL org.opencontainers.image.title="Nginx alpine slim application"
LABEL org.opencontainers.image.description="This is a custom image for nginx server"
LABEL org.opencontainers.image.version="1.0"
LABEL org.opencontainers.image.created="2025-21-02"
LABEL org.opencontainers.image.authors="Sudhanshu Bhagat"
LABEL org.opencontainers.image.url="github.com/being-striver/Dockerfiles-Labels"
LABEL org.opencontainers.image.documentation="github.com/being-striver/Dockerfiles-Labels/README.md"
LABEL org.opencontainers.image.documentation=""
LABEL org.opencontainers.image.source=""
LABEL org.opencontainers.image.vendor="eDaddy Inc."
LABEL org.opencontainers.image.licenses="APACHE-2.0"
LABEL org.opencontainers.image.ref.name="nginx-alpine-slim"
LABEL org.opencontainers.image.revision="1.0"
LABEL org.opencontainers.image.schema-version="1.0"

# Using copy to copy index.html file to the nginx server
COPY index.html /usr/share/nginx/html/
