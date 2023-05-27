from GameState import GameState
from enums.FrameType import FrameType
import tkinter as tk


class OverState(GameState):
    def __init__(self, context):
        self.context = context

    def pause(self):
        self.context.new_game()  # from over to new game
        self.context.controller.setup()  # sets every label/ button to appropriate value

    def help(self):
        string = self.context.session_info.active_language["game_frame"]

        optimal_path = self.context.optimal_path
        actual_path = self.context.move_history

        self.context.controller.game_frame.title_label.configure(text=f"{string['title_label_best']}: {len(optimal_path)}.")
        self.context.controller.game_frame.time_label.configure(text=f"{string['time_label_you']}: {len(actual_path)}.")

        for button in self.context.controller.game_frame.buttons.values():
            button.config(state=tk.DISABLED)

        self.context.controller.show_path(optimal_path)
        self.context.controller.show_path(actual_path)

        for button in self.context.controller.game_frame.buttons.values():
            button.config(state=tk.NORMAL)

    def quit(self):
        self.context.set_state(self.context.over_state)
        self.context.controller.master_controller.active_frame = FrameType.WelcomeFrame

    # jumping has no effect
    def jump(self, di, dj):
        return

    def run_clock(self):
        return
