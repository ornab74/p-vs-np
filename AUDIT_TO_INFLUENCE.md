# Exact Audit-Rejection to Resampling-Influence Theorem

This note replaces the invalid claim that `k` repeated audits automatically divide influence by `k`.

The correct relation is exact for a one-sample disagreement audit under a named product distribution.

## 1. Product-measure setup

Fix a focused witness tuple and let `J` be the set of off-witness block coordinates. Let

```text
mu = product_{j in J} mu_j
```

be a product distribution over their fixed-width encodings. Selected witness fields are treated as fixed conditioning data.

For a Boolean function `f`, let `X^(j)` be obtained by independently resampling coordinate `j` from `mu_j`, and define

```text
Inf_j^res(f) = Pr[f(X) != f(X^(j))].
```

The probability includes both `X~mu` and the fresh coordinate sample.

## 2. Uniform-coordinate disagreement audit

Define one audit trial:

1. sample `X~mu`;
2. sample `J0` uniformly from `J`;
3. independently resample coordinate `J0` to obtain `X^(J0)`;
4. reject exactly when `f(X) != f(X^(J0))`.

Let `rho` be its rejection probability.

### Theorem 2.1

```text
rho = (1/|J|) sum_{j in J} Inf_j^res(f).
```

Equivalently,

```text
sum_{j in J} Inf_j^res(f) = |J| rho.
```

### Proof

Condition on the sampled coordinate `J0=j`. The rejection probability is exactly `Inf_j^res(f)`. Averaging over the uniform choice of `j` proves the identity.

## 3. Consequence for function decomposition

The conditional Efron--Stein theorem gives a witness-block function `g` satisfying

```text
Pr[f(X) != g] <= sum_{j in J} Inf_j^res(f).
```

Combining with Theorem 2.1 yields

```text
Pr[f(X) != g] <= |J| rho.
```

Therefore, to obtain approximation error at most `eta`, the required single-trial rejection rate is

```text
rho <= eta / |J|.
```

This factor of `|J|` is unavoidable for a uniformly sampled coordinate unless stronger structure is proved.

## 4. Estimating the rejection probability

Run `N` independent one-coordinate trials and let `rho_hat` be the empirical rejection fraction. Hoeffding's inequality gives

```text
Pr[|rho_hat-rho| > eps] <= 2 exp(-2 N eps^2).
```

Thus confidence at least `1-delta` and additive error `eps` is obtained with

```text
N >= (1/(2 eps^2)) ln(2/delta).
```

This is statistical estimation only. It does not change the underlying influence.

## 5. Why "reject if any of k resamples changes" is insufficient

Suppose an audit samples a context `X` once and then performs `k` resamples, rejecting if any disagreement occurs. Let

```text
p(X) = Pr[f(X) != f(X^(J0)) | X]
```

for one fresh coordinate/resample trial. Its failure probability is

```text
E_X[1-(1-p(X))^k].
```

This quantity does not determine `E_X[p(X)]/k`. Rare contexts with `p(X)=1` can have measure `delta`; then the `k`-fold rejection probability and the one-trial influence are both `delta` for every `k`.

Repeated tests improve detection and estimation, but they do not by themselves prove an `O(delta/k)` average-influence bound.

## 6. Per-coordinate audits

If the test chooses a specified coordinate `j` instead of a uniform one, its rejection probability is exactly

```text
Inf_j^res(f).
```

Auditing every coordinate separately can establish individual bounds, but doing so requires explicit sample complexity and a union bound over `|J|` coordinates.

For example, estimating every influence within additive `eps` and total confidence `1-delta` requires on the order of

```text
|J| eps^(-2) log(|J|/delta)
```

samples.

## 7. Status

This closes the mathematical conversion:

```text
named product audit rejection
=> exact total off-witness resampling influence
=> Efron--Stein witness-block approximation.
```

It does not prove that a polynomial-size exact decider has low rejection probability on a distribution. A worst-case correct decider does have zero rejection on transformations that preserve the full language value pointwise; one-sided YES-preservation alone is not enough when the audit distribution includes NO instances.

The audit distribution must therefore use transformations with a proved two-sided language identity, or explicitly remain a conditioned YES-slice statement.