import random

from player import Move, Player


class Randommm(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "Randommm"

    def next_move(self):
        return random.choice([Move.a_safe_way, Move.betray, Move.cooperate, Move.deceive])

    def reward(self, result):
        pass
