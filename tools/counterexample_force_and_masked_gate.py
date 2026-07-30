#!/usr/bin/env python3
"""Small finite counterexamples for two proof-pipeline implications.

1. The original graph-only FORCE operation can answer YES even when no
   witness contains the requested prefix.
2. Semantic invariance of a circuit output cannot force the syntax of
   internal NOT gates because a mixed gate can be perfectly masked.
"""

from __future__ import annotations

from itertools import combinations
from typing import Callable, FrozenSet, Iterable, Set, Tuple

Vertex = int
Edge = FrozenSet[Vertex]


def edge(u: Vertex, v: Vertex) -> Edge:
    return frozenset((u, v))


def is_clique(vertices: Iterable[Vertex], edges: Set[Edge]) -> bool:
    vertices = tuple(vertices)
    return all(edge(u, v) in edges for u, v in combinations(vertices, 2))


def force_graph(
    vertices: Set[Vertex], edges: Set[Edge], prefix: Set[Vertex]
) -> Tuple[Set[Vertex], Set[Edge]]:
    """Model the repository's graph-only FORCE intuition.

    Vertices outside the prefix that are not adjacent to every prefix vertex
    are removed. Prefix vertices remain.
    """
    kept = set(prefix)
    for v in vertices - prefix:
        if all(edge(v, u) in edges for u in prefix):
            kept.add(v)
    kept_edges = {e for e in edges if e <= kept}
    return kept, kept_edges


def valid_witnesses(
    vertices: Set[Vertex],
    edges: Set[Edge],
    satisfiable: Set[Vertex],
    t: int,
) -> list[FrozenSet[Vertex]]:
    return [
        frozenset(c)
        for c in combinations(sorted(vertices), t)
        if set(c) <= satisfiable and is_clique(c, edges)
    ]


def demonstrate_force_failure() -> None:
    # Vertex 1 is a trap: it is adjacent to the real witness clique but its
    # local formula is unsatisfiable. The only valid witness is {2,3,4}.
    vertices = {1, 2, 3, 4}
    edges = {
        edge(2, 3),
        edge(2, 4),
        edge(3, 4),
        edge(1, 2),
        edge(1, 3),
        edge(1, 4),
    }
    satisfiable = {2, 3, 4}
    t = 3
    prefix = {1}

    original = valid_witnesses(vertices, edges, satisfiable, t)
    assert original == [frozenset({2, 3, 4})]
    assert not any(prefix <= witness for witness in original)

    forced_vertices, forced_edges = force_graph(vertices, edges, prefix)
    forced = valid_witnesses(forced_vertices, forced_edges, satisfiable, t)

    # FORCE says YES because the unrelated witness survives, even though no
    # valid witness contains the pinned vertex 1.
    assert forced == [frozenset({2, 3, 4})]
    print("FORCE counterexample: YES survives without extending the prefix")


def demonstrate_masked_gate_failure() -> None:
    # h mixes blocks y and z. The circuit contains NOT(h), yet the output is
    # exactly x because h OR NOT(h) is always true.
    def circuit(x: bool, y: bool, z: bool) -> bool:
        h = y ^ z
        return (x and h) or (x and (not h))

    for x in (False, True):
        outputs = {circuit(x, y, z) for y in (False, True) for z in (False, True)}
        assert outputs == {x}

    # The output is perfectly invariant under resampling y and z despite a
    # syntactically mixed NOT gate. Output audits cannot inspect that syntax.
    print("Masked-gate counterexample: zero output influence, mixed internal NOT")


def main() -> None:
    demonstrate_force_failure()
    demonstrate_masked_gate_failure()


if __name__ == "__main__":
    main()
