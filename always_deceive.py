from player import Move, Player


class AlwaysDeceive(Player):
    """Hráč vždy klamající (strategie D).
    
    Always-deceiving player (strategy D).
    """
    
    def __init__(self):
        """Nepotřebujeme si nic pamatovat.
        
        We don't need to store anything.
        """
        pass

    def author_name(self):
        return "Martin"

    def next_move(self):
        """Budeme klamat, ať se děje co se děje.
        
        We deceive no matter what.
        """
        return Move.deceive

    def reward(self, result):
        """Jak to dopadlo nás nezajímá.
        
        We don't care what the result was.
        """
        pass
