# Capacity-Wide Proof Audit

## Status

This repository contains an interesting **research program**, not a proof that `NP ⊄ P/poly` or `P ≠ NP`.

The current materials correctly identify several ambitious intermediate goals, but the dependency graph has more than one unresolved edge. In particular, the advertised Hash-Extendability lemma is not the sole remaining obstacle.

## Simulated Review Panel

### Primary solver

The viable core is the attempt to convert semantic invariances into a restricted circuit model and then invoke monotone lower bounds. The repository is strongest when it treats this as a modular program with explicit audits, distributions, and counterexample search.

### Expert reviewer A — complexity theory

The proof currently mixes three different claims:

1. a decision circuit can be used to recover a witness;
2. a circuit that is extensionally correct must expose a witness or obey particular audits;
3. audit compliance implies a syntactic LocalNOT representation.

These are not interchangeable. A function may have a witness-search self-reduction without every circuit computing that function internally emitting a witness. Likewise, extensional invariance of a Boolean function does not by itself force a syntactic property of one chosen circuit computing it.

### Expert reviewer B — lower bounds

The monotone extraction step needs a theorem about the **restricted function computed after fixing local inputs**, not merely an informal statement that NOT gates are “killed.” A NOT gate whose input depends on a local block can remain nonconstant after a restriction. Even if every local negation is absorbed into an oracle gate, the result is generally a monotone circuit *with local oracle gates*, not an ordinary monotone circuit. Classical CLIQUE lower bounds do not automatically apply to that richer model.

### Mirror agent from a future solved version

A future successful version would not claim that correctness reveals circuit internals. It would define a representation-independent complexity measure or a restricted model closed under the transformations used. The final contradiction would be stated directly in that model, with a lower bound proved for the same model.

## Theorem Ledger

| ID | Claimed implication | Current status | Main issue |
|---|---|---|---|
| T1 | Correct decision circuit → witness-emitting circuit | Open / parameter-sensitive | Generic search-to-decision can work for self-reducible NP relations, but the repository's FORCE transform and fixed-length oracle model are not fully specified. |
| T2 | Witness extraction → WV is forced on the original circuit | False as stated | Existence of an external oracle extractor does not imply the original circuit emits or internally computes a witness. |
| T3 | Correctness → FOCUS/BRC/SRC/SPA audit compliance | Unproved | A disagreement on two equivalent inputs shows at least one error only when equivalence and output requirements are established for that exact pair; this does not imply a structural audit theorem. |
| T4 | Per-block resampling stability → junta on witness blocks | Unproved in stated form | Small individual resampling probabilities only bound total influence after summation; the claimed junta size/error theorem needs precise hypotheses and may leave non-negligible spillover. |
| T5 | Approximate gadget identities → AND of block-local predicates | Unproved | Tests on separate gadget distributions do not automatically identify the function on arbitrary focused instances. |
| T6 | Audit compliance → syntactic LocalNOT circuit | Major open step | Functional behavior on a distribution does not generally determine the syntax of an arbitrary circuit representation. |
| T7 | LocalNOT → ordinary monotone circuit under restriction | False without stronger hypotheses | Local NOTs can survive restrictions; replacing them by local functions yields oracle gates, not necessarily monotone gates. |
| T8 | Resulting function is CLIQUE in a hard parameter regime | Unproved | Parameters must simultaneously preserve enough graph variables, remove auxiliary behavior, and land in the exact regime of the cited monotone lower bound. |
| T9 | Hashed language remains NP-hard on unique/focused audit slices | Not established by a deterministic many-one reduction | Valiant–Vazirani gives a randomized reduction to unique solutions, not the deterministic many-one claim stated in Chunk 7. |
| T10 | Hash-Extendability closes the entire proof | False | Even granting Hash-Extendability leaves T2, T3, T6, T7, T8, and T9 unresolved. |

## Explicit Logical Breaks

### 1. External extraction does not force witness emission

Suppose `f_n` is any correct one-bit decision circuit for the language. An oracle algorithm may query `f_n` repeatedly and recover a witness. This proves that the *language relation* is search-reducible to its decision problem. It does not prove that `f_n` itself has witness wires, that its internal gates encode a witness, or that it satisfies WV.

The transformation can build a new witness-producing circuit family, but the later audit and locality arguments must then be applied to that transformed circuit with a proved size bound and a precisely defined input/output interface. They cannot be retroactively imposed on the original circuit.

### 2. The FORCE transform does not encode `T ⊆ C`

The current FORCE operation removes vertices incompatible with `T`, but it does not force a surviving clique to contain `T`. A clique among the remaining common neighbors can avoid every vertex in `T`.

This does not necessarily destroy a standard greedy extractor—because the algorithm only needs each YES query to certify that *some* witness remains—but it invalidates the stated interpretation and several prefix arguments. A correct forcing gadget must either delete all witnesses not containing `T`, mark the vertices of `T` as mandatory through an explicit construction, or use deletion-based self-reduction instead.

### 3. Hash-Extendability is close to tautological under the stated definition

If a valid hashed witness `C*` remains present after FORCE and the seed is unchanged, then for every subset `T ⊆ C*`, the same witness `C*` still certifies YES. Thus the stated prefix property follows immediately provided FORCE preserves the vertices and edges of `C*`.

The real problem is not existence of an ordering of one known witness. It is whether the greedy oracle procedure's chosen query and update rule guarantee a consistent surviving witness, while preserving encoding length and the exact hashed relation.

### 4. Distributional correctness cannot become worst-case correctness by sampling

Finding one explicit bad input proves that the circuit is not worst-case correct; it does not contradict an assumption of `1 - 1/poly(n)` distributional correctness. A circuit may be correct on most inputs and wrong on a sparse, efficiently recognizable set. Chunk 5 conflates these notions.

To derive a worst-case lower bound from an average-case hypothesis, the program needs a genuine worst-case-to-average-case reduction or an error-correction/random-self-reduction theorem for the target language and distribution.

### 5. Random restrictions do not automatically erase LocalNOT

Let a NOT gate compute `¬x` where `x` is a bit in one live block. A block restriction that leaves that block unfixed leaves the NOT gate intact. A union bound over supports does not help unless the restriction fixes every support of every NOT gate, which may also fix the graph variables needed to retain a hard CLIQUE instance.

The right target may be a lower bound for **monotone circuits with bounded-locality oracle gates**, but that is a different theorem and must be proved explicitly.

## Presentation Defects

The root `README.md` is currently a concatenation of multiple LaTeX drafts, prose continuations, and malformed escape sequences. It should not be treated as a compilable paper. The repository should separate:

- a short project README;
- one canonical LaTeX source;
- historical drafts;
- machine-readable theorem obligations;
- counterexample scripts and experiments.

## Honest Revised Claim

A defensible current abstract would say:

> We propose an audit-based research program for relating semantic invariances of a structured NP language to restricted circuit models. We identify several necessary proof obligations, including representation-independent audit soundness, a correct decision-to-search reduction for the hashed relation, and lower bounds for the exact restricted model produced by local-oracle elimination. We provide counterexamples to naive versions of these implications and a machine-checkable roadmap for future work.

## Next Research Target

The highest-value next theorem is not Hash-Extendability. It is:

> **Local-oracle soundness theorem.** Define a circuit model in which each nonmonotone gate is confined to one input block. Prove either (a) a superpolynomial lower bound for CLIQUE in this model, or (b) a transformation from this model to ordinary monotone circuits that preserves a hard CLIQUE projection.

A proof of that statement would make the endgame mathematically meaningful. A counterexample would sharply delimit the audit program.
