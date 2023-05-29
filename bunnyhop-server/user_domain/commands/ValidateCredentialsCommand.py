from user_domain.commands.Command import Command
from services.ValidationService import ValidationService


class ValidateCredentialsCommand(Command):
    def __init__(self, username, password1, password2):
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.registration_validator = ValidationService()

    def execute(self):
        return self.registration_validator.validate(self.username, self.password1, self.password2)
