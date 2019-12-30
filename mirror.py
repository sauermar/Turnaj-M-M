import random

from player import Move, Player


class Mirror(Player):
    """Hráč "Zrcadlo".

    Začne kooperující strategií (C).
    V dalších tazích vybírá náhodně jednu z posledních tří strategií protihráče.
    """

    def __init__(self):
        """Budeme si pamatovat všechny soupeřovy tahy v poli."""
        self.opponent_moves = []

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Vybere náhodně jednu z posl. tří tahů protihráče."""
        if not self.opponent_moves:  # Je první kolo, zatím neproběhly žádné tahy.
            return Move.cooperate
        else:
            last_moves = self.opponent_moves[-3:]  # Vezmeme poslední tři tahy z našeho pole
            return random.choice(last_moves)

    def reward(self, result):
        """Zaznamená proběhlý tah do pole."""
        self.opponent_moves.append(result.opp_move)
