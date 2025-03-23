# Docker engine
------------------------
There is often confusion between “Docker Desktop” and “Docker Engine”. Docker Engine refers specifically to a subset of the Docker Desktop components which are free and open source and can be installed only on Linux. Docker Engine can build container images, run containers from them, and generally do most things that Docker Desktop can, but it is Linux only and doesn’t provide all of the developer experience polish that Docker Desktop provides.

# Docker underlying technology
---------------------------------
1. Namespaces
   ------------------------
   Docker namespaces are a fundamental feature of Linux that Docker uses to create isolated environments for containers. They provide a layer of isolation by creating separate instances of global system resources, making each container believe it has its own unique set of resources. Docker utilizes several types of namespaces, including PID (Process ID), NET (Network), MNT (Mount), UTS (Unix Timesharing System), IPC (InterProcess Communication), and USER namespaces and by leveraging these namespaces, Docker can create lightweight, portable, and secure containers that run consistently across different environments.

2. Cgroups
   -------------------------
   