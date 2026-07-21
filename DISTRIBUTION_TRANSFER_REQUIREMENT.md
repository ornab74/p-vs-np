# Distribution Transfer Requirement

## Purpose

The audit and Efron--Stein theorems are distributional. The monotone-CLO lower bound is stated on designated positive and negative instance sets. This note identifies the missing measure-transfer theorem between those two settings.

## Two measures

Let `mu` be the product measure used by BRC/SRC stability tests after a witness has been focused.

Let `nu` be the hard lower-bound measure, typically a distribution on pairs

```text
(u,v) in U x V,
```

where `U` is the positive clique family and `V` is the negative complete multipartite family.

A conclusion such as

```text
Pr_mu[f != g] <= epsilon
```

does not imply small error under `nu` unless a relation between `mu` and `nu` is proved.

## Basic obstruction

If the supports of `mu` and `nu` are disjoint, functions `f` and `g` can agree with probability one under `mu` and disagree with probability one under `nu`.

Even overlapping support is insufficient when the hard instances have exponentially small `mu`-mass.

Therefore distributional audit soundness cannot be inserted directly into a pointwise lower-bound argument.

## Valid transfer lemma

### Lemma

Suppose `nu` is absolutely continuous with respect to `mu` and

```text
d nu / d mu <= K
```

pointwise. Then for every event `E`,

```text
nu(E) <= K mu(E).
```

Consequently, if

```text
Pr_mu[f != g] <= epsilon,
```

then

```text
Pr_nu[f != g] <= K epsilon.
```

### Proof

By the Radon--Nikodym bound,

```text
nu(E) = integral_E (d nu / d mu) d mu <= K mu(E).
```

Apply this to the disagreement event.

## Pointwise alternative

A lower-bound theorem that requires exact separation of `U` and `V` cannot use average error alone. One must instead prove one of:

1. pointwise correctness on every element of `U union V`;
2. an error-correction procedure preserving size and locality;
3. a robust lower bound tolerating the exact error distribution obtained;
4. a transfer lemma with sufficiently small `K epsilon` and a cleanup theorem.

## Relation to oracle locality

CLO locality is measured on positive-negative pairs. Audit influence is measured by resampling auxiliary coordinates. These are different probability spaces.

A complete bridge must define a map

```text
Audit sample X  <->  hard pair (u,v)
```

and prove quantitative domination or coupling. Without this map, a small audit error gives no oracle-locality bound.

## Required theorem schema

The next representation theorem must include all of the following in one statement:

1. an audit measure `mu_n`;
2. hard sets `U_n,V_n` and hard-pair measure `nu_n`;
3. a transformation from audit failures to oracle rectangles;
4. a bound on the union locality under `nu_n`;
5. a transfer or cleanup step from `mu_n`-average correctness to pointwise separation of `U_n,V_n`.

## Small finite counterexample

Let the domain be `{a,b}`. Put `mu(a)=1` and `nu(b)=1`. Define

```text
f(a)=g(a)=0,
f(b)=0,
g(b)=1.
```

Then `Pr_mu[f!=g]=0` while `Pr_nu[f!=g]=1`.

This elementary example captures the exact logical gap in any proof that changes measures without a domination theorem.

## Status

The Efron--Stein theorem remains valid under its named product measure. It should be retained. But it cannot contribute to the final CLIQUE contradiction until this distribution-transfer component is supplied.
