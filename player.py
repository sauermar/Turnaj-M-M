import abc
import enum

class Move(enum.Enum):
    """Výčet popisující tahy.

    Jednotlivé možnosti mají jako hodnoty dvojice "písmenka ze zadání" a indexu do matice, jak je uložená v result.py."""

    a_safe_way = ("A", 0)
    betray = ("B", 1)
    cooperate = ("C", 2)
    deceive = ("D", 3)


class Player(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        """Inicializátor. Tady si můžete vytvořit atribut(y), např. pro pamatování
        vašich či soupeřových tahů."""

    @abc.abstractmethod
    def author_name(self) -> str:
        """Metoda vracející autorovo plné jméno (jako řetězec)"""

    @abc.abstractmethod
    def next_move(self) -> Move:
        """Metoda vracející další tah jako prvek výčtu (enum-u) Move"""

    @abc.abstractmethod
    def reward(self, res):
        """Metoda volaná po každém kole.
        Informace o právě proběhlém kole jsou dostupné
        v parametru res (typu Result)"""
