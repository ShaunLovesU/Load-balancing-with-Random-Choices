# Load-balancing-with-Random-Choices

Background: Load balancing is used in many systems, e.g., cloud computing, web server farms, Domain Name Servers (DNS). As an abstract model, we assume a set of $m$ servers work in parallel to serve customers. Each server could be modelled as a FIFO queueing system. When a new customer arrives, the customer must first go through a load balancer. The load balancer can use different strategies to dispatch the customer to a server. To simplify, we in this project consider a randomized strategy as follows:

(Step 1) The load balancer randomly selects $d$ servers ($d < m$)

(Step 2) The load balancer checks the queue length of the selected $d$ servers

(Step 3) The load balancer dispatches the incoming customer to the server that has the shortest queue length.

 

We denote the above scheduling method RandMin. The goal of this project is to compare its performance with two baseline methods and draw your conclusion based on your simulation results.

(Baseline 1) Purely random (PureRand): The load balancer randomly selects one server from the $m$ servers and dispatches the incoming customer to the selected server.

(Baseline 2) Round-robin (RR): The load balancer uses the round-robin method to dispatch incoming customers, i.e., the order of servers for dispatching customers is $1, 2, …, m, 1, 2, …, m, 1, 2, …$

 

Assumptions:

We assume that all servers’ service time follows exponential distribution of rate parameter $\mu$
We assume that the customer arrivals follow the Poisson arrival process with mean arrival rate $\lambda$
We ignore the processing time of the load balancer.
 

The following performance metrics should be evaluated: 

Maximum workload: defined as the longest queue length among the $m$ servers
Average workload: defined as the average queue length among the $m$ servers
Average system time: defined as the average time that all customers stay in the system.