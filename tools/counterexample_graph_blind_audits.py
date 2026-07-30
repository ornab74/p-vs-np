#!/usr/bin/env python3
"""Finite demonstration that auxiliary-only audits cannot constrain graph syntax.

The circuit below computes an arbitrary graph function D(H) while ignoring all
auxiliary blocks. Every audit that keeps H fixed and changes only auxiliaries
passes with probability one, regardless of how D is represented internally.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Iterable, Tuple


GraphBits = Tuple[int, ...]
AuxBits = Tuple[int, ...]


@dataclass(frozen=True)
class Input:
    graph: GraphBits
    aux: AuxBits


def nonmonotone_graph_circuit(graph: GraphBits) -> int:
    """A deliberately nonmonotone representation.

    Algebraically this returns graph[0], but the expression contains negations
    and mixed cancellations. An auxiliary-only black-box audit cannot observe
    or prohibit that syntax.
    """
    x = graph[0]
    y = graph[1] if len(graph) > 1 else 0
    hidden = (1 - x) ^ y
    return (x & hidden) | (x & (1 - hidden))


def extended_circuit(inp: Input) -> int:
    return nonmonotone_graph_circuit(inp.graph)


def auxiliary_transforms(aux: AuxBits) -> Iterable[AuxBits]:
    yield tuple(1 - bit for bit in aux)
    yield tuple(reversed(aux))
    yield tuple(0 for _ in aux)
    yield tuple(1 for _ in aux)


def audit_passes(inp: Input, circuit: Callable[[Input], int]) -> bool:
    baseline = circuit(inp)
    return all(
        circuit(Input(inp.graph, transformed_aux)) == baseline
        for transformed_aux in auxiliary_transforms(inp.aux)
    )


def exhaustive_check(graph_width: int = 3, aux_width: int = 4) -> None:
    total = 0
    for graph in product((0, 1), repeat=graph_width):
        for aux in product((0, 1), repeat=aux_width):
            total += 1
            inp = Input(tuple(graph), tuple(aux))
            assert audit_passes(inp, extended_circuit)
            assert extended_circuit(inp) == graph[0]

    print(f"checked {total} inputs")
    print("all auxiliary-only audits pass")
    print("the supplied graph circuit still contains explicit negations")


if __name__ == "__main__":
    exhaustive_check()
