## Circuit Breaker


## Upstream is the provider , Downstream is the consumer

## Problem
Repeatedly calling a broken downstream service ( payment gateway ) will cause the system resources to go into 
a bottleneck.

## The three states

Closed - normal operation, calls pass through, failure/successes are tracked in background

Open -  failure case, immediately block calls, failing fast with no wait for a cooldown period

Half-open - after cooldown, let a small number of test calls to let through to see if it passes or not. If yes      then go into closed, if not then open. It often requires a number of consecuive pass/fails to decide which state it should go


## Why fail fast matters
- Simply because we want to reduce the amount of resources wasted on the failure cases. 


