import tkinter as tk

import RequestType
from User import User
from enums.FrameType import FrameType
from session_info.SessionInfo import SessionInfo
from pattern_templates.Observer import Observer
from res import Style
from view.frame.AdminFrame import AdminFrame


class AdminController(Observer):
    def __init__(self, master_controller):
        self.master_controller = master_controller

        self.admin_frame = AdminFrame(master_controller.master_frame)

        self.session_info = SessionInfo()

        self.admin_frame.buttons["back"].config(command=self.on_back_button)
        self.admin_frame.buttons["add"].config(command=self.on_add_button)
        self.admin_frame.buttons["update"].config(command=self.on_update_button)
        self.admin_frame.buttons["delete"].config(command=self.on_delete_button)

        self.users = []

    def setup(self):
        self.update_user_list()

    def update_user_list(self):
        self.admin_frame.user_list_box.delete(0, tk.END)

        self.users = self.master_controller.enqueue_request(RequestType.GET_ALL_USERS)
        for user in self.users:
            self.admin_frame.user_list_box.insert(tk.END, Style.format_user_row(user))

    def on_back_button(self):
        self.master_controller.active_frame = FrameType.WelcomeFrame

    # basically registration
    def on_add_button(self):
        username = self.admin_frame.username_entry.get()
        password1 = self.admin_frame.password_entry1.get()
        password2 = self.admin_frame.password_entry2.get()
        is_admin = self.admin_frame.is_admin_var.get()

        valid_credentials, message = self.master_controller.enqueue_request(
            RequestType.CHECK_CREDENTIALS_VALIDITY,
            username=username,
            password1=password1,
            password2=password2
        )
        if not valid_credentials:
            self.admin_frame.message_label.config(
                text=self.session_info.active_language["registration_validator"][message]
            )
            return

        # register validated
        encrypted_password = self.master_controller.enqueue_request(
            RequestType.ENCRYPT_PASSWORD,
            password=password1
        )

        user = User(
            username=username,
            password=encrypted_password,
            is_admin=is_admin
        )

        self.master_controller.enqueue_request(
            RequestType.CREATE_USER,
            user=user
        )

        self.update_user_list()
        self.admin_frame.message_label.config(
            text=self.session_info.active_language["admin_frame"]["message_label_successful_add"])

    # partly registration
    def on_update_button(self):
        # function returns tuple, first element is index of row => index of list
        try:
            old_user = self.users[self.admin_frame.user_list_box.curselection()[0]]
        except IndexError:
            self.admin_frame.message_label.config(
                text=self.session_info.active_language["admin_frame"]["no_selected_user"])
            return

        username = self.admin_frame.username_entry.get()
        password1 = self.admin_frame.password_entry1.get()
        password2 = self.admin_frame.password_entry2.get()
        is_admin = self.admin_frame.is_admin_var.get()

        if username == "":
            username = None
        else:
            valid_username, message = self.master_controller.enqueue_request(
                RequestType.VALIDATE_USERNAME,
                username=username,
            )
            if not valid_username:
                self.admin_frame.message_label.config(
                    text=self.session_info.active_language["registration_validator"][message]
                )
                return
            # trying to update to same username will give error!
        if password1 == password2 == "":
            encrypted_password = None
        else:
            valid_password, message = self.master_controller.enqueue_request(
                RequestType.VALIDATE_PASSWORD,
                password1=password1,
                password2=password2
            )
            if not valid_password:
                self.admin_frame.message_label.config(
                    text=self.session_info.active_language["registration_validator"][message]
                )
                return

            encrypted_password = self.master_controller.enqueue_request(
                RequestType.ENCRYPT_PASSWORD,
                password=password1  # made sure no None is passed for encryption
            )

        # inputs validated
        new_user = User(
            username=username,
            password=encrypted_password,
            is_admin=is_admin)

        self.master_controller.enqueue_request(
            RequestType.UPDATE_USER,
            old_user=old_user,
            new_user=new_user
        )

        self.update_user_list()
        self.admin_frame.message_label.config(
            text=self.session_info.active_language["admin_frame"]["message_label_successful_update"])

    def on_delete_button(self):
        try:
            user = self.users[self.admin_frame.user_list_box.curselection()[0]]
        except IndexError:
            self.admin_frame.message_label.config(
                text=self.session_info.active_language["admin_frame"]["no_selected_user"])
            return

        self.master_controller.enqueue_request(
            RequestType.DELETE_USER,
            user=user
        )

        self.update_user_list()
        self.admin_frame.message_label.config(
            text=self.session_info.active_language["admin_frame"]["message_label_successful_delete"])

    def update(self, subject):
        string = self.session_info.active_language["admin_frame"]
        self.admin_frame.title_label.config(text=string["title_label"])
        self.admin_frame.username_label.config(text=string["username_label"])
        self.admin_frame.password_label1.config(text=string["password_label1"])
        self.admin_frame.password_label2.config(text=string["password_label2"])
        self.admin_frame.is_admin_checkbox.config(text=string["is_admin_checkbox"])
        self.admin_frame.buttons["add"].config(text=string["add_button"])
        self.admin_frame.buttons["update"].config(text=string["update_button"])
        self.admin_frame.buttons["delete"].config(text=string["delete_button"])
        self.admin_frame.buttons["back"].config(text=string["back_button"])

        self.admin_frame.header_list_box.delete(0, tk.END)
        self.admin_frame.header_list_box.insert(tk.END, Style.format_user_header(
            string["uid"], string["username"], string["is_admin"]))


