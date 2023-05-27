from abc import ABC, abstractmethod


class GameState(ABC):
    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def help(self):
        pass

    @abstractmethod
    def quit(self):
        pass

    @abstractmethod
    def jump(self, di, dj):
        pass

    @abstractmethod
    def run_clock(self):
        pass
