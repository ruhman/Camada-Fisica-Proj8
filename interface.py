import tkinter as tk
from recepcao import Receptor
from transmissao import Transmitter
import time
import threading as thd

class InterfaceTk():

    def __init__(self):
        self.receptor = Receptor()
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.resizable(False, False)


        thd.Thread(target=self.receive).start()
        self.transmissor = Transmitter()

        self.window.rowconfigure(0, minsize = 40)
        self.window.rowconfigure(1, minsize = 2.5)
        self.window.rowconfigure(2, minsize = 15)

        #tamanho colunas
        self.window.columnconfigure(0, minsize = 10)

        #mensagens já enviadas
        self.readmsg = tk.Text(self.window, height=18, width=42)
        self.readmsg.grid(row=0,column = 0, sticky = "sewn")

        #campo de envio de mensagem
        self.sendmsg = tk.Text(self.window, height=1, width = 1)
        self.sendmsg.grid(row = 1,column = 0,sticky = "sewn")
        self.sendmsg.insert(tk.END, "")

        #botão de enviar
        self.button = tk.Button(self.window, height = 1, width = 3, text = "Enviar")
        self.button.grid(row = 2, column = 0, sticky="sewn")
        self.button.configure(command = self.send)


    def send(self):
        inpt = self.sendmsg.get("1.0",tk.END)
        self.readmsg.insert(tk.END, "You: "+inpt)
        self.transmissor.mess = " " + inpt
        thd.Thread(target=self.transmissor.envia).start()

    def receive(self):
        
        thd.Thread(target=self.receptor.serverSocks).start()

        while True:
            if len(self.receptor.recebido) > 0:
                self.readmsg.insert(tk.END,"recebido: " + self.receptor.recebido + "  " "\n")
                self.receptor.recebido = ""

            time.sleep(0.5)

    def run(self):
        self.window.mainloop()


inter = InterfaceTk()
inter.run()