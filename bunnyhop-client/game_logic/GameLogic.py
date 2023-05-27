import RequestType
from enums.CellType import CellType
from enums.GameState import GameState
from game_logic.Pattern import Pattern

from session_info.SessionInfo import SessionInfo
from Game import Game
from pattern_templates.Singleton import Singleton


class GameLogic(metaclass=Singleton):

    game_state: GameState
    time: int
    move_history: list[(int, int)]

    def __init__(self, controller):
        self.controller = controller  # todo

        self.session_info = SessionInfo()
        self.pattern = Pattern()

    @property
    def current_pattern(self):
        return self.pattern.current_pattern

    @property
    def optimal_path(self):
        return self.pattern.optimal_path

    def new_game(self):
        self.game_state = GameState.Idle
        self.time = 0
        self.pattern.reset(self.session_info.difficulty_handler.difficulty)
        self.move_history = [self.pattern.start]

    def jump(self, di, dj):
        # current position about to become old position
        i_old, j_old = self.pattern.bunny_position

        # potential positions: where user wants to jump
        i_pot = i_old + di
        j_pot = j_old + dj

        # if out of bounds, we cannot talk about cell
        if i_pot >= self.pattern.difficulty\
                or j_pot >= self.pattern.difficulty\
                or i_pot < 0\
                or j_pot < 0:
            print("Jump: out of bounds!")
            return

        # else we take the type of cell we want to jump to
        cell = self.pattern.current_pattern[i_pot][j_pot]
        # for default, let's go with no move
        i_new = i_old
        j_new = j_old

        if cell == CellType.Trap:
            print("Jump: in a trap!")
            # threading.Thread(target=playsound, args=('res/sfx/trap.mp3',), daemon=True).start()
            i_new = self.pattern.start[0]
            j_new = self.pattern.start[1]
        elif cell == CellType.Carrot:
            print("Jump: found carrot!")
            # threading.Thread(target=playsound, args=('res/sfx/carrot.mp3',), daemon=True).start()
            i_new = i_pot
            j_new = j_pot
            self.game_state = GameState.Over
            user = self.session_info.user
            if user is not None:
                game = Game(
                    uid=user.uid,
                    time=self.time,
                    difficulty=self.pattern.difficulty,
                    optimal_path_length=len(self.pattern.optimal_path),
                    actual_path_length=len(self.move_history) + 1)
                # destination added to move history only at the end of this function

                self.controller.master_controller.enqueue_request(
                    RequestType.CREATE_GAME,
                    game=game
                )
        elif cell == CellType.Empty:
            print("Jump: to empty cell!")
            # threading.Thread(target=playsound, args=('res/sfx/jump.mp3',), daemon=True).start()
            i_new = i_pot
            j_new = j_pot

        # in any case, jumping consists of leaving an empty cell behind and occupying new cell
        self.pattern.current_pattern[i_old][j_old] = CellType.Empty
        self.pattern.current_pattern[i_new][j_new] = CellType.Bunny
        self.pattern.bunny_position = (i_new, j_new)

        # keep track of jump
        self.move_history.append((i_new, j_new))

    def update_clock(self):
        self.time += 1
