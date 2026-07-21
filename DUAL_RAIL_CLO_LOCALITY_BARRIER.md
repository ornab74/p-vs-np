# Dual-Rail Conversion Gives Maximal CLO Locality

## 1. Polynomial monotone representation with complementary inputs

Every Boolean circuit `C(x_1,...,x_N)` of size `s` can be transformed, by propagating positive and negative rails through De Morgan's laws, into a monotone circuit

```text
M(x_1,...,x_N, xbar_1,...,xbar_N)
```

of size `O(s)` such that

```text
M(x,1-x)=C(x).
```

Thus polynomial-size monotone representation is easy if every complemented input is supplied as an additional oracle value.

## 2. Turning complemented edge inputs into local oracles

Use the standard CLIQUE lower-bound sets:

- `U_{m,k}`: graphs consisting of exactly the edges of one `k`-clique;
- `V_{m,k}`: complete `(k-1)`-partite graphs on `[m]`.

For an edge `e`, the complementary input oracle is

```text
y_e(G)=1-E_e(G).
```

A valid positive-negative rectangle for this oracle is

```text
U_e = {u in U_{m,k}: E_e(u)=0},
V_e = {v in V_{m,k}: E_e(v)=1}.
```

On `U_e`, the oracle is 1; on `V_e`, it is 0.

## 3. Union-locality theorem

Assume `m>k>=3` and every multipartite graph in `V_{m,k}` has `k-1` nonempty parts. Then

```text
union_e (U_e x V_e) = U_{m,k} x V_{m,k}.
```

Consequently the union locality of the family of complemented-edge oracles is exactly

```text
mu = 1.
```

### Proof

Fix `u in U_{m,k}` and let `S` be its clique vertex set. Fix `v in V_{m,k}`.

Suppose, for contradiction, that no edge of `v` is absent from `u`. Then every edge of `v` lies inside `S`, because `u` has no edge incident to `[m]\S`.

Take a vertex `w outside S`, which exists because `m>k`. Since `v` has at least two nonempty parts, either:

1. some vertex of `S` lies in a part different from the part containing `w`, producing an edge of `v` incident to `w`; or
2. all of `S` lies in the part containing `w`, in which case two other nonempty parts, or one other nonempty part and a vertex outside that common part, produce an edge with at least one endpoint outside `S`.

In either case `v` contains an edge `e` not present in `u`. Hence `(u,v) in U_e x V_e`.

Since `(u,v)` was arbitrary, the rectangle union covers the entire product.

## 4. Consequence

The generic dual-rail conversion constructs a polynomial-size monotone circuit with local oracles, but its locality is maximal. It therefore cannot be combined with known CLIQUE CLO lower bounds requiring locality bounded away from 1, such as `mu <= 1/50`.

This isolates the compression problem more precisely:

> Construct a polynomial-size monotone/CLO representation whose use of negative graph information is compressed into oracle rectangles of genuinely small union locality.

Simply moving every graph negation to an input oracle does not accomplish this.

## 5. Status

- polynomial-size dual-rail representation: proved;
- pointwise correctness on consistent rails: proved;
- low CLO locality: false for the direct complemented-edge construction;
- special low-locality compression exploiting the layered audits: open.
