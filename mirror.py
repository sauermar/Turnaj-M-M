import random

from player import Move, Player


class Mirror(Player):
    """Hráč "Zrcadlo".
    Začne kooperující strategií (C).
    V dalších tazích vybírá náhodně jednu z posledních tří strategií protihráče.
	
	Mirror player.
	Start with a safe_way.
    In following turns, choose randomly one of last 3 moves our opponent made.
    """

    def __init__(self):
        """Budeme si pamatovat všechny soupeřovy tahy v poli.
		
		We remember all our opponent moves.
		"""
        self.opponent_moves = []

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Vybere náhodně jednu z posl. tří tahů protihráče.
		
		Choose randomly one of last 3 moves our opponent made.
		"""
        if not self.opponent_moves:  # Je první kolo, zatím neproběhly žádné tahy.   It's first round of the game, there has been no moves.
            return Move.cooperate
        else:
            last_moves = self.opponent_moves[-3:]  # Vezmeme poslední tři tahy z našeho pole.   We select last three moves from the list.
            return random.choice(last_moves)

    def reward(self, result):
        """Zaznamená proběhlý tah do pole.
		
		Records the history of the game.
		"""
        self.opponent_moves.append(result.opp_move)
