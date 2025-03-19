# Docker networking
----------------------------------------
Bridge networking
-------------------------
- default network driver for containers
- docker engine supports default and user-defined bridge network.
- it is a software bridge created by docker
- containers in the same bridge can communicate with each other where as other bridge network is blocked
- docker bridge network creates some rules(iptables) on the host machine


Host networking
---------------------------
- Host network driver wil assign a container with host network as your docker host machine uses
- we need to ensure that applications running on host and containers with host network driver do not use same port network
- host network only works on linux, not on docker desktop for Mac, windows
- it is not recommended to use host network driver for applications

Overlay networking
-----------------------------
- overlay network will ensure containers sitting in two different docker host machines can communicate with each other 
- this feature is available by default on docker swarm
- to impelment overlay network without using docker swarm, we need to use consul or etcd key-value storage


 #to check default available networks in docker host machine
 - docker network ls

 #if you try to delete default network, you won't be able to do that. please try below command to verify
 - docker network rm bridge
  output: Error response from daemon: bridge is pre-defined network and cannot be removed.


# Default Bridge network key points:
--------------------------------------------
Let's say you want to give fixed ip address to a container, you can do that via /*--ip*/ options. If it's a default bridge network, even if you assign the static ip, default bridge network won't provide the static ip. To do that, you can create your own bridge network(user defined bridge network) and you can assign static ip address to container.
- docker container run -dt --name nginx --ip 172.17.0.10 nginx

# Application running on different bridge network
--------------------------------------------------
container having interface etho while network interface having veth{random number}.that's the naming convention.

  #Let's create a user defined bridge network

  - docker network(it will give you what are the commands available in docker network)


 #create docker user defined network 
 - docker network create --help (it will show what parameters can be passed while creating)
  --subnet strings (subnet in CIDR format that represents a network segment)
  --gateway strings (IPv4 or IPv6 gateway for the master subnet)
  --driver string (driver to manage the network(default "bridge"))
  

