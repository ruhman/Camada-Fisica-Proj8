import tkinter as tk

class InterfaceTKRecebe:

    def __init__(self):
        self.window = tk.Tk()

        self.input_user = tk.StringVar()

        self.frame = tk.Frame(self.window, width=300, height=300)
        self.frame.pack_propagate(False)
        self.frame.pack()


    def putText(self, texto):
        self.label = tk.Label(self.frame, text=texto)
        self.input_user.set("")
        self.label.pack()

    def run(self):
        self.window.mainloop()

aaa = InterfaceTKRecebe()
aaa.run()
