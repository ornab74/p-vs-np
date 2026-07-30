# Layered Audit Specification

This note restates the audit suite for the formal positional language in `FORMAL_LAYERED_LANGUAGE.md`. It separates exact language identities from proposed statistical tests and from representation claims.

## 1. Instance and witness notation

An instance is

```text
I = (V_1,...,V_t, H, Phi, A_1,...,A_t, Rho, S).
```

A verified witness is

```text
W = ((v_1,...,v_t), alpha_1,...,alpha_t)
```

with `v_r in V_r`, `v_r in A_r`, all required cross-layer edges present, each assignment satisfying the selected block formula and mask, and the hash predicate accepting the ordered encoding.

Every audit below is conditioned on a witness that has first been verified. This condition is essential: without it, the transformation need not preserve the language.

## 2. WV: witness verification

### Exact statement

There is a deterministic polynomial-time predicate `Verify(I,W)` such that

```text
Verify(I,W)=1 iff W is a valid witness of I.
```

The runtime is polynomial in the fixed-width instance encoding because it checks:

- one membership bit in each vertex mask;
- `O(t^2)` graph edges;
- one assignment-mask bit for each assignment coordinate;
- all selected block clauses;
- one polynomial-time hash evaluation.

This is proved.

## 3. Positional FOCUS

For a verified witness tuple `v=(v_1,...,v_t)`, define `FOCUS(I,W)` as follows:

1. replace each vertex mask `A_r` by the singleton `{v_r}`;
2. retain the selected block formulas and assignment masks;
3. delete every graph edge except the cross-layer edges among the selected vertices;
4. optionally replace every unselected block formula by a fixed canonical unsatisfiable padded formula;
5. leave the hash seed unchanged.

### Exact identity

```text
Verify(I,W)=1  =>  L(FOCUS(I,W))=1.
```

Moreover, every witness of the focused instance uses exactly the same positional tuple `v`. Assignment multiplicity may remain if selected formulas have several satisfying assignments and the hash depends on assignments.

### Complexity

The transform scans the fixed-width graph, masks and formulas once and therefore runs in polynomial time.

This is a one-sided certified identity. It is not the statement `L(I)=L(FOCUS(I,W))` for arbitrary `(I,W)`; the premise `Verify(I,W)=1` is part of the theorem.

## 4. BRC: off-witness block resampling

Let `j` be a vertex not equal to any selected `v_r`. Let `ResampleBlock(I,j,z)` replace only the padded encoding of block `phi_j` and its assignment masks by a value `z` of the same width.

### Exact YES-preservation identity

For every verified witness `W` avoiding `j` and every replacement `z`,

```text
Verify(I,W)=1
=>
Verify(ResampleBlock(I,j,z),W)=1
=>
L(ResampleBlock(I,j,z))=1.
```

No distributional theorem is needed for this semantic statement.

### Important limitation

This proves only preservation of YES on a displayed-witness slice. It does not prove:

- preservation on arbitrary NO instances;
- small global influence under an arbitrary input distribution;
- syntactic locality of a circuit;
- closeness to a monotone representation.

A statistical BRC test must name its distribution and the rule used to select a verified witness.

## 5. SRC: seed resampling

An exact SRC identity requires an explicit seed factorization.

Suppose the seed is encoded as

```text
S = (S_used(W), S_unused(W))
```

and hash verification of `W` depends only on `S_used(W)`. Then replacing `S_unused(W)` preserves `W`.

### Exact conditional statement

If

```text
Hash(S,W) = Hash(S_used(W),W)
```

for all seeds and witnesses, then for every replacement `z`,

```text
Verify(I,W)=1
=>
Verify(ResampleUnusedSeed(I,W,z),W)=1.
```

### Current status

This is a schema, not yet an instantiated theorem. Standard dense linear or pairwise-independent hashes generally mix all seed bits into the value on `W`; the phrase "seed entries irrelevant to W" must be defined by the chosen hash representation. SRC cannot be claimed until that representation and factorization are supplied.

A safe redesign is to include per-position seed tables and resample table entries outside the selected positional coordinates. The encoding size and independence properties must then be accounted for explicitly.

## 6. SPA: star/pair associativity

The repository currently uses SPA as a proposed structure-forcing mechanism but does not provide one complete tuple of:

1. the star instance constructor;
2. the pair instance constructor;
3. the exact language identity connecting their outputs;
4. the distribution over gadget parameters;
5. the theorem derived from passing the test.

Therefore SPA is not yet a formal audit.

To become one, it must be stated in the form

```text
for all valid gadget inputs x,
L(Star(x)) = F(L(Pair_1(x)),...,L(Pair_m(x)))
```

for an explicit Boolean function `F`, with every constructor polynomial-time and length-preserving.

Even after such an identity is proved, it constrains the computed function only. A separate representation theorem is required to derive a circuit model such as `BlockCompose` or monotone circuits with local oracles.

## 7. A valid product-measure decomposition theorem

After positional FOCUS, fix the selected witness coordinates and let the off-witness block encodings be independent under a product measure `mu`.

For each off-witness block `j`, let `X^(j)` independently resample coordinate `j`, and define

```text
Inf_j^res(f) = Pr[f(X) != f(X^(j))].
```

Then there exists a function `g` depending only on the fixed witness coordinates such that

```text
Pr[f(X) != g(X_W)]
<= sum_{j outside W} Inf_j^res(f).
```

This is the conditional Efron--Stein/majority theorem recorded in `FUNCTION_DECOMPOSITION_AND_CLO_ROUTE.md`.

It is the correct semantic endpoint of BRC-style stability. It does not imply LocalNOT syntax.

## 8. Status table

| Audit | Exact semantic identity | Efficient transform | Current status |
|---|---:|---:|---|
| WV | yes | yes | proved |
| positional FOCUS | yes, conditioned on verified witness | yes | proved |
| BRC | yes-preserving on displayed-witness slice | yes | proved |
| SRC | only after explicit seed factorization | depends on hash | open |
| SPA | no complete constructor/identity supplied | unknown | open |

## 9. Next theorem obligation

The next falsifiable task is to instantiate SRC with a concrete length-efficient hash representation and to write one exact SPA identity. Neither task should mention internal NOT gates. Afterward, the project can ask whether the resulting semantic identities imply a bounded-locality `BlockCompose` or monotone-CLO representation.
