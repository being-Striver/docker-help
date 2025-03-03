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
  
  Note: Bind Mount is mostly used to inject data from host machine to container.while container is running, developer can do all code changes in host machine directory and that will be reflected in the container.
		but for preserving data purposes, the better option is volumes, docker volumes.
		
		
Lets see Volume examples:
   run command : docker volume
       commands :
	       create - create a volume
		   inspect - display detailed information on one or more volumes
		   ls - list volumes
		   prune - remove all unused local volumes
		   rm - remove one or more volumes
		   
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


# Volume mount options
---------------------------
- : --mount
- : -v

 **NOTE**: /*The --mount flag is the newer and more verbose way to specify volume mounts in Docker. It provides a clearer syntax and more options than the -v flag.*/
 



# Bind Mounts
----------------------
Bind mounts are dependent on directory structure and OS of the host machine. Volumes are completely managed by docker.


