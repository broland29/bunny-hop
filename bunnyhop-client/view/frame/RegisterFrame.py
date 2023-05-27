import tkinter as tk

import res.Color as Color
import res.Font as Font


class RegisterFrame(tk.Frame):
    def __init__(self, master_frame):
        tk.Frame.__init__(self, master_frame, bg=Color.LAVENDER)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # elements
        self.title_label = tk.Label(
            self,
            font=Font.HUGE_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)

        self.username_label = tk.Label(
            self,
            font=Font.BIG_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.username_entry = tk.Entry(
            self,
            font=Font.BIG_FONT,
            width=10,
            fg=Color.MOUNTBATTEN_PINK)

        self.password_label1 = tk.Label(
            self,
            font=Font.BIG_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.password_entry1 = tk.Entry(
            self,
            font=Font.BIG_FONT,
            width=10,
            fg=Color.MOUNTBATTEN_PINK,
            show="*")

        self.password_label2 = tk.Label(
            self,
            font=Font.BIG_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.password_entry2 = tk.Entry(
            self,
            font=Font.BIG_FONT,
            width=10,
            fg=Color.MOUNTBATTEN_PINK,
            show="*")

        self.message_label = tk.Label(
            self,
            text="",
            font=Font.MEDIUM_FONT,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK,
            pady=20)

        self.login_label = tk.Label(
            self,
            font=Font.MEDIUM_FONT,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK,
            pady=20)

        self.register_button = tk.Button(
            self,
            width=20,
            height=2,
            font=Font.MEDIUM_FONT,
            bg=Color.PALE_PURPLE,
            fg=Color.MOUNTBATTEN_PINK,
            activebackground=Color.ROSE_QUARTZ,
            activeforeground=Color.PALE_PURPLE)

        self.back_button = tk.Button(
            self,
            width=20,
            height=2,
            font=Font.MEDIUM_FONT,
            bg=Color.PALE_PURPLE,
            fg=Color.MOUNTBATTEN_PINK,
            activebackground=Color.ROSE_QUARTZ,
            activeforeground=Color.PALE_PURPLE)

        # placement of elements
        tk.Label(self, text="", bg=Color.LAVENDER, font=("Consolas", 40)).grid(row=0)
        self.title_label.grid(row=1, column=0, columnspan=2)

        self.username_label.grid(row=2, column=0)
        self.username_entry.grid(row=2, column=1)
        self.password_label1.grid(row=3, column=0)
        self.password_entry1.grid(row=3, column=1)
        self.password_label2.grid(row=4, column=0)
        self.password_entry2.grid(row=4, column=1)

        self.message_label.grid(row=5, column=0, columnspan=2)
        tk.Label(self, text="", bg=Color.LAVENDER, font=("Consolas", 10)).grid(row=6)

        self.register_button.grid(row=7, column=0, columnspan=2)
        tk.Label(self, text="", bg=Color.LAVENDER, font=("Consolas", 5)).grid(row=8)
        self.back_button.grid(row=9, column=0, columnspan=2)
        tk.Label(self, text="", bg=Color.LAVENDER, font=("Consolas", 5)).grid(row=10)
        self.login_label.grid(row=11, column=0, columnspan=2)
