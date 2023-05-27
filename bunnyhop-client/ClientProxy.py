import RequestType
from Client import Client
from IClient import IClient


class ClientProxy(IClient):
    def __init__(self):
        try:
            self.client = Client()
        except ConnectionRefusedError as e:
            print(e)
            print("HINT: make sure server is running.")
            exit(1)

    def enqueue_request(self, request_type, **kwargs):
        if request_type not in [
            RequestType.CREATE_GAME,
            RequestType.GET_GAMES_BY_USER,
            RequestType.CREATE_USER,
            RequestType.GET_USER_FROM_USERNAME,
            RequestType.GET_ALL_USERS,
            RequestType.UPDATE_USER,
            RequestType.DELETE_USER,
            RequestType.CHECK_NOT_ENCRYPTED_AGAINST_ENCRYPTED,
            RequestType.CHECK_CREDENTIALS_VALIDITY,
            RequestType.ENCRYPT_PASSWORD
        ]:
            print("Request Type declined by ClientProxy")
            return

        self.client.enqueue_request(request_type, **kwargs)

    def dequeue_response(self):
        self.client.dequeue_response()

    def start(self):
        self.client.start()

    def send_request(self, request_type, kwargs):
        self.client.send_request(request_type, kwargs)
