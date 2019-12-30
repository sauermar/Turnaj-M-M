from player import Move, Player


class ScoreCounting(Player):
    """Hráč počítající skóre.

    Začne kooperací.
    V dalších tazích kooperuje, pokud v aktuálním souboji získal aspoň tolik bodů, jako protihráč.
    Jinak je zrádce (strategie B)
    """

    def __init__(self):
        """Pamatujeme si, kolik už kdo získal bodů."""
        self.my_score = 0
        self.opponent_score = 0

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Zradíme, pokud prohráváme; jinak kooperujeme."""
        if self.my_score < self.opponent_score:
            return Move.betray
        else:
            return Move.cooperate

    def reward(self, result):
        """Připočteme právě získané body do celkového skóre"""
        self.my_score += result.get_my_score()
        self.opponent_score += result.get_opp_score()
