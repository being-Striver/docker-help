FROM nginx:alpine-slim 

#OCI Labels
LABEL org.opencontainers.image.authors="Sudhanshu Bhagat"
LABEL org.opencontainers.image.title="Nginx Web Server"
LABEL org.opencontainers.image.description="This is a simple Nginx Web Server"  
LABEL org.opencontainers.image.url="https://hub.docker.com/r/sudhanshubhagat/nginx-web-server"

# using COPY to copy a local file 
COPY copy-file.html /usr/share/nginx/html

#using ADD to copy a file and extract a tarball
ADD static_files.tar.gz /usr/share/nginx/html
