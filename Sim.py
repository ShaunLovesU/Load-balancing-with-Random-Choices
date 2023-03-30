'''
Main simulation file for the simulation of load-balancing in multiple servers.
'''

import numpy as np
import pandas as pd
import queue
import random
import math
from EventList import *
from Event import *
from Server import *


# Global variables for the simulation set below
# simulation variables
Clock  =0

# Num_server = int(input("Enter the number of servers: "))
# MeanInterArrivalTime = float(input("Enter the mean interarrival time: "))
# MeanServiceTime =float(input("Enter the mean service time: "))
# TotalCustomers  = int(input("Enter the total number of customers: "))

Num_server = 5
MeanInterArrivalTime = 4.5
MeanServiceTime =0.8
TotalCustomers  = 1000

LastEventTime =0
TotalBusy =0
MaxQueueLength =0
SumResponseTime =0

NumberOfCustomers=0
QueueLength=0
NumberInService=0

NumberOfDepartures=0
LongService=0

arrival = 1
departure = 2


FutureEventList = EventList()
Customers = queue.Queue()

# store the server list
server_list = []
# create the server list
for i in range(Num_server):
    locals()['server_'+str(i)] = Server(i)
    server_list.append(locals()['server_'+str(i)])
print(server_list)

# simulation variables

def Initialize():
    global Clock, QueueLength, NumberinService, LastEventTime, TotalBusy, MaxQueueLength, SumResponseTime, NumberOfCustomers, NumberOfDepartures, LongService
    global FutureEventList, Customers
    Clock = 0.0
    QueueLength = 0
    NumberinService = 0
    LastEventTime = 0.0
    TotalBusy = 0.0
    MaxQueueLength = 0
    SumResponseTime = 0.0
    NumberOfDepartures = 0
    LongService = 0




    # Create the first arrival event
    time = random.expovariate(1.0 / MeanInterArrivalTime)
    event = Event(arrival, time)
    # print(event.type, event.time)
    FutureEventList.insert(event)


def ProcessArrival(evt):
    global clock, QueueLength, TotalBusy,MaxQueueLength,LastEventTime
    print(1)
    print(evt.get_type(), evt.get_time(), evt.get_server_num())


def ProcessDeparture():
    pass

def loadBalancer():
    global server_list, Num_server

    k = random.randint(1, Num_server-1)
    r_list = random.sample(server_list, k= k)

    min_len =  math.inf
    for i in r_list:
        if i.get_length() < min_len:
            min_len = i.get_length()
            min_server = i

    return min_server

def main():
    global Clock, QueueLength, NumberinService, LastEventTime, TotalBusy, MaxQueueLength, SumResponseTime, NumberOfCustomers, NumberOfDepartures, LongService
    Initialize()
    print(NumberOfDepartures, TotalCustomers)
    while (NumberOfDepartures < TotalCustomers):
        evt = FutureEventList.findMin()
        Clock = evt.time
        # get the server with the least length
        if (evt.type == arrival):
            # dispatch the mission to the server which has the least length
            mission_dispatch = loadBalancer()
            # print(mission_dispatch,mission_dispatch.get_server())
            evt.set_server_num(mission_dispatch.get_server())
            ProcessArrival(evt)
            break
        else:
            ProcessDeparture()















if __name__ == '__main__':
    main()