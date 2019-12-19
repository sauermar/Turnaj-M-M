import abc
import enum


class Move(enum.Enum):
    a_safe_way = ("A", 0)
    betray = ("B", 1)
    cooperate = ("C", 2)
    deceive = ("D", 3)


class Player(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        """Constructor. You can create attribute(s) for remembering
        yours and/or opponent's moves here"""

    @abc.abstractmethod
    def author_name(self) -> str:
        """Returns author's name in a string"""

    @abc.abstractmethod
    def next_move(self) -> Move:
        """Returns next move as Move enum type"""

    @abc.abstractmethod
    def reward(self, res):
        """Called after each round.
        Information about the last round is available through
        the res object (of the Result type)"""
