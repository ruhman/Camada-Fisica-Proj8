import socket
import sys

class Receptor():
    
    def __init__(self):
        self.recebido = ""

    def serverSocks(self):

        print("Inicializando socket TCP/IP")

        LeDoor = 1337

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ("localhost", LeDoor)
        print("LeDoor {}".format(LeDoor))
        sock.bind(server_address)

        sock.listen(1)
        
        while True:
            print("Esperando conexão")
            connection, client_address = sock.accept()

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
            

