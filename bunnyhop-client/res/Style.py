from res import Color
import tkinter as tk

user_width = [10, 15, 10]
game_width = [5, 21, 7, 5, 5, 5]


def on_label_enter(event):
    widget = event.widget
    widget.config(bg=Color.ROSE_QUARTZ, fg=Color.LAVENDER)


def on_label_leave(event):
    widget = event.widget
    widget.config(bg=Color.LAVENDER, fg=Color.MOUNTBATTEN_PINK)


def format_user_header(uid, username, is_admin):
    return f"{uid: <{user_width[0]}}" \
           f"{username: <{user_width[1]}}" \
           f"{is_admin: <{user_width[2]}}"


def format_user_row(user):
    return f"{user.uid: <{user_width[0]}}" \
           f"{user.username: <{user_width[1]}}" \
           f"{user.is_admin: <{user_width[2]}}"


def format_game_header(gid, date, time, difficulty, optimal_path_length, actual_path_length):
    return f"{gid: <{game_width[0]}}" \
           f"{date: <{game_width[1]}}" \
           f"{time: <{game_width[2]}}" \
           f"{difficulty: <{game_width[3]}}" \
           f"{optimal_path_length: <{game_width[4]}}" \
           f"{actual_path_length: <{game_width[5]}}"


def format_game_row(game):
    return f"{game.gid: <{game_width[0]}}" \
           f"{str(game.date): <{game_width[1]}}" \
           f"{game.time: <{game_width[2]}}" \
           f"{game.difficulty: <{game_width[3]}}" \
           f"{game.optimal_path_length: <{game_width[4]}}" \
           f"{game.actual_path_length: <{game_width[5]}}"


def dummy_label(parent, size=5, text=""):
    return tk.Label(parent, text=text, font=("Consolas", size), bg=Color.LAVENDER)
