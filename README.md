# Docker
-----------------------------------------
a runtime environment for container.

   # docker deafult parameter
   -------------------------------
   once docker is installed, how would you verify that correct packages are installed or not? which command will you run to check that?

   commands :
    -dpkg -l | grep docker-ce 
    -dpkg -l | grep containerd.io 
    -dpkg -l | grep docker-compose-plugin 



# Terminology
-----------------------------------------
docker daemon:
-----------------
- the docker daemon(dockerd) listens for docker API requests and manages docker objects such as images, containers, networks and volumes.

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
        Image is a template which is used to create container.while containers are running instances of images and they are isolated 
        and they have their own environment and set of processes.





# To understand how docker works, lets understand how OS works?
--------------------------------------------------------------
in OS, there is OS kernel which is responsible for communicating with underlying hardware whereas OS kernel remains the same.
Its the softwares above it, that makes it diffrent.You need to have common linux OS kernel which shares across all OSes and some custom
 software which diffrentiate operating systems(oses) from each other.


    # Docker container shares the underlying os kernel:
    -------------------------------------------------------
    Lets say we have a system having ubuntu OS with docker installed on it.Docker can run any flavour of OS on top of it as long as 
    they based on the same kernel.In this case, linux.


    There are most of containerised version of apps are available today.They are available in public docker repository called dockerhub
    or docker store.


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

First we have to understand what we are containerising and what application we are creating an image for and how the application is 
built. So start by thinking what you might do if you want to build application manually.

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
Each line of instruction creates a new layer in the docker image with just change from the previous layer . Since each layer only store 
the changes from previous layer, it is reflected in size as well.

--docker history <image-name>

    All the layers built are cached by docker.so in case if a particular step fails, you want to fix the issue and rerun the docker 
    build,it will reuse the previous layers from the cache and continue to build remaining layers.
    The same is true if you have to add additonal steps in the docker file. This way rebuilding your image is faster and you don't have 
    to wait for docker to rebuild entire image each time.

    This is helpful, especially when you update source code of your application as it may change more frequently.Only the layers above 
    the updated layer needs to be rebuilt. 


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

**NOTE:** Please be sure container is running on what port.The process running on what port in container so you can map a host port. 
You cannot connect to this container directly because its going to be in a private network in the host machine, there will be private
 network.If you want to access outside from the container, then you have to map a host port, so you can access the host on that port and 
 then it is going to route that request to container on port that you have specified.
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


-- docker run --name <container-name> -p <host_port>:<container_port> <image-name>:<tag(optional)>

hostname of the container is the containerID for container.
-- docker exec <container-id> hostname


      # how to run command in container's terminal
       - docker exec -it <container-name or container-id> /bin/sh (it will connect you to container's terminal where you can execute shell command)

      # how to get index.html file in ngix
      - docker exec -it nginx /bin/sh
      - ls
      - cd /usr/share/nginx/html
      - cat index.html

  how to verify whether container is up and running or not?
  - docker ps
  
  test if application is back up or not
  - curl http://localhost:80
  - 

# Build docker image and push to docker hub
-----------------------------------------------
command to build docker image:
 - docker build -t <[image-name-you-want-to-name]>

In order to push image to docker hub, you need to login into docker hub.
-- docker login
you will be asked to provide username and password.


 steps to build docker image:
 
  #change to directory containing your Dockerfile
  cd Dockerfiles

  #build the docker image
  docker build -t <[image-name]>:<[tag]>

  #example
  docker build -t mynginx-custom:v1 . (why dot in the end? because where my currrent directory is present)



  # tag and push the docker image to dockerhub

   #list docker images
   docker images

   #tag the docker image
   docker tag myapp:v2 YOUR_DOCKER_USERNAME/myapp:v2

   #example
   docker tag myapp:v2 edaddy/myapp:v2

   #push the docker image to dockerhub
   docker push YOUR_DOCKER_USERNAME/myapp:v2

   #docker search commnds
   docker search nginx

   #limit the search result to 5
   docker search nginx --limit 5

   #filter search result by stars
   docker search --filter=stars=50 nginx

   #filter for official image only
   docker search --filter=is-official=true nginx

# Dockerfile - LABEL Instructions
-----------------------------------------
what is LABEL instructions in dockerfile?
- adds metadata to an image.
- an image can have more than one label.
- labels included in your base image are inherited by your image.


**NOTE**: jq is a light weight and flexible command line json processor, useful for parsing JSON output from command like *docker inspect*


    #Inspect the docker image 
    - docker image inspect <[myimage]>

    #example
    - docker image inspect <[image-name]>

    #get the creation date of docker-image
    - docker inspect --format='{{.Created}}' [image-name]:<[image-tage]>

    #get the docker image labels 
    - docker inspect --format='{{json.Config.Labels}}' [image-name]:<[image-tag]> | jq

# Dockerfile ADD and COPY Instructions
---------------------------------------------
What is COPY INSTRUCTION in dockerfile?
- The COPY instruction copies new files or directories from src and adds them to the filesystem of the image at the path destination.
- files and directories can be copied from the 
    - build context
    - build stage 
    - named context 
    - an image

What is ADD INSTRUCTION in Dockerfile?
- The ADD instruction copies new files or directories from SRC and adds them to the filesystem of the image at path destination.
- Files and directories can be copied from the 
    - a build context
    - a remote url  
    - a git repository 


   #Review app-files folder and tar the files

    #navigate to the app-files folder
    cd /Dockerfiles-Add-VS-Copy/App-files

    #Create a tar.gz archive of the files
    tar -czvf static-_files.tar.gz index.html file1.html file2.html file3.html file4.html file5.html 

    #copy the tar.gz file to the Dockerfiles directory
    ADD static_files.tar.gz ../Dockerfiles

    #Review the copy-file.html in dockerfiles
    cat ../Dockerfiles/copy-file.html
--------------------------------------------------------
       STOP and REMOVE CONTAINER IMAGES:

            # Stop and remove the container
            docker rm -f demo-add-vs-copy

            # Remove the Docker images
            docker rmi static_image:v1

            # List Docker Images to confirm removal
            docker images 
    

# Dockerfile: ADD - Fetch from URL(Github)
-----------------------------------------------
- To add files from a remote location, you can specify the
   - url
   - git release:  

    # Step 1: Create GitHub Repository and Upload Files
        Create a GitHub Repository:
            - Repository Name: docker-add-fetch-url-demo
            - Repository Type: Public
            - Initialize with a README (optional).
        
        Upload Files:
            - Upload docs folder into your repository.
            - You can drag and drop the docs folder for easy upload.
        
        Create a Git Release:
            - Go to the Releases section in your repository.
            - Click on Draft a new release.
            - Tag version: v1.0.0
            - Release title: Version 1.0.0
            - Click on Publish release.
   # Step 2: Create Dockerfile and ADD instructions
   # Step 3: Build docker image and run it.
   # Step 4: Stop and remove container and images


   RUN apk add --no-cache git
   - apk is a package manager for alipne linux(base image nginx:alpine-slim)
   - add installs a package(here git)
   - --no-cache prevents saving package cache, reducing image size.
  
  Effect : installs git inside the container.


  RUN git clone --depth 1 --branch v1.0.0 https://github.com/being-Striver/docker-add-fetch-url-demo.git /tmp/repo
  - git clone download the specified repository
  - --depth 1 clones only the latest commit, reducing the amount of downloaded history
  - --branch v1.0.0 checks out the specific branch
  - /tmp/repo is the destination folder inside the container

 Effect: clones the v1.0.0 branch of github repo into /tmp/repo

 cp -r /tmp/repo/docs /usr/share/nginx/html/
 - cp -r copies the /docs directory recursively

 Effect: moves the docs folder to nginx web root, making its conents available via a web browser

 rm -rf /tmp/repo
 - rm -rf forcefully removes the /tmp/repo directory
 - This frees up some space, since git repo is no longer needed.




# Dockerfile - ARG Instruction
---------------------------------------------------------
what is ARG instruction in dockerfile?
- defines a variable that users can pass at build time to the builder with 
- command : docker build --build-arg <variable-name>=<value>
- we can define one or more ARG instructions.
- we can define default values for ARG instructions in dockerfile.
-  ARG NGINX_VERSION=1.26
- An argument variable(ARG) definition comes into effect from the line on which it is defined.
- ENV variables always override ARG variables (if same variable defined in both places).



# docker system prune -af 
--------------------------------
This command will forcefully removes unused docker data, including:
 - all stopped containers
 - all dangling images(unused images without tags)
 - all unused networks
 - all unused build cache
 - This will not remove images currently in use.
 - -a(all) : removes all unused images, including untagged and unused images
 - -f(force): runs the command without asking for confirmation.
  
  When should you use this?
  - to free up disk space(especially after multiple builds)
  - to remove old images and containers that are not being used
  - to clean up unnecessary docker cache

  #USE BELOW COMMAND FIRST TO CHECK WHAT WILL BE REMOVED
  - docker system df

  #Remove only unused images
  - docker image prune -a
  
  #Remove only stopped containers
  - docker container prune
 
  #Remove only build cache
  - docker builder prune
  
  NOTE: When you run *docker system prune -af*, it deletes all unused images, including those without a tag. If you have images that you want to keep, but they are not currently used in a running container, they might be deleted. To prevent this, you should tag them.

  - docker tag [<image-id>] [image-name]:[tag(optional)]

  Tagging ensures important images are not lost during cleanup.




# RUN INSTRUCTION AND EXPOSE INSTRUCTION
------------------------------------------------------
what is RUN instruction in Dockerfile?
-The RUN instruction will execute any commands to create a new layer on top of the current image.

   - RUN apk add --no-cache git
     - apk is a package manager for alipne linux(base image nginx:alpine-slim)
     - add installs a package(here git)
     - --no-cache prevents saving package cache, reducing image size.
    
  Effect : installs git inside the container.


  - RUN git clone --depth 1 --branch v1.0.0 https://github.com/being-Striver/docker-add-fetch-url-demo.git /tmp/repo
    - git clone download the specified repository
    - --depth 1 clones only the latest commit, reducing the amount of downloaded history
    - --branch v1.0.0 checks out the specific branch
    - /tmp/repo is the destination folder inside the container

 Effect: clones the v1.0.0 branch of github repo into /tmp/repo

 - cp -r /tmp/repo/docs /usr/share/nginx/html/
   - cp -r copies the /docs directory recursively

 Effect: moves the docs folder to nginx web root, making its conents available via a web browser

 - rm -rf /tmp/repo
   - rm -rf forcefully removes the /tmp/repo directory
   - This frees up some space, since git repo is no longer needed.


# What is Cache Invalidation?
-------------------------------------
Docker uses a layered caching system to speed up image builds. Each instruction (RUN, COPY, ADD, etc.) creates a new layer. If an instruction changes, Docker invalidates that layer and all subsequent layers, forcing a rebuild.

 1. How Docker Caching Works in RUN
    - When you build a Docker image, Docker checks if a previously built layer can be reused.

        - If the RUN command has not changed, Docker uses the cache.
        - If the RUN command changes, Docker invalidates the cache and rebuilds from that step.
 2. When is Cache Invalidated?
      A) When a RUN Command is Modified
    - Even a small change in a RUN instruction invalidates the cache.


      B) using --no-cache 
      - This ensures that everything is built from scratch.


# What is EXPOSE instruction in docker?
----------------------------------------------
It informs the docker that the container listens on the specified networks ports at runtime.

command:
 - EXPOSE [LIST OF PORT NUMBER]


# CMD , WORKDIR and ENV INSTRUCTIONs
-----------------------------------------------------------------------------------------------------------------------------
 ENV INSTRUCTION:
 --------------------
  - ENV sets the environment variables.
 
 What is the key difference between ENV and ARG?
  - ENV is persisted in the final image and will be available in container when it is run from this image.
  - ARG is not persisted in the final image, so no scope of using that value in the container when it is running from this image.


WORKDIR INSTRUCTION:
----------------------------
 - Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, ADD instructions that follow it in the dockerfile.
 - The WORKDIR instruction can be used multiple times in the dockerfile.
 - If WORKDIR not specified, the default working directory is "/".
 - If we are using the base image "FROM PYTHON", WORKDIR likely to be set by the base image.
 - NOTE: To avoid unintended operations in unknown directories, it's best practice to set WORKDIR explicitely.

CMD INSTRUCTION:
-----------------------------
 - defines the command to run when starting a container from the image.
 - only one CMD instruction is allowed per dockerfile, if there are multiple, only the last one is used.
 - used to set default commands or parameters for the container.
 - Syntax options:
        - CMD ["executable", param1, param2]
        - CMD["param1", "param2"]

 - It can be overridden by specifying a different command during "docker run".
    : docker run --name demo-cmd -it demo-cmd:v1 /bin/sh 

 ERROR:
 ------------
 docker: Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:8080 -> 0.0.0.0:0: listen tcp 0.0.0.0:8080: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.

  steps to fix:
   1. check if port 8080 is already in use
      - netstat -ano | findstr :8080
   
   2. you can then find and terminate the process
      - taskkill /F /PID <PID>

   3. You can map different port.


      #Run Docker Container and override APP_ENVIRONMENT to 'qa'
      docker run --name my-arg-env-demo2-qa -p 8081:80 -e APP_ENVIRONMENT=qa -d demo9-arg-vs-env:v1

      #List Docker Containers
      docker ps

      #Print environment variables from Container
      docker exec -it my-arg-env-demo2-qa env | grep APP_ENVIRONMENT

      #Expected Output:
      #APP_ENVIRONMENT=qa

      #Access the application in your browser
      http://localhost:8081 

Question: How do you ensure the default environment is qa when building the Docker image without changing the Dockerfile?

Answer:
You can override the ENVIRONMENT build-time argument during the image build process using the --build-arg flag. This allows you
to set the default APP_ENVIRONMENT to qa in the image without modifying the Dockerfile.


NOTE: /*You can override ENV variables at runtime using the -e flag with docker run.*/




# ENTRYPOINT Instruction
----------------------------------
In Docker, the ENTRYPOINT instruction is used in the Dockerfile to specify the command that will be run when a container is 
started from the Docker image. It sets the primary command to be executed when the container starts.

- Overridden the ENTRYPOINT instruction using the --entrypoint flag

Best practices:
- Use ENTRYPOINT when you want to define a container with a specific executable.
- Use CMD to provide default arguments to the ENTRYPOINT
- docker run --name demo-entrp demo-entp --entrypoint -c /bin/sh 'echo "command overridden by sudhanshu"'
 




