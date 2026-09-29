## Service Discovery

Problem - autoscaling adds/removes them, deployments replace them. A hardcoded server list goes stale fast. Service discovery fixes this with a registry: a live, central list of "who's actually up right now."

## How server gets added
- Server registers itself when it start up ( with Ip/port)
- Send heartbeats ("Alive") to registry

## How dead server gets removed
- If a server crashes, it can't say goodbye — so the registry can't wait for that.
Instead: if no heartbeat arrives within a TTL (time-to-live) window, the registry assumes it's dead and removes it.
Tradeoff:
Short TTL → detects failures fast, but more heartbeat traffic/overhead.
Long TTL → cheap, but traffic keeps going to a dead server longer.

## Flapping problem
- A brief network blip can make healthy server miss 1 heartbeat
- If it missed based on single missed heartbeat, server keeps getting removed/added back in
- Fix: require several consecutive failed heartbeats before making it dead

## 2 way to use registry
1. Client side discovery
- CLient queries the register itself, 
- Have to lookup/retry its logic
- Netflix Eureka

2. Server-side discovery
- Load balancer does the query
- Client dont needa know shiii

## Registry cant be 1 server
- Single point of failure if so, replicate.

## What a regisration entry needs
- Identity (Port/IP)
- Metadata -  perfomrance metrics lookup, for load balancer to decide which is best.