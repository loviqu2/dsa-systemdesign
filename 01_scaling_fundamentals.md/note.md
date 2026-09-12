Vertical scaling - upgrading your existing system into something more capable. ( More ram, more compute power)
Horizontal scaling - adding more machines to work together with multiple machines. 

1. Vert scaling is simple and easy, but one point of failure / scaling predicition is off and you're fucked
2. Horizontal is hard to setup, but fault tolerance is high, easy to adapt with fast scaling businessnes


Latency - How long a request take from start to finish (speed)
Throughput - How much work can the sys handle per time (volume)

1. Depending on the scenario, one is better than another

If there is surge on a specific item, Throughput is better --- clients can wait, but clients do not wanna know our 
system is not working

If there is  important scenario that require fast response, then latency can be prio (stock trading system, voice calls) it matters more if there is live interaction
