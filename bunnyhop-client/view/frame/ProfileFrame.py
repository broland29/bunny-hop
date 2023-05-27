import tkinter as tk

from res import Color, Font, Style


class ProfileFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=Color.LAVENDER)

        self.title_label = tk.Label(
            self,
            font=Font.HUGE_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.title_label.pack()

        self.header_list_box = tk.Listbox(self, width=47, height=1, font=Font.MEDIUM_FONT)
        self.header_list_box.pack()
        self.game_list_box = tk.Listbox(self, width=47, font=Font.MEDIUM_FONT)
        self.game_list_box.pack()

        self.button_frame = tk.Frame(self, bg=Color.LAVENDER)
        self.buttons = {
            "stat":    tk.Button(self),
            "back":     tk.Button(self),
        }

        for i, button in enumerate(self.buttons.values()):
            button.configure(
                width=27,
                height=2,
                font=Font.MEDIUM_FONT,
                bg=Color.PALE_PURPLE,
                fg=Color.MOUNTBATTEN_PINK,
                activebackground=Color.ROSE_QUARTZ,
                activeforeground=Color.PALE_PURPLE)

        Style.dummy_label(self, size=10).pack()
        self.buttons["stat"].pack()
        Style.dummy_label(self, size=10).pack()
        self.buttons["back"].pack()
