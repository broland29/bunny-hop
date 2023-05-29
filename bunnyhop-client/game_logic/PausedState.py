from tkinter import messagebox

from game_logic.GameState import GameState
from enums.FrameType import FrameType


class PausedState(GameState):
    def __init__(self, context):
        self.context = context

    def pause(self):
        self.context.set_state(self.context.running_state)
        self.context.controller.run_clock()  # (re)start the clock
        self.context.controller.game_frame.buttons["pause"].config(
            text=self.context.session_info.active_language["game_frame"]["pause_button_pause"])

    def help(self):
        string = self.context.session_info.active_language["game_frame"]

        self.context.set_state(self.context.paused_state)
        self.context.controller.game_frame.buttons["pause"].config(
            text=self.context.session_info.active_language["game_frame"]["pause_button_resume"])
        messagebox.showinfo(
            title=string["title_messagebox"],
            message=string["help_messagebox"])

    def quit(self):
        self.context.set_state(self.context.over_state)
        self.context.controller.master_controller.active_frame = FrameType.WelcomeFrame

    def jump(self, di, dj):
        self.context.set_state(self.context.running_state)
        self.context.jump(di, dj)  # ?

    def run_clock(self):
        return
