import socket
import sys

class Transmitter():
    def __init__(self):
        self.porta = 1255
        print("Inicializando socket TCP/IP")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', self.porta)
        self.sock.connect(server_address)

    def send(self, text):
        # Create a TCP/IP socket
        self.sock.sendall(bytes(text, 'utf-8'))
        # self.sock.close()

t=Transmitter()
while True:
    print("O que deseja transmitir:")
    text = str(input(""))
    t.send(text)