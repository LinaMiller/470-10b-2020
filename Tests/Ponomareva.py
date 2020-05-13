import tkinter as tk
import time

class A(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create()

    def create(self):
        self.quit = tk.Button(self, text="Выход", font="Impact", fg="red", bg="white",  width=7,height=4, command=root.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = A(master=root)
app.mainloop()
