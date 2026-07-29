#!/usr/bin/env python3
"""Verify the spike-function separation between orientation support and edge-audit mass."""

from __future__ import annotations

import argparse
from itertools import product


def spike(x: tuple[int, ...]) -> int:
    return int(all(bit == 0 for bit in x))


def directional_mass(n: int, coord: int) -> float:
    violations = 0
    total = 0
    for context in product((0, 1), repeat=n - 1):
        low = list(context)
        high = list(context)
        low.insert(coord, 0)
        high.insert(coord, 1)
        total += 1
        violations += int(spike(tuple(low)) == 1 and spike(tuple(high)) == 0)
    return violations / total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs="?", default=8)
    args = parser.parse_args()
    if args.n < 1:
        raise SystemExit("n must be positive")

    masses = [directional_mass(args.n, i) for i in range(args.n)]
    support = sum(mass > 0 for mass in masses)
    audit_mass = sum(masses) / args.n
    expected = 2 ** (-(args.n - 1))

    print(f"n={args.n}")
    print(f"minimal_orientation_support={support}")
    print(f"directional_masses={masses}")
    print(f"edge_audit_rejection={audit_mass}")
    print(f"expected={expected}")

    assert support == args.n
    assert all(abs(mass - expected) < 1e-15 for mass in masses)
    assert abs(audit_mass - expected) < 1e-15
    print("verified")


if __name__ == "__main__":
    main()
