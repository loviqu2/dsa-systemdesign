SQL VS NO SQL

SQL (Relational Database)
- Structured data that lives in tables, consistency within every row of data
- Relationship between tables are explicit (FK), joining them is a core feature
- Atomicity, Consistency, Isolation, Durability (ACID) - to ensure data integrity, no half-completed transaction
- Schema is fixed - adding new kind of field changes the table structure
- PostgresSQL, MySQl, Oracle DB

NO SQL (Non relational database)
- Flexible structure, eg, document db (MongoDB) let record be a flexible JSON, record does not need identical field
- Built for flexibility and scalability, huge volume of data
- MongoDB, Redis, Cassandra, DynamoDB


Most companies uses multiple types of DB, SQL for structured data, NOSQL for unstructured, high volume data


Redis
- Super-fast dictionary that lives inside RAM instead of disk
- Known for caching, quick retrival of data
- Session storage
- Rate limiting