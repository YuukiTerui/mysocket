import socket
import pickle
from threading import Thread

import const
const.MSGLEN = 2**10

class Client:
    def __init__(self, host=None, port=None) -> None:
        self.host = host
        self.port = port
        self.sock = None
        self.send_log = []
        self.receive_log = []

    def connect_port(self, port=None):
        if port is None:
            port = self.port
        if self.sock:
            self.sock.close()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, port))

    def send(self, msg):
        if not self.sock:
            return -1
        msg = pickle.dumps(msg)
        self.sock.send(msg)
        self.sock.send(const.MSGEND)
        

        #msg = self.sock.recv(const.MSGLEN)
        #msg = pickle.loads(msg)
        