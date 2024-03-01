# Task Two: Distributed Setup with Redundancy
# https://imgur.com/a/YMglqyQ


## Infrastructure Design

- **Two Servers for Redundancy**: Each server hosts web server (like Nginx), application server, MySQL database, and website's codebase. If one server has issues, the other can step in to keep the site running.
- **Load Balancer (HAproxy)**: Helps evenly distribute incoming traffic between the two servers. If one server becomes overloaded or fails, the load balancer routes traffic to the other server to maintain availability. Utilizes Round Robin distribution algorithm.
- **Active-Active Setup**: All servers work simultaneously, sharing the workload. If one server stops, the others keep going. For an active-passive setup, some servers sit idle until they're needed. If the main server stops, one of the backups takes over.
- **Server Types**:
  - **Master**: Handles both writing and reading data. Changes made get copied to the other servers.
  - **Replica**: Only reads data. Copies what the primary server does and can take over if it breaks.

## Roles in the Application

- **Primary Node**: Responsible for both reading and writing data. Ensures everything stays up-to-date and correct.
- **Replica Node**: Focuses on reading data and copies actions of the primary node. Can step in and help out if the primary node is busy, but doesn't have the authority to make changes on its own.

## Issues with This Infrastructure

1. **Single Point of Failure (SPOF)**: The load balancer could become a single point of failure. Implementing a redundant load balancer setup can mitigate this risk by providing failover capabilities.
2. **Security Concerns**: Addressed by implementing firewalls to control incoming and outgoing traffic and enabling HTTPS to encrypt data in transit, ensuring user privacy and data integrity.
3. **Monitoring**: Deploying monitoring tools helps detect and address issues proactively by monitoring server performance, traffic patterns, and security incidents, ensuring the infrastructure remains healthy and available.

