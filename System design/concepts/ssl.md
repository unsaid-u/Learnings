### What are SSL Certificates?

**SSL (Secure Sockets Layer) certificates** are digital certificates used to establish a secure and encrypted connection between a web server and a web browser. SSL has been succeeded by TLS (Transport Layer Security), but the term "SSL" is still commonly used to refer to these certificates. 

### How SSL Certificates Work

1. **Encryption**: SSL certificates use encryption to ensure that data transmitted between the web server and browser remains private. This encryption makes it difficult for unauthorized parties to intercept or tamper with the data.

2. **Authentication**: SSL certificates authenticate the identity of the website. When a browser connects to a website, the SSL certificate ensures that the website is legitimate and not an imposter.

3. **Integrity**: SSL certificates provide data integrity by ensuring that the data sent between the server and the browser cannot be altered or corrupted without being detected.

### Process of Establishing an SSL Connection

1. **Handshake**: When a browser attempts to connect to a website secured with SSL, the browser and the server initiate an SSL handshake. This involves several steps:
   - The browser requests the server to identify itself.
   - The server sends a copy of its SSL certificate, including the server's public key.
   - The browser checks the certificate against a list of trusted Certificate Authorities (CAs). If the certificate is trusted, the browser generates a session key and encrypts it with the server's public key, then sends it to the server.
   - The server decrypts the session key using its private key and establishes a secure session.

2. **Encryption**: Once the handshake is complete, the browser and server use the session key to encrypt and decrypt the data they send to each other.

### Uses of SSL Certificates

- **Secure Online Transactions**: SSL certificates are essential for securing online transactions, such as online banking, shopping, and payment processing.
- **Data Privacy**: They ensure that any data transmitted between a user and a website is encrypted and secure from eavesdroppers.
- **Website Authentication**: They verify the identity of a website, ensuring users are interacting with the intended site and not a malicious imposter.
- **Trust**: SSL certificates increase user trust, as the presence of an SSL certificate is indicated by a padlock icon in the browser address bar and the use of "https" in the URL.

### What is HTTPS?

**HTTPS (Hypertext Transfer Protocol Secure)** is the secure version of HTTP, the protocol over which data is sent between a browser and a website. HTTPS uses SSL/TLS to encrypt data, ensuring secure communication.

### Benefits of HTTPS

- **Security**: HTTPS encrypts data, making it difficult for unauthorized parties to intercept or tamper with the data transmitted between the user and the website.
- **Authentication**: HTTPS authenticates the website, ensuring users are connecting to the legitimate site.
- **SEO Benefits**: Search engines like Google give preference to HTTPS sites, potentially improving search rankings.
- **User Trust**: HTTPS sites are perceived as more trustworthy by users, indicated by the padlock icon in the browser.

### Summary

- **SSL Certificates**: Digital certificates that provide encryption, authentication, and data integrity for secure communication between a web server and browser.
- **HTTPS**: The secure version of HTTP, utilizing SSL/TLS to encrypt data and ensure secure communication.
- **Uses**: SSL certificates and HTTPS are used for securing online transactions, protecting data privacy, authenticating websites, and building user trust.

### When Does SSL Certificate Verification Take Place?

**SSL certificate verification** occurs during the initial connection process between a client (e.g., a web browser or an API client) and a server. This process is part of the **SSL/TLS handshake** and happens before any data is transmitted between the client and server.

Here's how it works:
1. **Client Hello**: The client (e.g., a browser or API client) initiates the connection by sending a "Client Hello" message to the server, including the client's supported encryption methods.
   
2. **Server Hello and Certificate**: The server responds with a "Server Hello" message, which includes the server's SSL certificate.

3. **Certificate Verification**: The client checks the server's SSL certificate against a list of trusted Certificate Authorities (CAs) to verify that the certificate is valid, not expired, and has not been revoked. The client also checks that the domain name in the certificate matches the domain it is trying to connect to.

4. **Key Exchange and Secure Session**: If the certificate is valid, the client generates a session key, encrypts it with the server's public key (from the SSL certificate), and sends it to the server. The server decrypts the session key using its private key, and a secure session is established.

5. **Data Transmission**: Once the secure session is established, encrypted data can be transmitted between the client and server.

### Where Do I Store the SSL Certificate in My Application?

**For a web server or backend application**, the SSL certificate and private key are typically stored on the server that hosts your application. The specific location and method of storage depend on your web server software:

- **Apache**: The SSL certificate and private key are stored in the configuration files, often in the `/etc/ssl/certs/` and `/etc/ssl/private/` directories.
  
- **Nginx**: The SSL certificate and private key are specified in the server block configuration, typically stored in `/etc/nginx/ssl/` or similar directories.
  
- **Java-based Servers (e.g., Tomcat, Spring Boot)**: The SSL certificate and private key can be stored in a **Java KeyStore (JKS)** file, and the path to this file is specified in the server configuration.

- **Cloud Platforms**: If you're deploying to a cloud platform (like AWS, Azure, or Google Cloud), you might manage SSL certificates through the platform's services, such as AWS Certificate Manager (ACM).

**For client-side applications** (e.g., mobile apps or API clients), the trusted root CA certificates are usually stored in the operating system's certificate store. Custom certificates (e.g., for internal APIs) might need to be added to the certificate store manually or embedded in the application.

### Is an SSL Certificate Required for Every API Request?

**Yes, SSL/TLS is required for every API request** if you want to ensure secure communication. Once the initial SSL/TLS handshake is completed, a secure session is established, and all subsequent API requests and responses within that session are encrypted.

**Key Points**:
- **Single Handshake Per Session**: The SSL/TLS handshake happens once per session. After the handshake, all data within the session is encrypted using the session key.
  
- **Persistent Connections**: If you're using persistent HTTP connections (e.g., keep-alive), the SSL/TLS handshake happens once at the start of the connection, and all API requests over that connection are encrypted.
  
- **Session Reuse**: Some protocols, like HTTP/2, allow for connection reuse, where a single TLS session can be reused for multiple requests, reducing the need for repeated handshakes.

**Important**: Even though the handshake happens only once per session, every API request benefits from the established secure connection, ensuring data privacy, integrity, and authentication.