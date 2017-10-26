import socket
import sys

class Transmitter():
    def __init__(self):
        self.porta = 1255
        self.head = '++++++++++++++++++'
        self.eop = '=============='
        print("Inicializando socket TCP/IP")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('localhost', self.porta)
        self.sock.connect(server_address)
        print("Conexão com GNU Radio realizada ")

    def send(self, text):
        pacote = bytes(self.head, 'utf-8') + bytes(text, 'utf-8') + bytes(self.eop, 'utf-8')
        self.sock.send(pacote)
        print('Mensagem enviada')

t=Transmitter()
while True:
    print("O que deseja transmitir:")
    text = str(input(""))
    t.send(text)