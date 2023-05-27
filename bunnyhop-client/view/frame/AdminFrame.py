import tkinter as tk
import res.Color as Color
import res.Font as Font
from res import Style


class AdminFrame(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=Color.LAVENDER)

        self.title_label = tk.Label(
            self,
            font=Font.HUGE_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.title_label.pack()

        self.header_list_box = tk.Listbox(self, width=35, height=1, font=Font.MEDIUM_FONT)
        self.header_list_box.pack()
        self.user_list_box = tk.Listbox(self, width=35, font=Font.MEDIUM_FONT)
        self.user_list_box.pack()

        self.message_label = tk.Label(
            self,
            font=Font.MEDIUM_FONT,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK,
            pady=20)
        self.message_label.pack()

        self.bottom_frame = tk.Frame(self, bg=Color.LAVENDER)

        self.label_entry_frame = tk.Frame(self.bottom_frame, bg=Color.LAVENDER)
        self.username_label = tk.Label(
            self.label_entry_frame,
            font=Font.MEDIUM_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.username_entry = tk.Entry(
            self.label_entry_frame,
            font=Font.MEDIUM_FONT,
            width=10,
            fg=Color.MOUNTBATTEN_PINK)

        self.password_label1 = tk.Label(
            self.label_entry_frame,
            font=Font.MEDIUM_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.password_entry1 = tk.Entry(
            self.label_entry_frame,
            font=Font.MEDIUM_FONT,
            width=10,
            fg=Color.MOUNTBATTEN_PINK,
            show="*")

        self.password_label2 = tk.Label(
            self.label_entry_frame,
            font=Font.MEDIUM_FONT,
            pady=20,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK)
        self.password_entry2 = tk.Entry(
            self.label_entry_frame,
            font=Font.MEDIUM_FONT,
            width=10,
            fg=Color.MOUNTBATTEN_PINK,
            show="*")
        self.is_admin_var = tk.BooleanVar()
        self.is_admin_checkbox = tk.Checkbutton(
            self.label_entry_frame,
            font=Font.MEDIUM_FONT,
            bg=Color.LAVENDER,
            fg=Color.MOUNTBATTEN_PINK,
            activebackground=Color.ROSE_QUARTZ,
            activeforeground=Color.PALE_PURPLE,
            variable=self.is_admin_var,
            onvalue=True,
            offvalue=False
        )

        self.username_label.grid(row=2, column=0)
        self.username_entry.grid(row=2, column=1)
        self.password_label1.grid(row=3, column=0)
        self.password_entry1.grid(row=3, column=1)
        self.password_label2.grid(row=4, column=0)
        self.password_entry2.grid(row=4, column=1)
        self.is_admin_checkbox.grid(row=5, column=0, columnspan=2)
        self.label_entry_frame.grid(row=0, column=0)

        self.button_frame = tk.Frame(self.bottom_frame, bg=Color.LAVENDER)
        self.buttons = {
            "add":      tk.Button(self.button_frame),
            "update":   tk.Button(self.button_frame),
            "delete":   tk.Button(self.button_frame),
            "back":     tk.Button(self),
        }

        Style.dummy_label(self.bottom_frame, text="       ").grid(row=0, column=1)

        for i, button in enumerate(self.buttons.values()):
            button.configure(
                width=19,
                height=2,
                font=Font.MEDIUM_FONT,
                bg=Color.PALE_PURPLE,
                fg=Color.MOUNTBATTEN_PINK,
                activebackground=Color.ROSE_QUARTZ,
                activeforeground=Color.PALE_PURPLE)

        self.buttons["add"].pack()
        Style.dummy_label(self.button_frame).pack()
        self.buttons["update"].pack()
        Style.dummy_label(self.button_frame).pack()
        self.buttons["delete"].pack()
        self.button_frame.grid(row=0, column=2)

        self.bottom_frame.pack()

        Style.dummy_label(self.button_frame, size=20).pack()
        self.buttons["back"].pack()
