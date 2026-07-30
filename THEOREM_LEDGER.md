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
| T7h | Layered CLIQUE inherits `d(4w+1)=Omega(m)` for circuits whose every gate has orientation weight at most `w` | proved from Koroth--Sarma and exact projection | Restricted depth theorem only. |
| T7i | Layered CLIQUE inherits the mixed sparse/dense-negation lower bound | proved from corrected Koroth--Sarma theorem and exact projection | Allows a few arbitrary dense negations plus additional negations with small orientation support. |
| T7j | Layered CLIQUE inherits the vertex-support orientation depth lower bound | proved from Koroth--Sarma and exact projection | Measures graph vertices incident to oriented edge variables. |
| T7k | Minimal orientation weight and incident-vertex support are mechanically computable for finite gate truth tables | proved | Exact but exponential in gate arity. |
| T7l | Small random decreasing-edge audit rejection implies small orientation support | false without a violation-mass margin | The spike function has full support `N` but rejection probability `2^{-(N-1)}`. |
| T7m | Under the promise `nu_i=0` or `nu_i>=tau`, edge-audit error `delta` bounds orientation support by `N delta/tau` | proved | Useful only if a nontrivial `tau` follows from special structure. |
| T7n | Two-sided certificate complexity gives an anti-hiding margin `nu_i>0 => nu_i>=2^{-(C0+C1-2)}` | proved | Decreasing endpoints' certificates generate a violating subcube. |
| T7o | Gate-wise bounds `C0+C1<=c` and directional audit mass `delta` imply orientation weight at most `N delta 2^{c-2}` | proved | Activates the sparse-orientation depth theorem for this certified restricted class. |
| T7p | Full edge-flip mass plus two-sided certificates bounds ordinary variable support by `N delta_flip 2^{c-2}` | proved | Supplies the support quantity used by the mixed-negation theorem when internal-gate hypotheses are available. |
| T7q | Small average gate violation mass implies few high-orientation exceptional gates | proved by summation and Markov | Still requires white-box access to internal gate masses and certificate bounds. |
| T7r | Two-sided certificates automatically give polynomially many CLO rectangles | false in general | Constant certificate sum gives polynomially many candidate pairs, but logarithmic sum gives only quasipolynomial count. |
| T7s | Small certificate complexity implies small CLO locality | false | A single negated edge literal has `C0+C1=2` but its natural clique--multipartite rectangle has locality bounded away from zero and approaching `1`. |
| T7t | Compatible certificate pairs define valid gate-separation rectangles | proved | Robust CLO correctness and hard-pair coverage remain separate obligations. |
| T7u | Fixed vertex anchors give exact low-locality clique--multipartite rectangles | proved | Exact locality formula in `WITNESS_TEMPLATE_LOCALITY_CALCULUS.md`. |
| T7v | A large family of constant-size witness anchors can satisfy constant `A_d` | false | If `s(d+1)<=k`, condition `A_d` forces at most `d` distinct size-`s` anchors. |
| T7w | The complete family of edge-witness rectangles has low union locality | false | It covers every hard pair, so union locality is exactly `1`, and each positive clique lies in `binom(k,2)` positive sides. |
| T7x | For monochromatic-anchor rectangles, condition `A_d` implies union locality at most `d/(k-1)` | proved | Averaging gives total positive mass at most `d`; every anchor of size at least two has negative mass at most `1/(k-1)`. |
| T7y | Polynomial-size anchor families with constant `A_d` and locality below `1/50` exist | proved | Pairwise disjoint anchors of size `floor(k/(d+1))+1` give `Theta(n/k)` rectangles, `A_d`, and locality at most `d/(k-1)`. |
| T7z | Such bounded-load anchor families automatically cover all exceptional pairs of a small circuit | false from total defect alone | A function-preserving `O(n^2)` wrapper programs a defect slice `{K_B0} x V` of mass `1/binom(n,k)` containing pairs with no monochromatic anchor of size at least three. |
| T7aa | Small representation-level KW defect implies large-anchorability of every reversed pair | false | `KW_DEFECT_PROGRAMMING_BARRIER.md`; deterministic descent can be programmed by an equivalent wrapper. |
| T7ab | The programmed nonanchorable slice has cheap arbitrary-rectangle cleanup | proved | `{K_B0} x V` has locality `1/binom(n,k)` and positive overlap one, showing large anchors need not be the only oracle shape. |
| T7ac | A hybrid decomposition into anchorable bulk plus low-complexity cleanup suffices for the CLO route | open and central | Must bound cleanup rectangle count or positive-projection complexity and prove robust monotone simulation. |
| T8 | Constructed oracle model has sufficiently small CLO locality | open | Rectangle existence and locality are solved for anchor families; hybrid expressive coverage and robust simulation remain open. |
| T8a | Known arbitrary-depth CLO CLIQUE lower bound applies directly | false / not established | Requires a valid robust CLO construction with bounded positive-side overlap. |
| T8b | Distributional error yields pointwise separation of CLO hard sets | open | Requires transfer and cleanup. |
| T8c | Average-case cleanup is generically cheap | false | Repairing an arbitrary bad-pair set may require one correction rectangle per pair. |
| T9 | Hard graph projection matches a lower-bound parameter regime | clarified | Fixing CLIQUE parameter bits preserves polynomial circuit size under `NP subseteq P/poly`. |
| T9a | Formal layered language has superpolynomial lower bound for circuits with at most `(1/6) log log m` NOT gates | proved from Amano--Maruoka | Exact polynomial projection to their CLIQUE family. |
| T9b | Audits imply an equivalent circuit with few NOT gates | impossible from black-box audits alone | Would require white-box canonicalization or a new representation theorem. |
| T9c | Sparse or mixed orientation alone separates unrestricted `P/poly` | false / insufficient | The unrestricted assumption supplies circuits with no known orientation-support or certificate bound. |
| T10 | Therefore `NP not subseteq P/poly` | not established | Must prove the hybrid anchor/cleanup decomposition plus robust CLO simulation, or another unrestricted representation lower bound. |

## Required proof format

For every theorem or lemma, include exact parameters and quantifiers; circuit and input model; reduction type; error notion and distribution; size/advice accounting; smallest counterexamples; and explicit dependencies.

## Immediate priority order

1. Formalize a hybrid decomposition `Rev_C subseteq E_anchor union E_cleanup` with polynomial anchor and cleanup covers.
2. Bound cleanup positive-projection complexity rather than only total defect mass.
3. Prove robust CLO correctness for arbitrary separating interpretations of anchor and cleanup oracles.
4. Determine whether the resulting `A_d` parameter retains a superpolynomial published lower bound.
5. Keep all few-NOT, orientation, certificate-margin, anchor-family, and programmed-defect results as restricted, conditional, or barrier endpoints; do not describe them as an unrestricted separation.
