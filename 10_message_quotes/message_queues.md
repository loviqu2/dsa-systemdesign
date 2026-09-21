Message queues and async processing

synchronously - something that must be completed, must be confirmed before further action (you cannot start step 2 without 1)
asynchronously - a brief delay does not udnermine the actual result

Piece involved in this
Producer - responsible for creating the task and puts it inside the queue
Queue - hold the tasks in the queue, until something is ready to process them, same concept as FIFO
Consumer/Worker - a process that pulls messages from the queue and does the work like sending SMS

Why it is better?

Resilience - if SMS is temporarily down, the booking can still continue, where it processes from the message in the queue

Decoupling - booking service does not need to care about the SMS sending mechanism, just know how to drop a message on the queue and move on

Load absorption - if there is a traffic spike, queue can pile up messages safely, and processed steadily by workers, rather than the system trying to do everything in one go



