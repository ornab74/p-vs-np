# Exact Function Decomposition and the Monotone-CLO Route

This note replaces the incorrect Friedgut/Bourgain step with a direct product-measure theorem and states the precise lower-bound model that the project would need next.

## 1. Product-measure setup

Fix a verified witness support `C`. Let the remaining blocks be independent under a product distribution

`mu = mu_C x prod_{j notin C} mu_j`.

For a Boolean function `f` on these blocks, define the resampling influence

`Inf_j^res(f) = Pr[f(X) != f(X^(j))]`,

where `X^(j)` is obtained by independently resampling block `j` from `mu_j`.

No statement below concerns the syntax of a circuit. It concerns only the Boolean function computed under the named measure.

## 2. Direct off-witness junta theorem

### Theorem

There exists a Boolean function `g` depending only on the witness blocks `X_C` such that

`Pr_mu[f(X) != g(X_C)] <= sum_{j notin C} Inf_j^res(f)`.

### Proof

For fixed `X_C`, let

`q(X_C) = Pr[f(X)=1 | X_C]`

and define the conditional-majority predictor

`g(X_C) = 1[q(X_C) >= 1/2]`.

Its conditional error is

`min(q,1-q) <= 2 q(1-q) = 2 Var(f | X_C)`.

Conditional Efron-Stein gives

`Var(f | X_C) <= (1/2) sum_{j notin C} E[(f(X)-f(X^(j)))^2 | X_C]`.

Because `f` is Boolean, the squared difference is exactly the disagreement indicator. Averaging over `X_C` proves

`Pr[f != g] <= sum_{j notin C} Inf_j^res(f)`.

## 3. Consequence for the audit program

If the total off-witness resampling influence is at most `eta`, then `f` is `eta`-close, under the exact product distribution used in the theorem, to a function of the witness blocks alone.

This is stronger and cleaner than the uploaded Friedgut calculation:

- no global low-total-influence hypothesis is needed;
- no exponential junta-size formula is needed;
- no claim is made about circuit gates;
- the error and distribution are explicit.

On the polynomially focused slice `H downarrow C`, with the hash condition for `C` fixed to accept, the true language is exactly

`AND_{i in C} SAT(phi_i)`.

Thus a worst-case correct decider restricted to that slice computes this blockwise AND exactly. An approximately audit-stable function is close to some `C`-block function, and additional semantic gadget identities would be needed to identify that function as the AND of the local SAT predicates.

## 4. Why this still does not imply LocalNOT

The theorem gives a new function `g(X_C)`. It does not transform the supplied circuit for `f` into a circuit whose NOT gates are block-local.

A circuit may contain mixed gates that cancel internally while computing a block-local function. Therefore the next statement must be a separate representation theorem, not a corollary of influence.

A potentially meaningful target is:

> From the exact semantic decomposition and the audit identities, construct a polynomial-size monotone outer circuit with explicitly bounded local-oracle gates.

## 5. Known monotone circuits with local oracles

Krajicek and Oliveira study monotone circuits with local oracles (CLOs), where a monotone outer circuit receives additional oracle inputs that may compute unstructured functions. Their clique lower bounds require quantitative locality bounds and, for arbitrary depth, an additional restrictive condition on the oracle rectangles.

The relevant published result is:

- Jan Krajicek and Igor C. Oliveira, *On monotone circuits with local oracles and clique lower bounds*, Chicago Journal of Theoretical Computer Science, 2018; arXiv:1704.06241.

For `5 <= k <= n^(1/4)` and locality at most `1/50`, the paper proves `n^{Theta(sqrt(k))}` bounds under a restrictive oracle condition. This does not automatically apply to the current audit framework.

## 6. Exact obligations for a CLO endpoint

A valid bridge must construct, from the audit framework:

1. a monotone outer circuit in the graph-edge variables;
2. oracle functions with a formally defined positive-negative rectangle for each oracle;
3. a bound on the union locality `mu`, ideally below the threshold required by the lower bound;
4. the additional rectangle-intersection condition used by the arbitrary-depth theorem, or a new lower bound without that condition;
5. polynomial size accounting and a pointwise, not merely distributional, separation of the positive and negative clique instance sets.

At present none of these follow from BRC, SRC, SPA, or the proposed LocalNOT definition.

## 7. Parameter corrections

The uploaded merged draft also needs these repairs:

- `q=n^3` is not necessarily prime. Use a prime power such as `q=2^m`, or choose a prime in an explicitly specified interval and account for its construction.
- `n^{-3}` and `n^{-10}` are inverse-polynomial, not negligible.
- `L_mix^aug` is not proved NP-complete merely by setting every block formula to true when `t` is fixed as `log^2 n`. A reduction must preserve the chosen length-dependent clique parameter with polynomial blowup.
- A claim such as `|W| >= q B^{Omega(t)}` is false for arbitrary YES instances. A graph may have a unique witness clique. The free linear controls give many auxiliary assignments after a clique is fixed, but not many cliques.

## 8. Revised pipeline

The defensible pipeline is now:

`exact PIN self-reduction`

`=> verified witness`

`=> polynomial focus transform`

`=> exact semantic AND on focused slices`

`=> direct Efron-Stein off-witness decomposition under named product measures`

`=> OPEN: semantic gadget identities identify the local function`

`=> OPEN: representation as a monotone CLO with bounded locality`

`=> OPEN: apply or extend monotone-CLO clique lower bounds`.

This route is narrower than the original LocalNOT claim but is mathematically aligned with an existing lower-bound model.