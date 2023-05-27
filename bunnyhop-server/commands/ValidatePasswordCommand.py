from pattern_templates.Command import Command
from model.RegistrationValidator import RegistrationValidator


class ValidatePasswordCommand(Command):
    def __init__(self, password1, password2):
        self.password1 = password1
        self.password2 = password2
        self.registration_validator = RegistrationValidator()

    def execute(self):
        return self.registration_validator.validate_password(self.password1, self.password2)
