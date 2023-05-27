from typing import Protocol


class IClient(Protocol):
    def enqueue_request(self, request_type, **kwargs):
        ...

    def dequeue_response(self):
        ...

    def start(self):
        ...

    def send_request(self, request_type, kwargs):
        ...

