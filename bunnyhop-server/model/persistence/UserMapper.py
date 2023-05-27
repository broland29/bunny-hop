from User import User

uid_index = 0
username_index = 1
password_index = 2
is_admin_index = 3


class UserMapper:
    @staticmethod
    def db_to_class(user: list[str | int | bytes]) -> User:
        return User(
            uid=user[uid_index],
            username=user[username_index],
            password=user[password_index],
            is_admin=UserMapper.int_to_bool(user[is_admin_index])
        )

    @staticmethod
    def class_to_db(user: User) -> list[int | str | bytes]:
        return [
            user.uid,
            user.username,
            user.password,
            UserMapper.bool_to_int(user.is_admin)
        ]

    @staticmethod
    def int_to_bool(value: int):
        if value == 0:
            return False
        if value == 1:
            return True
        return None  # None propagates, other invalid values "discarded" (interpreted as None)

    @staticmethod
    def bool_to_int(value: bool):
        if value is True:
            return 1
        if value is False:
            return 0
        if value is None:
            return None  # None propagates - https://stackoverflow.com/questions/3914667/false-or-none-vs-none-or-false
        return None
