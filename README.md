# Docker
-----------------------------------------
a runtime environment for container.


# Terminology
-----------------------------------------
docker daemon:
-----------------
- the docker daemon(dockerd) listens for docker API requests and manages docker objects such as images, containers, networks and      volumes.

docker client:
-------------------
  - docker client can be present on either docker host or any other machine(local desktop).
  - the docker client(docker) is the primary way that many docker users interact with docker.
  - when you use commands such as *dcoker run*, the client sends these commands to *dockerd* (docker daemon), which carries them out.
  - the docker command uses the docker api.
  - the docker client can communicate with more than one daemon. 
# Container:
-----------------------------------------
    isolate the service and uses the same os kernel (kind of kernal trick).
    - process running in directory
    - A process(isolated)
    - A directory(Namespace/cgroups)
    - necessary bin/lib in the directory
    - a directory with IP address to connect
    - Containers share the machine's OS kernel and therefore do not require an OS per application.
    - A container is a standard unit of software that packages up 
        - code
        - dependencies

    - containers offer isolation not virtualisation.
    - Vms are hardware virtualisation
    - VMs need OS but container doesn't.
    - containers uses HOST OS for compute resources.
    - we can create, stop, start, move or delete a container using docker API or CLI.
    - we can connect a container to one or more networks, attach storage to it or even create a new image based on its current state.
    - when a container is removed, any changes to its state that are not stored in persistent storage, disappear. by default, container uses ephimeral storage.



    # Point to be noted:
    ------------------------------
    - Isolating services are important.(Need OS for that)(because OS creates boundary for isolation)
    - High availability achieved by multiple vms /instances
    - portability matters or eases the deployment
    - All this raises CapEx or OpEx.
    
    
    # Imagine isolation without OS?
    -------------------------------------
        - Imagine multiple services running in same OS but isolated.


    # Container vs image:
    -----------------------
        Image is a template which is used to create container.while containers are running instances of images and they are isolated and they have their own environment and set of processes.





# To understand how docker works, lets understand how OS works?
--------------------------------------------------------------
in OS, there is OS kernel which is responsible for communicating with underlying hardware whereas OS kernel remains the same.
Its the softwares above it, that makes it diffrent.You need to have common linux OS kernel which shares across all OSes and some custom software which diffrentiate operating systems(oses) from each other.


    # Docker container shares the underlying os kernel:
    -------------------------------------------------------
    Lets say we have a system having ubuntu OS with docker installed on it.Docker can run any flavour of OS on top of it as long as they based on the same kernel.In this case, linux.


    There are most of containerised version of apps are available today.They are available in public docker repository called dockerhub or docker store.


# what is docker image?
-----------------------------------------------------------------------------------------
- read only template with instructions for creating a docker container.
- A stopped container like VM image.
- consists of multiple layers
- An app will be bundled in image.
- containers run from images.
- images are called repositories in registry.
- often an image is based on another image with some additional customizations.

**NOTE:** Docker images - images become containers when they run on docker engine.

First we have to understand what we are containerising and what application we are creating an image for and how the application is built. So start by thinking what you might do if you want to build application manually.

We write down the steps required in the right order and creating an image for simple web application. 
  1. OS -ubuntu
  2. update apt repo
  3. install dependencies using apt
  4. install python dependencies using pip
  5. copy source code to /opt folder
  6. run the web server using flask command

Now I have the instructions, create a docker file using these.

    Quick overview of creating your own image.

    -----------------------------------------
    ```
    FROM Ubuntu
    RUN apt-get update && apt-get -y install python
    RUN pip install flask flask-mysql
    COPY . /opt/source-code
    ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
    ```

------------------------------------------
Dockerfile is text file written in specific format that docker can understand. it is in INSTRUCTION & ARGUMENT FORMAT.

When docker builds the images, it builds these in layered architecture.
Each line of instruction creates a new layer in the docker image with just change from the previous layer . Since each layer only store the changes from previous layer, it is reflected in size as well.

--docker history <image-name>

    All the layers built are cached by docker.so in case if a particular step fails, you want to fix the issue and rerun the docker build,it will reuse the previous layers from the cache and continue to build remaining layers.
    The same is true if you have to add additonal steps in the docker file. This way rebuilding your image is faster and you don't have to wait for docker to rebuild entire image each time.

    This is helpful, especially when you update source code of your application as it may change more frequently.Only the layers above the updated layer needs to be rebuilt. 


# Docker Registry:
--------------------------
- Storage for images
- DockerHub is default registry.
- Cloud based registry:
  - DockerHub
  - GCR(google container registry)
  - Amazon ECR
- Inhouse or local registry:
  - Nexus 3
  - Jfrog artifactory
  - DTR(docker trusted registry)

**NOTE:** Please be sure container is running on what port.The process running on what port in container so you can map a host port. You cannot connect to this container directly because its going to be in a private network in the host machine, there will be private network.If you want to access outside from the container, then you have to map a host port, so you can access the host on that port and then it is going to route that request to container on port that you have specified.
      -command : -p 7090:80 (this is called port mapping or port forwaring) -(you map a host port with container port)

As we know container is just a process running from directory. You can run "ps -ef" on my host machine. you will see process id of your container.
You can go to "cd /var/lib/docker"	path on your host machine.You can do ls. you will see diffrent directories.then go to container directory. then do ls. you will see all containers.

*Container can store data.You can have dynamic container or stateful container that store the data or reads the data and if you are going to do that, you have to make sure that you connect volumes to it.*

# If you want to login to container,basically there is no login, since its a process.How can you login into process?
--------------------------------------------------------------------------------------------------------------------
But you can attach to this container, you can run command also.
- docker exec <container_id> <command you want to execute within container> (with this, you will execute the commands in container but you are not connected to shell).

If you want to connect to that command, you can mention "-it".
-docker -exec -it <container_id> /bin/bash

**NOTE:** *Container is really stripped down version of operating system.(if you are trying to run ifconfig, ps commands, it will not run.)*
- Lets install the package that will give us ps.
This is actually debian based container so i can run "apt update" command.
- apt install procps -y (installation will happen in container)
if you run *ps -ef*, you will see running process within container.

# command :
---------------------------
- docker inspect <container_id>  :(it will show the metadata of image in json format).

- Run- start a container(docker run command is used to run a container from image)
   : docker run nginx (will run the nginx application on docker host)[if image is not present locally, it will pull image from docker hub)

    ps- list containers
        e.g. docker ps
        
    STOP- stop a container(to stop a docker container, you must provide container id)
        e.g.- docker stop <container_id or container_name>

    Rm- remove a container(to remove a container permanently)
    e.g. - docker ps -above
    
    So what about the nginx image which was dpwnloaded first?
    Since we are no longer using that image, how can we get rid of that?but first, how do we see list of images present in our host?

    images- list images
    eg - docker images (will list the available images and their sizes)
  
        rmi- remove images(to remove image)
        eg - docker rmi nginx
        you need to ensure that no container should be running of that image.
        Delete all dependent containers to remove image.
   
pull- download an image(only to pull image and not to run container)
 eg- docker pull nginx
 
docker run ubuntu
docker ps
--you wont see any container of ubuntu. 
reason - unlike virtual machines, containers are not to be meant to host operating system.
Containers are meant to run specific process or task. A container lives as long as process lives. Once the process ends, container exits.


What if we want to execute some commands in running containers?
--
Exec- execute a command
 eg- docker exec <container_name or id> <command you want to execute>
 
run - attach and detach
 
 -docker run kodecloud/simple-webapp
 =When you run docker command like this, it runs in the foreground or in attached mode meaning you will be attached to the console or you will see standard out of docker container
  and you will see the output of web service on your screen. You won't be able to do anything else on this console other than view the output until this docker container stops.
  
 -another option is to run the docker container in detach mode.
 docker run -d kodecloud/simple-webapp
 = this will run your docker container in background mode and you will be prompt back to immediately.
 
 
# docker run
-----------------
Run -tag

-docker run redis (it will run a container of latest version of redis services)

what if you want to run a specific version of redis service?
-thats where tag comes in picture.

  -docker run redis:4.0 (:version is called tag)
  
 if you don't specify any tag, docker will take latest version by default.


# Run -PORT mapping
---------------------
We will now look at port mapping and port publishing on containers.
Remember the under lying host where Docker is installed is called Docker host or docker engine.

When we run a containerised web application, it runs and we are able to see that the server is running.but how does a user access my application?
As you can see my application is listening to port 5000.but what ip do i use to access it from web browser?
 - two options are available:
    - one to use the ip of docker container(every docker container gets an ip by default. but this is an internal ip and is only accsible within docker host)
    - two by using docker host ip. but in order to it work,you must have mapped the port inside the docker container to a free port on the docker host.
  
 for ex- If i want users to access my web application through port 80 on my docker host, i could map port 80 of localhost to port 5000 on docker container using dash p in my parameter in my run command like this.
   - docker run -p 80:5000 kodecloud/simple-webapp
  
user can access my web application on http://192.168.1.5.80
   
   - this way you can route your traffic from port 80 to port 5000 on docker container.
   - through this way, you can run multiple instances of your application and map them to different ports on docker host or run instances of different applications on diffrent ports.
 





