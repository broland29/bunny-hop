import tkinter as tk

import res.Color as Color
import res.Font as Font


class GameFrame(tk.Frame):
    def __init__(self, master_frame):

        tk.Frame.__init__(self, master_frame, bg=Color.LAVENDER)

        self.header_frame = tk.Frame(self, bg="cyan")
        self.title_label = tk.Label(
            self.header_frame,
            font=Font.BIG_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.time_label = tk.Label(
            self.header_frame,
            font=Font.BIG_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK,
            width=10)
        self.title_label.grid(row=0, column=0)
        self.time_label.grid(row=0, column=1)
        self.header_frame.pack()

        self.button_frame = tk.Frame(self, bg=Color.LAVENDER, pady=50)
        self.button_array = None
        self.button_frame.pack()

        self.options_frame = tk.Frame(self, bg="yellow")
        self.buttons = {
            "pause":    tk.Button(self.options_frame),
            "quit":     tk.Button(self.options_frame),
            "help":     tk.Button(self.options_frame),
        }
        for i, button in enumerate(self.buttons.values()):
            button.configure(
                width=10,
                height=2,
                font=Font.MEDIUM_FONT,
                bg=Color.PALE_PURPLE,
                fg=Color.MOUNTBATTEN_PINK,
                activebackground=Color.ROSE_QUARTZ,
                activeforeground=Color.PALE_PURPLE,
            )
            button.grid(row=0, column=i)
        self.options_frame.pack()
