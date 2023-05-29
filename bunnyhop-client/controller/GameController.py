import time

from game_logic.GameContext import GameContext
from enums.CellType import CellType
from enums.FrameType import FrameType
from session_info.SessionInfo import SessionInfo
from pattern_templates.Observer import Observer

from PIL import ImageTk, Image

from res import Sprite
from view.frame.GameFrame import GameFrame
import tkinter as tk


class GameController(Observer):
    def __init__(self, master_controller):
        self.master_controller = master_controller

        self.game_frame = GameFrame(master_controller.master_frame)

        self.game_frame.buttons["pause"].config(command=self.on_pause_button)
        self.game_frame.buttons["help"].config(command=self.on_help_button)
        self.game_frame.buttons["quit"].config(command=self.on_quit_button)
        self.master_controller.master_frame.parent.bind("<Key>", self.on_key)  # ugh

        self.session_info = SessionInfo()

        # self.game_logic = GameLogic(self)
        self.game_context = GameContext(self)
        self.images = None

    # quit button only changes if language changes, pause and help need to be involved in other logic as well
    def update(self, subject):
        string = self.session_info.active_language["game_frame"]
        self.game_frame.title_label.config(text=string["title_label_time"])
        self.game_frame.buttons["pause"].config(text=string["pause_button_pause"])
        self.game_frame.buttons["quit"].config(text=string["quit_button"])
        self.game_frame.buttons["help"].config(text=string["help_button_help"])

    def setup(self):
        self.game_context.new_game()  # also sets game state to idle

        # necessary, or else old buttons will remain on the frame
        if self.game_frame.button_array is not None:
            for i in range(len(self.game_frame.button_array)):
                for j in range(len(self.game_frame.button_array[0])):
                    self.game_frame.button_array[i][j].destroy()

        difficulty = self.session_info.difficulty
        width = int(450 / difficulty)
        height = int(450 / difficulty)
        self.images = {
            CellType.Bunny:  ImageTk.PhotoImage(Sprite.images[CellType.Bunny].resize((width, height), Image.ANTIALIAS)),
            CellType.Empty:  ImageTk.PhotoImage(Sprite.images[CellType.Empty].resize((width, height), Image.ANTIALIAS)),
            CellType.Trap:   ImageTk.PhotoImage(Sprite.images[CellType.Trap].resize((width, height), Image.ANTIALIAS)),
            CellType.Carrot: ImageTk.PhotoImage(Sprite.images[CellType.Carrot].resize((width, height), Image.ANTIALIAS))
        }
        self.game_frame.button_array = [[tk.Button() for _ in range(difficulty)] for _ in range(difficulty)]
        for i in range(difficulty):
            for j in range(difficulty):
                self.game_frame.button_array[i][j] = tk.Button(self.game_frame.button_frame, width=width, height=height)
                self.game_frame.button_array[i][j].grid(row=i, column=j)
        self.refresh_cells()

        string = self.session_info.active_language["game_frame"]
        self.game_frame.title_label.config(text=string["title_label_time"])
        self.game_frame.time_label.configure(text=string["time_label_dashed"])
        self.game_frame.buttons["pause"].config(text=string["pause_button_start"])
        self.game_frame.buttons["help"].config(text=string["help_button_help"])

    def refresh_cells(self):
        current_pattern = self.game_context.current_pattern
        difficulty = self.session_info.difficulty
        for i in range(difficulty):
            for j in range(difficulty):
                cell_type = current_pattern[i][j]
                self.game_frame.button_array[i][j].config(image=self.images[cell_type])

    def run_clock(self):
        self.game_context.run_clock()
        self.game_frame.after(100, self.run_clock)

    def on_key(self, event=None):
        if self.master_controller.active_frame != FrameType.GameFrame:
            return

        match event.keysym:
            case "KP_1":
                self.game_context.jump(1, -1)
            case "KP_2":
                self.game_context.jump(1, 1)
            case "KP_4":
                self.game_context.jump(-1, -1)
            case "KP_5":
                self.game_context.jump(-1, 1)
            case "KP_Down" | "KP_End" | "KP_Begin" | "KP_Left":
                print("TURN ON NUM LOCK!")
            case _:
                print("Key pressed: " + event.keysym)

    def on_pause_button(self, event=None):
        self.game_context.pause()

    def on_quit_button(self, event=None):
        self.game_context.quit()

    def on_help_button(self, event=None):
        self.game_context.help()

    def show_path(self, path):
        print(path)
        old_i, old_j = path[0]
        car_i, car_j = path[-1]
        self.game_frame.button_array[old_i][old_j].config(image=self.images[CellType.Bunny])
        self.game_frame.button_array[car_i][car_j].config(image=self.images[CellType.Carrot])
        self.game_frame.update_idletasks()
        time.sleep(1 / self.session_info.difficulty)

        for i in range(len(path) - 1):
            new_i, new_j = path[i + 1]
            self.game_frame.button_array[old_i][old_j].config(image=self.images[CellType.Empty])
            self.game_frame.button_array[new_i][new_j].config(image=self.images[CellType.Bunny])
            self.game_frame.update_idletasks()
            old_i, old_j = new_i, new_j
            time.sleep(1 / self.session_info.difficulty)
