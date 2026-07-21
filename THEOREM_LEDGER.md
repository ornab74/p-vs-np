# Theorem Ledger

This file records the actual dependency graph of the program. A claim may move to `proved` only after a complete statement, parameter regime, quantifier order, and proof are present.

| ID | Claim | Current status | Main obstruction |
|---|---|---|---|
| T0 | `L_mix^hash ∈ NP` | proved, assuming polynomially bounded encodings | Witness verification is polynomial-time. |
| T1 | Base `L_mix` is NP-hard | plausible / routine | Needs one precise reduction and parameter encoding. |
| T2 | Hashed language is NP-hard under deterministic many-one reductions | unproved and likely misstated | Valiant–Vazirani is randomized and promise-sensitive; inverse-polynomial success does not itself give deterministic many-one NP-hardness. |
| T3 | A correct decision circuit can emit witnesses with polynomial overhead | unproved in the stated framework | Standard self-reduction changes queries and sometimes input length; the current FORCE transform does not encode membership of the chosen prefix. |
| T4 | Hash-Extendability | not the right isolated bottleneck as currently stated | For a surviving witness `C`, every subset of `C` trivially leaves `C` present under the current FORCE operation; the real issue is whether FORCE semantically forces inclusion and supports greedy extraction. |
| T5 | Correctness forces FOCUS/BRC/SRC/SPA audits | unproved | A correct Boolean function satisfies true semantic identities, but this does not constrain a particular circuit representation or provide an efficient verifier for all claimed equal-language pairs. |
| T6 | Approximate audit compliance implies closeness to LocalNOT | open | Influence/junta conclusions are distributional function statements, not syntactic NOT-gate locality. A rigorous reconstruction theorem is missing. |
| T7 | LocalNOT circuits can be restricted into monotone circuits for a hard CLIQUE projection | false as stated | Fixing the support variables of a NOT gate does not necessarily remove that NOT. Random restrictions may also collapse the hard instance. |
| T8 | The restricted function remains a hard CLIQUE instance in the required regime | unproved | Must preserve enough live edge variables and the exact clique parameter while controlling all local oracle/block inputs. |
| T9 | Monotone lower bounds apply to the extracted model | unproved | If local predicates survive as arbitrary block computations, the correct model is closer to monotone circuits with local oracles, not ordinary monotone circuits. |
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

1. Replace FORCE with a transformation satisfying an exact equivalence:
   `L(FORCE*(I,T)) = 1` iff there exists a valid witness of `I` containing `T`.
2. Prove or falsify the audit-to-function-decomposition theorem without mentioning circuit syntax.
3. State a separate representation theorem converting that decomposition to a lower-bound-compatible circuit model.
4. Prove a restriction/projection lemma for that exact model.
5. Only then reconnect to monotone CLIQUE lower bounds.
