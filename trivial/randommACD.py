import random

from player import Move, Player


class RandommACD(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandommACD"

    def next_move(self):
        return random.choice([Move.a_safe_way, Move.cooperate, Move.deceive])

    def reward(self, result):
        pass
