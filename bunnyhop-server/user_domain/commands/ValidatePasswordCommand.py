from user_domain.commands.Command import Command
from services.ValidationService import ValidationService


class ValidatePasswordCommand(Command):
    def __init__(self, password1, password2):
        self.password1 = password1
        self.password2 = password2
        self.registration_validator = ValidationService()

    def execute(self):
        return self.registration_validator.validate_password(self.password1, self.password2)
