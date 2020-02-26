import random

from player import Move, Player


class RandomBC(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandomBC"

    def next_move(self):
        return random.choice([Move.betray, Move.cooperate])

    def reward(self, result):
        pass
