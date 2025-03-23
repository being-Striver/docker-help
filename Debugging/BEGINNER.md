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


# Executing commands inside the container
-----------------------------------------------
docker exec command allow you to run arbitrary commands within a runtime container. This is the foundation for using system utilities for debugging.
- docker exec -it <container-name> <command>

   #Process monitoring with ps
   - docker exec -it <container-name> ps aux
     :a- show processes for all users
     :u- display process's user/owner
     :x- show processes not attached to a terminal

  The output will show a list of processes with information like:

                USER: The user that owns the process.
                PID: The process ID.
                %CPU: The percentage of CPU being used by the process.
                %MEM: The percentage of memory being used by the process.
                VSZ: Virtual memory size of the process (in kilobytes).
                RSS: Resident set size, the non-swapped physical memory a process has used (in kilobytes).
                STAT: Process state codes.
                START: The time the process started.
                COMMAND: The command that started the process.


  Interpreting ps Output
  The STAT column is particularly useful. Common status codes include:

                R: Running.
                S: Sleeping (waiting for an event).
                D: Uninterruptible sleep (usually waiting for I/O).
                T: Stopped (e.g., by a signal).
                Z: Zombie (a dead process that hasn't been reaped by its parent).

ps -ef: Shows the full command line for each process, which can be helpful for identifying the exact arguments being used.


  #Monitoring Virtual memory statistics with vmstat
  -----------------------------------------------------------
  The vmstat (virtual memory statistics) command provides information about system memory, processes, CPU activity, and I/O. It's useful for identifying bottlenecks related to memory or I/O.
  - docker exec -it <container-id> vmstat 1

  The 1 argument tells vmstat to update the statistics every 1 second.

  The output includes:

            procs: Information about running and blocked processes.
            memory: Information about virtual and real memory usage.
            swap: Information about swap usage.
            io: Information about block I/O.
            system: Information about CPU usage (interrupts, context switches).
            cpu: Information about CPU usage (user, system, idle, wait).

 Interpreting vmstat Output:
      - High swap usage indicates that the system is running out of physical memory and is swapping data to disk, which can significantly slow down performance.
      - High io values indicate that the system is spending a lot of time waiting for I/O operations, which can be a bottleneck.
      - High cs (context switches) values can indicate that the system is spending a lot of time switching between processes, which can also impact performance.
      - Low id (idle) CPU values indicate that the CPU is heavily utilized.
      - High wa (wait) CPU values indicate that the CPU is waiting for I/O operations.

 #Monitoring I/O statistics with iostat
 -----------------------------------------------
 The iostat (I/O statistics) command provides detailed information about I/O usage by block devices. It's useful for identifying which devices are experiencing high I/O load.

 Firstly you might have to install sysstat package which include iostat.

 - docker exec -it <container-name> apt-get update && apt-get install -y sysstat


- docker exec -it <container-name> iostat -x 1

The -x option provides extended statistics, and the 1 argument tells iostat to update the statistics every 1 second.

          The output includes:

                Device: The name of the block device.
                rrqm/s: Read requests merged per second.
                wrqm/s: Write requests merged per second.
                r/s: Read requests per second.
                w/s: Write requests per second.
                rkB/s: Kilobytes read per second.
                wkB/s: Kilobytes written per second.
                avgrq-sz: Average request size (in sectors).
                avgqu-sz: Average queue length.
                await: Average time (in milliseconds) for I/O operations to complete.
                r_await: Average time (in milliseconds) for read operations to complete.
                w_await: Average time (in milliseconds) for write operations to complete.
                svctm: Service time (in milliseconds).
                %util: Percentage of time the device is busy.

        Interpreting iostat Output
                - High %util values indicate that the device is heavily utilized and may be a bottleneck.
                - High avgqu-sz values indicate that there is a long queue of I/O requests waiting to be processed.
                - High await values indicate that I/O operations are taking a long time to complete.



  #Monitoring network connections with netstat
  -----------------------------------------------
  netstat (network statistics) is a command-line tool that displays network connections, routing tables, interface statistics, and masquerade connections. However, netstat is considered deprecated in favor of ss (socket statistics), which is faster and provides more information.

  - docker exec -it <container-name> netstat -an

  -a: show all socket
  -n: show numerical addresses instead of trying to determine symbolic host names


   Interpreting netstat and ss Output
   -----------------------------------------
  The output shows a list of network connections, including:

          State: The state of the connection (e.g., ESTABLISHED, LISTEN, TIME_WAIT).
          Recv-Q: The number of bytes not copied by the user program connected to this socket.
          Send-Q: The number of bytes not acknowledged by the remote host.
          Local Address: The local address and port.
          Foreign Address: The remote address and port.
          A large number of connections in the TIME_WAIT state can indicate a problem with connection management.
          Connections in the LISTEN state indicate that the process is listening for incoming connections on that port.
          Connections in the ESTABLISHED state indicate that a connection is active.
          High Recv-Q or Send-Q values can indicate network congestion or a problem with the application's ability to process data.

# Interactive debugging with shell
-----------------------------------------
 #install python debugger tool
 - apt-get upadte && apt-get install -y python3-pip
 - pip3 install ipdb


# Restarting services and observing changes
--------------------------------------------------
Restarting services and observing changes are fundamental aspects of debugging in a Docker Compose environment. When debugging, you'll often need to modify your application code or configuration, and then restart the relevant service to see the effect of your changes. This iterative process of making changes, restarting, and observing is crucial for identifying and fixing bugs. Docker Compose provides convenient commands for restarting services and viewing their logs, making this process efficient.


Understanding Service Restarts in Docker Compose
------------------------------------------------------
When working with Docker Compose, restarting a service involves stopping the existing container and creating a new one based on the updated image or configuration. This process allows you to apply changes made to your application code, environment variables, or Dockerfile. Docker Compose offers several ways to restart services, each with its own nuances.

The /*docker-compose restart*/ command is the most straightforward way to restart one or more services defined in your docker-compose.yml file. It stops the containers and then starts them again.

Behind the scenes:
he docker-compose restart command essentially performs two actions:

    docker stop: Sends a SIGTERM signal to the container, allowing it to shut down gracefully. After a timeout period (defaulting to 10 seconds), if the container hasn't stopped, a SIGKILL signal is sent to forcefully terminate it.
    docker start: Creates a new container based on the service's image and configuration, and then starts it.


 - **docker-compose up --no-deps -d --build <service_name>**

 --no-deps: This flag tells Docker Compose not to start any services that the specified service depends on. This is useful when you only want to restart a single service and avoid unnecessary restarts of its dependencies.

 --build: This flag forces Docker Compose to rebuild the image for the service before restarting it. This is essential when you've made changes to your Dockerfile or application code that require a new image to be built.



# Common dockerfile errors and how to avoid them
------------------------------------------------------
1. Not using .dockerignore file
   ------------------------------
  Error: Including unnecessary files and directories in the Docker image.

  Explanation: The COPY and ADD instructions copy files and directories from the host machine into the Docker image. If you don't exclude unnecessary files and directories, the image size will be larger than necessary


  How to Avoid: Create a .dockerignore file in the same directory as your Dockerfile. This file specifies files and directories that should be excluded from the Docker image.


2. Ordering Instructions Inefficiently
   --------------------------------------
  Error: Placing instructions that change frequently at the beginning of the Dockerfile.

  Explanation: Docker builds images layer by layer and caches each layer. If an instruction changes, all subsequent layers must be rebuilt. Placing frequently changing instructions at the beginning of the Dockerfile invalidates the cache for all subsequent layers, slowing down the build process.

  How to Avoid: Order instructions from least to most frequently changing. Place instructions that rarely change at the beginning of the Dockerfile and instructions that change frequently at the end.


3. Using ADD instead of COPY when not necessary
   --------------------------------------------
  Error: Using ADD when COPY would suffice.

  Explanation: The ADD instruction has more features than COPY, such as extracting tar archives and fetching files from URLs. However, these features can also introduce security risks and make the build process less predictable.

  How to Avoid: Use COPY unless you specifically need the features of ADD.

4. Installing Packages Without Updating the Package List
   -----------------------------------------------------
  Error: Running apt-get install <package> without first running apt-get update.

  Explanation: The package list needs to be updated before installing packages to ensure you're getting the latest versions and dependencies.

  How to Avoid: Always run apt-get update before apt-get install. Combine them into a single RUN instruction to reduce the number of layers.

 
5. Not Using a Specific Tag for the Base Image
   ----------------------------------------------
  Error: Using FROM ubuntu instead of FROM ubuntu:20.04.

  Explanation: When you don't specify a tag, Docker defaults to the latest tag. The latest tag is a floating tag, meaning it can change over time. This can lead to inconsistent builds and unexpected behavior if the latest image is updated with breaking changes.

  How to Avoid: Always specify a specific tag for your base image. This ensures that you're using a consistent version of the image.

6. Using `docker build --no-cache` for debugging
   ----------------------------------------------
   The Dockerfile is the blueprint for building Docker images. During the build process, Docker leverages a caching mechanism to speed up subsequent builds. This caching can be incredibly efficient, but it can also mask problems in your Dockerfile. When debugging, it's crucial to bypass this cache to ensure you're truly building the image from scratch and seeing the effects of your changes. The `docker build --no-cache` command is your primary tool for this purpose. It forces Docker to execute each instruction in the Dockerfile as if it were the first time, ignoring any cached layers. This ensures that any errors or unexpected behavior are not due to stale data or outdated instructions.


   How caching works in docker?
   -----------------------------
   When you run `docker build`, Docker checks each instruction in your Dockerfile against its cache. The cache key includes the instruction itself, the file's modification times (for COPY and ADD instructions), and the cache keys of the parent images. If Docker finds a matching cache key, it reuses the cached layer. If not, it executes the instruction and creates a new layer, which is then cached.


   Benefits of caching:
   --------------------
   - Faster Build Times: Reusing cached layers significantly reduces build times, especially for large images with many dependencies.
   - Reduced Resource Consumption: Caching avoids redundant operations, saving CPU, memory, and network bandwidth.

  Drawbacks of caching:
  ---------------------
  - Masking Errors: Caching can hide errors in your Dockerfile, especially when you're making changes and iterating quickly.If  an instruction fails, but a cached layer exists from a previous, successful build, Docker might reuse the cached layer, masking the error.
  - Stale Data: If a dependency changes without Docker detecting it (e.g., a file is modified outside of Docker's awareness), the cached layer might contain stale data, leading to unexpected behavior.


 The `--no-cache` option forces Docker to ignore all cached layers and build the image from scratch. This is essential for debugging Dockerfile issues because it ensures that you're seeing the true effects of your changes.


 When to Use `--no-cache` :
 ---------------------------
- After Making Changes to Your Dockerfile: Whenever you modify your Dockerfile, use `--no-cache` to ensure that your changes are being applied correctly.
- When Encountering Unexpected Behavior: If your container is behaving unexpectedly, and you suspect that caching might be the issue, use `--no-cache` to rule it out.
- When Updating Dependencies: If you've updated dependencies in your application (e.g., by running pip install -r requirements.txt or npm install), use `--no-cache` to ensure that the new dependencies are being installed correctly.
- Periodically for Sanity Checks: Even if you haven't made any changes, it's a good practice to periodically run docker build `--no-cache` to ensure that your Dockerfile is still working as expected.



# Multi-stage builds and debugging skills
--------------------------------------------
Multi-stage builds in Dockerfiles are a powerful technique for optimizing image size, improving security, and simplifying the build process. By using multiple `FROM` statements, you can leverage different base images for different stages of your build, ultimately resulting in a smaller and more efficient final image. This lesson will explore multi-stage builds in detail, focusing on debugging strategies to address common issues that arise during their implementation.


 Understanding of Multi-stage builds:
 ----------------------------------------
 Multi-stage builds allow you to use multiple `FROM` statements in a single Dockerfile. Each `FROM` instruction starts a new "stage" of the build. You can selectively copy artifacts from one stage to another, discarding unnecessary dependencies and intermediate files in the final image.


 Benefits of Multi-Stage Builds:
 ----------------------------------
 - Reduced Image Size: By only copying the necessary artifacts to the final stage, you can significantly reduce the size of your Docker image. This leads to faster downloads, reduced storage costs, and improved deployment times.
 - Improved Security: Multi-stage builds allow you to use different base images for different stages. For example, you can use a base image with build tools for compilation and then switch to a minimal base image for the final runtime environment, reducing the attack surface.
- Simplified Dockerfiles: Multi-stage builds can make your Dockerfiles more readable and maintainable by separating the build process into logical stages.
- Faster Build Times: Although it might seem counterintuitive, multi-stage builds can sometimes lead to faster build times. By isolating dependencies and build processes, you can leverage Docker's caching mechanism more effectively.


How Multi-Stage Builds Work:
------------------------------
Each `FROM` instruction in a Dockerfile defines a new stage. You can give each stage a name using the `AS` keyword. This allows you to reference stages later in the Dockerfile when copying artifacts.

Naming Stages:
------------------------------
Naming stages using the `AS` keyword is crucial for referencing them later in the Dockerfile. Stage names must be unique within the Dockerfile. If you don't name a stage, Docker assigns it an `integer ID`, but using names is much more readable and maintainable.

 #Debugging strategies for multi-stage builds:
 ------------------------------------------------
 Isolating images:
 ---------------------
 The key to debugging multi-stage builds is to isolate each stage and verify that it is working correctly. You can do this by building each stage separately and running a container from it.

 - to build and run the `builder` stage:
  : `docker build -t builder-stage . --target builder`
  : `docker run --rm -it builde-stage bash`

  This will build the builder stage and start a container with a bash shell. You can then use this container to inspect the file system, run commands, and verify that the build process is working as expected.

 Using `docker build --progress=plain` :
 ----------------------------------------
 The `docker build --progress=plain` option provides detailed output of each build step, making it easier to identify errors. This option is especially useful for debugging multi-stage builds because it shows the output of each stage separately.
 
 example command:
  : `docker build --progess=plain -t my-image .`


using environment variables for debugging:
------------------------------------------
You can use environment variables to control the behavior of your build process and enable debugging features. For example, you can set an environment variable to enable verbose logging or to skip certain steps in the build process.

Leveraging HEALTHCHECKS:
----------------------------
You can define healthchecks in your final stage to ensure that your application is running correctly. If the healthcheck fails, Docker will restart the container, giving you an opportunity to investigate the issue.

 #Optimizing Dockerfile for faster builds and smaller images
 -----------------------------------------------------------
 Optimizing Dockerfiles is crucial for creating efficient and scalable applications. Smaller images translate to faster deployments, reduced storage costs, and improved security. Faster builds mean quicker iteration cycles and more efficient development workflows.

  Steps:
  ---------
  1. leveraging multi-stage build
  2. optimizing layer ordering
     -----------------------------
     The order of instructions in a Dockerfile significantly impacts build time due to caching. Docker caches each layer of the image. If a layer changes, all subsequent layers must be rebuilt. Therefore, it's crucial to place instructions that change frequently towards the end of the Dockerfile and instructions that change infrequently towards the beginning.

     General Layer Ordering Strategy:
     ------------------------------------
      - Base Image: FROM instruction.
      - Install System Dependencies: RUN apt-get update && apt-get install -y ...
      - Copy Dependency Files: COPY package*.json ./ or COPY requirements.txt .
      - Install Dependencies: RUN npm install or RUN pip install -r requirements.txt
      - Copy Application Code: COPY . .
      - Define Entrypoint and Command: ENTRYPOINT and CMD
  3. Using `.dockerignore` files
    -----------------------------
    A `.dockerignore` file specifies files and directories that should be excluded from the Docker build context. This prevents unnecessary files from being copied into the image, reducing the image size and improving build time. 

    Benefits of Using `.dockerignore`:
    ------------------------------------
    Reduced Image Size: Prevents unnecessary files from being included in the image.
    Improved Build Time: Reduces the amount of data that needs to be copied during the build process.
    Enhanced Security: Prevents sensitive files from being included in the image.

  4. Choosing the Right Base Image
  5. Minimizing Layers
     -------------------
     Combine multiple instructions into a single RUN instruction using the && operator. This reduces the number of layers and improves caching.

  6. Using shell scripting
     ----------------------
     Use shell scripting to perform complex operations within a single `RUN`instruction. This reduces the number of layers and improves readability.

  7. Using specific package version:
     ---------------------------------
     When installing packages, specify the exact version number to avoid unexpected updates or changes in behavior. This ensures that your application is running with the expected dependencies.


# Using Remote debugging tools
------------------------------------