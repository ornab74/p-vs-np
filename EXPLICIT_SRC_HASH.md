# Explicit Polynomial Hash with Exact SRC Factorization

This note instantiates the seed-resampling audit for the formal layered language. The construction is a pairwise-independent affine hash on the complete sparse witness encoding, organized into independent per-vertex seed blocks.

It repairs the statement "resample seed entries irrelevant to the witness" by defining exactly which seed entries are unused.

## 1. Sparse witness encoding

Let every local assignment have width `d`. For each vertex `v`, define a block

```text
z_v(W) in F_2^(d+1)
```

by

```text
z_v(W) = (1, alpha_r)  if W selects v at layer r,
z_v(W) = 0^(d+1)      otherwise.
```

The leading presence bit distinguishes an unselected vertex from a selected vertex carrying the all-zero assignment.

Concatenating all vertex blocks gives a polynomial-length sparse encoding `z(W)`.

## 2. Seed and hash definition

For output width `m`, sample the seed

```text
S = (b, (A_v)_{v in V}),
```

where

- `b` is uniform in `F_2^m`;
- each `A_v` is an independent uniform matrix in `F_2^{m x (d+1)}`.

Define

```text
h_S(W) = b XOR XOR_{v in V} A_v z_v(W).
```

Only selected vertices contribute because `A_v 0 = 0` for every unselected vertex.

The seed length is

```text
m + |V| m (d+1),
```

which is polynomial in the fixed-width instance parameters. Evaluation takes polynomial time.

## 3. Pairwise independence

### Theorem 3.1

For any two distinct witness encodings `W != W'`, the pair

```text
(h_S(W), h_S(W'))
```

is uniform on `F_2^m x F_2^m` when `S` is uniform.

### Proof

Because `W != W'`, there exists a vertex `v*` with

```text
Delta = z_{v*}(W) XOR z_{v*}(W') != 0.
```

Condition on every seed block except `A_{v*}` and `b`. The hash difference is

```text
h_S(W) XOR h_S(W') = constant XOR A_{v*} Delta.
```

For a uniform binary matrix `A_{v*}` and nonzero vector `Delta`, each row inner product is an independent uniform bit. Hence `A_{v*} Delta` is uniform in `F_2^m`, so the hash difference is uniform.

Independently, the uniform offset `b` makes `h_S(W)` uniform for every fixed choice of the other seed blocks. A uniform value together with an independent uniform difference gives a uniform ordered pair. Therefore the family is pairwise independent.

## 4. Exact used/unused seed factorization

For a displayed witness `W`, let

```text
Sel(W) = {v : z_v(W) != 0}.
```

Define

```text
S_used(W)   = (b, (A_v)_{v in Sel(W)}),
S_unused(W) = (A_v)_{v notin Sel(W)}.
```

Then

```text
h_S(W) = b XOR XOR_{v in Sel(W)} A_v z_v(W),
```

so the value is independent of every block in `S_unused(W)`.

### Corollary 4.1: exact SRC

For every instance `I`, verified witness `W`, and arbitrary replacement collection

```text
(A'_v)_{v notin Sel(W)},
```

replacing all unused matrices by `A'_v` leaves `h_S(W)` unchanged. Therefore `W` remains a witness, and the transformed instance remains YES.

This is pointwise and distribution-free; no approximation theorem is needed.

## 5. Isolation status

Because the family is pairwise independent on complete witness encodings, it is compatible with the standard Valiant--Vazirani style randomized isolation analysis after the output width or target level is sampled appropriately.

The exact claim supported here is limited:

- polynomial seed and evaluation: proved;
- pairwise independence: proved;
- pointwise SRC on unused vertex seed blocks: proved;
- deterministic many-one NP-hardness of the nontrivial hashed language: **not** proved;
- guaranteed isolation on every instance: **not** proved.

Any use of isolation must separately state its randomized reduction, promise, and inverse-polynomial success probability.

## 6. Interaction with pinning and focus

Vertex and assignment pinning leave the seed unchanged. Once a witness is extracted and verified, positional focus preserves the selected vertex blocks and therefore preserves the hash calculation.

Off-witness seed matrices may then be resampled arbitrarily without affecting the displayed witness. This instantiates SRC exactly for the repaired layered language.

## 7. Limitation

Exact SRC is a semantic YES-preservation theorem. It does not imply:

- low global seed influence under an unnamed distribution;
- syntactic locality of gates reading seed bits;
- monotonicity in graph edges;
- a polynomial monotone-CLO representation.

Those remain separate obligations.