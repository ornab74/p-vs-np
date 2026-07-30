# Sparse-Orientation Depth Lower Bound for the Layered Language

## 1. Purpose

This note records a second unconditional restricted-circuit theorem for the formal layered language. It uses the semantic orientation measure of Koroth and Sarma rather than raw NOT-gate count.

It does not prove an unrestricted size lower bound and does not imply `NP not subseteq P/poly`.

## 2. Orientation

For a Boolean function `f:{0,1}^N -> {0,1}`, a vector `beta in {0,1}^N` is an orientation of `f` if there exists a monotone Boolean function `h:{0,1}^{2N} -> {0,1}` such that

```text
f(x) = h(x, x xor beta)
```

for every `x`.

The weight `|beta|` is the number of original variables whose complemented rails are needed.

For a circuit `C`, say that `C` is gate-wise weight-`w` oriented if every internal gate `g`, regarded as a Boolean function of the original input variables, has some orientation `beta_g` satisfying

```text
|beta_g| <= w.
```

This is a semantic restriction on every gate function. It is not a bound on the number of syntactic NOT gates.

## 3. Published input theorem

Koroth and Sarma prove the following depth-orientation tradeoff.

> Let `C` be a bounded-fan-in Boolean circuit of depth `d` computing a monotone Boolean function `f` that is sensitive on all of its input variables. If every internal gate has an orientation of weight at most `w>0`, then
>
> ```text
> d(4w+1) >= KW^+(f),
> ```
>
> where `KW^+(f)` is the deterministic communication complexity of the monotone Karchmer--Wigderson relation of `f`.

For the standard CLIQUE family used in their paper, the known monotone Karchmer--Wigderson lower bound is linear in the number `m` of graph vertices. Thus

```text
d(4w+1) = Omega(m).
```

Reference: Sajin Koroth and Jayalal Sarma, *Depth Lower Bounds against Circuits with Sparse Orientation*, arXiv:1404.7443.

## 4. Layered projection

Fix a graph size `m` and clique parameter `k`. Build a trivial-hash layered instance from a graph `G` on `[m]`:

1. create `k` layers `V_1,...,V_k`, each containing one copy `(r,v)` of every `v in [m]`;
2. set every local formula to the same canonical tautology;
3. open every vertex and assignment mask;
4. use hash length zero;
5. for `r != s`, place the cross-layer edge

```text
((r,u),(s,v))
```

exactly when

```text
u != v and {u,v} in E(G).
```

Then

```text
G has a k-clique
iff
the layered instance is YES.
```

Every variable cross-layer edge is either an original graph-edge variable or the constant zero. Every auxiliary input is fixed to a constant.

## 5. Orientation under restriction and projection

Suppose a circuit `C_layer` computes the layered language and every gate of `C_layer` has orientation weight at most `w` with respect to the full layered input.

Restrict all auxiliary coordinates to the constants in the projection and identify duplicated cross-layer copies of an original graph edge with the corresponding graph variable. The resulting circuit `C_clique` computes CLIQUE.

For every restricted gate, an orientation is obtained from its old orientation by:

1. deleting fixed coordinates;
2. merging coordinates identified with the same graph variable;
3. setting a merged orientation bit to one if any preimage orientation bit was one.

Consequently, orientation weight does not increase:

```text
weight(beta'_g) <= weight(beta_g) <= w.
```

Circuit depth also does not increase.

## 6. Transferred theorem

### Theorem

Let `C_layer` be a bounded-fan-in circuit computing the trivial-hash layered slice corresponding to the standard CLIQUE family on `m` graph vertices. If

```text
depth(C_layer) = d
```

and every internal gate has orientation weight at most `w`, then

```text
d(4w+1) = Omega(m).
```

### Proof

Apply the layered-to-CLIQUE restriction and projection. The resulting circuit computes the CLIQUE function, has depth at most `d`, and remains gate-wise weight-`w` oriented. The Koroth--Sarma theorem then gives the claimed inequality.

## 7. Consequences

If

```text
w = polylog(m),
```

then the layered slice requires depth

```text
Omega(m / polylog(m)).
```

In particular, it has no polylogarithmic-depth bounded-fan-in circuit family whose internal gates all have polylogarithmic orientation weight.

More generally, for every fixed `a,b >= 0`, circuits satisfying

```text
d = O(log^a m)
```

and

```text
w = O(log^b m)
```

cannot compute this layered CLIQUE slice for all sufficiently large `m`.

## 8. What this theorem does not say

It does not show that ordinary polynomial-size circuits have sparse gate orientations.

It does not derive orientations from BRC, SRC, SPA, or any black-box semantic audit.

It does not yield a superpolynomial size lower bound, because a depth lower bound alone only implies that size is at least the depth.

It does not separate `P` from `NP` or `NP` from `P/poly`.

## 9. Exact remaining bridge

A useful unrestricted advance would need a theorem converting an arbitrary small circuit for the layered language into one of the following without losing pointwise correctness:

1. a circuit whose every gate has small orientation weight;
2. a circuit with few dense-orientation gates and many sparse-orientation gates in a regime covered by a published lower bound;
3. a bounded-locality CLO whose oracle rectangles encode the dense-orientation exceptional pairs.

The present black-box audits do not establish any of these properties.