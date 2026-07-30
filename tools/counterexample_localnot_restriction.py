#!/usr/bin/env python3
"""Minimal counterexample to the claim that fixing a NOT gate's support kills it.

The circuit f(x, y) = (not x) and y is LocalNOT when x and y are separate
blocks and the sole NOT depends on the single block {x}. Restricting that block
by fixing y leaves not x unchanged. Thus support-size calculations alone do not
show that random block restrictions produce a monotone circuit.
"""

from itertools import product


def f(x: int, y: int) -> int:
    return (1 - x) & y


def restricted_y_one(x: int) -> int:
    return f(x, 1)


def is_monotone_unary(g) -> bool:
    return g(0) <= g(1)


def main() -> None:
    table = [(x, y, f(x, y)) for x, y in product((0, 1), repeat=2)]
    print("f(x,y) = NOT(x) AND y")
    for row in table:
        print(row)

    print("After restricting y=1:")
    print([(x, restricted_y_one(x)) for x in (0, 1)])
    print("Monotone in x:", is_monotone_unary(restricted_y_one))

    assert restricted_y_one(0) == 1
    assert restricted_y_one(1) == 0
    assert not is_monotone_unary(restricted_y_one)
    print("COUNTEREXAMPLE CONFIRMED")


if __name__ == "__main__":
    main()
