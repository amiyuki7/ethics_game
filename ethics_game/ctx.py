from collections import deque
from curses import A_BOLD, window
from enum import Enum, auto
from getpass import getuser


from .globals import Colors
from .globals import Globals as G
from .lib.singleton import singleton


class Player:
    """
    Player class to keep track of all the player state
    """

    def __init__(self, y: int, x: int) -> None:
        self.__y = y
        self.__x = x
        self.hp = 5
        self.progress = 0

        self.rel_y = y + G.padding_height
        self.rel_x = x + G.padding_width
        self.map_y = y + G.center_y - 1
        self.map_x = x + G.center_x - 1

    @property
    def y(self) -> int:
        return self.__y

    @property
    def x(self) -> int:
        return self.__x

    @y.setter
    def y(self, y2) -> None:
        self.__y = y2
        self.rel_y = y2 + G.padding_height
        self.map_y = y2 + G.center_y - 1

    @x.setter
    def x(self, x2) -> None:
        self.__x = x2
        self.rel_x = x2 + G.padding_height
        self.map_x = x2 + G.center_x - 1


player = Player(176, 61)

##### EVERYTHING TO DO WITH THE SIDE #####


class SideState(Enum):
    default = auto()
    console = auto()
    prompt = auto()


@singleton
class Side:
    """
    Singleton object used for keeping track of the UI on the side pad, and some temporary state
    """

    def __init__(self, pad: window, stdscr: window) -> None:
        self.pad = pad
        self.pad.bkgd(" ", Colors.WALL)

        self.text: str = ""
        self.state: SideState = SideState.default
        self.previous_state: SideState = SideState.default

        # Game Console logging
        self.log_buffer: deque[str] = deque()
        self.prompt_buffer: str = ""

        self.max_log_length: int = G.game_height - 2 - 7
        self.max_prompt_length: int = G.padding_width - 4 - 18

        self.stdscr = stdscr

    def draw_stats(self) -> None:
        """
        Draws the UI for the main side page
        """
        draw = self.pad.addstr
        user = getuser()
        name = user if len(user) <= G.padding_width - 4 else user[: G.padding_width - 7] + "..."

        self.pad.clear()

        draw(f"{name}\n\n", A_BOLD)

        draw(f"\n\nPlayer Y: ", A_BOLD)
        draw(f"{player.y}")
        draw(f"\nPlayer X: ", A_BOLD)
        draw(f"{player.x}")
        draw(f"\nHP: ", A_BOLD)
        draw(f"{player.hp} / 5")
        draw(f"\nProgress: ", A_BOLD)
        draw(f"{player.progress} / 11")

    def draw_console(self, prompt: bool) -> None:
        """
        Draws the UI for the console/prompt page
        """
        draw = self.pad.addstr

        self.pad.clear()

        if not prompt:
            draw("~~~CONSOLE/LOG~~~\n\n")

            for t in self.log_buffer:
                draw(f"{t}\n")
        else:
            draw("~~~CONSOLE/PROMPT~~~\n\n")

            for t in self.log_buffer:
                draw(f"{t}\n")

            extra_lines = self.max_log_length - len(self.log_buffer)
            for _ in range(extra_lines + 2):
                draw(f"\n")

            draw("COMMAND:\n", Colors.HEAL)
            draw(self.prompt_buffer, Colors.HEAL)

    def log(self, t: str) -> None:
        """
        Appends to the log buffer queue. Pops the earliest element in the queue if there is text overflow
        """
        if len(self.log_buffer) > self.max_log_length:
            raise Exception("Log buffer length is over the max space")

        for line in t.split("<BR>"):
            max_line_length = G.padding_width - 5
            chunks = [line[i : i + max_line_length] for i in range(0, len(line), max_line_length)]

            for chunk in chunks:
                self.log_buffer.append(chunk)

                if len(self.log_buffer) == self.max_log_length:
                    self.log_buffer.popleft()

            # self.log_buffer.append(line)

    def toggle_console(self) -> None:
        self.state = SideState.console if self.state != SideState.console else SideState.default

    def toggle_prompt(self) -> None:
        # Can only toggle the prompt whne in console mode
        self.state = SideState.prompt

    def render(self) -> None:
        match self.state:
            case SideState.default:
                self.draw_stats()
            case SideState.console:
                self.draw_console(prompt=False)
            case SideState.prompt:
                self.draw_console(prompt=True)

        self.pad.refresh(
            0,
            0,
            G.padding_height + 1,
            2,
            G.padding_height + G.game_height - 2,
            G.padding_width - 3,
        )


def Log(s: str) -> None:
    Side().log(s)  # type: ignore
