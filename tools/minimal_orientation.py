from __future__ import annotations

from itertools import product
from typing import Callable, Iterable

BitTuple = tuple[int, ...]
BooleanFunction = Callable[[BitTuple], int]


def hypercube(n: int) -> Iterable[BitTuple]:
    """Enumerate the Boolean cube in lexicographic order."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    return product((0, 1), repeat=n)


def validate_boolean(value: int, *, name: str = "function value") -> int:
    if value not in (0, 1, False, True):
        raise ValueError(f"{name} must be Boolean, got {value!r}")
    return int(value)


def minimal_orientation(f: BooleanFunction, n: int) -> BitTuple:
    """Return the unique minimal orientation from decreasing cube edges.

    Coordinate i is oriented exactly when some edge in direction i decreases:

        x_i = 0, f(x) = 1, f(x with x_i=1) = 0.
    """
    if n < 0:
        raise ValueError("n must be nonnegative")

    orientation = [0] * n
    for x in hypercube(n):
        fx = validate_boolean(f(x))
        if fx == 0:
            continue
        for i, bit in enumerate(x):
            if bit != 0 or orientation[i]:
                continue
            y = list(x)
            y[i] = 1
            if validate_boolean(f(tuple(y))) == 0:
                orientation[i] = 1
    return tuple(orientation)


def orientation_weight(f: BooleanFunction, n: int) -> int:
    return sum(minimal_orientation(f, n))


def is_monotone(f: BooleanFunction, n: int) -> bool:
    return orientation_weight(f, n) == 0


def main() -> None:
    monotone_or = lambda x: int(any(x))
    negated_first = lambda x: int(not x[0])
    mixed = lambda x: int((not x[0]) and x[1])

    assert minimal_orientation(monotone_or, 3) == (0, 0, 0)
    assert minimal_orientation(negated_first, 3) == (1, 0, 0)
    assert minimal_orientation(mixed, 3) == (1, 0, 0)
    assert is_monotone(monotone_or, 3)
    assert not is_monotone(negated_first, 3)

    print("minimal orientation verifier: PASS")


if __name__ == "__main__":
    main()
