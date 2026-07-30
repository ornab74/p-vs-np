# Formal Layered Language and Complete Same-Length Self-Reduction

This note defines the repaired witness language used by the proof-audit branch. Its purpose is precise:

1. remove permutation multiplicity from clique witnesses;
2. give a deterministic NP-hardness reduction;
3. pin both selected vertices and assignment bits without changing circuit input length;
4. isolate the remaining audit, representation, and lower-bound obligations.

It does **not** prove a circuit lower bound.

## 1. Fixed-width parameters

For each input length parameter `n`, fix polynomially bounded quantities:

- `t=t(n)`: number of positional layers;
- `B=B(n)`: maximum total number of vertices;
- `d=d(n)`: assignment width attached to a selected vertex;
- `c=c(n)`: padded formula-encoding width;
- `m=m(n)`: hash output width.

The vertex set is partitioned into disjoint layers

```text
V = V_1 disjoint-union ... disjoint-union V_t,
```

with `|V| <= B`. Empty padding slots are allowed so every instance of the same parameter length has the same encoding width.

Each vertex `v` has:

- a padded Boolean formula encoding `phi_v` of width `c` over `d` local variables;
- an assignment mask `R_v` encoded by two bits per coordinate, specifying whether `0`, `1`, or both values are allowed;
- a candidate bit in the positional mask `A_r` when `v in V_r`.

A canonical padded tautology `TOP` and contradiction `BOT` are fixed for every width.

## 2. Instances and witnesses

An instance is

```text
I = (V_1,...,V_t, H, Phi, A_1,...,A_t, R, S),
```

where:

- `H` is a `t`-partite graph with edges only between distinct layers;
- `Phi=(phi_v)_{v in V}` is the tuple of padded local formulas;
- `A_r subseteq V_r` is the allowed-vertex mask for position `r`;
- `R=(R_v)_{v in V}` is the tuple of fixed-width assignment masks;
- `S` is a seed for a polynomial-time hash family.

A witness is

```text
W = ((v_1,...,v_t), alpha_1,...,alpha_t)
```

with `v_r in V_r` and `alpha_r in {0,1}^d`.

The verifier accepts exactly when:

1. `v_r in A_r` for every `r`;
2. every cross-layer pair `{v_r,v_s}` is an edge of `H`;
3. `alpha_r` obeys the mask `R_{v_r}`;
4. `alpha_r` satisfies `phi_{v_r}`;
5. `Hash_S(W)=0^m`.

Call the language `L_layer^hash`.

Because the layers are disjoint and the witness chooses exactly one vertex from each layer, there is no `t!` multiplicity from ordering a single ordinary clique. The order is the layer order.

## 3. Membership in NP

The witness length is polynomial. Verification checks:

- `t` candidate-mask bits;
- `O(t^2)` graph edges;
- `t*d` assignment-mask bits;
- `t` padded formulas;
- one polynomial-time hash evaluation.

Therefore `L_layer^hash in NP` whenever all named parameters and the hash evaluator are polynomially bounded.

## 4. Deterministic NP-hardness of the trivial-hash slice

We reduce 3SAT to the slice with `m=0`, so the hash predicate is vacuous.

Let

```text
F = C_1 AND ... AND C_t
```

be a 3CNF. Create one layer `V_r` for clause `C_r`. A vertex in `V_r` represents one satisfying truth assignment to the variables occurring in `C_r`; there are at most seven such assignments.

Connect vertices in different layers exactly when their local assignments agree on every variable that occurs in both clauses.

Set:

- every candidate mask `A_r = V_r`;
- every local formula `phi_v = TOP`;
- every assignment mask unrestricted;
- `m=0`.

If `F` is satisfiable, its global satisfying assignment chooses a mutually compatible satisfying local assignment in every layer, producing a layered clique. Conversely, pairwise compatibility of the selected local clause assignments yields a consistent assignment on every variable appearing in the formula, and every clause is satisfied.

The construction has `O(t)` vertices and `O(t^2)` potential edges and is polynomial-time. Hence the unrestricted, polynomially encoded trivial-hash slice is NP-hard. Together with membership, it is NP-complete.

This statement does **not** establish NP-hardness for an arbitrarily fixed relation such as `t=log^2 n`; that requires a separate padding theorem.

## 5. Exact vertex pinning

For a positional prefix

```text
P = (u_1,...,u_k),  u_r in V_r,
```

define `PINVERT(I,P)` by replacing

```text
A_r <- {u_r}  for r <= k
```

and leaving every other fixed-width field unchanged.

### Lemma 5.1: exact vertex pinning

For every instance `I` and valid positional prefix `P`,

```text
L_layer^hash(PINVERT(I,P)) = 1
```

if and only if `I` has a valid witness whose first `k` selected vertices are exactly `P`.

### Proof

A witness of the pinned instance must select `u_r` from each singleton mask. All other checks are unchanged, so it is a witness of `I` extending `P`. Conversely, a witness of `I` extending `P` obeys all singleton masks and remains valid after pinning.

The transform changes bits inside a fixed-width mask and therefore preserves input length.

## 6. Exact assignment-bit pinning

Suppose position `r` has already been vertex-pinned to `v_r`. For coordinate `j` and bit `b`, define

```text
PINBIT(I,r,j,b)
```

by changing the two-bit mask for coordinate `j` of `R_{v_r}` to allow only `b`.

### Lemma 6.1: exact bit pinning

For every instance in which position `r` is pinned to `v_r`,

```text
L_layer^hash(PINBIT(I,r,j,b)) = 1
```

if and only if the current instance has a valid witness with `alpha_r[j]=b`.

The proof is the same singleton-mask argument. The formula encoding itself is not rewritten, so the circuit input length remains unchanged.

## 7. Complete same-length decision-to-witness extraction

Assume a worst-case correct decision circuit `D_n` for the fixed-width language at length `n`.

### Vertex phase

For `r=1,...,t`:

1. enumerate `v in A_r`;
2. query `D_n` on the instance with the previous choices and `v` vertex-pinned;
3. retain the first `v` receiving YES.

The exact vertex-pinning lemma guarantees that every retained prefix extends to a full witness.

### Assignment phase

After every vertex is pinned, process each assignment coordinate. Query the instance with the coordinate pinned to `0`; keep `0` on YES and otherwise pin `1`.

The exact bit-pinning lemma guarantees continuation.

### Complexity

The number of oracle calls is at most

```text
sum_r |V_r| + t*d <= B + t*d,
```

which is polynomial. Every query has exactly the same input length as the original instance.

Thus, for the repaired layered language,

```text
worst-case decision correctness
=> polynomial same-length witness extraction.
```

No Hash-Extendability assumption is required.

## 8. Polynomial positional focus

Given a verified witness `W=((v_1,...,v_t),alpha_1,...,alpha_t)`, define `FOCUS(I,W)` by:

1. setting every `A_r={v_r}`;
2. retaining only the selected cross-layer edges `{v_r,v_s}`;
3. replacing every unselected formula by the canonical padded contradiction `BOT`;
4. leaving selected formulas, assignment masks, and the hash seed unchanged.

The transform scans the fixed-width encoding and is polynomial-time.

If `Verify(I,W)=1`, then `W` remains a witness of `FOCUS(I,W)`. Every witness of the focused instance uses the same selected vertex tuple, although multiple selected assignments may remain when formulas or the hash allow them.

## 9. Exact trivial-hash focused slice

Further restrict a focused instance by setting `m=0`, retaining the selected clique edges, and varying only the selected formulas and assignment masks.

Define the local predicate

```text
P_r(phi_{v_r},R_{v_r}) = 1
iff
there exists alpha in {0,1}^d obeying R_{v_r} and satisfying phi_{v_r}.
```

Then the restricted language is exactly

```text
L_focus = AND_{r=1}^t P_r.
```

This is a function identity. It does not imply that an arbitrary circuit computing the function has a block-local or monotone representation.

## 10. Remaining obligations

The completed language and self-reduction do not prove:

1. that seed resampling is valid for an unspecified hash encoding;
2. that a star/pair identity forces any circuit representation;
3. that semantic stability gives LocalNOT syntax;
4. that a small nonmonotone circuit for the graph projection converts to a small monotone circuit or monotone circuit with local oracles;
5. that known CLIQUE lower bounds apply to the resulting model.

Those remain separate theorem obligations.