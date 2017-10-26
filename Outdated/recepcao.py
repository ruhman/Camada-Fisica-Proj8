import socket
import sys

class Receptor():
    def __init__(self):
        self.porta = 1238
        print("Inicializando socket TCP/IP")

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        self.server_address = ('localhost', self.porta)
        print("Porta {}".format(self.porta))
        self.sock.bind(self.server_address)

        # Listen for incoming connections
        self.sock.listen(1)

        while True:
            # Wait for a connection
            print("Esperando conexão")
            self.connection, self.client_address = self.sock.accept()
            print("Conexão de: {}".format(self.client_address))
            string =''

            while True:
                print('Listening...')
                data = str(self.connection.recv(16),'utf-8')
                print(data)

                if data == '+':
                    print('Found Head')

                elif data == '=':
                    print('Found EOP')
                    print(string)

                if data != '+' and data != '=':
                    string += data
                    
Receptor()