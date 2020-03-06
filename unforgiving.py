from player import Move, Player


class Unforgiving(Player):
    """Neodpouštějící hráč.
    Dokud nebyl zrazen (strategie B), kooperuje.
    Když je zrazen, stane se z něj neodpouštějící zrádce.
    
    Unforgiving player.
    Until he has been betrayed, always cooperates.
    As soon as he is betrayed, he betrays back and never forgives.
    """

    def __init__(self):
      
        """Zapamatujeme si, jestli nás už soupeř zradil.
        
        We remember whether the opponent ever betrayed us."""
        
        self.was_betrayed = False

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Zradíme, pokud jsme již byli zrazeni. Jinak kooperujeme.
        
        Cooperate unless you were betrayed in the past. Otherwise betray.
        """
        
        if self.was_betrayed:
            return Move.betray
        else:
            return Move.cooperate

    def reward(self, result):
        """Zapamatujeme si, pokud nás protihráč zradil.
        
        If opponent ever betrays us, we remember that.
        """
        
        if result.opp_move == Move.betray:
            self.was_betrayed = True
