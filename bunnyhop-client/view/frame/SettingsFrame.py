import tkinter as tk

from res import Font, Color, Style


class SettingsFrame(tk.Frame):
    def __init__(self, master_frame):
        tk.Frame.__init__(self, master_frame, bg=Color.LAVENDER)

        self.title_label = tk.Label(
            self,
            font=Font.HUGE_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.title_label.pack()

        Style.dummy_label(self, size=30).pack()

        self.difficulty_label = tk.Label(
            self,
            font=Font.MEDIUM_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.difficulty_label.pack()

        self.difficulty_slider = tk.Scale(
            self,
            from_=4,
            to=15,
            orient='horizontal',
            font=Font.MEDIUM_FONT,
            length=200,
            troughcolor=Color.ROSE_QUARTZ,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.difficulty_slider.pack()

        Style.dummy_label(self, size=30).pack()

        self.language_label = tk.Label(
            self,
            font=Font.MEDIUM_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.language_label.pack()

        self.language_button_frame = tk.Frame(self, bg=Color.LAVENDER)
        self.language_buttons = {
            "english":      tk.Button(self.language_button_frame, text="En"),
            "hungarian":    tk.Button(self.language_button_frame, text="Hu"),
            "romanian":     tk.Button(self.language_button_frame, text="Ro")
        }
        for button in self.language_buttons.values():
            button.configure(
                width=5,
                height=2,
                font=Font.MEDIUM_FONT,
                bg=Color.PALE_PURPLE,
                fg=Color.MOUNTBATTEN_PINK,
                activebackground=Color.ROSE_QUARTZ,
                activeforeground=Color.PALE_PURPLE)
        self.language_buttons["english"].grid(row=0, column=0)
        Style.dummy_label(self.language_button_frame, text="   ").grid(row=0, column=1)
        self.language_buttons["hungarian"].grid(row=0, column=2)
        Style.dummy_label(self.language_button_frame, text="   ").grid(row=0, column=3)
        self.language_buttons["romanian"].grid(row=0, column=4)
        self.language_button_frame.pack()

        Style.dummy_label(self, size=60).pack()

        self.back_button = tk.Button(
            self,
            width=18,
            height=2,
            font=Font.MEDIUM_FONT,
            bg=Color.PALE_PURPLE,
            fg=Color.MOUNTBATTEN_PINK,
            activebackground=Color.ROSE_QUARTZ,
            activeforeground=Color.PALE_PURPLE)
        self.back_button.pack()
