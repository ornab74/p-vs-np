# Vertex-Support Orientation Lower Bound for the Layered CLIQUE Slice

## 1. Motivation

Orientation weight counts graph-edge coordinates. For graph functions this can be unnecessarily pessimistic: a large set of oriented edges may all lie inside a small set of graph vertices.

Koroth and Sarma prove a stronger structural lower bound using the number of vertices touched by the oriented edge coordinates. This note transfers that theorem to the trivial-hash layered CLIQUE slice.

## 2. Vertex support of an orientation

Let `beta` be an orientation vector indexed by graph edges.

Define

```text
VSupp(beta)
```

to be the set of graph vertices incident to at least one edge `e` with

```text
beta_e = 1.
```

The vertex-support size is

```text
vsupp(beta) = |VSupp(beta)|.
```

A gate may therefore have large orientation weight but small vertex support when all oriented edges are concentrated in a small induced subgraph.

## 3. Published theorem used

Koroth and Sarma prove that if a depth-`d` circuit computes CLIQUE and every gate `g` has an orientation `beta_g` whose oriented edge coordinates touch at most `w` graph vertices, then

```text
d w = Omega(n / log n).
```

Their communication argument sends the touched vertices and, on the negative input side, the partition labels of those vertices. The partition labels account for the logarithmic factor.

## 4. Layered CLIQUE slice

For graph size `n` and clique parameter `r`, define

```text
LayerClique(n,r)(G) = L_layer(I_G)
```

using the standard layered projection:

1. `r` positional layers, each a copy of `[n]`;
2. tautological local formulas;
3. open vertex and assignment masks;
4. trivial hash;
5. a cross-layer edge between copies of `u` and `v` iff `u != v` and `{u,v}` is an edge of `G`.

Then

```text
LayerClique(n,r) = CLIQUE(n,r)
```

pointwise as a function of the original graph-edge variables.

## 5. Transferred theorem

### Theorem

Let `C_layer` be a bounded-fan-in circuit of depth `d` computing a standard hard layered CLIQUE slice on graphs with `n` vertices.

Assume that every internal gate `g`, considered as a Boolean function of the original graph-edge variables, has an orientation `beta_g` satisfying

```text
vsupp(beta_g) <= w.
```

Then

```text
d w = Omega(n / log n).
```

### Proof

Because the layered slice is exactly the corresponding CLIQUE function, `C_layer` is a circuit for CLIQUE on the same graph variables. The orientation and its incident-vertex set are unchanged. Applying the published vertex-support theorem gives the bound.

## 6. Consequences

If

```text
w = polylog(n),
```

then

```text
d = Omega(n / polylog(n)).
```

More precisely, if

```text
w = O(log^b n),
```

then

```text
d = Omega(n / log^(b+1) n).
```

Thus polylogarithmic-depth circuits cannot compute the layered slice when every gate's nonmonotonicity is confined to a polylogarithmic-size vertex set.

This theorem is incomparable with the raw orientation-weight bound:

- a gate may orient many edges among few vertices, making vertex support much smaller than weight;
- a gate may orient a sparse matching across many vertices, making weight smaller than vertex support.

## 7. Certificate model

A certificate for a gate `g` consists of:

1. an orientation bit-vector `beta_g` over graph edges;
2. a monotone extension or a complete finite truth-table check establishing that `beta_g` is an orientation;
3. the incident vertex set `VSupp(beta_g)`;
4. verification that `|VSupp(beta_g)| <= w`.

For circuits with a small number of graph variables this is mechanically testable by exhaustive truth-table analysis. For asymptotic circuits, polynomial verification requires succinct monotone-extension certificates or a restricted gate basis.

## 8. Uniform-orientation submodel

A stronger special case occurs when every gate shares one orientation `beta`.

The published uniform-orientation theorem shows that if there is a vertex subset `U` of size at least

```text
log^(k+epsilon) n
```

such that no edge internal to `U` is oriented, then a circuit for CLIQUE must have depth

```text
omega(log^k n).
```

The same conclusion transfers to the layered slice.

The paper also gives a transformation from an arbitrary depth-`d` CLIQUE circuit to an equivalent uniform-orientation circuit whose orientation avoids an arbitrary vertex set of size approximately `d`. The gap between the available avoided-set size and the lower-bound threshold is itself identified there as an avenue toward separating NP from NC.

## 9. Remaining bridge

The current layered audits do not bound vertex support of gate orientations.

A meaningful new graph-sensitive condition would need to imply one of:

```text
vsupp(beta_g) <= polylog(n) for every gate g;
```

or

```text
all but a small number of gates have small vertex support;
```

or

```text
a common orientation avoids a sufficiently large induced vertex set.
```

Any of these would activate a published depth lower bound without requiring a full monotone conversion.