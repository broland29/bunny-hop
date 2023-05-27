import tkinter as tk

import res.Color as Color
import res.Font as Font


class NotifyPopup(tk.Toplevel):
    def __init__(self, parent, message):
        tk.Toplevel.__init__(self, bg=Color.LAVENDER)

        self.width = 200
        self.height = 100
        self.x = int(self.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(self.winfo_screenheight() / 2 - self.height / 2)
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        tk.Label(self,
                 text=message,
                 font=Font.MEDIUM_FONT,
                 bg=Color.LAVENDER,
                 pady=20,
                 padx=10,
                 wraplength=180,
                 justify="left").pack()
