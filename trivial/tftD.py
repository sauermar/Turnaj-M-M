from player import Move, Player


class TftD(Player):

    def __init__(self):
        self.last = Move.deceive
	
    def author_name(self):
        return "TitForTatD"

    def next_move(self):
        return self.last

    def reward(self, result):
        self.last = result.opp_move