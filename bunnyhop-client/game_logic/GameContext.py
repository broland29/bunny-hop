from game_logic.GameState import GameState
from game_logic.IdleState import IdleState
from game_logic.OverState import OverState
from game_logic.PausedState import PausedState
from game_logic.RunningState import RunningState
from game_logic.Pattern import Pattern
from session_info.SessionInfo import SessionInfo


class GameContext:
    state: GameState
    time: int
    move_history: list[(int, int)]

    def __init__(self, controller):
        self.controller = controller  # todo

        self.idle_state = IdleState(self)           # before playing, everything in starting position
        self.running_state = RunningState(self)     # bunny was moved at least once
        self.paused_state = PausedState(self)       # user paused
        self.over_state = OverState(self)           # bunny reached the carrot

        self.session_info = SessionInfo()
        self.pattern = Pattern()

    def set_state(self, state: GameState):
        self.state = state

    def pause(self):
        self.state.pause()

    def help(self):
        self.state.help()

    def quit(self):
        self.state.quit()

    def jump(self, di, dj):
        self.state.jump(di, dj)

    def run_clock(self):
        self.state.run_clock()

    @property
    def current_pattern(self):
        return self.pattern.current_pattern

    @property
    def optimal_path(self):
        return self.pattern.optimal_path

    def new_game(self):
        self.state = self.idle_state
        self.time = 0
        self.pattern.reset(self.session_info.difficulty_handler.difficulty)
        self.move_history = [self.pattern.start]
