# Introduction
------------------------------------------------------------------------------------------------------------------------
You can control the order of service startup and shutdown with the depends_on attribute. Compose always starts and stops containers in dependency order, where dependencies are determined by depends_on, links, volumes_from, and network_mode: "service:...".

With the depends_on attribute, you can control the order of service startup and shutdown. It is useful if services are closely coupled, and the startup sequence impacts the application's functionality.