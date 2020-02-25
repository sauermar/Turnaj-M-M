from player import Move, Player


class AlwaysC(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "AlwaysC"

    def next_move(self):
        return Move.cooperate

    def reward(self, result):
        pass
