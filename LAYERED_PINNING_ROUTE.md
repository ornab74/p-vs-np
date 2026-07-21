# Exact Layered Witness Pinning Route

This note replaces the current graph-only `FORCE(I,T)` operation with an exact self-reduction. It repairs the decision-to-witness step, but it does **not** repair audit soundness or the LocalNOT-to-monotone step.

## 1. Why the original FORCE operation is insufficient

The current operation deletes vertices outside `T` that are not adjacent to every vertex in `T`. A surviving clique may still avoid `T`. Consequently,

```text
L(FORCE(I,T)) = 1
```

does not imply that a valid witness containing `T` exists.

A greedy extractor requires the exact equivalence

```text
L(PIN(I,T)) = 1
iff
there is a valid witness of I extending T.
```

## 2. Layered masked language

Fix a graph `H` on vertex set `[B]` and a witness length `t`. Add `t` candidate masks

```text
A_1, ..., A_t subseteq [B].
```

Each mask is encoded as a `B`-bit vector, so changing a mask does not change the input length.

An instance is

```text
I = (H, Psi, A_1, ..., A_t, S),
```

where `Psi = (psi_1,...,psi_B)` is the tuple of disjoint block formulas and `S` is the hash seed.

A witness is an ordered tuple

```text
W = ((v_1,...,v_t), beta_{v_1},...,beta_{v_t})
```

satisfying:

1. `v_r in A_r` for every position `r`;
2. the vertices `v_1,...,v_t` are distinct;
3. every pair `{v_r,v_s}` is an edge of `H`;
4. `beta_{v_r}` satisfies `psi_{v_r}`;
5. `h_S(v_1,...,v_t)=0`.

Call this language `L_layer^hash`.

The hash is applied to the ordered witness encoding. Pairwise-independent hashing and witness verification remain polynomial-time because the tuple has polynomial length.

## 3. Basic complexity facts

### Membership in NP

The tuple, assignments, mask membership, distinctness, all clique edges, and the hash value are polynomial-time verifiable.

### Deterministic NP-hardness of the un-hashed slice

Map a CLIQUE instance `(H,t)` to:

```text
A_r = [B] for all r,
psi_v = true for all v,
hash length m = 0.
```

There is a valid ordered tuple iff `H` has a `t`-clique. Each ordinary clique has `t!` ordered encodings, which does not affect existence.

This establishes a clean deterministic reduction for the trivial-hash slice. Any claim about randomized Valiant--Vazirani isolation must still state the reduction type separately.

## 4. Exact PIN transform

For a partial ordered prefix

```text
P = (u_1,...,u_k),
```

define `PIN(I,P)` by replacing

```text
A_r <- {u_r} for r <= k
```

and leaving all later masks, formulas, the graph, and the hash seed unchanged.

Because masks have fixed-width encodings, `PIN(I,P)` has the same input length as `I`.

### Exact pinning lemma

For every instance `I` and prefix `P`,

```text
L_layer^hash(PIN(I,P)) = 1
```

if and only if `I` has a valid witness whose first `k` positions equal `P`.

#### Proof

A witness for the pinned instance must choose `u_r` in every singleton mask `{u_r}`, so it extends `P`. Conversely, any witness of `I` extending `P` obeys the singleton masks and remains a witness after pinning. No probabilistic extendability statement is needed.

## 5. Decision-to-witness extraction

Assume a worst-case correct decision circuit for `L_layer^hash`.

For positions `r=1,...,t`:

1. iterate through `v in A_r` not already selected;
2. query the decision circuit on `PIN(I,(v_1,...,v_{r-1},v))`;
3. retain the first `v` producing YES.

The exact pinning lemma guarantees that every retained prefix has a full hash-zero completion. At the end, the selected tuple is a valid clique tuple satisfying the original hash condition.

Assignments can then be extracted by ordinary literal pinning within the already selected blocks. Formula encodings must reserve padding so literal restrictions remain at the same circuit input length.

The number of oracle calls is at most `B*t` plus the total number of formula variables, hence polynomial for polynomially encoded parameters.

## 6. What this route actually repairs

It repairs the theorem obligation:

```text
worst-case decision correctness
=> polynomial decision-to-witness extraction.
```

It also shows that the former Hash-Extendability lemma was compensating for an inexact query transformation rather than a necessary property of hashing.

The free field variables `z_i` may still be useful for assignment-level algebraic completion, but they are unnecessary for clique-prefix extraction once masks provide exact pinning.

## 7. What remains open

This route does not imply any of the following:

1. semantic audit compliance gives a syntactic LocalNOT circuit;
2. low output influence bounds the influence of an internal NOT gate;
3. SPA identities characterize circuit representations;
4. LocalNOT circuits become monotone after auxiliary inputs are fixed;
5. the resulting model is covered by ordinary monotone CLIQUE lower bounds.

Those must be stated as separate function-decomposition, representation, and lower-bound theorems.

## 8. Next falsifiable target

Define a function class `BlockCompose(q)` consisting of functions of the form

```text
G(H,S, y_1(psi_1), ..., y_B(psi_B)),
```

where each `y_i` is block-local and `G` is monotone in the local outputs and graph-edge variables.

The next useful theorem is not "audits force every NOT gate to be local." It is:

> Passing a precisely stated audit distribution implies closeness, under that same distribution, to `BlockCompose(q)` with explicit error and size parameters.

Only after proving that function-level statement should the project seek a representation theorem and a monotone-with-local-oracles lower bound.