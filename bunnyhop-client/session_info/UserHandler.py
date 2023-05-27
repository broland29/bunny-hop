from pattern_templates.Subject import Subject


class UserHandler(Subject):
    def __init__(self):
        self._observers = []
        self._user = None

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
    def user(self):
        return self._user

    @user.setter
    def user(self, value: user):
        self._user = value
        self.notify()
