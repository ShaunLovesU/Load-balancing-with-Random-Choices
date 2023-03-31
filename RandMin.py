# RandMin.py
'''
A queuing system wherein a job chooses the m server(less than total number) to dispacth mission.
'''

import simpy
import random
import math
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
RANDOM_SEED = 204204
NUM_SERVERS = 5  # Number of servers in the system
Mean_interarrival = 2  # Exponential distribution mean
Mean_service = 20  # Exponential distribution mean
total_customers = 300  # Total number of customers


Queues = []

def load_balancer(n,servers):
    global Queues
    return random.sample(range(len(servers)), n)

def NoInSystem(R):
    """Total number of jobs in the resource R"""
    global Queues
    return len(R.put_queue) + len(R.users)

def customer(env, name, servers):
    """The customer arrives, dispatch customer to a shortest queue."""

    global Queues
    arrive = env.now
    print('%7.4f %s: Arrived' % (arrive, name))

    # get the random num of servers
    num_selected_server = random.randint(1, NUM_SERVERS-1)
    # get selected server's queue length
    each_length = {i: NoInSystem(servers[i]) for i in load_balancer(num_selected_server, servers)}

    # need to change
    Queues.append({i: len(servers[i].put_queue) for i in range(len(servers))})
    

    choice = [k for k, v in sorted(each_length.items(), key=lambda a: a[1])][0]

    with servers[choice].request() as req:
        yield req

        wait = env.now - arrive
        print('%7.4f %s: Waited %6.3f, start service' % (env.now, name, wait))

        service_time = random.expovariate(1.0 / Mean_service)
        yield env.timeout(service_time)
        print('%7.4f %s: departure' % (env.now, name))

        # for i in range(len(servers)):
        #     Queues.append({i: len(servers[i].put_queue)})
        Queues.append({i: len(servers[i].put_queue) for i in range(len(servers))})




def source(env, number, interval, servers):
    """Source generates customers randomly"""
    global Queues
    for i in range(number):
        c = customer(env, 'Customer#%02d' % i, servers)

        env.process(c)
        each_arrival = random.expovariate(1.0 / interval)
        yield env.timeout(each_arrival)


def main():
    global Queues
    print('m/m/m queueing system with load balancer (RandMin)')
    random.seed(RANDOM_SEED)
    env = simpy.Environment()

   
    servers = [simpy.Resource(env, capacity=1) for i in range(NUM_SERVERS)]
    env.process(source(env, total_customers, Mean_interarrival, servers))

    print('Running simulation...')
    env.run(until = 100000)

    print('finish simulation')

    # print(Queues)

    df = pd.DataFrame(Queues).plot()
    plt.title('Queue length over time')
    plt.xlabel('Time')
    plt.ylabel('Queue length')
    plt.show()

    exit(0)

if __name__ == '__main__':
    main()