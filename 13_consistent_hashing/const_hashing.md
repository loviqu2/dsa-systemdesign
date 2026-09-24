Consistent Hashing

Problem:
1. Distributing keys across servers with (hash(key) % number_of_servers) works okay until you need to add or remove a server, the divisor changes, that means every key that maps onto a server changes, which causes a cache stampede

eg, 17 % 5 and 17 % 4 is not the same answer, it leads towards a different server. 

Solution 
- Hash both servers and keys into a circular ring 9 ( from 0 to a max value, then wrap back to 0). Like a clock, a key belong to the first server found clockwise from the key's position

How it fixes it
- Instead of having to reassign the key towards the correct server when trying to add another server, by using a hash ring, the other servers are completely unaffected. 

The risk
- If the server is placed unevenly within the ring, one server can end up being bottlenecks. Use a virtual node, where you hash each real server into many scattered ring positions instead of a new one, spreading tis territory more evenly. 