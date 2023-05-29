import re

from user_domain.model.persistence.UserDAO import UserDAO


# methods return a tuple (boolean, message) (parentheses not needed at return)
class ValidationService:

    @staticmethod
    def validate(username, password1, password2):
        if len(username) == 0 or len(password1) == 0 or len(password2) == 0:
            return False, "message_label_empty_fields"

        valid_username, username_message = ValidationService.validate_username(username)
        if not valid_username:
            return False, username_message

        valid_password, password_message = ValidationService.validate_password(password1, password2)
        if not valid_password:
            return False, password_message

        return True, "message_label_successful_validate"

    @staticmethod
    def validate_username(username):
        if len(username) < 3:
            return False, "message_label_short_username"
        if len(username) > 10:
            return False, "message_label_long_username"
        if not bool(re.match('^[a-zA-Z0-9]+$', username)):
            return False, "message_label_bad_username"

        # check if username not taken
        user_dao = UserDAO()
        potential_user = user_dao.get_user_from_username(username)
        if potential_user is not None:
            return False, "message_label_taken_username"
        return True, "message_label_successful_validate_username"

    @staticmethod
    def validate_password(password1, password2):
        if password1 != password2:
            return False, "message_label_password_mismatch"
        if len(password1) < 3:
            return False, "message_label_short_password"
        if len(password1) > 10:
            return False, "message_label_long_password"
        if not bool(re.match('^[a-zA-Z0-9]+$', password1)):
            return False, "message_label_bad_password"
        return True, "message_label_successful_validate_password"
