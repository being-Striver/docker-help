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
   `cgroups` or “control groups” are a Linux kernel feature that allows you to allocate and manage resources, such as CPU, memory, network bandwidth, and I/O, among groups of processes running on a system. It plays a crucial role in providing resource isolation and limiting the resources that a running container can use. Docker utilizes cgroups to enforce resource constraints on containers, allowing them to have a consistent and predictable behavior.


3. Union FileSystems
   -------------------------
   Union file systems, also known as `UnionFS`, play a crucial role in the overall functioning of Docker. It’s a unique type of filesystem that creates a virtual, layered file structure by overlaying multiple directories. Instead of modifying the original file system or merging directories, UnionFS enables the simultaneous mounting of multiple directories on a single mount point while keeping their contents separate. This feature is especially beneficial in the context of Docker, as it allows us to manage and optimize storage performance by minimizing duplication and reducing the container image size.


