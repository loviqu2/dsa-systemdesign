Replication is something that allows fault tolerance whenever the primary system crashes.
It keeps multiple copies of the same database in sync, across multiple servers.


- The server act as the primary, where it writes changes into it
- The replica server only copies whatever changes happen on the primary, getting ready to be used whenever main server crashes.

Replication lag
- copying from primary to replica takes a small amount of time, even if it just is milisec. This might show that data can be old, which is called Eventual Consistency.
- replica will eventually catch up to the primary system changes. 