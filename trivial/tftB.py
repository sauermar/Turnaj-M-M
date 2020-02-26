from player import Move, Player


class TftB(Player):

    def __init__(self):
        self.last = Move.betray
	
    def author_name(self):
        return "TitForTatB"

    def next_move(self):
        return self.last

    def reward(self, result):
        self.last = result.opp_move