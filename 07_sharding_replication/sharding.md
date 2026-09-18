Replication creates fault tolerance for servers, but when the actual data itself is too big for the server to hold
- Replication can take long amount fo time

Sharding comes in
- splitting data in to smaller pieces (shards), where each shards lives on a different server, it is not the copy of the same data, but different pieces of it

Example
- Clinic chain grows rapidly ( international )
- Db server cannot hold amount of data anymore
- Data gets sharded by location ( MY to Server A ), (SG to Server B), etc...

Sharding key
- How to decide how shards are seperated, range of id (1-10000) on server A, so on so forth

Cost
- Queries can be hard, where spanning multiple shards get hard
- IF i wanted data of patients across every country who booked a facial
- Queries need to be done seperately, and combining them into one
- Bad sharding key can cause hotspot problems, where one of the shards has more traffic than others