from player import Move, Player


class AlwaysCooperate(Player):
    """Hráč vždy kooperující (strategie C).
	
	Always-cooperating player (strategy C).
	"""

    def __init__(self):
        """Nepotřebujeme si nic pamatovat.
		
		We don't need to store anything.
		"""
        pass

    def author_name(self):
        return "Marketa"

    def next_move(self):
        """Budeme kooperovat, ať se děje co se děje.
		
		We cooperate no matter what.
		"""
        return Move.cooperate

    def reward(self, result):
        """Jak to dopadlo nás nezajímá.
		
		We don't care what the result was.
		"""
        pass
