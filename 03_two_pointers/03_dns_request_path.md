Domain Name System (DSN) and the path a request takes

Flowline of searching a domain (abc.com)
1. browser checks if IP is already cached, if it yes go to step 4
2. if not, it ask DNS resolver whats the ip for abc.com
3. if the resolver does not know still, it searches into servers, (root server) then into the specific 
server until it finds the specific IP address
4. once found the IP, it opens a connection to the Ip and then send the actual request
5. server processes and send the respond back

why browser cannot just skip DNS? because infra needs IP address to route, if you just give a name, routers switches and all those cannot understand.