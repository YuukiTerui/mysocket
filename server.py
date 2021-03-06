import sys
import time
import socket
import pickle
from threading import Thread

import const


class Server(object):
    def __init__(self, host=None, port=None) -> None:
        self.host = host if host else socket.gethostbyname(socket.gethostname())
        self.port = port
        self.sock = None
        self.connection = 0
        self.clients = []
        self.is_running = False

    def connect_port(self, port=None):
        if port is None:
            port = self.port
        if self.sock:
            self.sock.close()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, port))
        self.sock.listen()

    def receive(self, client):
        data = b''
        while True:
            tmp = client.recv(const.MSGLEN)
            if tmp == const.MSGEND:
                break
            data += tmp
        data = pickle.loads(data)
        return data

    def client_process(self, client, address):
        self.clients.append((client, address))

        while True:
            data = self.receive(client)
            print(data)

    def start(self):
        self.is_running = True
        th = Thread(target=self.run, daemon=True)
        th.start()

    def run(self):
        while self.is_running:
            time.sleep(1)
            if not self.sock:
                continue
            client, address = self.sock.accept()
            th = Thread(target=self.client_process, args=(client, address), daemon=True)
            th.start()

    def stop(self):
        self.is_running = False


def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    server = Server(host, port)
    server.connect_port()
    server.start()
    try:
        while True:
            tmp = input()
            eval(f'server.{tmp}')
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()