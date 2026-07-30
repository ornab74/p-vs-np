# Witness-Template Locality Calculus

## 1. Purpose

This note identifies a hard-distribution-specific family of positive-negative rectangles for the standard CLIQUE hard sets and computes two quantities exactly:

1. their locality under the clique-coloring product distribution;
2. their positive-side overlap parameter in condition `A_d`.

The resulting tradeoff is sharp enough to rule out constant-size witness templates as the basis of a large constant-overlap oracle family.

## 2. Hard sets and distribution

Let

```text
U_{n,k} = {K_B : B subseteq [n], |B|=k}
```

be the positive `k`-clique graphs.

Let `q=k-1`. Sample a coloring

```text
chi : [n] -> [q]
```

uniformly, conditioned on `chi` being nonconstant, and let `G(chi)` contain exactly the edges whose endpoints receive different colors. This induces the standard negative distribution on `V_{n,k}`.

The locality measure is the product distribution

```text
D_{n,k}=D^U_{n,k} x D^V_{n,k}.
```

## 3. Monochromatic witness templates

Fix a vertex set

```text
S subseteq [n], |S|=s,
```

where `2<=s<=k`.

Define

```text
U_S = {K_B in U_{n,k} : S subseteq B},
V_S = {G(chi) in V_{n,k} : chi is constant on S}.
```

For every pair `(K_B,G(chi)) in U_S x V_S`, all edges inside `S` are present in `K_B` and absent from `G(chi)`.

Thus `U_S x V_S` is a natural Karchmer--Wigderson witness rectangle anchored by the vertex pattern `S`.

## 4. Exact positive probability

A uniformly random `k`-set contains `S` with probability

```text
p_U(n,k,s)
= binom(n-s,k-s)/binom(n,k)
= (k)_s/(n)_s,
```

where `(a)_s=a(a-1)...(a-s+1)`.

In particular,

```text
p_U(n,k,s) <= (k/n)^s.
```

## 5. Exact negative probability

There are

```text
q^(n-s+1)
```

colorings that are constant on `S`: choose the common color and color the remaining `n-s` vertices arbitrarily.

Among them, exactly `q` colorings are globally constant. Since the negative distribution conditions on nonconstant colorings,

```text
p_V(n,k,s)
= (q^(n-s+1)-q)/(q^n-q)
= (q^(n-s)-1)/(q^(n-1)-1).
```

For fixed `s` and large `n`, this is asymptotic to

```text
q^(1-s)=(k-1)^(1-s).
```

## 6. Exact rectangle locality

The locality of the single template rectangle is

```text
mu_S
= p_U(n,k,s) p_V(n,k,s)
= [(k)_s/(n)_s]
  * [(q^(n-s)-1)/(q^(n-1)-1)].
```

The simple bound

```text
mu_S <= (k/n)^s q^(1-s)/(1-q^(1-n))
```

shows that constant-size witness templates can have very small individual locality.

For `s=2`,

```text
mu_S
= [k(k-1)/(n(n-1))]
  * [(q^(n-2)-1)/(q^(n-1)-1)],
```

which is asymptotic to

```text
k/n^2.
```

This is the opposite behavior of the negated-edge rectangle, whose positive side consists of cliques avoiding an edge and therefore has locality close to one.

## 7. Template families and condition A_d

Let

```text
F subseteq binom([n],s)
```

be a family of distinct templates, with one oracle rectangle `U_S x V_S` for each `S in F`.

A positive clique `K_B` belongs to exactly

```text
lambda_F(B)
= |{S in F : S subseteq B}|
```

positive sides.

Therefore the CLO condition `A_d` is equivalent, for this template family, to

```text
max_{B in binom([n],k)} lambda_F(B) <= d.
```

Call this maximum the `k`-set load of `F`.

## 8. Constant-template collapse theorem

### Theorem

If

```text
s(d+1) <= k
```

and the family satisfies `A_d`, then

```text
|F| <= d.
```

### Proof

Assume there are `d+1` distinct templates

```text
S_1,...,S_{d+1} in F.
```

Their union has size at most

```text
|S_1 union ... union S_{d+1}| <= s(d+1) <= k.
```

Extend this union to a `k`-set `B`. Then every `S_j` is contained in `B`, so

```text
lambda_F(B) >= d+1,
```

contradicting `A_d`.

## 9. Large-anchor necessity

The contrapositive is useful:

> A template family with more than `d` distinct oracle rectangles satisfying `A_d` must contain anchors whose size exceeds `k/(d+1)`, or must abandon the uniform fixed-size containment form.

In particular, when `d` is constant and `k` grows, a polynomially large oracle family cannot be built from constant-size positive witness anchors.

Large anchors have extremely small positive mass:

```text
p_U(n,k,s) <= (k/n)^s.
```

For

```text
s > k/(d+1),
```

this becomes

```text
p_U <= (k/n)^(k/(d+1)).
```

This is excellent for locality but creates a separate representation problem: the oracle must be indexed by, or otherwise encode, a large fraction of a clique witness.

## 10. Edge-witness specialization

For `s=2`, identify templates with graph edges `e` and write

```text
R_e
= {K_B : e subseteq B}
  x
  {G(chi) : endpoints of e have the same color}.
```

For an edge family `F`, the `A_d` parameter is exactly

```text
d(F)=max_{|B|=k}|F intersect binom(B,2)|.
```

If

```text
2(d+1) <= k,
```

then `A_d` implies

```text
|F| <= d.
```

So a constant-overlap CLO cannot contain a large family of ordinary edge-witness oracle rectangles in the growing-`k` regime.

## 11. Union-locality bound

For an arbitrary template family `F`, the union locality satisfies the union bound

```text
mu(F)
<= sum_{S in F} mu_S.
```

For uniform size `s`,

```text
mu(F)
<= |F| [(k)_s/(n)_s]
       [(q^(n-s)-1)/(q^(n-1)-1)].
```

Under `A_d` and `s(d+1)<=k`, the collapse theorem improves this to

```text
mu(F)
<= d [(k)_s/(n)_s]
      [(q^(n-s)-1)/(q^(n-1)-1)].
```

Hence these families simultaneously have small locality and very small expressive capacity.

## 12. Complete edge family

The family of all edge templates covers every hard pair:

```text
U_{n,k} x V_{n,k}
= union_{e in binom([n],2)} R_e.
```

Indeed, every `k` vertices colored with only `k-1` colors contain a monochromatic pair.

Therefore the union locality of the complete family is exactly

```text
1.
```

Each positive clique belongs to exactly

```text
binom(k,2)
```

positive sides, so the family satisfies `A_d` only for

```text
d >= binom(k,2).
```

This recovers the central tradeoff:

- complete hard-pair coverage gives maximal locality and large overlap;
- constant overlap permits only a constant number of constant-size templates.

## 13. Consequence for the layered program

A successful low-locality CLO conversion cannot merely attach an oracle to every local missing-edge witness.

It must instead prove one of the following:

1. only `O(d)` witness templates are needed;
2. exceptional pairs are anchored by large vertex sets of size `Omega(k/d)`;
3. positive sides are defined by a more sophisticated family whose `k`-set load is at most `d` despite polynomial cardinality;
4. the applicable lower bound can tolerate `d` growing with `k` while retaining a superpolynomial exponent.

The first three are structural representation theorems. The fourth requires a quantitatively stronger CLO lower bound than the currently transferred `n^{Omega(sqrt(k)/d)}` theorem.

## 14. Reference point

Krajicek and Oliveira define condition `A_d` as the requirement that no positive hard input belongs to more than `d` oracle positive sides, and prove a lower bound of size `n^{Omega(sqrt(k)/d)}` for locality bounded by a small constant. The calculations above specialize that condition to witness-containment templates.