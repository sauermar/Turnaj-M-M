from player import Player
from player import Move


class AlwaysDeceive(Player):
    def __init__(self):
        pass

    def author_name(self):
        return "Martin"

    def next_move(self):
        return Move.deceive

    def reward(self, result):
        pass
