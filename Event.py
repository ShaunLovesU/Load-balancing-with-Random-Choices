class Event:
    def __init__(self, type, time):
        self.type = type
        self.time = time
        self.server_num = None

        self.left = None
        self.right = None

    def set_server_num(self, server_num):
        self.server_num = server_num

    def get_server_num(self):
        return self.server_num

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