# Task Three: Secure and Monitored Web Infrastructure
### Link to image:
https://imgur.com/vR6a6Gy

## Key Components for Enhancement

1. **Three Servers for Redundancy**: Ensures redundancy and fault tolerance. If one server encounters problems, the other two can continue serving the website.
2. **Firewalls for Enhanced Security**: Each server equipped with a firewall to filter and control network traffic, preventing unauthorized access and protecting against potential threats.
3. **SSL Certificate for HTTPS**: Enables HTTPS encryption to safeguard sensitive information from interception. Ensures data exchanged between users' browsers and the website is encrypted.
4. **Monitoring for Infrastructure Health**: Deploying monitoring tools allows us to monitor server performance, track traffic patterns, and detect security incidents, enabling proactive management and timely resolution of issues.

## Additional Details

- **Firewalls**: Control incoming and outgoing traffic, protecting against hackers and malware.
- **HTTPS**: Encrypts traffic, making it harder for hackers to spy on or tamper with data.
- **Monitoring**: Checks for issues like slow performance, unusual activity, or security threats by constantly collecting data on CPU usage, memory usage, network traffic, and error logs.
- **Queries Per Second (QPS) Monitoring**: Tracks the number of requests a server is handling per second, allowing optimization of performance.

## Issues with This Infrastructure

1. **SSL Termination**: Careful configuration needed to maintain data security. Terminating SSL at the load balancer level requires proper configuration to maintain end-to-end encryption.
2. **Resource Allocation**: Tailoring resource allocation based on specific needs of each server component optimizes performance and prevents resource bottlenecks.
3. **MySQL Server Redundancy**: Implementing a primary-replica cluster for MySQL ensures data availability and redundancy, minimizing the risk of data loss in case of server failure.

