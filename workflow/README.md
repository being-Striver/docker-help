# Docker Container creation workflow
---------------------------------
- docker cli used for executing a command
- docker client uses the appropriate api payload POSTs to the correct API endpoints
- docker daemon receives instructions
- docker daemon calls containerd to start a new container
- docker daemon uses gRPC ( a CRUD style API)
- containerd creates an OCI bundle from the docker image
- containerd tells runc to create a container using the OCI bundle.
- runc interfaces with OS kernel to get the constructs needed to create a container
- which includes Namespaces, CGroups, etc
- container process starts as a child process
- runc exits once the container starts
- process is complete and container is running


# What is OCI bundle?
----------------------------------
An OCI (Open Container Initiative) Bundle is a filesystem layout that contains everything needed to run a container. It follows the OCI Runtime Specification and is used by container runtimes like runc, crun, and Kata Containers.

An OCI Bundle consists of:
1️⃣ Root Filesystem (rootfs/) → The container’s root filesystem.
2️⃣ Configuration (config.json) → Defines the container's settings.

/my-container/
│── config.json      # OCI container configuration
└── rootfs/          # Root filesystem (Linux file system for the container)
    ├── bin/
    ├── lib/
    ├── usr/
    └── etc/



# Docker container restarts  policy
------------------------------------------
Docker restart policies control whether a container automatically restarts when it stops or crashes. This is useful for high availability and fault tolerance.

Docker provides four restart policies:
---------------------------------------------------------------------------------------------------------------------------------------
| Restart Policy	           |                 Behavior
----------------------------------------------------------------------------------------------------------------------------------------
| no (default)	               |      The container never restarts, even if it crashes.
----------------------------------------------------------------------------------------------------------------------------------------
| always	                   |       The container always restarts, regardless of the exit status.
----------------------------------------------------------------------------------------------------------------------------------------
| unless-stopped	           |          The container restarts unless manually stopped.
----------------------------------------------------------------------------------------------------------------------------------------
| on-failure[:max-retries]     |	The container restarts only if it fails (non-zero exit code). Optional: set a retry limit.
----------------------------------------------------------------------------------------------------------------------------------------




# How to set restart policy?
--------------------------------
- docker run -d --restart=<policy> nginx

# How to Change Restart Policy of an Existing Container?
-----------------------------------------------------------
You cannot modify restart policies directly for running containers. Instead, you must remove and recreate the container.

1. docker rm -f my-container
2. docker run -d --restart=unless-stopped --name my-container nginx

# how to check restart policy of running container?
---------------------------------------------------------
-docker inspect --format='{{.HostConfig.RestartPolicy.Name}}' <container-id>

**NOTE** : When you see exit code 0, it means your container stopped successfully. When you see exit status code > 0, it means it fails due to some reason.


