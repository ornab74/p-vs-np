# Complete Lower Bound for the Few-NOT Circuit Class

## Result

This note gives an unconditional end-to-end theorem for the formal layered language against a restricted but nontrivial circuit class. It does not prove an unrestricted circuit lower bound.

## Published input theorem

Amano and Maruoka prove that there is an explicit growing clique parameter `k(m)` for which every Boolean circuit computing `CLIQUE_{m,k(m)}` and containing at most

```text
floor((1/6) log log m)
```

NOT gates has superpolynomial size.

Reference: Kazuyuki Amano and Akira Maruoka, *A Superpolynomial Lower Bound for a Circuit Computing the Clique Function with at most (1/6) log log n Negation Gates*, SIAM Journal on Computing 35(1), 2005.

## Layered projection

For graph size `m` and clique parameter `k=k(m)`, construct a `k`-layer instance of the formal layered language as follows.

1. Every layer contains a copy of the vertex set `[m]`.
2. The candidate mask in every layer is all of `[m]`.
3. Every local formula is the canonical padded tautology and every assignment mask is fully open.
4. The hash length is zero, so the hash predicate always accepts.
5. For distinct layers `r<s`, connect copy `(r,u)` to copy `(s,v)` iff `u != v` and `{u,v}` is an edge of the input graph `G`.

This transform has size polynomial in `m` and `k` and is computable in polynomial time.

## Exact equivalence

The layered instance is YES iff `G` contains a clique of size `k`.

### Proof

A layered witness chooses one vertex copy from each of the `k` layers. The cross-layer edge rule requires the chosen original vertices to be distinct and pairwise adjacent, so their originals form a `k`-clique in `G`.

Conversely, order the vertices of any `k`-clique arbitrarily and choose its `r`th vertex in layer `r`. Every required cross-layer edge exists, all tautological formulas accept, and the trivial hash accepts.

Thus the layered slice computes exactly `CLIQUE_{m,k}`.

## Circuit transfer

Suppose the formal layered language had polynomial-size circuits with at most `floor((1/6) log log m)` NOT gates on this slice. Compose such a circuit with the polynomial projection above. Fixing the non-graph input bits to the canonical layer, formula, mask, and hash encodings does not increase size or NOT count. The resulting circuit computes `CLIQUE_{m,k(m)}` with the same asymptotic size and no more NOT gates.

This contradicts the Amano--Maruoka theorem.

## Theorem

For the explicit layered family obtained from `k(m)` above, every Boolean circuit with at most

```text
floor((1/6) log log m)
```

NOT gates has superpolynomial size.

This theorem is unconditional once the published lower bound is taken as input. It is a genuine completed lower bound for the formal layered language, but it does not apply to unrestricted polynomial-size circuits.