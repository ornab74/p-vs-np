from __future__ import annotations

from itertools import product
from typing import Callable, Iterable

BitTuple = tuple[int, ...]
BooleanFunction = Callable[[BitTuple], int]


def hypercube(n: int) -> Iterable[BitTuple]:
    return product((0, 1), repeat=n)


def minimal_orientation(f: BooleanFunction, n: int) -> BitTuple:
    """Return the unique minimal orientation from decreasing hypercube edges.