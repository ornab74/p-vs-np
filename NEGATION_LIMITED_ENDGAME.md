# Negation-Limited Endgame

## Motivation

The universal monotone-compression route is blocked by exponential gaps between unrestricted and monotone circuit complexity. A narrower endpoint is available: prove that the hard graph projection has only a very small number of NOT gates, then invoke a lower bound for negation-limited CLIQUE circuits directly.

## Known lower bound

Amano and Maruoka prove a superpolynomial size lower bound for circuits computing a suitable CLIQUE family when the circuit contains at most

```text
floor((1/6) log log m)
```

NOT gates, where `m` is the number of graph vertices. Their theorem uses a specific growing clique parameter and gives a strongly superpolynomial gate lower bound.

This result applies to nonmonotone circuits and therefore does not require a monotone-circuit conversion.

## Conditional endgame theorem

### Structural hypothesis

Assume there is a polynomial-time or nonuniform polynomial-size transformation `N` with the following property.

For every polynomial-size circuit `C_m` computing the relevant projected CLIQUE function, if `C_m` satisfies the exact layered audit hypotheses, then `N(C_m)`:

1. computes the same CLIQUE function pointwise;
2. has polynomial size;
3. contains at most `floor((1/6) log log m)` NOT gates.

### Theorem

Under the structural hypothesis,

```text
NP is not contained in P/poly.
```

### Proof

Assume `NP subseteq P/poly`. Then the ordinary CLIQUE language has polynomial-size circuits. For every graph size `m`, restrict the input bits encoding the clique parameter to the value required by the Amano--Maruoka lower-bound family. This yields a polynomial-size unrestricted circuit `C_m` for that fixed-parameter CLIQUE function.

Apply the structural transformation `N`. The result is a polynomial-size circuit computing the same function with at most `floor((1/6) log log m)` NOT gates.

This contradicts the known superpolynomial lower bound for that negation-limited circuit class. Hence `NP not subseteq P/poly`.

## Important parameter point

The fixed-parameter CLIQUE family does not itself need a separate NP-hardness proof. The assumption `NP subseteq P/poly` supplies circuits for the full CLIQUE language, and fixing the parameter bits preserves polynomial size.

This avoids the earlier incorrect inference that `CLIQUE_{m,k(m)}` must independently be shown NP-hard for the chosen growing `k(m)`.

## What remains to prove

The entire burden moves to the structural hypothesis:

```text
exact audits
=> equivalent polynomial-size circuit with very few NOT gates.
```

The current audits do not imply this. In particular:

- auxiliary-only audits are blind to arbitrary graph negations;
- semantic monotonicity does not bound the number of NOT gates;
- block-local NOT syntax does not bound the total number of surviving NOT gates;
- replacing gates by conditional-majority constants is not a pointwise circuit transformation.

## Possible intermediate models

A weaker but potentially useful progression is:

1. prove bounded negation width;
2. use known lower bounds relating negation width to monotone complexity;
3. prove sparse orientation in a monotone Karchmer--Wigderson framework;
4. derive an explicit total-NOT bound after a graph restriction.

Each statement must include polynomial size accounting and pointwise correctness.

## Comparison with the CLO route

The negation-limited route avoids:

- oracle rectangle definitions;
- CLO union-locality estimates;
- the restrictive arbitrary-depth oracle condition.

But it replaces them with a very strong graph-sensitive normalization theorem. Neither route is currently complete.

## Reference

Kazuyuki Amano and Akira Maruoka, *A Superpolynomial Lower Bound for a Circuit Computing the Clique Function with at most (1/6) log log n Negation Gates*, SIAM Journal on Computing 35(1), 2005.
