# Certificate-Complexity Anti-Hiding Theorem

## 1. Purpose

`ORIENTATION_MASS_BARRIER.md` shows that random decreasing-edge audits do not control orientation support for arbitrary Boolean functions. This note gives an exact sufficient condition under which they do: small two-sided certificate complexity.

The result yields another rigorous restricted circuit endpoint. It remains a white-box condition on internal gate functions and is not implied by output correctness alone.

## 2. Certificates

Let

```text
f : {0,1}^N -> {0,1}.
```

A `b`-certificate for an input `x` with `f(x)=b` is a set of fixed coordinates and their values such that every input extending those assignments also has value `b`.

Define

```text
C_b(f) = max over x with f(x)=b
         of the minimum size of a b-certificate for x.
```

Write

```text
c(f) = C_0(f) + C_1(f).
```

## 3. Directional violation mass

For coordinate `i`, sample the other `N-1` coordinates uniformly and write the two completions as `z^(i,0)` and `z^(i,1)`.

Define

```text
nu_i(f) = Pr_z[f(z^(i,0))=1 and f(z^(i,1))=0].
```

The unique minimal orientation contains coordinate `i` exactly when `nu_i(f)>0`.

## 4. Certificate margin lemma

### Lemma

If `nu_i(f)>0`, then

```text
nu_i(f) >= 2^(-(C_0(f)+C_1(f)-2)).
```

### Proof

Choose a decreasing edge `(x^(i,0),x^(i,1))` with

```text
f(x^(i,0))=1,
f(x^(i,1))=0.
```

Let `A` be a minimum 1-certificate for `x^(i,0)` and `B` a minimum 0-certificate for `x^(i,1)`.

Both certificates must contain coordinate `i`:

- if `A` omitted `i`, then `x^(i,1)` would extend `A`, contradicting `f(x^(i,1))=0`;
- if `B` omitted `i`, then `x^(i,0)` would extend `B`, contradicting `f(x^(i,0))=1`.

Outside coordinate `i`, the two endpoint assignments agree. Hence the assignments in `A` and `B` are compatible on all other coordinates.

Fix every coordinate appearing in `(A union B) \ {i}` to its common endpoint value. There are at most

```text
(C_1(f)-1) + (C_0(f)-1)
= C_0(f)+C_1(f)-2
```

such constraints.

For every completion of the remaining coordinates:

- the `i=0` endpoint extends `A` and therefore has value 1;
- the `i=1` endpoint extends `B` and therefore has value 0.

Thus the decreasing contexts contain a subcube of codimension at most `C_0(f)+C_1(f)-2`, proving the bound.

## 5. Orientation-support theorem

Define the random directional edge-audit failure

```text
delta_dir(f) = (1/N) sum_i nu_i(f).
```

### Theorem

If

```text
C_0(f)+C_1(f) <= c
```

and

```text
delta_dir(f) <= delta,
```

then the minimal orientation weight satisfies

```text
|beta_min(f)| <= N delta 2^(c-2).
```

### Proof

Every oriented coordinate has violation mass at least `2^(-(c-2))`. Therefore

```text
N delta
>= sum_i nu_i(f)
>= |beta_min(f)| 2^(-(c-2)).
```

Rearrange.

## 6. Gate-wise circuit consequence

Let `C` be a bounded-fan-in circuit whose internal gates are regarded as Boolean functions of the original graph-edge variables after the layered-to-CLIQUE projection.

Assume for every internal gate `g`:

```text
C_0(g)+C_1(g) <= c
```

and

```text
delta_dir(g) <= delta.
```

Then every gate has orientation weight at most

```text
w = N delta 2^(c-2).
```

The sparse-orientation transfer theorem therefore gives

```text
depth(C) (4 N delta 2^(c-2) + 1) = Omega(m),
```

where `m` is the number of graph vertices and `N=binom(m,2)` is the number of graph-edge variables.

This is an end-to-end lower bound for the certified gate class.

## 7. Inverse-polynomial regime

If

```text
c = O(log N)
```

and each gate has sufficiently small directional audit mass, then `w` can be polynomially or polylogarithmically bounded.

For example, if

```text
c <= a log_2 N + 2
```

and

```text
delta <= w_0 / N^(a+1),
```

then every gate has orientation weight at most `w_0`.

The theorem therefore converts a quantitative gate-level audit into a sparse-orientation certificate whenever two-sided certificates are logarithmic.

## 8. Bidirectional support variant

Define

```text
rho_i(f) = Pr_z[f(z^(i,0)) != f(z^(i,1))]
```

and

```text
delta_flip(f) = (1/N) sum_i rho_i(f).
```

Coordinate `i` belongs to the ordinary variable-dependence support exactly when `rho_i(f)>0`.

The same certificate proof gives

```text
rho_i(f)>0
=>
rho_i(f) >= 2^(-(C_0(f)+C_1(f)-2)).
```

Hence

```text
|supp(f)| <= N delta_flip(f) 2^(c-2).
```

This variant is relevant to the mixed-negation theorem, whose low-support condition concerns the full graph-variable support of negation-input functions rather than only decreasing orientation coordinates.

## 9. Average-gate exceptional-set bound

Let `G` be a collection of gate functions satisfying `C_0(g)+C_1(g)<=c`, and let

```text
average_delta = (1/|G|) sum_g delta_dir(g).
```

For any threshold `w_0>0`, the number of gates with orientation weight greater than `w_0` is at most

```text
|G| N average_delta 2^(c-2) / w_0.
```

This follows by summing the gate-wise support bounds and applying Markov's inequality.

The analogous statement with `delta_flip` bounds the number of gates with large full variable support.

## 10. Limitations

The theorem does not show that arbitrary small circuits have small certificate complexity at every gate.

It does not show that output-level BRC, SRC, SPA, or graph resampling bounds the internal gate quantities `delta_dir(g)`.

Black-box access to the final output cannot observe canceled internal violations.

Thus the theorem defines a rigorous restricted model and an exact sufficient bridge, but not the unrestricted normalization needed for `NP not subseteq P/poly`.

## 11. New precise target

A genuine unrestricted advance could now take either of two forms:

1. construct a polynomial-size canonical circuit whose gates have logarithmic two-sided certificate complexity and small directional violation mass; or
2. prove a circuit-to-CLO theorem using the polynomial subcubes supplied by the certificate-margin lemma as oracle rectangles.

The certificate lemma guarantees polynomially thick violation rectangles when `c=O(log N)`, addressing the anti-hiding obstruction for that class.