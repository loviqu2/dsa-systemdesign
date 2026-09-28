## Retries with Exponential Backoff

## Problem
During a failed downstream service, retry calls cannot instantly happen, especially if there are a huge volume of users trying in the same timeline. This creates a problem called 'Thundering Herd'

## Exponential Backoff
Wait progressively longer each retry, wait_time = base_delay * 2^n. 2s, 4s, 8s, 16s
This provides the service area of breath. ( Breathing room to recover resources)

## Jitter
Although using exponential backoff is good, it can still cause thundering herd problem
If many clients follow the same schedule of retries, we go back into the same problem
# Fix
Add randomness towards the schedule of retries, so that retries are spread out instead of being in a cluster

## Correlation with circuit breaker
Circuit breaker ----> Exponential backoff

The circuit breaker is a gatekeeper checked before every call attempt, incl the first ( Open, Closed, Half Open)
Backoff only comes into play where circuit breaker are in Closed/Half-Open states. Every attempt pass/fail feeds into circuit breaker's failure count, where it decides whether the state needs to change or not