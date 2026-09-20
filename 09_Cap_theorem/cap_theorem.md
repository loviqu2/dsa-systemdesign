CAP theorem

Consistency - every read gets the most recent write, where all servers agree on one data at all times, with no stale answers
Availability - every request gets some response, even if under failure conditions
Partition Tolerance - system keeps working even if servers cannot communicate with each other

Theorem explaination
- when a network partition happens, you can only pick one of two, availability or consistency 
- partition tolerance is a non negotiable 

Example:
If a primary db and replica momentarily lose connection, and a patient tries to check availability slots, hitting the replica

Two options:
- Consistency, replica does not answer (" Gives out an error message "), wait until it can reconnect and confirm
- Availability, still proceeds to give data, even if it is a stale data

In this case, consistency prevails, if we were to choose availability, stale data might occur and it may cause double booking, where the two users collide with each other on one appointment. In Contrarary to consistency, giving them an error message is better as it can avoid double booking to occur. 

