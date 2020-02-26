import random

from player import Move, Player


class RandomAB(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandomAB"

    def next_move(self):
        return random.choice([Move.a_safe_way, Move.betray])

    def reward(self, result):
        pass
