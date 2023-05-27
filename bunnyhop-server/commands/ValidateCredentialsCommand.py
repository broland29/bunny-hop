from pattern_templates.Command import Command
from model.RegistrationValidator import RegistrationValidator


class ValidateCredentialsCommand(Command):
    def __init__(self, username, password1, password2):
        self.username = username
        self.password1 = password1
        self.password2 = password2
        self.registration_validator = RegistrationValidator()

    def execute(self):
        return self.registration_validator.validate(self.username, self.password1, self.password2)
