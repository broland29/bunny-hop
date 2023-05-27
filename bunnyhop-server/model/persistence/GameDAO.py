from model.persistence.DatabaseConnector import DatabaseConnector
from Game import Game
from User import User
import model.persistence.GameMapper as GM
import model.persistence.UserMapper as UM


class GameDAOException(Exception):
    def __init__(self, message):
        super().__init__(message)


class GameDAO:
    def __init__(self, database="bunnyhop"):
        dc = DatabaseConnector(database)
        self.db = dc.db
        self.cursor = dc.cursor

    # inserts a game into the database based on input game object
    def create_game(self, game: Game):
        if game is None:
            raise GameDAOException("Game not provided (None)!")
        if game.uid is None:
            raise GameDAOException("UID not provided!")
        if game.time is None:
            raise GameDAOException("Time not provided!")
        if game.difficulty is None:
            raise GameDAOException("Difficulty not provided!")
        if game.optimal_path_length is None:
            raise GameDAOException("Optimal path length not provided!")
        if game.actual_path_length is None:
            raise GameDAOException("Actual path length not provided!")

        game_db = GM.GameMapper.class_to_db(game)
        query = """INSERT INTO game (uid, time, difficulty, optimal_path_length, actual_path_length)
                   VALUES (%s, %s, %s, %s, %s)"""
        self.cursor.execute(query, [
            game_db[GM.uid_index],
            game_db[GM.time_index],
            game_db[GM.difficulty_index],
            game_db[GM.optimal_path_length_index],
            game_db[GM.actual_path_length_index]])
        self.db.commit()

    # https://stackoverflow.com/questions/56869778/how-to-fix-mysql-select-command-giving-wrong-result-after-the-update-in-another
    # notice commit at end, even though reading and not updating
    # returns a list of game objects reflecting the games of a given user
    def get_games_by_user(self, user: User):
        if user is None:
            raise GameDAOException("User not provided (None)!")
        if user.uid is None:
            raise GameDAOException("UID not provided!")

        user_db = UM.UserMapper.class_to_db(user)
        query = """SELECT *
                     FROM game
                    WHERE uid = %s"""
        self.cursor.execute(query, [user_db[UM.uid_index]])
        results = self.cursor.fetchall()

        games = []
        for result in results:
            games.append(GM.GameMapper.db_to_class(result))
        self.db.commit()
        return games
