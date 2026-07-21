from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Iterable


BitTuple = tuple[int, ...]
Edge = tuple[int, int]


@dataclass(frozen=True)
class OrientationReport:
    orientation: BitTuple
    weight: int
    vertices: frozenset[int]

    @property
    def vertex_support(self) -> int:
        return len(self.vertices)


def minimal_orientation(num