# ACID Transactions

## The problem
Multiple related database writes (e.g. subtract from savings +
add to checking; deduct deposit + create booking) need to succeed
or fail together, survive crashes, and not corrupt each other when
happening at the same time as other transactions.

## Atomicity
All operations in a transaction succeed together, or none do
(rollback). BEGIN → writes → COMMIT (success, permanent) or
ROLLBACK (undo everything since BEGIN).
Exception: once COMMIT has actually happened, the transaction is
already successful — a lost network response afterward does NOT
mean rollback. Naively retrying on "no confirmation received" risks
double-processing (e.g. double bank transfer); real systems check
actual transaction state instead of blindly retrying.

## Consistency
Every transaction must move the database from one valid state to
another valid state, obeying all defined business rules/constraints
(e.g. "one booking per slot").

## Isolation
Transactions that conflict with each other (e.g. two customers
booking the same slot simultaneously) must not interfere in a way
that produces an invalid result — enforced via locking, so one
transaction finishes or cancels before a conflicting one proceeds.
Unrelated transactions can still run concurrently.

## Durability
Once committed, data must survive any subsequent failure (crash,
power loss). Achieved via writing to disk + replication (ties to
Day 6) before confirming commit.