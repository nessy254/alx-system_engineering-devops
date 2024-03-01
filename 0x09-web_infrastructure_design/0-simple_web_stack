# Task One: Single Web Infrastructure Design
# https://imgur.com/gallery/2HFXhrx

## Components and Functions

- A server is a device that manages actions and stores information. It handles requests from users and stores data.
- A domain name allows access to the web. It is like a web address that people use to find a website, but it actually points to a server's location on the internet.
- The type of DNS record www in www.foobar.com is a CNAME record, which directly associates the domain with an IP address.
- The role of the web server is to receive requests from users' web browsers and respond with the necessary information to display on a webpage.
- The application server processes information from the web server but also hosts the actual logic of the website or application, handling tasks like user authentication, data processing among others.
- The database stores and manages data for retrieval. It is like a digital filing cabinet where information is stored, and it also handles data sent to and from the client.
- To communicate with the user's computer, the server uses HTTP (HyperText Transfer Protocol), though increasingly, HTTPS (HTTP Secure) is used for secure communication.

## Issues with a one-server infrastructure

1. SPOF (Single Point of Failure): This means if the server stops working, there's no backup to take over. So, if something goes wrong with the server, like it crashes or has a problem, the website might not work properly, or it might even go offline completely.
2. Downtime during Maintenance: This is when the website needs to be updated or fixed, but during that time, it can't be accessed by users. To prevent this, we can use a load balancer, which helps manage requests while updates are happening, so the website can stay online.
3. Scalability Issues: This happens when too many people try to use the website at once, and it can't handle all the requests. So, the website might become really slow or even crash. To fix this, we need to make sure the infrastructure can handle more users by adding more servers or using other techniques.

