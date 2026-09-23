Rate limiting

Problem
1. A client can hit an endpoint far more times than intended, maybe because of malicious intent, by accident or whatever the case may be. It can cause server overload, so rate limiting is introduced to avoid that, when a user takes up too many request within a short amount of time, an error of (429 too many request will be shown)

Fixed window counter
- Basically having to limit the rate of user sending in a request within a fixed time frame
- Example, Only 5 request in a 5 minute window
- This method has a flaw where users can exploit it by sending a request and the end of the 5 minutes, and when it refreshes, sends another 5 request. at t=59, and t=61, so that means 10 request within 2 seconds

Sliding window
- This is where sliding window is introduced, where instead of having a fixed clock boundary, we can continously check " how many request happens within the last N seconds, counting backward from now". 

Trade off 
- Although sliding window cost more to compute but it is worth for business critical endpoints such as bookings. 