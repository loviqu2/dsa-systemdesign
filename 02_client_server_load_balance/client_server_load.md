Client vs server, basically means client send a request over the internet towards a server, and server 
does the work (check availability, saves booking into db) and then send back a response towards the client

Load balancing, if there are 7000 requests coming in a short time
Common two appraches are to load balance the request so that there will not be a server that is overloaded are:
1. Round robin approach, if there a server (A, B, C) req 1 will go to A, 2 will go B, 3 will go C, and 4 will go back to A, and this repeats
2. Least connections, this method sends whichever server that has the fewest active request

Load balancing speads traffic across app servers, but if many request with the same data are needed from one db, that db will be a bottleneck, load balancing does not fix hotspot at the data layer, but only at request-routing layer.