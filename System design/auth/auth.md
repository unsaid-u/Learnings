Stateless Auth - JWT , OAuth
Stateful Auth - Sessions , cookies


Statful - sessions 
    - /login -> username, password ---> DB 
    - DB -> after matching -> return session_id 
            - save this session_id in redis (n-memory database)
    - session_id --> return to client -> will be used for api auth (x-session-id)
    - so this session_id has a an expiration time and is revoked after logout

    Pros:
        - short term Auth (ex: banking website)
        - controlled access 
    Cons:
        - memory dependent - difficult scalability
        - Server storage dependent
        - memory can be a point a failure


Stateless - JWT 
    - /login -> username, password ---> DB 
    - DB -> after match -> payload to be signed  -> sign(payload + secret_key) ---> signature
    - server returns a signed JOSN payload to client (aka access token) with a shorter expiration time
    - on request from client server verifies signature with its key 

    Pros:
        - memory efficient
        - longer session duration

    Cons:
        - difficult to manage 
        - less secure ?

___

if i am JWT token auth
so far i know that on cliet req the server will generate a token send it to the client, which will be used later by client for making api requests 
correct me if i am wrong
and on this step the server will verify the token
now i am not sure how does the server verifies it, does it store the token somewhere

what will be the best practice for doing such  verifictaion ??

You’re correct in understanding the basic flow of JWT authentication. Let me clarify the process and best practices for verifying JWT tokens.

#### JWT Authentication Flow

1. **Client Request**: The client authenticates by providing credentials (e.g., username and password) to the server.
2. **Server Response**: Upon successful authentication, the server generates a JWT (including a payload with user information and a signature) and sends it back to the client.
3. **Client Storage**: The client stores the JWT (typically in localStorage or sessionStorage).
4. **Subsequent Requests**: For protected API requests, the client includes the JWT in the `Authorization` header as a Bearer token.

#### Server Verification Process

##### 1. **No Storage Needed**

One of the key benefits of JWTs is that they are **stateless**. The server does not need to store the token; instead, the server verifies the token's authenticity using the signature included in the JWT.

##### 2. **Token Structure**

A JWT consists of three parts:
- **Header**: Contains information about how the token is signed (e.g., algorithm used).
- **Payload**: Contains the claims or user data.
- **Signature**: Created by encoding the header and payload with a secret key or public/private key pair (in the case of asymmetric signing).

The general structure is: 
```
header.payload.signature
```

##### 3. **Verification Steps**

When the server receives a JWT:

1. **Extract Token**: The server extracts the token from the `Authorization` header.
2. **Decode Header and Payload**: Decode the JWT into header, payload, and signature parts.
3. **Verify Signature**:
   - **Algorithm**: Check if the algorithm specified in the header matches the expected algorithm.
   - **Signature**: Recompute the signature using the header and payload with the server's secret key (or public key in case of asymmetric encryption) and compare it to the signature part of the token.
4. **Check Expiry**: Verify the `exp` claim to ensure the token is still valid.
5. **Validate Claims**: Optionally, check other claims in the payload to ensure they are valid (e.g., issuer, audience).

##### 4. **Best Practices**

- **Secret Key Security**: Keep your secret key safe and secure. It should be sufficiently complex and private.
- **Use HTTPS**: Always use HTTPS to encrypt the transmission of the token to prevent interception.
- **Token Expiry**: Include an `exp` (expiry) claim in the JWT to limit the token's lifetime and reduce security risks if a token is compromised.
- **Refresh Tokens**: Implement refresh tokens to allow users to get a new JWT without re-authenticating, improving user experience and security.
- **Handle Revocation**: Since JWTs are stateless, handling token revocation (e.g., logging out) can be tricky. Common approaches include maintaining a blacklist of tokens (less ideal) or implementing short-lived tokens with refresh tokens.
- **Algorithm Selection**: Use strong algorithms for signing (e.g., RS256 or HS256). Avoid deprecated or weak algorithms.
- **Claims Validation**: Validate all relevant claims in the JWT, including the `aud` (audience) and `iss` (issuer) to ensure the token is intended for your application and issued by a trusted source.

#### Example of JWT Verification

Here’s a simplified example of how JWT verification might be implemented in Node.js with the `jsonwebtoken` library:

```javascript
const jwt = require('jsonwebtoken');

// Middleware to verify JWT
function verifyToken(req, res, next) {
    const token = req.headers['authorization']?.split(' ')[1];
    if (!token) return res.status(401).send('Token is missing');

    jwt.verify(token, 'your-secret-key', (err, decoded) => {
        if (err) return res.status(403).send('Invalid token');
        
        // Attach user info to request object
        req.user = decoded;
        next();
    });
}
```

In this example:
- The `verifyToken` middleware extracts the token from the `Authorization` header.
- It then verifies the token using `jsonwebtoken`’s `verify` method with the secret key.
- If valid, it attaches the decoded user information to the request object for further processing.

#### Summary

- **JWT Verification**: The server verifies a JWT using its signature and does not need to store tokens.
- **Stateless**: JWTs are stateless and self-contained.
- **Best Practices**: Secure your secret key, use HTTPS, handle token expiry, and validate claims. Consider implementing refresh tokens and handling revocation appropriately.


You have used Firebase - what it is 
- i think it implements OAuth2 - session based auth ???? 