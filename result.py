from player import Move


class Result:
    """
    Výplatní matice prvního hráče (pro druhého hráče se prohodí indexy, protože je bimatice hry symetrická)
    
    The payoff matrix for the first player (swap indexes for the second player, the bimatrix is symmetric)
    """
    rewards = ((6, 3, 3, 3),
               (1, 2, 8, 8),
               (1, 0, 10, 1),
               (1, 0, 18, 4))

    def __init__(self, move1: Move, move2: Move):
        """
        Inicializátor, umožní získat informace o předchozím tahu pomocí atributů instancí.
        
        Class constructor, allows to get the previous move values through instance attributes
        """
        if (not isinstance(move1,Move)) or (not isinstance(move2,Move)):
            raise ValueError("Can't create result object from {} and {}".format(type(move1),type(move2)))
        self.my_move = move1
        self.opp_move = move2

    def get_my_score(self):
        """
        Vrací počet bodů, které jste získali v posledním kole.
        
        Returns number of your scored points in last round.
        """
        return self.rewards[self.my_move.value[1]][self.opp_move.value[1]] # Tenhle řádek je jen přístup do matice výše podle indexů, které jsou uložené ve výčtu jednotlivých strategií v souboru player.py

    def get_opp_score(self):
        """
        Vrací počet bodů, které protihráč získal v posledním kole.
        
        Returns number of opponent's scored points in last round.
        """
        return self.rewards[self.opp_move.value[1]][self.my_move.value[1]] # Stejné jako v get_my_score s prohozenými indexy
