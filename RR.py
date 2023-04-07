# RandMin.py
'''
A queuing system wherein a job chooses the m server(less than total number) to dispacth mission.
'''

import simpy
import random
import math
import matplotlib.pyplot as plt
import pandas as pd

choice = 0
# Parameters
RSEED = 204204
SERVERS_N = 5  # Number of servers in the system
mean_arrtime = 7  # Exponential distribution mean
mean_sertime = 90  # Exponential distribution mean
customers_n = 300  # Total number of customers

class  QSYSTEM:
    def __init__(self, rand_seed, servers_n, mean_arrtime, mean_sertime, customers_n):
        self.rand_seed = rand_seed
        self.servers_n = servers_n
        self.mean_arrtime = mean_arrtime
        self.mean_sertime = mean_sertime
        self.customers_n = customers_n
        self.queues = []
    def source(self, environment, servers):
        """Source generates customers randomly"""
        for i in range(self.customers_n):
            c = self.customer(environment, 'Customer#%02d' % i, servers)
            environment.process(c)
            each_arrival = random.expovariate(1.0 / self.mean_arrtime)
            yield environment.timeout(each_arrival) 
            
    def customer(self, environment, name, servers):
        """The customer arrives, dispatch customer to a shortest queue."""
        global choice
        arrive = environment.now
        print('%7.4f %s: Arrived' % (arrive, name))
        
        # The load balancer uses the round-robin method to dispatch incoming customers, i.e., the order of servers for dispatching customers is $1, 2, …, m, 1, 2, …, m, 1, 2, …$
        
        if choice == len(servers):
            choice = 0
        print('dispich to :',choice)
        with servers[choice].request() as req:
            choice+=1
            yield req
            wait = environment.now - arrive
            print('%7.4f %s: Waited %6.3f, start service' % (environment.now, name, wait))

            service_time = random.expovariate(1.0 / self.mean_sertime)
            yield environment.timeout(service_time)
            print('%7.4f %s: departure' % (environment.now, name))
            tmp = {}
            for i in range(len(servers)):
                tmp[i] = len(servers[i].put_queue)
            self.queues.append(tmp)
        

    def draw(self):
        df = pd.DataFrame(self.queues).plot()
        plt.title('Queue length')
        plt.xlabel('Time')
        plt.show()
    def creat_environment(self):
        print('m/m/m queueing system with load balancer (RandMin)')
        random.seed(self.rand_seed)
        environment = simpy.Environment()    
        servers = []
        for i in range(self.servers_n):
            servers.append(simpy.Resource(environment, capacity=1))
        environment.process(self.source(environment, servers))

        print('Running simulation...')
        environment.run(until = 100000)

        print('finish simulation')
        return environment

def main():
    
    qs = QSYSTEM(RSEED, SERVERS_N, mean_arrtime, mean_sertime, customers_n)
    qs.creat_environment()
    qs.draw()

    exit(0)

if __name__ == '__main__':
    main()