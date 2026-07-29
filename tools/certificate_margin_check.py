#!/usr/bin/env python3
"""Exhaustively verify the certificate-margin lemma on small Boolean functions.

For a truth table f:{0,1}^n->{0,1}, the script computes:
- C0(f), C1(f)
- minimal orientation support
- directional decreasing-edge masses nu_i
- the lower bound nu_i >= 2^{-(C0+C1-2)} on oriented coordinates

The exhaustive search is intended for small n only.
"""

from __future__ import annotations

from itertools import combinations, product
from typing import Dict, Iterable, List, Sequence, Tuple

Bits = Tuple[int, ...]
TruthTable = Dict[Bits, int]


def cube_points(n: int) -> List[Bits]:
    return list(product((0, 1), repeat=n))


def is_certificate(
    table: TruthTable,
    x: Bits,
    coordinates: Sequence[int],
    value: int,
) -> bool:
    for y, fy in table.items():
        if all(y[i] == x[i] for i in coordinates) and fy != value:
            return False
    return True


def certificate_complexity(table: TruthTable, value: int) -> int:
    n = len(next(iter(table)))
    worst = 0
    for x, fx in table.items():
        if fx != value:
            continue
        best = n
        for size in range(n + 1):
            found = False
            for coords in combinations(range(n), size):
                if is_certificate(table, x, coords, value):
                    best = size
                    found = True
                    break
            if found:
                break
        worst = max(worst, best)
    return worst


def directional_masses(table: TruthTable) -> List[float]:
    n = len(next(iter(table)))
    masses: List[float] = []
    for i in range(n):
        violations = 0
        contexts = 0
        for z in product((0, 1), repeat=n - 1):
            x0 = list(z)
            x0.insert(i, 0)
            x1 = list(z)
            x1.insert(i, 1)
            contexts += 1
            if table[tuple(x0)] == 1 and table[tuple(x1)] == 0:
                violations += 1
        masses.append(violations / contexts)
    return masses


def check_table(table: TruthTable) -> None:
    c0 = certificate_complexity(table, 0)
    c1 = certificate_complexity(table, 1)
    masses = directional_masses(table)
    margin = 2.0 ** (-(c0 + c1 - 2)) if c0 + c1 >= 2 else 1.0

    for i, mass in enumerate(masses):
        if mass > 0 and mass + 1e-15 < margin:
            raise AssertionError(
                f"coordinate {i}: mass={mass}, margin={margin}, C0={c0}, C1={c1}"
            )


def spike_table(n: int) -> TruthTable:
    return {x: int(all(bit == 0 for bit in x)) for x in cube_points(n)}


def enumerate_functions(n: int) -> Iterable[TruthTable]:
    points = cube_points(n)
    for outputs in product((0, 1), repeat=len(points)):
        yield dict(zip(points, outputs))


def main() -> None:
    for n in range(1, 4):
        checked = 0
        for table in enumerate_functions(n):
            if len(set(table.values())) < 2:
                continue
            check_table(table)
            checked += 1
        print(f"n={n}: verified {checked} nonconstant functions")

    for n in range(2, 7):
        table = spike_table(n)
        c0 = certificate_complexity(table, 0)
        c1 = certificate_complexity(table, 1)
        masses = directional_masses(table)
        expected = 2.0 ** (-(n - 1))
        assert all(abs(m - expected) < 1e-15 for m in masses)
        print(
            f"spike n={n}: C0={c0}, C1={c1}, "
            f"orientation_weight={sum(m > 0 for m in masses)}, mass={expected}"
        )


if __name__ == "__main__":
    main()
