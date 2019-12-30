from player import Move, Player


class AlwaysCooperate(Player):
    """Hráč vždy kooperující (strategie C)."""

    def __init__(self):
        """Nepotřebujeme si nic pamatovat."""
        pass

    def author_name(self):
        return "Marketa"

    def next_move(self):
        """Budeme kooperovat, ať se děje co se děje."""
        return Move.cooperate

    def reward(self, result):
        """Jak to dopadlo nás nezajímá."""
        pass
