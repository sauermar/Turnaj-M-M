import random

from player import Move, Player


class RandommABD(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandommABD"

    def next_move(self):
        return random.choice([Move.a_safe_way, Move.betray, Move.deceive])

    def reward(self, result):
        pass
