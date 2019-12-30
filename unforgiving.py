from player import Move, Player


class Unforgiving(Player):

    """Neodpouštějící hráč.

    Dokud nebyl zrazen (strategie B), kooperuje.
    Když je zrazen, stane se z něj neodpouštějící zrádce
    """

    def __init__(self):
      
        """Zapamatujeme si, jestli nás už soupeř zradil."""
        
        self.was_betrayed = False

    def author_name(self):
        return "Honza"

    def next_move(self):

        """Zradíme, pokud jsme již byli zrazeni. Jinak kooperujeme"""
        
        if self.was_betrayed:
            return Move.betray
        else:
            return Move.cooperate

    def reward(self, result):

        """Zapamatujeme si, pokud nás protihráč zradil."""
        
        if result.opp_move == Move.betray:
            self.was_betrayed = True
