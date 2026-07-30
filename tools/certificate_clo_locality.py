#!/usr/bin/env python3
"""Verify the exact hard-pair locality of a negated edge literal.

Positive hard set: k-clique graphs K_S with S uniform among k-subsets of [n].
Negative hard set: complete (k-1)-partite graphs from a uniform coloring
conditioned on using at least two colors.
"""

from __future__ import annotations

import argparse
import itertools
from math import comb


def exact_formula(n: int, k: int) -> float:
    if not (2 <= k <= n):
        raise ValueError("require 2 <= k <= n")
    pos = 1.0 - (k * (k - 1)) / (n * (n - 1))
    neg = ((k - 2) / (k - 1)) / (1.0 - (k - 1) ** (1 - n))
    return pos * neg


def brute_force(n: int, k: int) -> float:
    if n > 9:
        raise ValueError("brute force intended for n <= 9")
    vertices = range(n)
    edge = (0, 1)

    positives = list(itertools.combinations(vertices, k))
    u_mass = sum(not ({edge[0], edge[1]} <= set(S)) for S in positives) / len(positives)

    colors = range(k - 1)
    colorings = [c for c in itertools.product(colors, repeat=n) if len(set(c)) >= 2]
    v_mass = sum(c[edge[0]] != c[edge[1]] for c in colorings) / len(colorings)
    return u_mass * v_mass


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--skip-bruteforce", action="store_true")
    args = parser.parse_args()

    value = exact_formula(args.n, args.k)
    print(f"exact locality mu_e = {value:.12f}")

    if not args.skip_bruteforce:
        brute = brute_force(args.n, args.k)
        print(f"brute-force locality = {brute:.12f}")
        assert abs(value - brute) < 1e-12
        print("verified")


if __name__ == "__main__":
    main()
