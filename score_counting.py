from player import Move, Player


class ScoreCounting(Player):
    """Hráč počítající skóre.
    Začne kooperací.
    V dalších tazích kooperuje, pokud v aktuálním souboji získal aspoň tolik bodů, jako protihráč.
    Jinak je zrádce (strategie B)
    
    Score-counting player.
    Start with cooperate.
    In following turns, chooses cooperate if he has score greater or equal to his opponent's.
    Otherwise chooses betray.
    """

    def __init__(self):
        """Pamatujeme si, kolik už kdo získal bodů.
        
        We remember our overall scores.
        """
        self.my_score = 0
        self.opponent_score = 0

    def author_name(self):
        return "Honza"

    def next_move(self):
        """Zradíme, pokud prohráváme; jinak kooperujeme.
        
        Choose betrayal if you are loosing. Otherwise cooperate.
        """
        if self.my_score < self.opponent_score:
            return Move.betray
        else:
            return Move.cooperate

    def reward(self, result):
        """Připočteme právě získané body do celkového skóre.
        
        Add score from the last round to overall scores.
        """
        self.my_score += result.get_my_score()
        self.opponent_score += result.get_opp_score()
