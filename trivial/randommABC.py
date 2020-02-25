import random

from player import Move, Player


class RandommABC(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandommABC"

    def next_move(self):
        return random.choice([Move.a_safe_way, Move.betray, Move.cooperate])

    def reward(self, result):
        pass
