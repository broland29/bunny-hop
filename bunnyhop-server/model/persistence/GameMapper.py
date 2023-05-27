from datetime import datetime
from Game import Game

gid_index = 0
uid_index = 1
date_index = 2
time_index = 3
difficulty_index = 4
optimal_path_length_index = 5
actual_path_length_index = 6


class GameMapper:
    @staticmethod
    def db_to_class(game: list[int | datetime]):
        return Game(
            gid=game[gid_index],
            uid=game[uid_index],
            date=game[date_index],  # mapping done automatically (we get datetime directly from query)
            time=game[time_index],
            difficulty=game[difficulty_index],
            optimal_path_length=game[optimal_path_length_index],
            actual_path_length=game[actual_path_length_index]
        )

    @staticmethod
    def class_to_db(game: Game):
        return [
            game.gid,
            game.uid,
            game.date,
            game.time,
            game.difficulty,
            game.optimal_path_length,
            game.actual_path_length
        ]
