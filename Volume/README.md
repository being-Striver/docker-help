# Docker Volume:
------------------
Containers are generally known for its volatile nature.That's because containers are disposable.The way you make any changes in 
container, through image.thats because its called volatile.
if you store any data in the container and if we have to replace it, its going to remove the container and create a new container so when it removes the container, all the data will be also gone.but what if you have container which is stateful like Mysql that needs DB, it stores databases and reads from the database. if you happen to replace that container, all the data will be also gone.So for that we have containers volumes.

Container data:
- The data doesn't persist when the container no longer exists and it can be difficult to get data out of container if another process 
  need it.
- A container's writable layer is tightly coupled to host machine where the container is running. You can't easily move data somewhere
  else.

- Docker has two options for containers to store files in the host machine.
  : volumes(it's a wrapper where in the docker's volumes directory) it will create a directory and then you can attach that to your 
    container.So whatever data you store in a container at a separate directory, you will attach it to a directory.All that data from 
	container directory will be going to the volumes which is your host machine.so its safe in your host 
   machine.(managed by Docker(/var/lib/docker/volumes/ on Linux))
   : Bind Mounts (same as vagrant sync directories)-store anywhere in the host machine.
   
Note: -e option is to export variable while executing docker command.
 
Lets see Bind Mounts example:
  #docker run --name vprodb -d -e MYSQL_ROOT_PASSWORD=mysecpass -p 3030:3306 -v /home/ubuntu/vprodbdata:/var/lib/mysql mysql:5.7
  here -v specify volumes. Here we seeing bind volumes. first we will specify our path of our host machine that will be mapped with container directroy /var/lib/mysql.
  
  if you do ls /home/ubuntu/vprodbdata, it will give all the files that would in container.
  if you go to container using command "docker exec -it vprodb /bin/bash" and then do "ls /var/bin/mysql" it will give same result files as we see in host machine.
  Even if you delete container, container data will be reside in host machine.
  
  Note: Bind Mount is mostly used to inject data from host machine to container.while container is running, developer can do all code changes in host machine directory and that will be reflected in the container.but for preserving data purposes, the better option is volumes, docker volumes.
		
		
Lets see Volume examples:
   run command : docker volume
       commands :
          - create - create a volume
          - inspect - display detailed information on one or more volumes
          - ls - list volumes
          - prune - remove all unused local volumes
          - rm - remove one or more volumes
          
	-docker volume create myvprodbdata
	-docker run --name vprodb -d -e MYSQL_ROOT_PASSWORD=mysecpass -p 3030:3306 -v myvprodbdata:/var/lib/mysql mysql:5.7 (make sure previous mysql container should not be running 
	 otherwise you can't do same port mapping).
	 - docker inspect vprodb
	 (from this json metadata, you can see lots of information. like private ip address of host machine. You cannot connect outside of host machine using that ip address.This is the network inside the host machine.if you are already in host machine, you can use that ip address to connect your container also.Its running mysql service,so we can use mysql client to connect mysql services using below command
	   - mysql -h <ip_address> -u root -pmysecpass
	   
NOTE: Once you are done with activity, make sure you clean up.





- Volumes are easier to back up and migrate than bind mounts.
- Volumes can be managed by docker cli or api.
- Volumes can be shared across multiple containers.
- Volume drivers let you store volumes on remote hosts or cloud providers, encrypt the contents of volume or add other functionality.


# Docker volume types
-----------------------------
1. Named volumes
2. Anonymous volumes
   : docker volume create (it will create anonymous volume).


# Commands
---------------------------
  #create an anonymous volume
   -- docker volume create
  
  #List docker volumes
   -- docker volume ls
  #Inspect the docker volume
   -- docker volume inspect <volume-name>

  #delete volumes 
   --  docker volume prune

  #delete specific volume
   -- docker volume rm 

  #docker root directory
  -- `docker info`


# Volume mount options
---------------------------
- : --mount
- : -v

 **NOTE**: /*The --mount flag is the newer and more verbose way to specify volume mounts in Docker. It provides a clearer syntax and more options than the -v flag.*/
 
- `docker run -d --name nginx-demo --mount type=volume,src=nginx-data,dst=/usr/share/nginx/html,readonly nginx`

- Mounting volume as readonly
  : `docker run -d -v app_data:/app:ro alpine:latest` 

- Reusing volume when container restarts
  :  you can use `--volumes-from` to automatically include another container’s volumes:
  : `docker run -d --name backup --volumes-from db backup-image:latest`

  here db container should be running.




# Bind Mounts
----------------------
Bind mounts are dependent on directory structure and OS of the host machine. Volumes are completely managed by docker.
Any file system on your docker host machine can be mounted to container.

You can use `-v` option to bind mount. 
The only difference between mount and bind mount is, bind mount is associated with host directory. whatever file will be present in the host directory, same will present in container directory.

example: `docker run -d --name nginx-demo -v /nginx-data:/usr/share/nginx/html nginx`



# Jenkins deployment on docker engine using volume mount
----------------------------------------------------------
`docker run -d --name jenkins-server -p8090:8080 -v jenkins-data:/var/jenkins_home jenkins/jenkins:lts` 

for getting intial password, you can check the defined path in container logs or you run `docker logs <container-id>`

if you use volume mount, even if you delete the container, data won't be lost as you can re-use same volume to mount the data into new container.
you can try deleting jenkins container and creating new one with mounting previosuly created volume.



# Docker tmpfs mount
--------------------------
This will only for linux operating system.
`--tmpfs` option is used.

- `docker run -d --name nginx-demo --tmpfs /var/tmp nginx`

NOte: tmpfs doesn't give you flexibility about opting options. Instead we can use `--mount` option to acheive that.

example:
 - `docker run -d --name nginx-demo --mount type=tmpfs,dst=/var/tmp,tmpfs-size=1024,tmpfs-mode=700 nginx`

 here, src won't be there as tmpfs is ram memory.
      tmpfs-size will be calculated in kb.
      tmpfs-mode option will be used to provide access.

      It will live inside container and will stay alive as long as container live.


# Points to remember while working with volumes
----------------------------------------------------
- We have to use volume mount for most of the applications deployed on docker engine, where location doesn't matter.
- Volume mount is created under docker root area only.
- we can share volume and bind mounts to multiple containers
- Use bind mount to share any file system on docker host machine to containers
- Need to use bind mount only if necessary and there is no choice
- Taking a backup of docker root area will backup docker volume mount, not in the case of bind mount
- For bind mount, we need to know the path on host machine and take backups is any cronjobs
- --tmpfs is only available in linux.


# Understanding remote storage  using NFS server
------------------------------------------------------
Now the concerns here is, what if your docker host machine is down, how would you recover your application data?

We can do that using external storage called NFS.

Jenkins deloyment on docker engine using external storage
-----------------------------------------------------------

  #install nfs server on different host machine
  - apt install -y nfs-kernel-server

  #Now I have to tell nfs server, pls allow this directory to access client over particular network
  - mkdir nfs-data
  - chown -R nobody:nogroup /nfs-data/ (it means anybody can read/write data to this folder)
  - vi /etc/exports (it is where we will tell nfs server which directory should be shared across client over internet)
   
   Once the file is open, please add two below things:
   /nfs-data      192.168.1.40(rw,sync,no_subtree_check, no_root_squash)

  - exportfs -av (to export the ip address to the folder)
  - systemctl restart nfs-kernel-server

#To configure nfs storage on docker host machine,
`docker run -d --name jenkins-demo --mount 'type=volume,src=jenkins-data,dst=/var/jenkins_home,volume-driver=local,volume-opt=type=nfs,volume-opt=device=:/nfs-data,"volume-opt=o=addr="192.168.1.50,rw,nfsvers=4,async"'  jenkins/jenkins:lts`

try deleting containers as well as volume. It will delete all data but you can spinup new container and make sure utilize the nfs volume.

if you run above command, it will fetch data from nfs server.



