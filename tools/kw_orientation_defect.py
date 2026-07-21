from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Literal, Sequence


Kind = Literal["var", "not_var", "and", "or"]


@dataclass(frozen=True)
class Node:
    kind: Kind
    index: int | None = None
    left: "Node | None" = None
    right: "Node | None" = None

    @staticmethod
    def var(index: int