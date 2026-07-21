# Theorem Ledger

This file records the actual dependency graph of the program. A claim may move to `proved` only after a complete statement, parameter regime, quantifier order, and proof are present.

| ID | Claim | Current status | Main obstruction |
|---|---|---|---|
| T0 | Formal layered language is in NP | proved | Fixed-width witness verification is polynomial-time. |
| T1 | Formal layered language is NP-complete | proved | Standard 3SAT-to-layered-compatibility reduction. |
| T2 | Pairwise-independent hashed layered language has a deterministic many-one NP-hardness proof for nonzero hash length | open | The trivial-hash slice is NP-complete; nonzero isolation remains randomized/promise-sensitive. |
| T3 | Original graph-only FORCE supports witness extraction | false | A surviving witness can avoid the proposed prefix. |
| T3a | Formal layered language has exact same-length vertex and assignment pinning | proved | Fixed-width masks give exact extension equivalences. |
| T3b | Worst-case decision correctness gives polynomial same-length witness extraction | proved for the redesigned language | Uses at most `Bt+tell` oracle calls. |
| T4 | Free field variables close clique-prefix extraction | false as stated | They solve a residue only after the clique is fixed. |
| T5 | Verified-witness polynomial FOCUS exists | proved | Singleton positional masks and isolated outside vertices. |
| T5a | BRC is an exact semantic identity | proved on displayed-witness slices | Does not by itself imply global influence or circuit syntax. |
| T5b | SRC can be instantiated with polynomial seed length and exact unused-seed resampling | proved for the per-vertex affine hash | `EXPLICIT_SRC_HASH.md`; pairwise independence retained. |
| T5c | A complete length-preserving SPA identity exists | proved on focused trivial-hash instances | `EXACT_SPA_IDENTITY.md`; identifies the semantic AND only. |
| T6 | Small off-witness resampling influence implies closeness to a witness-block function | proved under a named product measure | Conditional Efron--Stein; function theorem only. |
| T6a | Single-resample audit rejection equals average resampling influence | proved by definition under the named experiment | Repetition has exact `E[1-(1-p(X))^k]` behavior, not `delta/k`. |
| T6b | Repeated audits with failure `delta` imply influence `O(delta/k)` | false without uniformity | Rare catastrophic contexts survive amplification. |
| T6c | SPA plus stability forces LocalNOT syntax | false / unsupported | Equivalent circuits can contain canceled mixed NOT gates. |
| T7 | Focused trivial-hash language has an exact monotone DNF over local SAT oracle bits and graph edges | proved | `CANONICAL_MONOTONE_REPRESENTATION.md`; size can be exponential in `t`. |
| T7a | Every polynomial-size decider can be converted to a polynomial-size monotone/CLO representation | open and central | Requires a new compression/representation theorem. |
| T8 | The resulting oracle model has sufficiently small CLO locality | open | Current audits do not bound positive-negative oracle rectangles. |
| T8a | Known arbitrary-depth CLO CLIQUE lower bound applies directly | false / not established | Requires bounded locality and an extra rectangle condition. |
| T9 | A hard projection preserves the needed parameter regime and pointwise positive/negative sets | open | Fixed `t=log^2 n` NP-hardness was not established. |
| T10 | Therefore `NP not subseteq P/poly` | not established | Depends on T7a--T9. |

## Required proof format

For every theorem or lemma, include: exact parameters and quantifiers; circuit and input model; reduction type; error notion and distribution; size/advice accounting; smallest counterexamples; and explicit dependencies.

## Immediate priority order

1. Attempt the polynomial-size monotone/CLO compression theorem from semantic audits.
2. Define CLO oracle rectangles for the constructed representation and calculate locality.
3. Check or replace the extra rectangle condition in known arbitrary-depth lower bounds.
4. Prove a hard projection with a valid NP-hard parameter map.
5. Perform barrier and external-review checks before any separation claim.