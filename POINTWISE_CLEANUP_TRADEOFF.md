# Distributional-to-Pointwise Cleanup Tradeoff

Any lower-bound endpoint must separate the named positive and negative hard sets pointwise.  Average correctness under an audit distribution is not enough.

This note records the exact cleanup statements that are available and the locality cost they impose.

## 1. Average error does not imply pointwise correctness

Let `Omega` be a finite hard set and let `D` be uniform on `Omega`.

If a classifier has average error `epsilon`, it may still be wrong on an arbitrary subset of size

```text
epsilon * |Omega|.
```

Thus a constant or inverse-polynomial average error leaves many possible hard-set errors when `|Omega|` is exponential.

No generic cleanup theorem can turn this into pointwise correctness without an additional hypothesis.

## 2. Integrality threshold

### Lemma

If a deterministic classifier has uniform average error

```text
epsilon < 1/|Omega|,
```

then it is correct on every point of `Omega`.

### Proof

One error contributes exactly `1/|Omega|` to the uniform error.  Therefore an error smaller than this value implies zero errors.

### Limitation

For CLIQUE hard sets, `|Omega|` is exponential in the graph encoding length.  Reaching this threshold requires exponentially small average error.

## 3. Pointwise randomized error amplification

Suppose a distribution over classifiers has the stronger guarantee

```text
for every x in Omega,
Pr_r[C_r(x) != f(x)] <= rho
```

for a constant `rho<1/2`.

Take `q` independent samples and output their majority.  For each fixed `x`, a Chernoff bound gives

```text
Pr[majority is wrong on x]
<= exp(-Theta((1/2-rho)^2 q)).
```

Choosing

```text
q = Theta(log |Omega| + log(1/delta))
```

and applying a union bound gives probability at least `1-delta` that the majority classifier is correct on every point of `Omega`.

Hence there exists a deterministic fixing of the samples that is pointwise correct.

## 4. Monotonicity and circuit size

Majority is monotone.  Therefore if every sampled classifier is a monotone circuit or monotone CLO, their majority can be implemented by a monotone circuit with polynomial overhead in `q`.

If each circuit has size `s`, the amplified size is

```text
poly(q) * s.
```

Since `q=O(log |Omega|)`, this remains polynomial when the hard-set description length is polynomial and `log |Omega|` is polynomial.

## 5. Locality accumulation

Suppose the `j`th sampled CLO has oracle rectangles whose union locality is at most `mu` under a hard-pair measure.

Combining `q` independent CLOs uses the union of all oracle rectangles.  The elementary union bound gives

```text
mu_total <= q * mu.
```

Therefore pointwise cleanup preserving a target locality `mu_star` requires

```text
mu <= mu_star / q.
```

For a graph on `m` vertices, the edge encoding has `Theta(m^2)` bits and the natural positive and negative hard sets have exponential cardinality.  Consequently

```text
log |Omega| = Theta(m^2)
```

up to the exact hard-set definition, and pointwise majority cleanup may require

```text
q = Theta(m^2).
```

To finish with locality at most `1/50`, the starting randomized CLO would then need locality on the order of

```text
O(1/m^2),
```

not merely a fixed constant below `1/50`.

## 6. Average-pair error is weaker still

A guarantee such as

```text
Pr_{(u,v)~nu,r}[protocol error] <= epsilon
```

is only average over pairs and randomness.  It does not imply the per-pair bound required for the majority-plus-union-bound cleanup.

Rare pairs may have error probability `1` while the global average remains small.

A valid route must provide one of:

1. a uniform per-pair error bound;
2. an exponentially small average error below the integrality threshold;
3. a structural cleanup lemma exploiting the geometry of the hard sets;
4. a lower bound that tolerates distributional rather than pointwise separation.

## 7. Consequence for the audit program

The audit-to-influence theorem gives an average statement under a named product measure.  It does not provide a per-hard-pair guarantee.

Thus the following implication is invalid without more work:

```text
small audit failure
=> pointwise low-locality CLO separator.
```

The exact missing bridge is:

> Convert average orientation defect or average audit error into either pointwise correctness or a hard-set lower-bound model that accepts distributional error, while keeping oracle locality below the required threshold.

## 8. Status

The amplification theorem above is proved and supplies a sufficient condition.  It also shows that straightforward cleanup incurs a factor `Theta(log |Omega|)` in locality.

For the currently targeted CLIQUE lower bounds, this factor is too expensive unless the initial locality is inverse-polynomially small.
