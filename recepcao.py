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

            try:
                print(" Conectado {}".format(client_address))
                while True:
                    data = connection.recv(16)
                    data = data.decode("utf-8")

                    print("{}".format(data))
                    if(len(data) <= 0):
                        break

            finally:
                
                connection.close()
