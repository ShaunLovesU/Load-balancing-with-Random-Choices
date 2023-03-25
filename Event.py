
'''
Define the Event class, which is used to store the event information.

'''

class Event:
    def __init__(self, type, time):
        self.type = type
        self.time = time

        self.left = None
        self.right = None


    def get_type(self):
        return self.type
    def get_time(self):
        return self.time
    
    def compare(self, other):
        if self.time < other.time:
            return -1
        elif self.time == other.time:
            return 0
        else:
            return 1
        