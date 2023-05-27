import webbrowser

from enums.FrameType import FrameType
from pattern_templates.Observer import Observer
from res import Style
from session_info.SessionInfo import SessionInfo
from view.frame.WelcomeFrame import WelcomeFrame
from view.popup.NotifyPopup import NotifyPopup


class WelcomeController(Observer):
    def __init__(self, master_controller):
        self.master_controller = master_controller

        self.welcome_frame = WelcomeFrame(master_controller.master_frame)

        self.session_info = SessionInfo()

        self.welcome_frame.buttons["login"].config(command=self.on_login_button)
        self.welcome_frame.buttons["play"].config(command=self.on_play_button)
        self.welcome_frame.buttons["settings"].config(command=self.on_settings_button)
        self.welcome_frame.buttons["profile"].config(command=self.on_profile_button)

        self.welcome_frame.admin_label.bind("<Button-1>", self.on_admin_label)
        self.welcome_frame.admin_label.bind("<Enter>", Style.on_label_enter)
        self.welcome_frame.admin_label.bind("<Leave>", Style.on_label_leave)

        self.welcome_frame.github_label.bind("<Button-1>", self.on_github_label)
        self.welcome_frame.github_label.bind("<Enter>", Style.on_label_enter)
        self.welcome_frame.github_label.bind("<Leave>", Style.on_label_leave)

    def setup(self):
        user = self.session_info.user
        string = self.session_info.active_language["welcome_frame"]
        if user is None:
            self.welcome_frame.username_label.config(text=f"{string['username_label_not_logged']}!")
            self.welcome_frame.buttons["login"].config(text=string["login_button_not_logged"])
        else:
            self.welcome_frame.username_label.config(text=f"{string['username_label_logged']}, {user.username}!")
            self.welcome_frame.buttons["login"].config(text=string["login_button_logged"])

    def on_login_button(self, event=None):
        user = self.session_info.user
        if user is None:
            self.master_controller.active_frame = FrameType.LoginFrame
        else:
            self.session_info.user = None
            self.setup()  # to refresh UI
            NotifyPopup(self, self.session_info.active_language["welcome_frame"]["notify_popup_log_out"])

    def on_play_button(self, event=None):
        self.master_controller.active_frame = FrameType.GameFrame

    def on_settings_button(self, event=None):
        self.master_controller.active_frame = FrameType.SettingsFrame

    def on_profile_button(self, event=None):
        user = self.session_info.user
        if user is None:
            NotifyPopup(self, self.session_info.active_language["welcome_frame"]["notify_popup_not_logged"])
        else:
            self.master_controller.active_frame = FrameType.ProfileFrame

    def on_admin_label(self, event=None):
        user = self.session_info.user
        if user is None:
            NotifyPopup(self, self.session_info.active_language["welcome_frame"]["notify_popup_not_logged"])
        elif user.is_admin == 0:
            NotifyPopup(self, self.session_info.active_language["welcome_frame"]["notify_popup_not_admin"])
        else:
            self.master_controller.active_frame = FrameType.AdminFrame

    @staticmethod
    def on_github_label(event=None):
        webbrowser.open("https://github.com/broland29")

    def update(self, subject):
        user = self.session_info.user
        string = self.session_info.active_language["welcome_frame"]

        self.welcome_frame.title_label.config(text=string["title_label"])
        if self.session_info.user is None:
            self.welcome_frame.username_label.config(text=f"{string['username_label_not_logged']}!")
            self.welcome_frame.buttons["login"].config(text=string["login_button_not_logged"])
        else:
            self.welcome_frame.username_label.config(text=f"{string['username_label_logged']}, {user.username}!")
            self.welcome_frame.buttons["login"].config(text=string["login_button_logged"])
        self.welcome_frame.buttons["play"].config(text=string["play_button"])
        self.welcome_frame.buttons["settings"].config(text=string["settings_button"])
        self.welcome_frame.buttons["profile"].config(text=string["profile_button"])
        self.welcome_frame.admin_label.config(text=string["admin_label"])
        self.welcome_frame.github_label.config(text=string["github_label"])
