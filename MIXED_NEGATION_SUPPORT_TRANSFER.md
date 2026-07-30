# Mixed Sparse/Dense Negation Depth Lower Bound for the Layered CLIQUE Slice

## 1. Purpose

This note transfers the corrected mixed-negation theorem of Koroth and Sarma to the trivial-hash CLIQUE slice of the formal layered language.

It strengthens the earlier restricted endpoints by allowing:

- a small number of negation gates whose input/output functions may have arbitrary orientation; and
- additional negation gates whose relevant graph-variable support is small.

It is a depth lower bound for a restricted circuit class. It is not an unrestricted circuit lower bound.

## 2. The projected layered function

For graph size `n` and clique parameter `r`, let

```text
LayerClique(n,r)(G) = L_layer(I_G),
```

where `I_G` is the fixed-width layered instance with:

1. `r` layers, each containing a copy of `[n]`;
2. tautological local formulas;
3. fully open masks;
4. trivial hash;
5. a cross-layer edge between `(a,u)` and `(b,v)` exactly when `u != v` and `{u,v}` is an edge of `G`.

Then

```text
LayerClique(n,r)(G) = CLIQUE(n,r)(G).
```

Thus every circuit lower bound for the graph function transfers pointwise to this layered slice.

## 3. Support of a negation gate

Let `C` be a bounded-fan-in circuit on the graph-edge variables.

For a negation gate `N`, let `p_N` be the Boolean function computed at its input and let `q_N = not p_N` be the function computed at its output.

Call `N` **w-supported** when the union of the sensitivity supports of `p_N` and `q_N` contains at most `2w` graph variables. Equivalently, the input and output functions together depend nontrivially on at most `2w` edge coordinates.

This is the support condition used in the corrected mixed-negation theorem. It is stronger than merely saying that the syntactic input wire of the negation is one bit.

## 4. Published theorem used

Let

```text
alpha = 2^(ell+1) - 1.
```

Koroth and Sarma prove the following for the CLIQUE family.

Suppose a circuit computing

```text
CLIQUE(n, n^(1/(6 alpha)))
```

contains `ell + k` negation gates, where:

```text
ell <= (1/6) log log n;
```

at least `k` of those negation gates are `w`-supported; and

```text
k w <= n/8.
```

The remaining `ell` negations may have arbitrary orientation and arbitrary support. Then

```text
depth(C) >= n^(1/(2 ell + 8)).
```

The proof first removes all vertices touched by the low-support negations, causing those negations to become constant, and then invokes the depth lower bound for the remaining `ell` arbitrary negations.

## 5. Layered transfer theorem

### Theorem

Let

```text
alpha = 2^(ell+1) - 1,
r = n^(1/(6 alpha)).
```

Let `C_layer` be a bounded-fan-in circuit computing the layered slice

```text
LayerClique(n,r).
```

Assume `C_layer` has `ell + k` negation gates such that:

1. `ell <= (1/6) log log n`;
2. at least `k` negation gates are `w`-supported with respect to the original graph-edge variables;
3. `k w <= n/8`;
4. the remaining `ell` negation gates are unrestricted.

Then

```text
depth(C_layer) >= n^(1/(2 ell + 8)).
```

### Proof

The layered slice is exactly `CLIQUE(n,r)` as a Boolean function of the graph-edge variables. Therefore `C_layer` is already a circuit for the CLIQUE function appearing in the published theorem. All hypotheses are identical, so the bound follows directly.

No separate NP-hardness claim for the fixed parameter `r(n)` is needed.

## 6. Consequences

### Constant number of dense exceptions

For constant `ell`, the theorem gives a polynomial depth lower bound:

```text
depth(C_layer) >= n^c
```

for the constant

```text
c = 1/(2 ell + 8).
```

Thus subpolynomial-depth circuits are impossible even when a constant number of negation gates have arbitrary dense orientation, provided all remaining negations have sufficiently small total support.

### Sparse negations at leaves

Taking `ell = 0` and `w = 1` recovers a strong lower bound for circuits whose negations are confined to graph literals, subject to the total-support condition.

### Support budget interpretation

The low-support negations may be numerous, but their aggregate budget must obey

```text
k w <= n/8.
```

The result therefore controls a mixed model using two parameters:

```text
(number of dense exceptions, total sparse support budget).
```

## 7. What the theorem does not establish

It does not show that BRC, SRC, SPA, or any black-box audit forces the support condition.

It does not handle `Theta(log n)` arbitrary dense negations.

It gives a depth lower bound, not an unrestricted superpolynomial size lower bound.

It does not prove `NP not subseteq P/poly` or `P != NP`.

## 8. New exact bridge

A useful white-box advance would be a polynomial-time canonicalization or certificate theorem proving that every small layered decider can be represented so that:

```text
ell <= (1/6) log log n
```

negations are arbitrary, while every other negation is `w`-supported and

```text
k w <= n/8.
```

Closing that statement would immediately activate the transferred polynomial depth lower bound.