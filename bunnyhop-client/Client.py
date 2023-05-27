import pickle
import queue
import socket

from IClient import IClient
from Request import Request


class Client(IClient):
    def __init__(self):
        self.server_host = socket.gethostname()  # as both code is running on same pc
        self.server_port = 5000  # socket server port number

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.settimeout(1)
        self.client_socket.connect((self.server_host, self.server_port))  # connect to the server

        self.request_queue = queue.Queue()
        self.response_queue = queue.Queue(maxsize=1)

    def enqueue_request(self, request_type, **kwargs):
        self.request_queue.put([request_type, kwargs])

    def dequeue_response(self):
        print("before dequeue")
        response = self.response_queue.get()
        print("after dequeue")
        return response

    def start(self):
        try:
            while True:
                request_type, kwargs = self.request_queue.get()  # blocking
                self.send_request(request_type, kwargs)
        except KeyboardInterrupt:
            self.client_socket.close()  # close the connection

    def send_request(self, request_type, kwargs):
        request_data = kwargs

        pickled_request_data = pickle.dumps(request_data)
        pickled_request = pickle.dumps(Request(request_type, pickled_request_data))
        self.client_socket.send(pickled_request)  # send message

        data = []
        try:
            while True:
                packet = self.client_socket.recv(1024)
                print("got something")
                data.append(packet)
        except TimeoutError:
            print("got out of loop")

        pickled_response_data = (b"".join(data))
        response_data = pickle.loads(pickled_response_data)

        print(f'Received from server: {response_data}')  # show in terminal
        self.response_queue.put(response_data)
