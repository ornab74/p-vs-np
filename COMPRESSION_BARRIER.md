# Barrier to a Universal Monotone Compression Theorem

## Purpose

The repaired program needs a theorem converting a small unrestricted Boolean circuit for a monotone target into a small monotone circuit, or into a small monotone circuit with local oracles. This note records why no such theorem can hold merely from monotonicity of the computed function.

## Universal compression statement

Consider the following proposed statement.

> There is a polynomial `p` and an effective transformation `T` such that, for every monotone Boolean function `f:{0,1}^n->{0,1}` and every Boolean circuit `C` of size `s` computing `f`, `T(C)` is a monotone Boolean circuit computing `f` of size at most `p(n,s)`.

This statement is false.

## Barrier theorem

### Theorem

No universal polynomial-size transformation of the above form exists.

### Proof

Tardos constructed an explicit monotone Boolean function family `f_n` that is computable in polynomial time, and hence has polynomial-size unrestricted Boolean circuits, but whose monotone circuit complexity is exponential.

If the universal transformation existed, applying it to the polynomial-size unrestricted circuits for `f_n` would produce polynomial-size monotone circuits for `f_n`, contradicting the monotone lower bound.

Therefore any valid compression theorem must use properties substantially stronger than:

1. the target function is monotone;
2. the target has a polynomial-size unrestricted circuit;
3. the target satisfies black-box semantic monotonicity identities.

## Consequence for this repository

The statement

```text
small unrestricted decider
=> small monotone circuit
```

cannot be a generic circuit-normalization lemma.

A viable theorem must exploit a special invariant of the formal layered language, its witness structure, or a restricted circuit model. The assumptions must exclude known monotone functions exhibiting exponential monotone/nonmonotone gaps.

## Local-oracle version

Allowing unrestricted oracle gates does not solve the problem. If an oracle may compute an arbitrary function on the full input, then every target has a size-one representation:

```text
y_1(x) := f(x)
output := y_1(x).
```

The representation becomes meaningful only after imposing a quantitative locality condition on the positive-negative rectangles associated with the oracle gates.

Thus the actual target is not mere existence of a monotone-CLO representation. It is:

> Construct a polynomial-size monotone-CLO representation whose oracle union locality is below the threshold of an applicable lower bound and whose oracle rectangles satisfy every required structural condition.

## What the audits would have to prove

To bypass the barrier, the audits must yield at least one property not shared by arbitrary monotone functions with easy nonmonotone circuits. Candidate properties include:

1. a bounded number of surviving negations after a named restriction;
2. bounded negation width;
3. a low-communication monotone Karchmer-Wigderson protocol with controlled errors;
4. bounded-locality oracle rectangles;
5. a feasible-interpolation structure;
6. a special decomposition theorem tied to the layered witness relation.

No current audit proves one of these properties.

## Falsifiable next target

A noncircular compression theorem must state an explicit hypothesis `P(C)` and prove:

```text
C computes the layered target and P(C)
=> polynomial-size bounded-locality monotone CLO.
```

It must then prove independently that the semantic audits imply `P(C)`. If `P(C)` is merely equivalent to having a small monotone representation, the argument is circular.

## References

- Eva Tardos, *The gap between monotone and non-monotone circuit complexity is exponential*, Combinatorica 8(1), 1988.
- Bruno P. Cavalar and Igor C. Oliveira, *Constant-depth circuits vs. monotone circuits*, 2023, for modern separations and explicit discussion of the difficulty of monotone simulations.
