from __future__ import annotations

from itertools import combinations, product
from math import comb, factorial


def edges(vertices: tuple[int, ...]) -> set[tuple[int, int]]:
    return {tuple(sorted(e)) for e in combinations(vertices, 2)}


def clique_edges(block: tuple[int, ...]) -> set[tuple[int, int]]:
    return edges(block)


def coloring_edges(coloring: tuple[int, ...]) -> set[tuple[int, int]]:
    n = len(coloring)
    return {
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if coloring[i] != coloring[j]
    }


def selector_edges(n: int, b0: tuple[int, ...]) -> set[tuple[int, int]]:
    all_edges = edges(tuple(range(n)))
    return all_edges - edges(b0)


def selector(graph: set[tuple[int, int]], h_edges: set[tuple[int, int]]) -> int:
    return int(bool(graph & h_edges))


def largest_color_class_on(block: tuple[int, ...], coloring: tuple[int, ...]) -> int:
    counts: dict[int, int] = {}
    for v in block:
        counts[coloring[v]] = counts.get(coloring[v], 0) + 1
    return max(counts.values())


def verify(n: int, k: int) -> None:
    if not (3 <= k < n):
        raise ValueError("require 3 <= k < n")
    q = k - 1
    b0 = tuple(range(k))
    h = selector_edges(n, b0)

    positives = list(combinations(range(n), k))
    zero_positives = [b for b in positives if selector(clique_edges(b), h) == 0]
    assert zero_positives == [b0]

    colorings = [c for c in product(range(q), repeat=n) if len(set(c)) > 1]
    assert colorings
    assert all(selector(coloring_edges(c), h) == 1 for c in colorings)

    balanced = [c for c in colorings if set(c[v] for v in b0) == set(range(q))]
    assert balanced
    assert all(largest_color_class_on(b0, c) == 2 for c in balanced)

    counted = comb(k, 2) * factorial(k - 1) * (k - 1) ** (n - k)
    assert len(balanced) == counted

    defect_mass = 1 / comb(n, k)
    balanced_probability = counted / ((k - 1) ** n - (k - 1))
    assert defect_mass > 0
    assert balanced_probability > 0

    print(
        "programmed KW defect barrier: PASS",
        f"n={n}",
        f"k={k}",
        f"defect_slice={defect_mass:.8f}",
        f"nonanchorable_negative_mass={balanced_probability:.8f}",
    )


if __name__ == "__main__":
    verify(n=6, k=4)
