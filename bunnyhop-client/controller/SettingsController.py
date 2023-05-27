from enums.FrameType import FrameType
from enums.LanguageType import LanguageType
from session_info.SessionInfo import SessionInfo
from pattern_templates.Observer import Observer
from view.frame.SettingsFrame import SettingsFrame


class SettingsController(Observer):
    def __init__(self, master_controller):
        self.master_controller = master_controller

        self.settings_frame = SettingsFrame(master_controller.master_frame)

        self.session_info = SessionInfo()

        self.settings_frame.language_buttons["english"].config(command=self.on_english_button)
        self.settings_frame.language_buttons["hungarian"].config(command=self.on_hungarian_button)
        self.settings_frame.language_buttons["romanian"].config(command=self.on_romanian_button)
        self.settings_frame.back_button.config(command=self.on_back_button)

    def on_english_button(self):
        self.session_info.active_language = LanguageType.English

    def on_hungarian_button(self):
        self.session_info.active_language = LanguageType.Hungarian

    def on_romanian_button(self):
        self.session_info.active_language = LanguageType.Romanian

    def on_back_button(self):
        self.session_info.difficulty = self.settings_frame.difficulty_slider.get()
        self.master_controller.active_frame = FrameType.WelcomeFrame

    def update(self, subject):
        string = self.session_info.active_language["settings_frame"]
        self.settings_frame.title_label.config(text=string["title_label"])
        self.settings_frame.difficulty_label.config(text=string["difficulty_label"])
        self.settings_frame.language_label.config(text=string["language_label"])
        self.settings_frame.back_button.config(text=string["back_button"])
