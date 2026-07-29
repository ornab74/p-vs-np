# Theorem Ledger

This file records the actual dependency graph of the program. A claim may move to `proved` only after a complete statement, parameter regime, quantifier order, and proof are present.

| ID | Claim | Current status | Main obstruction |
|---|---|---|---|
| T0 | Formal layered language is in NP | proved | Fixed-width witness verification is polynomial-time. |
| T1 | Formal layered language is NP-complete | proved | Standard 3SAT-to-layered-compatibility reduction. |
| T2 | Pairwise-independent hashed layered language has deterministic many-one NP-hardness for nonzero hash length | open | Trivial-hash slice is NP-complete; isolation remains randomized/promise-sensitive. |
| T3 | Original graph-only FORCE supports witness extraction | false | A surviving witness can avoid the proposed prefix. |
| T3a | Formal layered language has exact same-length vertex and assignment pinning | proved | Fixed-width masks give exact extension equivalences. |
| T3b | Worst-case decision correctness gives polynomial same-length witness extraction | proved for redesigned language | Polynomially many same-length oracle calls. |
| T4 | Free field variables close clique-prefix extraction | false as stated | They solve a residue only after the clique is fixed. |
| T5 | Verified-witness polynomial FOCUS exists | proved | Singleton positional masks and isolated outside vertices. |
| T5a | BRC is an exact semantic identity | proved on displayed-witness slices | Does not imply global influence or syntax. |
| T5b | SRC has polynomial seed length and exact unused-seed resampling | proved for per-vertex affine hash | Pairwise independence retained. |
| T5c | Complete length-preserving SPA identity exists | proved on focused trivial-hash instances | Identifies semantic AND only. |
| T6 | Small off-witness resampling influence implies closeness to a witness-block function | proved under named product measure | Conditional Efron--Stein; function theorem only. |
| T6a | Single-resample audit rejection equals average resampling influence | proved | Repetition follows `E[1-(1-p(X))^k]`, not `delta/k`. |
| T6b | Repeated audits with failure `delta` imply influence `O(delta/k)` | false without uniformity | Rare catastrophic contexts survive amplification. |
| T6c | SPA plus stability forces LocalNOT syntax | false / unsupported | Equivalent circuits can contain canceled mixed NOT gates. |
| T6d | Any black-box audit can upper-bound NOT count of a circuit representation | false | Functionally equivalent circuits are indistinguishable; arbitrary canceled negation gadgets may be inserted. |
| T6e | Audit-measure closeness transfers automatically to hard CLIQUE pairs | false | Requires domination, coupling, cleanup, or pointwise theorem. |
| T7 | Focused trivial-hash language has exact monotone DNF over SAT-oracle bits and graph edges | proved | Size can be exponential in `t`. |
| T7a | Every small unrestricted circuit for a monotone function has polynomial monotone simulation | false in general | Known exponential monotone/nonmonotone gaps. |
| T7b | Layered audits imply special polynomial-size monotone/CLO compression | open and central | Must exploit structure beyond monotonicity. |
| T7c | Generic dual-rail conversion gives usable CLO locality | false | The construction has locality exactly `1`, above known lower-bound regimes. |
| T7d | Auxiliary-only audits constrain graph-edge subcircuit | false | Any graph-only circuit passes them. |
| T7e | A general circuit has a well-defined KW orientation-defect mass on named hard-pair distributions | proved as a representation-level invariant | Reversed terminal literals define the defect set; equivalent circuits can have different defect. |
| T7f | Small KW orientation defect yields a polynomial-size CLO of comparable locality | open | Requires an explicit circuit-to-CLO construction and rectangle accounting. |
| T7g | Every Boolean gate function has a unique minimal orientation equal to its set of decreasing hypercube coordinates | proved | `CERTIFIED_ORIENTATION_MODEL.md`; finite verification is exponential in gate fan-in but exact. |
| T7h | Layered CLIQUE inherits `d(4w+1)=Omega(m)` for circuits whose every gate has orientation weight at most `w` | proved from Koroth--Sarma and exact projection | `SPARSE_ORIENTATION_TRANSFER.md`; restricted depth theorem only. |
| T7i | Layered CLIQUE inherits the mixed sparse/dense-negation lower bound | proved from corrected Koroth--Sarma theorem and exact projection | Allows a few arbitrary dense negations plus additional negations with small orientation support. |
| T7j | Layered CLIQUE inherits the vertex-support orientation depth lower bound | proved from Koroth--Sarma and exact projection | Measures graph vertices incident to oriented edge variables. |
| T7k | Minimal orientation weight and incident-vertex support are mechanically computable for finite gate truth tables | proved | Exact but exponential in gate arity. |
| T7l | Small random decreasing-edge audit rejection implies small orientation support | false without a violation-mass margin | The spike function has full support `N` but rejection probability `2^{-(N-1)}`; see `ORIENTATION_MASS_BARRIER.md`. |
| T7m | Under the promise `nu_i=0` or `nu_i>=tau`, edge-audit error `delta` bounds orientation support by `N delta/tau` | proved | Exact counting argument; useful only if a nontrivial `tau` follows from special structure. |
| T7n | Two-sided certificate complexity gives an anti-hiding margin `nu_i>0 => nu_i>=2^{-(C0+C1-2)}` | proved | `CERTIFICATE_MARGIN_ORIENTATION_THEOREM.md`; decreasing endpoints' certificates generate a violating subcube. |
| T7o | Gate-wise bounds `C0+C1<=c` and directional audit mass `delta` imply orientation weight at most `N delta 2^{c-2}` | proved | Activates the sparse-orientation depth theorem for this certified restricted class. |
| T7p | Full edge-flip mass plus two-sided certificates bounds ordinary variable support by `N delta_flip 2^{c-2}` | proved | Supplies the support quantity used by the mixed-negation theorem when the internal-gate hypotheses are available. |
| T7q | Small average gate violation mass implies few high-orientation exceptional gates | proved by summation and Markov | Still requires white-box access to internal gate masses and certificate bounds. |
| T8 | Constructed oracle model has sufficiently small CLO locality | open | Current audits do not bound positive-negative oracle rectangles. |
| T8a | Known arbitrary-depth CLO CLIQUE lower bound applies directly | false / not established | Requires bounded locality and extra rectangle condition. |
| T8b | Distributional error yields pointwise separation of CLO hard sets | open | Requires transfer and cleanup. |
| T8c | Average-case cleanup is generically cheap | false | Repairing an arbitrary bad-pair set may require one correction rectangle per pair; polynomial cleanup needs special rectangle structure. |
| T9 | Hard graph projection matches a lower-bound parameter regime | clarified | Fixing CLIQUE parameter bits preserves polynomial circuit size under `NP subseteq P/poly`. |
| T9a | Formal layered language has superpolynomial lower bound for circuits with at most `(1/6) log log m` NOT gates | proved from Amano--Maruoka | Exact polynomial projection to their CLIQUE family. |
| T9b | Audits imply an equivalent circuit with few NOT gates | impossible from black-box audits alone | Would require white-box canonicalization or a new representation theorem. |
| T9c | Sparse or mixed orientation alone separates unrestricted `P/poly` | false / insufficient | The unrestricted assumption supplies circuits with no known orientation-support or certificate bound. |
| T10 | Therefore `NP not subseteq P/poly` | not established | Must close a special CLO compression/locality theorem or another unrestricted representation lower bound. |

## Required proof format

For every theorem or lemma, include exact parameters and quantifiers; circuit and input model; reduction type; error notion and distribution; size/advice accounting; smallest counterexamples; and explicit dependencies.

## Immediate priority order

1. Test whether certificate-generated violating subcubes yield polynomial CLO rectangle covers with controlled locality.
2. Search for a canonicalization theorem giving logarithmic two-sided gate certificates and small internal directional mass.
3. Prove or falsify circuit-to-CLO conversion from small KW orientation defect with explicit rectangle accounting.
4. Search for graph-sensitive identities that imply vertex concentration or polynomially templated decreasing edges.
5. Keep all few-NOT, orientation, and certificate-margin results as restricted endpoints and do not describe them as an unrestricted separation.
