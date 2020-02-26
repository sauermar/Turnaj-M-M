import random

from player import Move, Player


class RandomAD(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandomAD"

    def next_move(self):
        return random.choice([Move.a_safe_way, Move.deceive])

    def reward(self, result):
        pass
