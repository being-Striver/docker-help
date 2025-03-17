# How to deploy multi-container applications in docker
----------------------------------------------------------
In Docker, multi-container applications are typically managed using Docker Compose. This allows you to define and run multiple containers as a single application. Each container in a multi-container setup usually serves a specific purpose, and Docker Compose helps manage their interactions and dependencies.

**Docker Compose:** It's a tool for defining and running multi-container Docker applications. You use a YAML file (docker-compose.yml) to configure your application's services and how they interact.


By default, containers run in isolation and don't know anything about other processes or containers on the same machine.

How do you allow one container to talk to another?
- through container networking. If you place two containers in the same network, they can talk to each other.

    #Listing docker network
    - docker network ls 
    
    #create a new docker network for the multi-container network 
    - docker network create ums-app 

   #list docker networks to verify the creation of docker network 
   - docker network ls 

   #create and run mysql container 
   - docker run -d \
     --network ums-app --network-alias mysql \
     --name ums-mysqldb \
     -v 








