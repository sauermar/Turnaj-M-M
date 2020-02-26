from player import Move, Player


class TftC(Player):

    def __init__(self):
        self.last = Move.cooperate
	
    def author_name(self):
        return "TitForTatC"

    def next_move(self):
        return self.last

    def reward(self, result):
        self.last = result.opp_move