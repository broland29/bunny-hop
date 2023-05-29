import mysql.connector


class DatabaseConnector:
    def __init__(self, database):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="0000",
            database=database
        )
        self.cursor = self.db.cursor(buffered=True)
        # https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone
        # else error when submit twice
