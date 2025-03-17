# Access API that displays the container ID
--------------------------------------------------------
- curl http://localhost:8080/hello1

# Run a loop to check load balancing between multiple app-ums containers
- while true; do curl http://localhost:8080/hello1; echo ""; sleep 1; done

Observation: requests will be distributed across the containers


# Option 1: Restart NGINX service
docker compose restart web-nginx

# Option 2: Reload NGINX configuration without stopping the container
docker compose ps # Get container name
docker exec <nginx_container_name> nginx -s reload
docker exec ums-nginx nginx -s reload



- Scaling with Docker Compose: The /*deploy*/ option helps to scale services by specifying the number of replicas. This works in concert with load balancers like NGINX to distribute traffic.
- Session Persistence: Stateful applications like UMS WebApp require session persistence. Using ip_hash in NGINX ensures that client requests are routed consistently to the same container for a session.
- Custom NGINX Configuration: Leveraging Docker’s internal DNS resolver and custom NGINX configurations allows fine-grained control over service load balancing and session management.


Key features of deploy option:
- replicas: defines the number of container instances to run for a service


NOTE: For simple local development setups, deploy can be omitted, and service scaling can be done manually with commands like /*docker-compose up --scale*/