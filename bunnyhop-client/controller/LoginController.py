import RequestType
from enums.FrameType import FrameType
from session_info.SessionInfo import SessionInfo
from pattern_templates.Observer import Observer
from res import Style
from view.frame.LoginFrame import LoginFrame


class LoginException(Exception):
    def __init__(self, message):
        self.message = message


class LoginController(Observer):
    def __init__(self, master_controller):
        self.master_controller = master_controller

        self.login_frame = LoginFrame(master_controller.master_frame)

        self.session_info = SessionInfo()

        self.login_frame.login_button.config(command=self.on_login_button)
        self.login_frame.back_button.config(command=self.on_back_button)

        self.login_frame.register_label.bind("<Button-1>", self.on_register_label)
        self.login_frame.register_label.bind("<Enter>", Style.on_label_enter)
        self.login_frame.register_label.bind("<Leave>", Style.on_label_leave)

    def setup(self):
        self.login_frame.username_entry.delete(0, "end")
        self.login_frame.password_entry.delete(0, "end")
        self.login_frame.message_label.config(text="")

    def on_login_button(self, event=None):
        username = self.login_frame.username_entry.get()
        password = self.login_frame.password_entry.get()

        try:
            if len(username) == 0 or len(password) == 0:
                raise LoginException("message_label_empty_fields")

            # check if username exists in database
            user = self.master_controller.enqueue_request(RequestType.GET_USER_FROM_USERNAME, username=username)
            if user is None:
                raise LoginException("message_label_incorrect_credentials")

            # check if password provided is correct
            valid_password = self.master_controller.enqueue_request(
                RequestType.CHECK_NOT_ENCRYPTED_AGAINST_ENCRYPTED,
                not_encrypted=password,
                encrypted=user.password
            )
            if not valid_password:
                raise LoginException("message_label_incorrect_credentials")

            # login validated
            self.session_info.user = user
            self.master_controller.active_frame = FrameType.WelcomeFrame
        except LoginException as e:
            self.login_frame.message_label.config(
                text=self.session_info.active_language["login_frame"][e.message])

    def on_back_button(self, event=None):
        self.master_controller.active_frame = FrameType.WelcomeFrame

    def on_register_label(self, event=None):
        self.master_controller.active_frame = FrameType.RegisterFrame

    def update(self, subject):
        string = self.session_info.active_language["login_frame"]

        self.login_frame.title_label.config(text=string["title_label"])
        self.login_frame.username_label.config(text=string["username_label"])
        self.login_frame.password_label.config(text=string["password_label"])
        self.login_frame.register_label.config(text=string["register_label"])
        self.login_frame.login_button.config(text=string["login_button"])
        self.login_frame.back_button.config(text=string["back_button"])