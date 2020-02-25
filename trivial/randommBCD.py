import random

from player import Move, Player


class RandommBCD(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandommBCD"

    def next_move(self):
        return random.choice([Move.betray, Move.cooperate, Move.deceive])

    def reward(self, result):
        pass
