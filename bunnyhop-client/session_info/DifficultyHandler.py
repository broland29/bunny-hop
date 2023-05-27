from pattern_templates.Subject import Subject


class DifficultyHandler(Subject):
    def __init__(self):
        self._observers = []
        self._difficulty = 5

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
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value: int):
        self._difficulty = value
        self.notify()
