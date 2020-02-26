import random

from player import Move, Player


class RandomCD(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandomCD"

    def next_move(self):
        return random.choice([Move.cooperate, Move.deceive])

    def reward(self, result):
        pass
