import RequestType
from enums.FrameType import FrameType
from session_info.SessionInfo import SessionInfo
from pattern_templates.Observer import Observer
from res import Style
from view.frame.ProfileFrame import ProfileFrame
import tkinter as tk
import matplotlib.pyplot as plt


class ProfileController(Observer):
    def __init__(self, master_controller):
        self.master_controller = master_controller

        self.profile_frame = ProfileFrame(master_controller.master_frame)

        self.session_info = SessionInfo()

        self.profile_frame.buttons["stat"].config(command=self.on_stat_button)
        self.profile_frame.buttons["back"].config(command=self.on_back_button)

        self.games = []

    def setup(self):
        self.update_game_list()

    def update_game_list(self) -> None:
        self.profile_frame.game_list_box.delete(0, tk.END)

        self.games = self.master_controller.enqueue_request(
            RequestType.GET_GAMES_BY_USER,
            user=self.session_info.user
        )
        for game in self.games:
            self.profile_frame.game_list_box.insert(tk.END, Style.format_game_row(game))
        print(self.games)

    def on_stat_button(self, event=None):
        # https://www.geeksforgeeks.org/python-count-occurrences-element-list/
        difficulties = []
        for game in self.games:
            difficulties.append(game.difficulty)
        occurrence = {item: difficulties.count(item) for item in difficulties}

        labels = occurrence.keys()
        sizes = occurrence.values()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.legend(title=self.session_info.active_language["profile_frame"]["plot_legend"])
        plt.title(self.session_info.active_language["profile_frame"]["plot_title"])
        plt.show()

    def on_back_button(self, event=None):
        self.master_controller.active_frame = FrameType.WelcomeFrame

    def update(self, subject):
        string = self.session_info.active_language["profile_frame"]
        self.profile_frame.title_label.config(text=string["title_label"])
        self.profile_frame.buttons["stat"].config(text=string["stat_button"])
        self.profile_frame.buttons["back"].config(text=string["back_button"])

        self.profile_frame.header_list_box.delete(0, tk.END)
        self.profile_frame.header_list_box.insert(tk.END, Style.format_game_header(
            string["gid"],
            string["date"],
            string["time"],
            string["difficulty"],
            string["optimal_path_length"],
            string["actual_path_length"]
        ))
