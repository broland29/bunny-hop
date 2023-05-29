from user_domain.commands.Command import Command
from services.ValidationService import ValidationService


class ValidateUsernameCommand(Command):
    def __init__(self, username):
        self.username = username
        self.registration_validator = ValidationService()

    def execute(self):
        return self.registration_validator.validate_username(self.username)
