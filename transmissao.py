import socket
import sys

class Transmitter():
    def __init__(self):
        self.porta = 1255
        print("Inicializando socket TCP/IP")

    def send(self, text):
         # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', self.porta)
        self.sock.connect(server_address)

        try:
            self.sock.sendall(bytes(text, 'utf-8'))

        finally:
            print("Closing connection")
            self.sock.close()

t=Transmitter()
print("O que deseja transmitir:")
text = str(input(""))
t.send(text)