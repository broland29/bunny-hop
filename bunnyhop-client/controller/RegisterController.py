import RequestType
from enums.FrameType import FrameType
from session_info.SessionInfo import SessionInfo
from User import User
from pattern_templates.Observer import Observer
from res import Style
from view.frame.RegisterFrame import RegisterFrame


class RegisterException(Exception):
    def __init__(self, message):
        self.message = message


class RegisterController(Observer):
    def __init__(self, master_controller):
        self.master_controller = master_controller

        self.register_frame = RegisterFrame(master_controller.master_frame)

        self.session_info = SessionInfo()

        self.register_frame.register_button.config(command=self.on_register_button)
        self.register_frame.back_button.config(command=self.on_back_button)

        self.register_frame.login_label.bind("<Button-1>", self.on_login_label)
        self.register_frame.login_label.bind("<Enter>", Style.on_label_enter)
        self.register_frame.login_label.bind("<Leave>", Style.on_label_leave)

    def setup(self):
        self.register_frame.username_entry.delete(0, "end")
        self.register_frame.password_entry1.delete(0, "end")
        self.register_frame.password_entry2.delete(0, "end")
        self.register_frame.message_label.config(text="")

    def on_register_button(self, event=None):
        username = self.register_frame.username_entry.get()
        password1 = self.register_frame.password_entry1.get()
        password2 = self.register_frame.password_entry2.get()

        valid_credentials, message = self.master_controller.enqueue_request(
            RequestType.CHECK_CREDENTIALS_VALIDITY,
            username=username,
            password1=password1,
            password2=password2
        )
        if not valid_credentials:
            self.register_frame.message_label.config(
                text=self.session_info.active_language["registration_validator"][message])
            return

        # register validated
        encrypted_password = self.master_controller.enqueue_request(
            RequestType.ENCRYPT_PASSWORD,
            password=password1
        )
        user_without_uid = User(
            username=username,
            password=encrypted_password,
            is_admin=False)

        self.master_controller.enqueue_request(
            RequestType.CREATE_USER,
            user=user_without_uid
        )

        user_with_uid = self.master_controller.enqueue_request(
            RequestType.GET_USER_FROM_USERNAME,
            username=username
        )

        self.session_info.user = user_with_uid
        self.master_controller.active_frame = FrameType.WelcomeFrame

    def on_login_label(self, event=None):
        self.master_controller.active_frame = FrameType.LoginFrame

    def on_back_button(self):
        self.master_controller.active_frame = FrameType.WelcomeFrame

    def update(self, subject):
        string = self.session_info.active_language["register_frame"]

        self.register_frame.title_label.config(text=string["title_label"])
        self.register_frame.username_label.config(text=string["username_label"])
        self.register_frame.password_label1.config(text=string["password_label1"])
        self.register_frame.password_label2.config(text=string["password_label2"])
        self.register_frame.login_label.config(text=string["login_label"])
        self.register_frame.register_button.config(text=string["register_button"])
        self.register_frame.back_button.config(text=string["back_button"])