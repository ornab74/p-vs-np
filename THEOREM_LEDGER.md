# Theorem Ledger

This file records the actual dependency graph of the program. A claim may move to `proved` only after a complete statement, parameter regime, quantifier order, and proof are present.

| ID | Claim | Current status | Main obstruction |
|---|---|---|---|
| T0 | `L_mix^hash ∈ NP` | proved, assuming polynomially bounded encodings | Witness verification is polynomial-time. |
| T1 | Base `L_mix` is NP-hard | plausible / routine | Needs one precise reduction and parameter encoding. |
| T1a | The parameter choice `t=log^2 n`, `B=n^3` is NP-hard because CLIQUE is NP-hard | unproved and likely unusable as stated | Standard CLIQUE NP-hardness has `t` supplied by the reduction. Fixing a length-dependent logarithmic `t` needs a polynomial padding reduction; brute force is quasipolynomial in this regime. |
| T1b | The formal layered language with unrestricted polynomially encoded layer count is NP-complete | proved | Membership is direct; NP-hardness follows from the standard 3SAT-to-compatibility-graph reduction with one layer per clause and one vertex per satisfying local clause assignment. |
| T2 | Hashed language is NP-hard under deterministic many-one reductions | unproved and likely misstated | Valiant–Vazirani is randomized and promise-sensitive; inverse-polynomial success does not itself give deterministic many-one NP-hardness. |
| T3 | A correct decision circuit can emit witnesses with polynomial overhead for the original language | unproved in the stated framework | Standard self-reduction changes queries and sometimes input length; the current FORCE transform does not encode membership of the chosen prefix. |
| T3a | The layered-mask language admits exact same-length vertex pinning | proved as a redesigned-language lemma | Singleton candidate masks give `L(PIN(I,P))=1` iff a witness extends ordered prefix `P`. |
| T3b | The formal layered language admits complete same-length witness extraction | proved | Fixed-width vertex masks and assignment-bit masks permit exact oracle pinning of every witness coordinate with polynomially many same-length queries. |
| T3c | The layered redesign retains the exact audit and lower-bound pipeline | open | Audits must be restated for positional witnesses and masks, and the ultimate lower-bound model remains unresolved. |
| T4 | Hash-Extendability | not the right isolated bottleneck as currently stated | For a surviving witness `C`, every subset of `C` trivially leaves `C` present under the current FORCE operation; the real issue is whether FORCE semantically forces inclusion and supports greedy extraction. |
| T4a | Free field variables `z_i` make the additive residue extendable after `C` is fixed | proved as a local algebraic observation | The equation can be solved using one nonzero coefficient, but it does not pin or isolate the clique and does not repair FORCE. |
| T4b | The augmented additive hash closes decision-to-witness extraction | false as stated | A YES answer to `FORCE(I,T∪{v})` may be witnessed by a clique avoiding `T∪{v}`; the induction used by the greedy extractor fails. |
| T5 | Correctness forces FOCUS/BRC/SRC/SPA audits | unproved | A correct Boolean function satisfies true semantic identities, but this does not constrain a particular circuit representation or provide an efficient verifier for all claimed equal-language pairs. |
| T5a | The stated `H⟨C⟩` normalization is efficiently computable in the hard regime | false for the stated implementation | Enumerating all `(t-2)`-subsets is polynomial only for constant `t`; choices such as `t=log^2 n` make the audit transformation superpolynomial. |
| T5b | A verified witness admits a polynomial focus transform | proved as a semantic lemma | Keep only the internal edges of `C` and isolate every outside vertex. This is `O(B^2)` and makes `C` the unique possible `t`-clique, conditioned on witness verification. |
| T6 | Approximate audit compliance implies closeness to LocalNOT | open | Influence/junta conclusions are distributional function statements, not syntactic NOT-gate locality. A rigorous reconstruction theorem is missing. |
| T6a | The uploaded Friedgut calculation yields a constant-size junta | false by arithmetic / theorem misuse | One draft gives `I/η^2=n^7`; the revised draft uses only outside influence and does not satisfy the stated global theorem hypotheses. |
| T6b | BRC on conditioned YES slices bounds every global block influence by `1/n^2` | unproved | The draft changes distributions and omits NO instances, multi-witness cases, and conditional-to-unconditional conversion. Also inverse-polynomial error is not negligible. |
| T6c | Any mixed internal NOT gate creates observable output influence | false | Mixed gates can be masked or canceled, e.g. `x∧h ∨ x∧¬h = x` with `h` depending on two blocks. Semantic audits see zero dependence while the supplied circuit contains a mixed NOT. |
| T6d | Small total off-witness resampling influence implies closeness to a witness-block function | proved under a named product distribution | Conditional Efron–Stein plus conditional majority gives error at most `sum_{j∉C} Inf_j^res(f)`. This is a function theorem only. |
| T6e | `k` repeated audits with failure `δ` imply average influence `O(δ/k)` | false without a uniformity hypothesis | Rare catastrophic contexts of measure `δ` make every resample fail there. The `k`-fold audit failure and average influence are both `δ`, independent of `k`. |
| T7 | LocalNOT circuits can be restricted into monotone circuits for a hard CLIQUE projection | false as stated | Fixing auxiliary blocks does not necessarily remove NOTs on graph variables, and semantic monotonicity does not provide a polynomial monotone-circuit conversion. Random restrictions may also collapse the hard instance. |
| T8 | The restricted function remains a hard CLIQUE instance in the required regime | unproved | Must preserve enough live edge variables and the exact clique parameter while controlling all local oracle/block inputs. |
| T9 | Monotone lower bounds apply to the extracted model | unproved | If local predicates survive as arbitrary block computations, the correct model is closer to monotone circuits with local oracles, not ordinary monotone circuits. |
| T9a | Known arbitrary-depth clique lower bounds for monotone circuits with local oracles apply directly | false / not established | Krajicek–Oliveira require bounded locality and an additional restrictive oracle-rectangle condition. The audit framework has not produced either property. |
| T10 | Therefore `NP ⊄ P/poly` | not established | Depends on T2–T9. |

## Required proof format

For every theorem or lemma, add:

1. **Exact statement:** all parameters and quantifiers.
2. **Model:** circuit basis, fan-in, uniform/nonuniform assumptions, input partition, and distribution.
3. **Reduction type:** deterministic, randomized, promise, Turing, or many-one.
4. **Error notion:** pointwise, average-case, total variation, or closeness under a named distribution.
5. **Size accounting:** transformed circuit size and advice length.
6. **Counterexample search:** smallest finite cases and known barrier checks.
7. **Dependency list:** theorem IDs used by the proof.

## Immediate priority order

1. Restate FOCUS/BRC/SRC/SPA for the formal layered language using the polynomial focus transform.
2. Use the direct Efron–Stein theorem to obtain function-level off-witness decomposition under an explicit product measure.
3. Prove or falsify that SPA identifies the resulting witness-block function as the intended AND of local predicates.
4. Formulate a representation theorem into monotone circuits with local oracles and bound the oracle locality.
5. Check the extra oracle-rectangle hypothesis required by known arbitrary-depth CLO lower bounds, or prove a new lower bound without it.
6. Only then reconnect to CLIQUE lower bounds.
