# What is docker?
-------------------------
It is a platform which provides runtime for containers. It provides developers to package applications into containers.

# How containers are different from VMs?
-----------------------------------------
Docker containers share the same host machine OS kernel, making them lightweight and efficient. It provides process level isolation.
whereas VMs in contrast run full guest OSs on a hypervisor, consuming more resources and stronger isolation. 

# what is docker lifecycle?
-----------------------------------------


# what are different docker components?
--------------------------------------------
- docker cli (client)
- docker daemon
- containers
- docker network
- iamges
- registry

# what is the difference between COPY and ADD?
----------------------------------------------------
Docker ADD can copy the files from url unlike docker COPY which only copy files from host system into the container.


# what is the diference between CMD and ENTRYPOINT in docker?
---------------------------------------------------------------


# What are the networking types in docker and what are default?
-----------------------------------------------------------------
- Bridge
- None
- Overlay
- Host
- MacVlan

# Can you explain how to isolate networking between containers?
----------------------------------------------------------------------


# What is multi-stage build in docker?
-----------------------------------------------
Multi stage build allows you to build your docker image in multiple stages allowing you to copy artifacts from one stage to another. The major advantage of this is to build light weight containers.

# what are distro less images in docker?
----------------------------------------------------
Distro less images contain only your application and its runtime dependencies with a very minimum operating system libaries.
They do not contain package managers, shell or any other programs. very small and liht weights


# Real time challenges with docker
--------------------------------------------
Docker is a single daemon process which can cause a single point of failure. if the docker daemon goes down for some reason, all appplication will go down. 

Docker daemon runs as a root user which is a security threat. Any process running as a root user have adverse affect.

Rsource constraints: if too many containers running on single host, you may face issue with resource constraints.

# what steps would you take to secure docker?
--------------------------------------------------
- use distro less images with not too many packages as your final image in multi stage build, so that there is less chance of security risk
- ensure networking is configured properly
- use utilities like SYNC to scan your container images

# Can you describe a situation where you have used docker to solve a specific problem?
-----------------------------------------------------------------------------------------
In my project, we used docker to make sure that there is no deployment inconsistency in develpment and production environment. Previously we used to face so many inconsistency in dev and prod while deployment.


# You are in charge of maintaining docker environment in your company and you have noticed many stopped containers and unused networks taking up space. Describe how would you clean up these resources effectively to optimize docker environments.
------------------------------------------------------------------------------------------------------------------------------
/*docker prune*/ command is used to cleanup unused docker resources, such as containers, volumes, networks and images.
- docker container prune : removed stopped containers
- docker image prune : removes unused images
- docker network prune : cleans up unused network
- docker volume prune : removes unused volumes
- docker system prune -af : combines all these in single command

# You are working on a project that requires docker containers to persistently store data. How would you handle persistent storage in docker?
--------------------------------------------------------------------------------------------------------------------------------
Docker volumes can be used for persistent storage. They are managed by docker and can be attached to one or more containers.
Another approach is to use bind mounts, which are linked to host file system.


# A company wants to create thousands of containers. is there a limit on how many containers you can run in docker?
----------------------------------------------------------------------------------------------------------------------
There is no limit of number of containers you can run within docker. It totally relies on hardware. major deciding factors are program size and cpu.

# You are managing a docker environment and need to ensure that each containers operates within defined CPU and memory limits.How do you limit the CPU and memory usage of a docker container?
-----------------------------------------------------------------------------------------------------------------------------
You can set the cpu limit with --cpu option.
you can set the memory limit with --memory option.

for example :  docker run --cpu 2 --memory 2g mycontainer

# what is dockerfile and how it is used in docker?
----------------------------------------------------------
A dockerfile is a text file which contains commands or instructions to build docker image. It specify the base image.

# You have been tasked with ensuring the application can handle increased loads by scaling docker container horizontally.How do you scale docker container horizontally?
-------------------------------------------------------------------------------------------------------------------------------
To scale docker container horizontally, we can use container orchestartion tool like K8s or docker swarm.


# what is the difference between docker container and K8s pod?
---------------------------------------------------------------------
docker container is a lightweight and isolated runtime environment that runs single instance of an application.
whereas K8s pod is high level abstraction which can run more than one containers(or other runtime environemnts)

# You're part of a development team deploying micro-services architecture using docker containers. One of the containers, critical to the system's functionlity has suddenly started failing without clear error message. How do you debug issues in a failing docker container?
----------------------------------------------------------------------------------------------------------------------------
Several ways to debug the issue:
- logging: docker captures the standard output and error streams of containers, making it easy to inspect logs using /*docker logs*/ command.
- shell access:  /*docker exec -it*/ 
- image inspection: /*docker image inspect*/  
- health checks: 

# can you describe a situation where you optimized a dockerfile for faster build times or smaller image size?
------------------------------------------------------------------------------------------------------------------------------
optimizing a dockerfile could involve various strategies like using a smaller base image, reducing the number of layers by combining commands or using multi-stage builds to exclude unnecessary files from the final image.

# how do you create a custom docker network?
---------------------------------------------------------
- docker network create mynetwork (it will create bridge network by default)
- you can specify a different driver using --driver option.

# You're working on a critical application running in docker containers, and an update needs to be applied without risking data loss. How do you update a docker container without losing data?
-----------------------------------------------------------------------------------------------------------------------------
The steps to update a docker container without losing data are:
- create a backup of any important data stored within the container
- stop the container gracefully using docker stop command
- pull the latest version of the container image using docker pull
- run the container with updated image and make sure to map correct volume or bind mounts

 

