from player import Move, Player


class AlwaysB(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "AlwaysB"

    def next_move(self):
        return Move.betray

    def reward(self, result):
        pass
