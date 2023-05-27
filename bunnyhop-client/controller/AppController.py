import threading
from time import sleep

from Client import Client
from ClientProxy import ClientProxy
from controller.MasterController import MasterController
from view.AppWindow import AppWindow


class AppController:
    def __init__(self):
        self.client = ClientProxy()
        threading.Thread(target=self.client.start, args=(), daemon=True).start()

        self.app_window = AppWindow()
        self.master_controller = MasterController(self, self.app_window)
        self.app_window.mainloop()

    def enqueue_request(self, request_type, **kwargs):
        self.client.enqueue_request(request_type, **kwargs)
        return self.client.dequeue_response()
