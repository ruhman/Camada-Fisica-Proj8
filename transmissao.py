import socket
import sys

class Transmitter():
    def __init__(self):
        self.mess =""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 2443)
        self.sock.connect(server_address)
    
    def envia(self):

        try:
    
            msg_bytes = self.mess.encode('utf-8')

            self.sock.sendall(msg_bytes)

            amount_received = 0
            amount_expected = len(self.mess)
            
            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)

        finally:
            self.sock.close()