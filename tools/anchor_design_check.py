#!/usr/bin/env python3
"""Finite checks for automatic locality and disjoint-anchor designs."""

from itertools import combinations, product
from math import comb, floor


def positive_prob(n: int, k: int, s: int) -> float:
    return comb(n - s, k - s) / comb(n, k)


def negative_prob(n: int, k: int, s: int) -> float:
    q = k - 1
    return (q ** (n - s) - 1) / (q ** (n - 1) - 1)


def disjoint_anchors(n: int, k: int, d: int):
    s = floor(k / (d + 1)) + 1
    anchors = []
    start = 0
    while start + s <= n:
        anchors.append(frozenset(range(start, start + s)))
        start += s
    return s, anchors


def max_positive_load(n: int, k: int, anchors) -> int:
    best = 0
    for b in combinations(range(n), k):
        bset = frozenset(b)
        load = sum(1 for s in anchors if s <= bset)
        best = max(best, load)
    return best


def exact_union_locality(n: int, k: int, anchors) -> float:
    positives = [frozenset(b) for b in combinations(range(n), k)]
    q = k - 1
    colorings = [c for c in product(range(q), repeat=n) if len(set(c)) > 1]
    total = len(positives) * len(colorings)
    covered = 0
    for b in positives:
        for coloring in colorings:
            if any(s <= b and len({coloring[v] for v in s}) == 1 for s in anchors):
                covered += 1
    return covered / total


def verify_case(n: int, k: int, d: int) -> None:
    assert 2 <= k <= n
    assert 1 <= d < k
    s, anchors = disjoint_anchors(n, k, d)
    load = max_positive_load(n, k, anchors)
    assert load <= d, (n, k, d, s, load)

    union_bound = sum(positive_prob(n, k, len(a)) * negative_prob(n, k, len(a)) for a in anchors)
    automatic = d / (k - 1)
    assert union_bound <= automatic + 1e-12

    exact = exact_union_locality(n, k, anchors)
    assert exact <= union_bound + 1e-12
    assert exact <= automatic + 1e-12

    print(
        f"n={n} k={k} d={d} s={s} anchors={len(anchors)} "
        f"load={load} exact={exact:.8f} union_bound={union_bound:.8f} "
        f"automatic={automatic:.8f}"
    )


def main() -> None:
    for n, k, d in [(6, 3, 1), (7, 4, 1), (8, 4, 2), (8, 5, 2)]:
        verify_case(n, k, d)
    print("all bounded-load anchor checks passed")


if __name__ == "__main__":
    main()
