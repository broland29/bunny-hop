from database_connector.DatabaseConnector import DatabaseConnector
from User import User
from user_domain.model.persistence.UserMapper import UserMapper, uid_index, username_index, password_index, is_admin_index
from services.SecurityService import SecurityService


class UserDAOException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserDAO:
    def __init__(self, database="bunnyhop"):
        dc = DatabaseConnector(database)
        self.db = dc.db
        self.cursor = dc.cursor
        self.password_manager = SecurityService()

    # inserts a user into the database based on input user object
    def create_user(self, user: User):
        if user is None:
            raise UserDAOException("User not provided (None)!")
        if user.username is None:
            raise UserDAOException("Username not provided!")
        if user.password is None:
            raise UserDAOException("Password not provided!")
        if user.is_admin is None:
            raise UserDAOException("Is Admin not provided!")

        user_db = UserMapper.class_to_db(user)
        query = """INSERT INTO user (username, password, is_admin)
                   VALUES (%s, %s, %s)"""
        self.cursor.execute(query, [
            user_db[username_index],
            user_db[password_index],
            user_db[is_admin_index]])
        self.db.commit()

    # https://stackoverflow.com/questions/56869778/how-to-fix-mysql-select-command-giving-wrong-result-after-the-update-in-another
    # notice commit, even though reading and not updating
    # used for example when logging: first to check if exists, then to check if password is correct
    def get_user_from_username(self, username: str):
        query = """SELECT *
                     FROM user
                    WHERE username = %s"""
        self.cursor.execute(query, [username])
        result = self.cursor.fetchone()
        self.db.commit()

        if self.cursor.rowcount == 0:
            return None
        else:
            return UserMapper.db_to_class(result)

    # used for example in admin frame
    def get_all_users(self):
        query = """SELECT *
                     FROM user"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        users = []
        for result in results:
            users.append(UserMapper.db_to_class(result))
        return users

    def update_user(self, old_user: User, new_user: User):
        if old_user is None:
            raise UserDAOException("Old user not provided (None)!")
        if new_user is None:
            raise UserDAOException("New user not provided (None)!")
        old_user_db = UserMapper.class_to_db(old_user)
        new_user_db = UserMapper.class_to_db(new_user)

        #print(f"old: {old_user_db}")
        #print(f"new: {new_user_db}")
        #print(new_user_db[is_admin_index] is None)

        uid = old_user_db[uid_index] if new_user_db[uid_index] is None else new_user_db[uid_index]
        username = old_user_db[username_index] if new_user_db[username_index] is None else new_user_db[username_index]
        password = old_user_db[password_index] if new_user_db[password_index] is None else new_user_db[password_index]
        is_admin = old_user_db[is_admin_index] if new_user_db[is_admin_index] is None else new_user_db[is_admin_index]
        #print(is_admin)

        query = """UPDATE user
                      SET username=%s, password=%s, is_admin=%s
                    WHERE uid=%s"""
        self.cursor.execute(query, [username, password, is_admin, uid])
        self.db.commit()

    def delete_user(self, user: User):
        if user is None:
            raise UserDAOException("User not provided (None)!")
        if user.uid is None:
            raise UserDAOException("UID not provided!")
        user_db = UserMapper.class_to_db(user)
        query = """DELETE FROM user
                    WHERE uid = %s"""
        self.cursor.execute(query, [user_db[uid_index]])
        self.db.commit()
