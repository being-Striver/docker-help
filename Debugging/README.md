# Docker engine configuration
---------------------------------------
Docker Engine is configured through command-line options and configuration files.

- daemon.json: This file is used to configure various Docker daemon settings, such as logging, storage drivers, and network settings. It's typically located in /etc/docker/daemon.json on Linux systems.
- Logging: Configure the logging driver to control how Docker logs are collected and stored. Common logging drivers include json-file, syslog, and journald.
- Storage Driver: Choose a storage driver to manage how Docker images and containers are stored on disk. Common storage drivers include overlay2, aufs, and devicemapper.
- Network: Configure Docker networks to allow containers to communicate with each other. You can create custom networks with specific IP address ranges and DNS settings.


Example:
-------------------
To configure Docker Engine to use the syslog logging driver, you would create or modify the /etc/docker/daemon.json file with the following content:
    {
  "log-driver": "syslog"
    }

Then, restart the Docker daemon to apply the changes:
 sudo systemctl restart docker


# Troubleshooting common installation issue
----------------------------------------------------
1. Permissions Issues: On Linux, you might encounter permission issues when running Docker commands. This is typically because your user is not a member of the docker group. To fix this, add your user to the docker group and restart your system:
   - sudo usermod -aG docker $USER
   - newgrp docker

2. Virtualization Issues: Docker requires virtualization to be enabled in your BIOS. If you're using Docker Desktop on Windows or macOS, make sure that virtualization is enabled.

 #you can remove and stop container in a single command.
 -docker stop <container_id> && docker rm <container_id>


3. Port Conflicts: If you try to run a container on a port that is already in use, Docker will return an error. To resolve this, either stop the process using the port or use a different port for the container. You can use the /*netstat or ss*/ command to find out which process is using a particular port.

  Use netstat -tulnp (Linux) or Get-Process -Id (Get-NetTCPConnection -LocalPort <port_number>).OwningProcess (PowerShell on Windows) to find the process using the port

4. Image Not Found: This error occurs when Docker cannot locate the specified image, either locally or in a remote registry like Docker Hub.
  Error:
   -docker: Error response from daemon: manifest for nonexistingimage:latest not found: manifest unknown: manifest unknown.
See 'docker run --help'.


5. Container Exiting immediately: A container might exit immediately after starting due to various reasons, such as an incorrect entry point, a missing command, or an application error.
 
 example:
  The container starts and then immediately stops. docker ps -a shows the container with an "Exited" status.

  Causes:
        - Incorrect entry point or command: The ENTRYPOINT or CMD in the Dockerfile might be incorrect or missing.
        - Application error: The application running inside the container might be encountering an error and exiting.
        - Missing dependencies: The container might be missing required dependencies.
        - Insufficient permissions: The application might not have the necessary permissions to run.

 Troubleshooting:
    - inspect container logs
    - Check the Dockerfile: Review the ENTRYPOINT and CMD instructions in the Dockerfile to ensure they are correct.
    - Execute a shell inside the container: Use docker exec -it <container_id> bash to enter the container and investigate the environment. This allows you to manually run commands and check for missing dependencies or permission issues
    - Override the entrypoint: When running the container, override the entrypoint to run a shell and investigate.


6. Volume mount issues: Problems with volume mounts can prevent your application from accessing necessary data or persisting data correctly.

    example:
     The application inside the container cannot access files in the mounted volume, or changes made to files in the volume are not reflected on the host.

     Causes:
       - Incorrect path: The host path or container path might be incorrect.
       - Permissions issues: The container might not have the necessary permissions to access the volume.
       - Volume not mounted: The volume might not be mounted correctly.
     
    Troubleshooting:
      - Verify the volume mount: Use docker inspect <container_id> to check the volume mount configuration. Look for the Mounts section
      - Check file permissions: Ensure that the container user has the necessary permissions to read and write to the volume. You might need to adjust file permissions on the host or within the container.
      - Verify the host path: Make sure the host path exists and is accessible
      - Use named volumes: Consider using named volumes instead of host path mounts for better portability and management

7. Resource Constraints: Containers might experience performance issues or fail to start if they are limited by CPU, memory, or other resources.
    Example:
     - The application inside the container runs slowly or crashes due to insufficient memory.
  
   Cause:
     - Insufficient memory: The container might be running out of memory.
     - CPU throttling: The container might be throttled due to CPU limits.
     - Disk I/O limitations: The container might be experiencing slow disk I/O.

   Troubleshooting:
     - Monitor resource usage: Use docker stats to monitor the resource usage of containers.
     - Adjust resource limits: Increase the memory or CPU limits for the container using the --memory and --cpus flags in the docker run command or in the Docker Compose file.


# Technique to debug
----------------------------
 #following logs in real-time
 - docker logs -f <container-id>

 #Displaying recent logs
 - docker logs --tail <number-of-lines> <container-id>

 #showing timestamp
 - docker logs -t (--timestamps) <container-id>

 #filtering logs by time
 - You can filter logs based on a specific time range using the --since and --until options.
 - --since option: Show logs since timestamp (e.g., 2023-10-26T12:00:00, 10m, 10 minutes ago)
 - --until option:  Show logs until timestamp (e.g., 2023-10-26T13:00:00)
  
 - docker logs --since <timestamp> --until <timestamp> <container_id_or_name>

  #example
  To display logs from the my-flask-app container between 12:00 PM and 1:00 PM on October 26, 2023:
  - docker logs --since "2023-10-26T12:00:00" --until "2023-10-26T13:00:00" my-flask-app


# understanding log driver
-------------------------------
Docker uses log drivers to manage how container logs are handled. The default log driver is json-file, which stores logs as JSON files on the host machine. However, Docker supports several other log drivers, each with its own advantages and disadvantages. Understanding log drivers is crucial for configuring logging appropriately for your applications.


Common log drivers:

- json-file (Default): Stores logs as JSON files on the host machine. Simple to use but can consume disk space if not properly managed.
- syslog: Sends logs to a syslog server. Useful for centralized logging and integration with existing monitoring infrastructure.
- journald: Sends logs to the systemd journal. Integrates well with systemd-based systems.
- fluentd: Sends logs to a Fluentd collector. Provides flexible log processing and routing capabilities.
- awslogs: Sends logs to Amazon CloudWatch Logs. Suitable for applications running on AWS.
- gelf: Sends logs to a Graylog server. Designed for structured logging and analysis.

 #Configuring log drivers
 -----------------------------
 You can configure the log driver for a container using the --log-driver option when running the container:
 - docker run --log-driver=<log_driver_name> <image-name>

example:
  To run a container using syslog log driver:
   - docker run --log-driver=syslog --name my-syslog-app myimage
  
  You can also configure log driver options using the --log-opt option. For example, to specify the syslog address:
  - docker run --log-driver=syslog --log-opt syslog-address=tcp://192.168.1.10:514 --name my-syslog-app myimage
  

#Inspecting log driver configuration
- docker inspect <container-id>

The  output will include a section LogConfig section that shows the configured log drivers and options.



# Understand docker inspect output
----------------------------------------
The docker inspect command returns a JSON (JavaScript Object Notation) document containing detailed information about a Docker object (container, image, volume, network, etc.). The specific information returned depends on the type of object being inspected. For containers, this includes network settings, mount points, environment variables, command-line arguments, and much more. For images, it includes information about the layers, architecture, and entry point.

  Basic syntax: docker inspect <container-id or image or volume or network>


Key Sections of the Output:
-------------------------------------
The JSON output of docker inspect is structured hierarchically. Here's a breakdown of some of the most important sections when inspecting a container:

    - Id: The unique identifier of the container.
    - Created: The timestamp when the container was created.
    - Path: The command that will be executed when the container starts.
    - Args: Arguments passed to the command.
    - State: Information about the container's current state (running, stopped, etc.), including its status, start time, and any error messages.
    - Image: The ID of the image used to create the container.
    - ResolvConfPath: The path to the container's DNS configuration file.
    - HostnamePath: The path to the container's hostname file.
    - HostsPath: The path to the container's hosts file.
    - LogPath: The path to the container's log file.
    - Name: The name of the container.
    - RestartCount: The number of times the container has been restarted.
    - Driver: The storage driver used by the container.
    - Platform: The platform the container is running on (e.g., linux).
    - Mounts: A list of mount points, showing how volumes and host directories are mounted into the container.
    - Config: Configuration settings defined in the image, such as environment variables, exposed ports, and labels.
    - Env: A list of environment variables set for the container.
    - ExposedPorts: A list of ports exposed by the container.
    - Labels: A set of key-value pairs used to add metadata to the container.
    - NetworkSettings: Information about the container's network configuration.
    - Networks: Details about the networks the container is connected to, including its IP address, gateway, and MAC address.



Inspecting Images:
---------------------------------
When inspecting images, docker inspect provides information about the image's layers, architecture, and configuration. Key sections include:

    - Id: The unique identifier of the image.
    - Created: The timestamp when the image was created.
    - Architecture: The architecture the image is built for (e.g., amd64).
    - Os: The operating system the image is based on (e.g., linux).
    - RootFS: Information about the image's root filesystem, including the layers that make up the image.
    - Config: Configuration settings defined in the image, such as the entry point, command, environment variables, and labels.
    - Env: A list of environment variables defined in the image.
    - Labels: A set of key-value pairs used to add metadata to the image.