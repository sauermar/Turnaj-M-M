from player import Move, Player


class AlwaysA(Player):

    def __init__(self):
        pass

    def author_name(self):
        return "AlwaysA"

    def next_move(self):
        return Move.a_safe_way

    def reward(self, result):
        pass
