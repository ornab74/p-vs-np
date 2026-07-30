from __future__ import annotations

from itertools import combinations, product
from math import comb


def exact_formula(n: int, k: int, s: int) -> float:
    q = k - 1
    p_u = comb(n - s, k - s) / comb(n, k)
    p_v = (q ** (n - s + 1) - q) / (q**n - q)
    return p_u * p_v


def brute_force(n: int, k: int, s: int) -> float:
    vertices = tuple(range(n))
    q = k - 1
    anchor = frozenset(range(s))
    positives = [frozenset(x) for x in combinations(vertices, k)]
    colorings = [c for c in product(range(q), repeat=n) if len(set(c)) > 1]

    pos_hits = sum(anchor <= clique for clique in positives)
    neg_hits = sum(len({c[v] for v in anchor}) == 1 for c in colorings)
    return (pos_hits / len(positives)) * (neg_hits / len(colorings))


def verify_complete_edge_cover(n: int, k: int) -> None:
    vertices = tuple(range(n))
    q = k - 1
    for clique in combinations(vertices, k):
        clique_set = set(clique)
        for coloring in product(range(q), repeat=n):
            if len(set(coloring)) <= 1:
                continue
            assert any(
                coloring[u] == coloring[v]
                for u, v in combinations(clique_set, 2)
            )


def verify_ad_collapse(n: int, k: int, s: int, d: int) -> None:
    templates = list(combinations(range(n), s))
    if s * (d + 1) > k or len(templates) < d + 1:
        return
    chosen = templates[: d + 1]
    union = set().union(*map(set, chosen))
    if len(union) <= k:
        witness = union | set(v for v in range(n) if v not in union)
        witness = set(list(witness)[:k])
        assert sum(set(t) <= witness for t in chosen) >= d + 1


def main() -> None:
    for n, k, s in [(5, 3, 2), (6, 4, 2), (6, 4, 3)]:
        formula = exact_formula(n, k, s)
        brute = brute_force(n, k, s)
        assert abs(formula - brute) < 1e-12
        print(f"n={n} k={k} s={s}: locality={formula:.12f}")

    verify_complete_edge_cover(6, 4)
    verify_ad_collapse(8, 6, 2, 2)
    print("complete edge cover and A_d collapse verified")


if __name__ == "__main__":
    main()
