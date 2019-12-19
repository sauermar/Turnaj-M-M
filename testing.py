#!/usr/bin/python3
import importlib
import sys

from player import Move
from result import Result


def pick_next():
    while True:
        pick = input("Pick your next move: ")
        for m in Move:
            if m.value[0].lower() == pick.lower():
                return m

        print("pick options: A,B,C,D")


def print_result(res, sc1, sc2):
    print("Your move was: {}".format(res.opp_move.value[0]))
    print("Your opponent's move was: {}".format(res.my_move.value[0]))
    print("You scored {}".format(res.get_opp_score()), ", total: {}".format(sc2))
    print("Your opponent scored {}".format(res.get_my_score()), ", total: {}".format(sc1))
    print("--------------------------->")


def print_score(sc1, sc2):
    print("THE GAME HAS ENDED")
    print("--------------------------->")
    print("You scored in total {} points.".format(sc2))
    print("AI player scored in total {} points.".format(sc1))


def main():
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

    try:
        path = sys.argv[1]
        strategy_module, strategy_class_name = path.rsplit('.', 1)
        strategy1 = importlib.import_module(strategy_module)
    except IOError:
        print('An error occurred trying to read the file.')
        exit(1)
    except ImportError:
        print("NO module found")
        exit(1)

    s1 = getattr(strategy1, strategy_class_name)()
    sc1 = 0
    sc2 = 0

    for i in range(iterations):
        move1 = s1.next_move()
        move2 = pick_next()
        res = Result(move1, move2)
        sc1 += res.get_my_score()
        sc2 += res.get_opp_score()
        print_result(res, sc1, sc2)
        s1.reward(res)

    print_score(sc1, sc2)


if __name__ == "__main__":
    main()
