# Docker compose networks(front-end and back-end networks)
-------------------------------------------------------------
3-Tier deployment
Nginx -> UMS Web App -> MYSQL DB
-------------------------------------------
This configuration showcases a typical multi-tier application setup:

    - web-nginx (frontend) communicates with app-ums over the frontend network, acting as a reverse proxy.

    - app-ums communicates with db-mysql over the backend network, ensuring that the database is securely isolated from the external environment.

    - The separation of networks (frontend and backend) ensures that services only interact with those that they need to, providing both isolation and security.

    - frontend: The web-nginx and app-ums services are attached to this network, meaning these two services can communicate directly with each other. This network is typically used for communication between the reverse proxy (web-nginx) and the web application (app-ums).

    - backend: Both the app-ums and db-mysql services are connected to this network. The backend network facilitates communication between the application (app-ums) and the database (db-mysql). The db-mysql service is not accessible from web-nginx because it is only attached to the backend network, providing a level of security by isolating the database from the external-facing services.

    The networks provide an internal DNS-based service discovery mechanism, allowing services to communicate using service names instead of IP addresses. For example, app-ums can reach the db-mysql container by referring to it as db-mysql (via the DB_HOSTNAME environment variable).



#Start the stack
-------------------------------
- docker compose up -d
- docker ps

#verify and inspect docker networks
--------------------------------------
- docker network ls
- docker network inspect ums-stack_frontend
- docker network inspect ums-stack_backend

#verify connectivity between containers from web-nginx
----------------------------------------------------------
1. Communication between services: web-nginx and app-ums:
   -------------------------------------------------------
   web-nginx acts as a reverse proxy, forwarding incoming requests from port 8080 of the host to app-ums. Since both services share the frontend network, web-nginx can resolve and access app-ums via its container name (app-ums).

2. Network Usage for web-nginx (Nginx Reverse Proxy):
   ----------------------------------------------------
   - Attached to the frontend network.
   - It forwards incoming traffic from the host's port 8080 to the app-ums service. Since both web-nginx and app-ums are on the same frontend network, web-nginx can reach app-ums via its container name.
   - No access to db-mysql: Since web-nginx is not connected to the backend network, it cannot directly communicate with the database service, ensuring the database remains isolated.


                # Connect to web-nginx container
                docker exec -it ums-nginx /bin/sh

                # Alpine-based images: Install iputils
                apk update
                apk add iputils bind-tools

                # Debian/Ubuntu-based images: Install iputils
                apt-get update
                apt-get install -y iputils-ping dnsutils

                # Ping Services
                ping web-nginx
                ping app-ums
                ping db-mysql

                # Observation:
                # 1. web-nginx and app-ums will work.
                # 2. db-mysql will fail as there is NO ACCESS TO backend network.

                # nslookup services
                nslookup web-nginx
                nslookup app-ums
                nslookup db-mysql

                # Observation:
                # 1. web-nginx and app-ums will work.
                # 2. db-mysql will fail as there is NO ACCESS TO backend network.

                # dig
                dig web-nginx
                dig app-ums
                dig db-mysql

                # Observation:
                # 1. web-nginx and app-ums will work.
                # 2. db-mysql will fail as there is NO ACCESS TO backend network.


#app-ums: Verify Connectivity Between Containers from app-ums
--------------------------------------------------------------
1. Communication Between Services: app-ums and db-mysql:
   -----------------------------------------------------
   - app-ums communicates with db-mysql using the database hostname db-mysql and port 3306. Both services are attached to the backend network, allowing app-ums to resolve db-mysql via DNS without exposing the database to the external network.

2. Network Usage for app-ums (User Management WebApp):
   ----------------------------------------------------
   - Connected to both the frontend and backend networks.
   - This service can communicate with:
         - web-nginx over the frontend network.
         - db-mysql over the backend network using the environment variable DB_HOSTNAME=db-mysql.
   - app-ums scales to two replicas, meaning two instances of the application will be created. All replicas share the same networks and can access db-mysql over the backend network



            # Connect to app-ums container (one of the replicas)
            docker exec -it --user root ums-stack-app-ums-1 /bin/bash

            # Debian/Ubuntu-based images: Install iputils
            apt-get update
            apt-get install -y iputils-ping dnsutils

            # Ping Services
            ping web-nginx
            ping app-ums
            ping db-mysql

            # Observation:
            # 1. web-nginx, app-ums, and db-mysql will work.
            # 2. app-ums Service needs connectivity to both frontend and backend db.

            # nslookup services
            nslookup web-nginx
            nslookup app-ums
            nslookup db-mysql

            # Observation:
            # 1. web-nginx, app-ums, and db-mysql will work.
            # 2. app-ums Service needs connectivity to both frontend and backend db.

            # dig
            dig web-nginx
            dig app-ums
            dig db-mysql

            # Observation:
            # 1. web-nginx, app-ums, and db-mysql will work.
            # 2. app-ums Service needs connectivity to both frontend and backend db.


