import tkinter as tk
import transmissao

class InterfaceTK:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.resizable(False, False)
        self.Transmitter = transmissao.Transmitter()

        #tamanho linhas
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
        self.button.configure(command = self.Transmitter.send("gvdvgjacvgudasvgusavgydsvagudvsguavguadvugdsavhdsavhudasvuhdsvhdvhavdaskvjkdsvkasvkdvdavkasdvkasvdhsdvjvhdjsavhjds"))


    def run(self):
        self.window.mainloop()


interface = InterfaceTK()

interface.run()