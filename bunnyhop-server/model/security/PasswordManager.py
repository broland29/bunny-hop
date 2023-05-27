import bcrypt


class PasswordManager:
    @staticmethod
    def encrypt_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def check_not_encrypted_against_encrypted(not_encrypted, encrypted):
        return bcrypt.checkpw(not_encrypted.encode('utf-8'), encrypted.encode('utf-8'))
