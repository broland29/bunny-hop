from tkinter import messagebox

import RequestType
from Game import Game
from GameState import GameState
from enums.CellType import CellType
from enums.FrameType import FrameType


class RunningState(GameState):
    def __init__(self, context):
        self.context = context

    def pause(self):
        self.context.set_state(self.context.paused_state)
        self.context.controller.game_frame.buttons["pause"].config(
            text=self.context.session_info.active_language["game_frame"]["pause_button_resume"])  # from paused to running

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
        # current position about to become old position
        i_old, j_old = self.context.pattern.bunny_position

        # potential positions: where user wants to jump
        i_pot = i_old + di
        j_pot = j_old + dj

        # if out of bounds, we cannot talk about cell
        if i_pot >= self.context.pattern.difficulty\
                or j_pot >= self.context.pattern.difficulty\
                or i_pot < 0\
                or j_pot < 0:
            print("Jump: out of bounds!")
            return

        # else we take the type of cell we want to jump to
        cell = self.context.pattern.current_pattern[i_pot][j_pot]
        # for default, let's go with no move
        i_new = i_old
        j_new = j_old

        if cell == CellType.Trap:
            print("Jump: in a trap!")
            # threading.Thread(target=playsound, args=('res/sfx/trap.mp3',), daemon=True).start()
            i_new = self.context.pattern.start[0]
            j_new = self.context.pattern.start[1]
        elif cell == CellType.Carrot:
            print("Jump: found carrot!")
            # threading.Thread(target=playsound, args=('res/sfx/carrot.mp3',), daemon=True).start()
            i_new = i_pot
            j_new = j_pot

            user = self.context.session_info.user
            if user is not None:
                game = Game(
                    uid=user.uid,
                    time=self.context.time,
                    difficulty=self.context.pattern.difficulty,
                    optimal_path_length=len(self.context.pattern.optimal_path),
                    actual_path_length=len(self.context.move_history) + 1)
                # destination added to move history only at the end of this function

                self.context.controller.master_controller.enqueue_request(
                    RequestType.CREATE_GAME,
                    game=game
                )

            string = self.context.session_info.active_language["game_frame"]
            self.context.controller.game_frame.buttons["pause"].config(text=string["pause_button_again"])
            self.context.controller.game_frame.buttons["help"].config(text=string["help_button_solution"])
            self.context.controller.refresh_cells()

            self.context.set_state(self.context.over_state)
        elif cell == CellType.Empty:
            print("Jump: to empty cell!")
            # threading.Thread(target=playsound, args=('res/sfx/jump.mp3',), daemon=True).start()
            i_new = i_pot
            j_new = j_pot

        # in any case, jumping consists of leaving an empty cell behind and occupying new cell
        self.context.pattern.current_pattern[i_old][j_old] = CellType.Empty
        self.context.pattern.current_pattern[i_new][j_new] = CellType.Bunny
        self.context.pattern.bunny_position = (i_new, j_new)

        # keep track of jump
        self.context.move_history.append((i_new, j_new))
        self.context.controller.refresh_cells()

        self.context.controller.game_frame.buttons["pause"].config(
            text=self.context.session_info.active_language["game_frame"][
                "pause_button_pause"])

    def run_clock(self):
        self.context.time += 1
        self.context.controller.game_frame.time_label.config(text=str(self.context.time))
