# Review of the Augmented-Hash and Audit-Soundness Drafts

## Status

The uploaded continuations contain a useful gadget idea, but they do not close the proof. The strongest salvageable contribution is the addition of free field elements `z_i`, which can act as an assignment-level adjuster after a witness clique has already been selected. The drafts still leave the clique-selection, audit-soundness, representation, and monotone-projection steps open.

## 1. What the free `z_i` gadget actually proves

Let every selected block carry a free value `z_i ∈ F_q`, and require

```text
Σ_{i∈C} s_i z_i = 0,
```

with every `s_i ≠ 0`.

After a clique `C` and satisfying assignments for its CNFs are known, one designated block `v_t` can absorb the residue:

```text
z_{v_t} = -s_{v_t}^{-1} Σ_{i∈C\{v_t}} s_i z_i.
```

Therefore the linear equation does not obstruct assignment extraction. This is a valid local completion observation.

It does **not** isolate a clique or solve clique extraction. Indeed, because one free coordinate can always absorb the residue, the linear condition is existentially vacuous with respect to the choice of `C`: every clique with satisfiable blocks has some `z`-assignment satisfying the equation.

## 2. The current FORCE operation still does not pin the prefix

The draft's greedy extractor repeatedly asks whether `FORCE(I,T∪{v})` is YES. The stated FORCE operation removes vertices incompatible with `T`, but it does not require the next witness to contain `T`.

A YES answer may therefore be witnessed by a clique avoiding one or more vertices already placed in `T`. The induction

```text
current T ⊆ one fixed surviving witness C*
```

is not justified after the first oracle-selected vertex.

The required replacement must satisfy the exact equivalence

```text
L(FORCE*(I,T)) = 1
iff
there exists a valid witness C of I with T ⊆ C.
```

Possible rigorous encodings include:

1. a partial-witness field `T` included in the language and checked by the verifier;
2. the standard common-neighborhood reduction, with target clique size changed from `t` to `t-|T|`, plus a length-preserving padding theorem;
3. a selector gadget that makes every valid size-`t` witness include designated vertices.

Until one of these is formalized, neither deterministic Hash-Extendability nor decision-to-witness extraction follows.

## 3. NP-hardness of the augmented language is not NP-hardness of the audit slice

Setting the clique hash to the trivial map and all block formulas to tautologies can establish ordinary NP-hardness of a broad augmented language, assuming the encoding is polynomial.

That does not establish hardness under the unique-witness, focused, resampled, or amplified distributions used by the audits. A separate reduction theorem must state its exact type:

- deterministic many-one;
- randomized reduction;
- promise reduction;
- or nonuniform Turing reduction.

Valiant--Vazirani isolation cannot be silently converted into deterministic many-one NP-hardness.

## 4. The proposed Friedgut calculation has a fatal arithmetic error

The audit-soundness draft states

```text
I(f) ≤ B ε = n^5 · n^-2 = n^3,
η = n^-2,
K ≤ 2^{O(I(f)/η^2)}.
```

Even accepting that stated theorem form, the substitution is

```text
I(f)/η^2
= n^3 / (n^-2)^2
= n^3 / n^-4
= n^7,
```

not `1/n`. Hence the claimed bound is

```text
K ≤ 2^{O(n^7)},
```

not a constant-size junta.

This alone invalidates the claimed completion of Audit Soundness.

Also, `1/n^2` is inverse-polynomial, not negligible in the standard complexity-theoretic sense. A negligible function must eventually be smaller than `1/n^c` for every constant `c > 0`.

## 5. BRC on conditioned YES slices does not give the claimed global influence bound

The BRC statement concerns resampling blocks outside a particular displayed witness on a conditioned YES distribution. The draft then concludes

```text
Inf_i[f] ≤ 1/n^2 for every block i
```

under a global distribution over all instances. That conclusion does not follow.

Missing steps include:

1. an exact named distribution over encodings;
2. treatment of NO instances;
3. treatment of YES instances with multiple witnesses;
4. conversion from conditional resampling disagreement to unconditional block influence;
5. control of the probability that `i` lies in every surviving witness;
6. a valid amplification argument with quantified dependence on `B`, `t`, and circuit size.

The assertion that an event of probability `1/poly(n)` is automatically much smaller than `1/n^2` is also false without specifying the polynomial's degree.

## 6. Function approximation cannot establish syntactic LocalNOT

Influence and junta theorems characterize Boolean functions under distributions. `LocalNOT` is a property of a particular circuit representation.

The same function can have:

- a circuit with only local negations;
- another equivalent circuit with redundant cross-block negations;
- or a circuit in which nonlocal negations cancel algebraically.

Therefore

```text
f is close to a block junta
```

cannot directly imply

```text
the given circuit's NOT gates are block-local.
```

A separate reconstruction theorem is required. It must construct a new small circuit in an explicitly defined restricted model from the semantic decomposition.

## 7. SPA is currently a desired conclusion, not a proof

The statement that a cross-block NOT would be exposed by a star/pair swap is only a proof sketch. To become a theorem, SPA needs:

1. exact gadget definitions;
2. the distribution of gadget inputs;
3. a quantitative test-to-structure theorem;
4. an explicit reconstruction algorithm;
5. error accumulation bounds;
6. circuit-size accounting.

Graph automorphism invariance by itself does not imply gate locality.

## 8. The monotone projection still needs a stronger representation theorem

Fixing all formula blocks, `z` values, and hash inputs leaves the graph `H` live. To conclude that the remaining circuit is monotone in the edge variables, the reconstructed model must prohibit every surviving negation from depending on graph bits.

The current LocalNOT definition is ambiguous about graph and seed inputs. If graph-edge negations are allowed, the projection need not be monotone. If they are forbidden, that stronger restriction must be derived, not assumed.

The safer target is:

```text
monotone circuits in graph-edge variables
with bounded local oracle gates on auxiliary blocks.
```

Then one must prove a lower bound for that exact oracle model.

## 9. Corrected theorem dependency

The most defensible current chain is:

```text
Free z-adjuster lemma
    => assignment-level linear completion after C is fixed.

Exact prefix-pinning self-reduction
    => decision-to-witness extraction.                 [open]

Audit identities
    => function-level block decomposition.             [open]

Block decomposition
    => small monotone-with-local-oracles representation.[open]

Hard CLIQUE projection for that model
    => contradiction with a matching lower bound.      [open]
```

The uploaded drafts improve the first line only. They do not establish the remaining four implications, and they should not be merged as a completed separation proof.