Content Delivery Network


Problem:
1. A website images are live on one origin server. Visitors from all over the country, has to fetch those files from the same distance every time, if their further from origin they get slower.


CDN keeps cached copies of files distributed all over the world. It solves the distance issue where they keep "static files" ( those that hardly change like images ) served from a nearby edge server. 

Cache Miss - edge server does not have the file yet, does an origin pull to cache its first copy
Cache Hit - edge server already has it cached, serve immediately

Staleness 
- What if the origin server has uploaded a more clearer picture, but the CDN is sitll caching the old one? 
- Wait until TTL expires, so that clearer photo gets cached
- Manually refetch the newer picture 

What belongs to a CDN:
1. static files, where data do not often change. Low risk of serving something wrong

DO NOT BELONG to CDN:
1. fast changing data, where it updates every 1-2 minutes or even faster, these data can go stale really quick. 