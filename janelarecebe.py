import tkinter as tk

class InterfaceTKRecebe:

    def __init__(self):
        self.window = tk.Tk()
        self.input = tk.StringVar()
        

        self.frame = tk.Frame(self.window, height=300, width=300)
        self.frame.pack_propagate(False)
        self.frame.pack()


    def read(self, text):
        self.label = tk.Label(self.frame, text=text)
        self.input.set("")
        self.label.pack()


    def run(self):
        self.window.mainloop()

interfacer = InterfaceTKRecebe()
interfacer.run()
