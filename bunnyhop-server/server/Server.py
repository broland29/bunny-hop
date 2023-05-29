import pickle
import socket

import RequestType
from user_domain.commands.ValidateCredentialsCommand import ValidateCredentialsCommand
from user_domain.commands.ValidatePasswordCommand import ValidatePasswordCommand
from user_domain.commands.ValidateUsernameCommand import ValidateUsernameCommand
from game_domain.model.persistence.GameDAO import GameDAO
from user_domain.model.persistence.UserDAO import UserDAO
from services.SecurityService import SecurityService


class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5000

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))

        self.game_dao = GameDAO()
        self.user_dao = UserDAO()
        self.password_manager = SecurityService()

    def start(self):
        self.server_socket.listen(2)  # maximum two clients
        conn, address = self.server_socket.accept()
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            pickled_request = conn.recv(1024)
            if not pickled_request:
                break
            request = pickle.loads(pickled_request)
            request_type = request.request_type
            data = pickle.loads(request.pickled_data)

            print(f"Received from client {address} request_type {request_type} and data {data}")
            match request_type:
                case RequestType.CREATE_GAME:
                    self.game_dao.create_game(
                        data["game"]
                    )
                    # data = Game(gid=1, uid=1, time=12, difficulty=5, optimal_path_length=5, actual_path_length=5)
                    response_data = None
                case RequestType.GET_GAMES_BY_USER:
                    response_data = self.game_dao.get_games_by_user(
                        data["user"]
                    )
                case RequestType.CREATE_USER:
                    self.user_dao.create_user(
                        data["user"]
                    )
                    response_data = None
                case RequestType.GET_USER_FROM_USERNAME:
                    response_data = self.user_dao.get_user_from_username(
                        data["username"]
                    )
                case RequestType.GET_ALL_USERS:
                    response_data = self.user_dao.get_all_users()
                case RequestType.UPDATE_USER:
                    self.user_dao.update_user(
                        data["old_user"],
                        data["new_user"]
                    )
                    response_data = None
                case RequestType.DELETE_USER:
                    self.user_dao.delete_user(
                        data["user"]
                    )
                    response_data = None
                case RequestType.CHECK_NOT_ENCRYPTED_AGAINST_ENCRYPTED:
                    response_data = self.password_manager.check_not_encrypted_against_encrypted(
                        data["not_encrypted"],
                        data["encrypted"])
                case RequestType.CHECK_CREDENTIALS_VALIDITY:
                    response_data = ValidateCredentialsCommand(
                        data["username"],
                        data["password1"],
                        data["password2"]
                    ).execute()
                case RequestType.ENCRYPT_PASSWORD:
                    response_data = self.password_manager.encrypt_password(
                        data["password"]
                    )
                case RequestType.VALIDATE_USERNAME:
                    response_data = ValidateUsernameCommand(
                        data["username"]
                    ).execute()
                case RequestType.VALIDATE_PASSWORD:
                    response_data = ValidatePasswordCommand(
                        data["password1"],
                        data["password2"]
                    ).execute()
                case _:
                    print(f"Unexpected request type {request_type}, sending None")
                    response_data = None

            pickled_response = pickle.dumps(response_data)
            conn.send(pickled_response)  # send data to the client
            print("sent response")

        conn.close()  # close the connection
