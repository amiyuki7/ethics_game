import random
from curses import window
from math import floor

from dataclasses import dataclass, field

from .ctx import (
    Side,
    player,
    Log,
)
from .globals import Colors
from .globals import Globals as G
from .lib.parser import Tile


@dataclass(repr=False, eq=False)
class EnemyResult:
    enemy: Tile | None = field(default=None)
    pos: tuple[int, int] | None = field(default=None)
    name: str | None = field(default=None)
    question: str | None = field(default=None)
    answer: str | None = field(default=None)


# class EnemyResult:
#     # Enemy object
#     def __init__(
#         self,
#         enemy: Tile | None = None,
#         pos: tuple[int, int] | None = None,
#         name: str | None = None,
#         question: str | None = None,
#         answer: str | None = None,
#     ) -> None:
#         self.enemy = enemy
#         self.pos = pos
#         self.name = name
#         self.question = question
#         self.answer = answer


# GameObject
class Game:
    """The naming might be confused with GameWrapper in ./app.py , but this is actually the rendered game"""

    def __init__(
        self, pad: window, game_map: list[list[Tile]], y_offset: int = 0, x_offset: int = 0
    ) -> None:
        self.pad = pad

        self.game_map = game_map
        self.y_offset = y_offset or player.rel_y
        self.x_offset = x_offset or player.rel_x

        self.enemy: EnemyResult | None = None

        self.redraw()

        self.render()

    def redraw(self) -> None:
        self.pad.clear()
        for row in self.game_map:
            for col in row:
                self.pad.addch(col.char, col.color)
            self.pad.addch("\n")

    def render(self) -> None:
        self.pad.refresh(
            self.y_offset,
            self.x_offset,
            G.padding_height + 1,
            G.padding_width + 1,
            G.padding_height + G.game_height - 2,
            G.padding_width + G.game_width - 2,
        )

    def is_block(self, y, x) -> bool:
        """
        Check if a specific tile cannot be passed
        """

        match self.game_map[y][x].id:
            # Walls, enemies, locks
            case t if t in list(range(21)) + [22, 32]:
                return True
            case _:
                return False

    def check_enemy(self, y, x) -> EnemyResult:
        """
        Check if there is an enemy adjacent to a specific tile
        """

        up = self.game_map[y - 1][x]
        down = self.game_map[y + 1][x]
        left = self.game_map[y][x - 1]
        right = self.game_map[y][x + 1]

        tiles = [up, down, left, right]
        ids = [up.id, down.id, left.id, right.id]

        try:
            enemy_idx = ids.index(22)
        except ValueError:
            return EnemyResult()

        enemy = tiles[enemy_idx]

        # Normalised coordinates of enemy
        ny = nx = 0
        if enemy == up:
            ny, nx = player.y - 1, player.x
        if enemy == down:
            ny, nx = player.y + 1, player.x
        if enemy == right:
            ny, nx = player.y, player.x + 1
        if enemy == left:
            ny, nx = player.y, player.x - 1

        # Map coordinates of the enemy tile
        y = [self.game_map.index(r) for r in self.game_map if enemy in r][0]
        x = [r.index(enemy) for r in self.game_map if enemy in r][0]

        from .data.game_items import Enemies

        enemy_data = Enemies[(ny, nx)]

        return EnemyResult(
            enemy, (y, x), enemy_data["name"], enemy_data["question"], enemy_data["answer"]
        )

    def remove_tile(self, y, x) -> None:
        self.game_map[y][x] = Tile(".", False, Colors.PATH, 21, "PATH")
        self.redraw()

    def interact_tile(self) -> None:
        """
        Handles game interactions when the E key is pressed
        """
        y, x = player.map_y, player.map_x
        match self.game_map[y][x].id:
            case 34:  # FIGHT
                if self.game_map[player.map_y][player.map_x].id != 34:
                    return

                enemy = self.check_enemy(player.map_y, player.map_x)
                if not enemy.enemy:
                    return

                self.enemy = enemy

                Log("━━━━━━━━━━━━━━━━━━━━━━━")
                Log(f"{enemy.name}")
                Log(f"{enemy.question}")
                Log("━━━━━━━━━━━━━━━━━━━━━━━")
                Side().toggle_prompt()  # type: ignore

            case _:
                pass

    # All these displacement functions shift the rendered map around the player, giving the illusion that the
    # player is moving around the map
    def displace_up(self) -> None:
        if self.y_offset - 1 > G.padding_height and not self.is_block(
            player.map_y - 1, player.map_x
        ):
            self.y_offset -= 1
            player.y -= 1

    def displace_down(self) -> None:
        if self.y_offset < 256 + G.padding_height and not self.is_block(
            player.map_y + 1, player.map_x
        ):
            self.y_offset += 1
            player.y += 1

    def displace_left(self) -> None:
        if self.x_offset - 1 > G.padding_width and not self.is_block(
            player.map_y, player.map_x - 1
        ):
            self.x_offset -= 1
            player.x -= 1

    def displace_right(self) -> None:
        if self.x_offset < 256 + G.padding_width and not self.is_block(
            player.map_y, player.map_x + 1
        ):
            self.x_offset += 1
            player.x += 1
