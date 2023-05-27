from pattern_templates.Command import Command
from model.RegistrationValidator import RegistrationValidator


class ValidateUsernameCommand(Command):
    def __init__(self, username):
        self.username = username
        self.registration_validator = RegistrationValidator()

    def execute(self):
        return self.registration_validator.validate_username(self.username)
