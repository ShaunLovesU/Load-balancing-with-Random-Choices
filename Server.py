class Server:
    def __init__(self,server_id):
        self._server = server_id
        self.length = 0

    def get_server(self):
        return self._server
    
    def get_length(self):
        return self.length