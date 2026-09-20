Indexing
- Index is a seperate structure db that lets it jump into matching rows instead of searching it one by one
- If there was no indexing, it would be a O(n), where you need to do a full table scan
- Indexing typically uses a B-tree, where it can reduce the amount of times needed to be searched, becoming O(log n)

Indexes are not free
- Whenever indexes are done into a database column that has never been searched before, every INSERT/UPDATE requires index updating, causing slower writes, regardless if it is used for indexing
- Index requires extra storage
- Read speedup are only acquired if the query has been done before
- Querying never before indexed columns require to pay the write off storage cost while getting no benefit back