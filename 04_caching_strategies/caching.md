Caching - store the result of the extra work, so we dont have to redo every time.

Cache hit - data wanted is already in the cache, so we get a fast answer
Cache miss - data wasnt it in the cache, redo the whole work to store the result in cache for next time 
TTL (Time to live ) - how long a cached value is stored until it is stale and refreshed
Eviction policy - cache have limited space, so new entries need to replace the old ones. Common approach
is LRU (Least Recently Used) so we evict whatever cached that has not been accessed a long time. 

Common problem 
- TTL serves a stored answer in a fixed window amount of time, so if data is changed mid-window, cache will 
hand out the old, which is the wrong data, until the TTL expires, creating conflicts

Fixes
- Shorten the TTL timeframe
- actively clearing cache the moment data changes instead of waiting
- Dont trust cache alone for final write/commit step and let db handle it (cache for reads can afford to be slightly stale, but its important to verify against the real source if something becomes permanent gets commited.)