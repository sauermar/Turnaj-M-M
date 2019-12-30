#!/usr/bin/python3
import importlib
import sys

from player import Move
from result import Result


def pick_next() -> Move:
    """Ptáme se uživatele, co chce zahrát.

    Ptáme se ho tak dlouho, dokud nevybere nějaké písmenko strategie, které je uvedeno ve výčtu Move v player.py"""
    while True:
        pick = input("Pick your next move: ")
        for m in Move:
            if m.value[0].lower() == pick.lower():
                return m

        print("pick options: A,B,C,D")


def print_result(res: Result, sc1: int, sc2: int):
    """Vypíše výsledek tahu.

    Parametry sc1 a sc2 jsou celková skóre od začátku turnaje, parametr res je poslední výsledek.
    """
    print("Your move was: {}".format(res.opp_move.value[0]))
    print("Your opponent's move was: {}".format(res.my_move.value[0]))
    print("You scored {}".format(res.get_opp_score()), ", total: {}".format(sc2))
    print("Your opponent scored {}".format(res.get_my_score()), ", total: {}".format(sc1))
    print("--------------------------->")


def print_score(sc1: int, sc2: int):
    """Vypíše závěrečné výsledky."""
    print("THE GAME HAS ENDED")
    print("--------------------------->")
    print("You scored in total {} points.".format(sc2))
    print("AI player scored in total {} points.".format(sc1))


def main():
    # Chceme správný počet parametrů správných typů
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Argument error")
        exit(1)

    try:
        iterations = int(sys.argv[2])
    except IndexError:
        iterations = 10
    except ValueError:
        print("The second argument should be a number!")
        exit(1)

    # Načteme modul se strategií (objekt strategie se uloží do s1)
    try:
        path = sys.argv[1]
        strategy_module, strategy_class_name = path.rsplit('.', 1)
        strategy1 = importlib.import_module(strategy_module)
        s1 = getattr(strategy1, strategy_class_name)()
    except IOError:
        print('An error occurred trying to read the file.')
        exit(1)
    except ImportError:
        print("NO module found")
        exit(1)

    # Inicializace skóre obou hráčů

    sc1 = 0
    sc2 = 0

    # Provedeme `iterations` kol
    for i in range(iterations):
        # Zeptáme se hráčů, co hrají
        move1 = s1.next_move()
        move2 = pick_next()
        # Vyhodnotíme kolo
        res = Result(move1, move2)
        sc1 += res.get_my_score()
        sc2 += res.get_opp_score()
        # Sdělíme oběma hráčům, co se stalo
        print_result(res, sc1, sc2)
        s1.reward(res)

    # Vypíšeme závěrečné výsledky
    print_score(sc1, sc2)


if __name__ == "__main__":
    main()
