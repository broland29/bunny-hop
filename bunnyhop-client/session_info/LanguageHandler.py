import json

from enums.LanguageType import LanguageType
from pattern_templates.Subject import Subject


class LanguageHandler(Subject):
    def __init__(self):
        self._observers = []
        with open("res/string/English.json", "r") as f:
            self.english = json.load(f)
        with open("res/string/Hungarian.json", "r") as f:
            self.hungarian = json.load(f)
        with open("res/string/Romanian.json", "r") as f:
            self.romanian = json.load(f)
        self._active_language = self.english

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    # usually subject needs to be passed to have access to info
    # though, in my case, controller already has such info
    def notify(self):
        print(self._observers)
        for observer in self._observers:
            observer.update(self)

    @property
    def active_language(self):
        return self._active_language

    @active_language.setter
    def active_language(self, value: LanguageType):
        match value:
            case LanguageType.English:
                self._active_language = self.english
            case LanguageType.Hungarian:
                self._active_language = self.hungarian
            case LanguageType.Romanian:
                self._active_language = self.romanian
        self.notify()
