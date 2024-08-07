Proxy servers act as intermediaries between clients and servers, facilitating or controlling access to resources. 
There are two primary types of proxy servers: forward proxies and reverse proxies. 


- A forward proxy acts on behalf of the client, retrieving data from the internet and delivering it to the client. It hides the client’s IP address from the server.
     A forward proxy caches frequently accessed web pages. When a user requests a cached page, the proxy serves it without fetching it from the web server again.


- A reverse proxy acts on behalf of the server, intercepting requests from clients and forwarding them to the appropriate backend server. It hides the server's details from the client.
    load balancing
    Security
    SSL Termination
    Caching and Compression

    - if the reverse proxy fails it can be a single point of failure

Example - 
Nginx
    Description: A high-performance web server and reverse proxy server.
    Use Cases: Load balancing, SSL termination, serving static content, caching.

## Reverse Proxy vs load balancer

In a microservice architecture, both reverse proxies and load balancers play crucial roles in managing and directing traffic, but they serve different purposes and have distinct functionalities. Here’s a comparison of reverse proxies and load balancers:

### Reverse Proxy

**Purpose**: A reverse proxy acts as an intermediary for requests from clients seeking resources from servers. It forwards client requests to the appropriate backend servers and then returns the server's response to the client.

**Key Functions**:
1. **Security**: Protects backend servers by hiding their identity and preventing direct access from clients.
2. **Load Distribution**: Distributes incoming requests among multiple backend servers to optimize resource use and avoid overloading any single server.
3. **SSL Termination**: Handles SSL encryption and decryption to offload this task from backend servers.
4. **Caching**: Stores copies of frequently accessed resources to reduce the load on backend servers and improve response times.
5. **Compression**: Compresses responses to reduce the amount of data transmitted over the network.
6. **Logging and Monitoring**: Provides centralized logging and monitoring of traffic, which is useful for troubleshooting and performance analysis.

**Examples**: Nginx, HAProxy, Apache HTTP Server, Traefik.

### Load Balancer

**Purpose**: A load balancer distributes incoming network or application traffic across multiple servers to ensure no single server becomes a bottleneck. It enhances the availability and reliability of applications.

**Key Functions**:
1. **Traffic Distribution**: Balances the load by distributing client requests across multiple servers based on various algorithms (e.g., round-robin, least connections, IP hash).
2. **High Availability**: Provides failover capabilities by automatically redirecting traffic from failed or unhealthy servers to healthy ones.
3. **Scalability**: Supports scaling out (adding more servers) to handle increased traffic.
4. **Session Persistence**: Ensures that requests from the same client are consistently routed to the same server to maintain session state.
5. **Health Checks**: Continuously monitors the health of backend servers and removes unhealthy servers from the pool until they are restored.

**Examples**: Nginx, HAProxy, AWS Elastic Load Balancer (ELB), Google Cloud Load Balancing, F5 BIG-IP.

### Comparison and Use Cases

1. **Reverse Proxy**:
   - **Microservice Routing**: In a microservice architecture, a reverse proxy can route requests to the appropriate microservice based on the URL path, hostname, or other request attributes.
   - **Security and Anonymity**: It provides an additional security layer by obscuring the backend infrastructure.
   - **Centralized Control**: Useful for implementing centralized policies, such as SSL termination and response caching.

2. **Load Balancer**:
   - **Load Distribution**: Primarily used to distribute incoming traffic evenly across multiple instances of a microservice to ensure no single instance is overwhelmed.
   - **Fault Tolerance**: Enhances reliability by rerouting traffic from failed instances to healthy ones.
   - **Scalability**: Essential for scaling microservices horizontally by adding more instances to handle increased traffic.

### Combined Usage

In many microservice architectures, reverse proxies and load balancers are used together to leverage the strengths of both:

- **Reverse Proxy at the Edge**: An edge reverse proxy handles client requests, providing SSL termination, caching, and routing to appropriate services.
- **Internal Load Balancing**: Within the internal network, load balancers distribute traffic among instances of individual microservices, ensuring even load distribution and high availability.

### Example Scenario

Imagine a microservice architecture for an e-commerce application:
- **Reverse Proxy (e.g., Nginx)** at the edge routes incoming requests to the appropriate service based on the URL path (e.g., `/api/products` to the product service, `/api/orders` to the order service).
- **Load Balancer (e.g., HAProxy)** distributes requests among multiple instances of each microservice, ensuring that no single instance becomes a bottleneck and enhancing fault tolerance.

By combining reverse proxies and load balancers, you can achieve a robust, scalable, and secure microservice architecture.


[Link to a medium article](https://medium.com/codenx/load-balancer-vs-reverse-proxy-vs-api-gateway-fcb79912abbf)
