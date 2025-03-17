# Basics of docker compose
------------------------------------------------------------------------------------------------------------------
- It is a tool for defining and running multi-container applications.
- It helps for an efficient development and deployment experience.
- Compose simplifies the control of your entire application stack, making it easy to manage services, networks and volumes in a single yaml configuartion file.
- compose works in all environments; production, staging, development, testing as well as CI workflows
- It also has commands for managing the whole lifecycle of your application:
     - start, stop and rebuild services
     - view the status of running services
     - Stream the log output of running services

# How to start containers
---------------------------------------
- docker compose up -d (it will start container in detach mode).
  
  #View MySQL container logs
  - docker compose logs mysql

  #Connect to MySQL container
  - docker exec -it ums-mysqldb mysql -u root -pdbpassword11
  - to come out of container, type exit


     #List Docker Volumes
     - docker volume ls

     #Inspect volume details
     - docker volume inspect ums-stack_mydb
  
    #Stop containers and remove volumes
     - docker compose down -v


NOTE: In this demo, we deployed a MySQL database using Docker Compose. The database was configured with persistent data storage using Docker volumes, ensuring that the data remains available even when containers are stopped or removed.


