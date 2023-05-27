import tkinter as tk


class AppWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Bunny Hop")

        self.width = 600
        self.height = 800
        self.x = int(self.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(self.winfo_screenheight() / 2 - self.height / 2)

        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.resizable(False, False)
