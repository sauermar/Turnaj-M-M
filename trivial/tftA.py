from player import Move, Player


class TftA(Player):

    def __init__(self):
        self.last = Move.a_safe_way
	
    def author_name(self):
        return "TitForTatA"

    def next_move(self):
        return self.last

    def reward(self, result):
        self.last = result.opp_move