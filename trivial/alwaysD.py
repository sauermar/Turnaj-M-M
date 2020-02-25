from player import Move, Player


class AlwaysD(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "AlwaysD"

    def next_move(self):
        return Move.deceive

    def reward(self, result):
        pass
