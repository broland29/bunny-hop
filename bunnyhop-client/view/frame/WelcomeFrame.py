import tkinter as tk

import res.Color as Color
import res.Font as Font


class WelcomeFrame(tk.Frame):
    def __init__(self, master_frame):
        tk.Frame.__init__(self, master_frame, bg=Color.LAVENDER)

        self.title_label = tk.Label(
            self,
            font=Font.HUGE_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)

        self.username_label = tk.Label(
            self,
            font=Font.MEDIUM_FONT,
            pady=15,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)

        self.title_label.pack()
        self.username_label.pack()

        tk.Label(self, text=" ", font=("Consolas", 20), bg=Color.LAVENDER).pack()   # dummy label for spacing

        self.buttons = {
            "login":        tk.Button(self),
            "play":         tk.Button(self),
            "settings":     tk.Button(self),
            "profile":      tk.Button(self)
        }
        for button in self.buttons.values():
            button.configure(
                width=20,
                height=2,
                font=Font.BIG_FONT,
                bg=Color.PALE_PURPLE,
                fg=Color.MOUNTBATTEN_PINK,
                activebackground=Color.ROSE_QUARTZ,
                activeforeground=Color.PALE_PURPLE
            )
            button.pack()
            tk.Label(self, text=" ", font=("Consolas", 2), bg=Color.LAVENDER).pack()

        self.admin_label = tk.Label(
            self,
            font=Font.MEDIUM_FONT,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK,
            activebackground=Color.ROSE_QUARTZ)

        self.github_label = tk.Label(
            self,
            font=Font.SMALL_FONT,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)

        tk.Label(self, text=" ", font=("Consolas", 70), bg=Color.LAVENDER).pack()
        self.admin_label.pack()
        tk.Label(self, text=" ", font=("Consolas", 10), bg=Color.LAVENDER).pack()
        self.github_label.pack()
