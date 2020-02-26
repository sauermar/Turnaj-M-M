import random

from player import Move, Player


class RandomBD(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "RandomBD"

    def next_move(self):
        return random.choice([Move.betray, Move.deceive])

    def reward(self, result):
        pass
