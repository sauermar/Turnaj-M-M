import abc
import enum

class Move(enum.Enum):
    """Výčet popisující tahy.
    
    This enum defines existing moves.
    """

    a_safe_way = ("A", 0)
    betray = ("B", 1)
    cooperate = ("C", 2)
    deceive = ("D", 3)


class Player(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        """Inicializátor. Tady si můžete vytvořit atribut(y), např. pro pamatování
        vašich či soupeřových tahů.
        
        Initializer. You can create attribute(s), e.g. for remembering
        yours and/or opponent's moves here.
        """

    @abc.abstractmethod
    def author_name(self) -> str:
        """Metoda vracející autorovo plné jméno (jako řetězec)
        
        Returns author's name in a string
        """

    @abc.abstractmethod
    def next_move(self) -> Move:
        """Metoda vracející další tah jako prvek výčtu (enum-u) Move
        
        Returns next move as Move enum type
        """

    @abc.abstractmethod
    def reward(self, res):
        """Metoda volaná po každém kole.
        Informace o právě proběhlém kole jsou dostupné
        v parametru res (typu Result)
        
        Called after each round.
        Information about the last round is available through
        the res object (of the Result type)
        """
