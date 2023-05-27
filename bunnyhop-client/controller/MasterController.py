from enums.FrameType import FrameType
from session_info.SessionInfo import SessionInfo

from controller.AdminController import AdminController
from controller.GameController import GameController
from controller.LoginController import LoginController
from controller.ProfileController import ProfileController
from controller.RegisterController import RegisterController
from controller.WelcomeController import WelcomeController
from controller.SettingsController import SettingsController

from view.frame.MasterFrame import MasterFrame


class MasterController:
    def __init__(self, app_controller, app_window):
        self.app_controller = app_controller
        self.master_frame = MasterFrame(app_window)

        self.controllers = {
            FrameType.AdminFrame:       AdminController(self),
            FrameType.GameFrame:        GameController(self),
            FrameType.LoginFrame:       LoginController(self),
            FrameType.RegisterFrame:    RegisterController(self),
            FrameType.ProfileFrame:     ProfileController(self),
            FrameType.SettingsFrame:    SettingsController(self),
            FrameType.WelcomeFrame:     WelcomeController(self),
        }
        self.frames = {
            FrameType.AdminFrame:       self.controllers[FrameType.AdminFrame].admin_frame,
            FrameType.GameFrame:        self.controllers[FrameType.GameFrame].game_frame,
            FrameType.LoginFrame:       self.controllers[FrameType.LoginFrame].login_frame,
            FrameType.RegisterFrame:    self.controllers[FrameType.RegisterFrame].register_frame,
            FrameType.ProfileFrame:     self.controllers[FrameType.ProfileFrame].profile_frame,
            FrameType.SettingsFrame:    self.controllers[FrameType.SettingsFrame].settings_frame,
            FrameType.WelcomeFrame:     self.controllers[FrameType.WelcomeFrame].welcome_frame,
        }

        self.session_info = SessionInfo()
        for frame in self.controllers.values():
            self.session_info.language_handler.attach(frame)
        self.session_info.language_handler.notify()  # to fill initial values

        for f in self.frames.values():
            f.grid(row=0, column=0, sticky="nsew")
        self.active_frame = FrameType.WelcomeFrame

    @property
    def active_frame(self):
        return self._active_frame

    @active_frame.setter
    def active_frame(self, value: FrameType):
        frame = self.frames[value]  # extract frame
        controller = self.controllers[value]

        setup = getattr(controller, "setup", None)
        if callable(setup):
            setup()
        else:
            print("Frame has no setup method!")

        frame.tkraise()
        self._active_frame = value

    def enqueue_request(self, request_type, **kwargs):
        return self.app_controller.enqueue_request(request_type, **kwargs)
