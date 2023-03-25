'''
Define the EventList class, which is used to store the event list by using splay tree.
Give reference to "https://github.com/anoopj/pysplay/blob/master/splay.py"
'''
from Event import *

class EventList: 
    # splay tree implementation from "https://github.com/anoopj/pysplay/blob/master/splay.py"
    def __init__(self):
        self.root = None
        self.header = Event(None,0) #For splay()
        self.size = 0
        self.left = Event(None,0)
        self.right = Event(None,0)
    def insert(self, n:Event):
        if (self.root == None):
            self.root = n
            return
        self.size +=1
        self.splay(n)
        if n.time <= self.root.time:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n
    def isEmpty(self):
        return self.root == None
    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x)
        return x
    def splay(self, n:Event):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if n.time <= t.time:
                if t.left == None:
                    break
                if n.time < t.left.time:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif n.time > t.time:
                if t.right == None:
                    break
                if n.time > t.right.time:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t