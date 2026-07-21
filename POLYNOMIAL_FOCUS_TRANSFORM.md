# Polynomial Verified-Witness Focus Transform

The repository's earlier normalization deletes every edge participating in a competing `t`-clique. Testing whether an edge participates in such a clique by enumerating `(t-2)`-subsets is polynomial only when `t` is constant. It is not an efficient audit transformation in regimes such as `t=log^2 n`.

A much simpler normalization works whenever FOCUS is conditioned on a locally verified witness.

## 1. Definition

Let

```text
W = (C, local assignments, auxiliary values)
```

be a witness accepted by the verifier for instance `I=(H,Phi,S)`, with `|C|=t>=2`.

Define `FOCUS_W(I)` by replacing `H` with `H_C`, where

```text
E(H_C) = { {u,v} : u,v in C and u != v }.
```

Thus `C` is retained as a complete graph and every vertex outside `C` is isolated. All formula blocks, masks, seed data, and fixed-width encodings are left unchanged.

This transformation takes `O(B^2)` time and preserves the input length.

For an ordered layered witness `(v_1,...,v_t)`, use `C={v_1,...,v_t}`. Candidate masks may either remain unchanged or be pinned to the verified tuple when an exact single-witness slice is wanted.

## 2. Conditional semantic equality

### Lemma

If `Verify(I,W)=1`, then

```text
L(I) = L(FOCUS_W(I)) = 1.
```

### Proof

Because the verifier accepts, `C` is a clique in `H`, every selected formula block is satisfiable under the supplied assignment, and every hash or auxiliary witness condition holds.

The focused graph keeps every edge inside `C`, and all non-graph witness data is unchanged. Therefore the same `W` witnesses `FOCUS_W(I)`.

The original instance is also YES because `W` verifies for it. Hence both values equal one.

The claim is explicitly conditional on witness verification. It is not an identity for arbitrary pairs `(I,C)`.

## 3. Uniqueness of the graph support

In `H_C`, no `t`-clique other than `C` exists when `t>=2`: every vertex outside `C` is isolated and therefore cannot participate in a clique of size at least two.

For the layered language, pinning each position mask to the verified tuple also removes ordered permutations, leaving one ordered witness support before assignment multiplicity is considered.

## 4. Exact block-resampling closure on the focused slice

Let `j notin C`. Replacing `phi_j` by any formula cannot invalidate the verified witness because `W` uses only blocks in `C`.

Furthermore, the focused graph has no competing clique containing `j`. Thus off-witness formula blocks are semantically irrelevant to existence of a witness on this focused graph.

This proves an exact **language-level** BRC statement:

```text
L(FOCUS_W(I)) = L(Resample_j(FOCUS_W(I))) = 1.
```

It does not prove that an arbitrary circuit representation ignores block `j`, nor does it constrain internal gates.

## 5. Seed-resampling requirements

SRC requires a precisely defined seed transformation `R_C` satisfying

```text
hash_{R_C(S)}(C) = hash_S(C)
```

and preserving every auxiliary condition used by `W`.

For an affine hash family, this can be implemented by sampling a new affine map conditioned on its value at the verified witness encoding. The paper must specify:

1. the hash family;
2. the seed encoding;
3. an efficient conditional sampler;
4. the resulting distribution;
5. whether the sampler preserves pairwise independence on other witness encodings.

Calling seed coordinates "irrelevant" is insufficient when matrix entries affect many possible witnesses simultaneously.

## 6. What this repair accomplishes

This replacement removes the parameter conflict between efficient FOCUS and a growing clique size. It provides:

- quadratic-time normalization;
- same-length instances;
- a single surviving graph support;
- exact off-support semantic irrelevance;
- a clean starting slice for function-level analysis.

It still does not establish:

```text
semantic closure => LocalNOT circuit syntax.
```

The next theorem must concern the computed function under an explicitly named conditional distribution, followed by a separate representation theorem.