#!/usr/bin/env python3
"""Counterexample to the claimed influence bound from repeated audits.

The draft argues that if k repeated resampling checks pass with probability
at least 1-delta, then average resampling influence is O(delta/k).

Rare catastrophic contexts refute this. With probability delta the context is
bad and every resample flips the answer; otherwise no resample flips it.
The k-fold audit fails with probability exactly delta for every k, while the
average single-resample influence is delta, not delta/k.
"""

from __future__ import annotations

import argparse
import random


def theoretical(delta: float, k: int) -> tuple[float, float, float]:
    average_influence = delta
    k_fold_failure = delta
    claimed_upper_bound = 2.0 * delta / k
    return average_influence, k_fold_failure, claimed_upper_bound


def simulate(delta: float, k: int, trials: int, seed: int) -> tuple[float, float]:
    rng = random.Random(seed)
    single_disagreements = 0
    audit_failures = 0

    for _ in range(trials):
        bad_context = rng.random() < delta

        # One fresh resampling query.
        if bad_context:
            single_disagreements += 1

        # k repeated queries. In a bad context all of them disagree;
        # in a good context none does.
        if bad_context and k > 0:
            audit_failures += 1

    return single_disagreements / trials, audit_failures / trials


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delta", type=float, default=0.01)
    parser.add_argument("--k", type=int, default=100)
    parser.add_argument("--trials", type=int, default=200_000)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()

    if not 0.0 < args.delta < 1.0:
        raise SystemExit("delta must lie in (0,1)")
    if args.k < 1:
        raise SystemExit("k must be positive")

    influence, failure, claimed = theoretical(args.delta, args.k)
    sim_influence, sim_failure = simulate(
        args.delta, args.k, args.trials, args.seed
    )

    print(f"theoretical average influence: {influence:.8f}")
    print(f"theoretical k-fold failure:    {failure:.8f}")
    print(f"claimed 2*delta/k bound:       {claimed:.8f}")
    print(f"simulated average influence:   {sim_influence:.8f}")
    print(f"simulated k-fold failure:      {sim_failure:.8f}")

    assert influence > claimed, (
        "choose k>2 to demonstrate violation of the claimed bound"
    )
    assert abs(failure - influence) < 1e-12


if __name__ == "__main__":
    main()
