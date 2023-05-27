from session_info.UserHandler import UserHandler
from session_info.DifficultyHandler import DifficultyHandler
from session_info.LanguageHandler import LanguageHandler
from enums.LanguageType import LanguageType
from User import User
from pattern_templates.Singleton import Singleton


class SessionInfo(metaclass=Singleton):

    def __init__(self):
        self.user_handler = UserHandler()
        self.difficulty_handler = DifficultyHandler()
        self.language_handler = LanguageHandler()

    @property
    def user(self):
        return self.user_handler.user

    @user.setter
    def user(self, value: User):
        self.user_handler.user = value

    @property
    def difficulty(self):
        return self.difficulty_handler.difficulty

    @difficulty.setter
    def difficulty(self, value: int):
        self.difficulty_handler.difficulty = value

    @property
    def active_language(self):
        return self.language_handler.active_language

    @active_language.setter
    def active_language(self, value: LanguageType):
        self.language_handler.active_language = value
