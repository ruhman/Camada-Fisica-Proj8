import socket
import sys

class Transmitter():
    def __init__(self):
        self.mess =""
        self.head = '++++++++++++++++++'
        self.eop = '=============='
        self.porta = 2443
        print("Inicializando socket TCP/IP")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = ('localhost', self.porta)
        self.sock.connect(server_address)
        print("Conexão com GNU Radio realizada ")
    
    def envia(self):
        pacote = bytes(self.head, 'utf-8') + bytes(self.mess, 'utf-8') + bytes(self.eop, 'utf-8')
        self.sock.send(pacote)
        print('Mensagem enviada')