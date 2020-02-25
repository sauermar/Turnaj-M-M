import random

from player import Move, Player


class RandomAC(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandomAC"

    def next_move(self):
        return random.choice([Move.a_safe_way, Move.cooperate])

    def reward(self, result):
        pass
