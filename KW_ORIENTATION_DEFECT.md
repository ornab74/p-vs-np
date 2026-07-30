# Karchmer--Wigderson Orientation Defect

This note replaces raw NOT-gate count by a more semantic, pair-based invariant.  The invariant measures how often the standard circuit descent for a monotone function terminates at a reversed literal.

The construction below is exact.  The final conversion from small defect to a bounded-locality CLO remains a separate theorem obligation.

## 1. Positive and negative hard sets

Let

```text
U,V subseteq {0,1}^n
```

be disjoint sets such that the target Boolean function `f` satisfies

```text
f(u)=1 for every u in U,
f(v)=0 for every v in V.
```

For a monotone Karchmer--Wigderson witness on `(u,v)`, a valid output is an index `i` such that

```text
u_i=1 and v_i=0.
```

## 2. Negation-normal form

Let `C` be a fan-in two Boolean circuit over `AND`, `OR`, and `NOT`, of size `s`, computing `f`.

Create for every gate `g` two gates

```text
g^+ = value computed by g,
g^- = complement of the value computed by g.
```

The recurrences are

```text
(a AND b)^+ = a^+ AND b^+,
(a AND b)^- = a^- OR b^-,
(a OR b)^+  = a^+ OR b^+,
(a OR b)^-  = a^- AND b^-,
(NOT a)^+   = a^-,
(NOT a)^-   = a^+.
```

At an input `x_i`, the leaves are `x_i` and `NOT x_i`.

This produces an equivalent negation-normal-form DAG `N(C)` of size at most `2s+O(n)`.  All internal gates are monotone; negations occur only in input literals.

## 3. Standard descent protocol

Fix `(u,v) in U x V`.  At the output gate of `N(C)`, the gate value is `1` on `u` and `0` on `v`.

Maintain a current gate `g` satisfying

```text
g(u)=1 and g(v)=0.
```

The descent rule is:

- If `g=a OR b`, Alice selects a child whose value on `u` is `1`.  Since `g(v)=0`, both children are `0` on `v`, so the selected child still differs as `1/0`.
- If `g=a AND b`, Bob selects a child whose value on `v` is `0`.  Since `g(u)=1`, both children are `1` on `u`, so the selected child still differs as `1/0`.

After finitely many steps the protocol reaches a literal.

There are two cases.

### Positive terminal

If the terminal is `x_i`, then

```text
u_i=1 and v_i=0,
```

so `i` is a valid monotone Karchmer--Wigderson answer.

### Reversed terminal

If the terminal is `NOT x_i`, then

```text
u_i=0 and v_i=1.
```

The pair differs, but in the wrong orientation for the monotone relation.

## 4. Orientation defect

Fix deterministic tie-breaking for the descent choices.  Define

```text
Rev_C subseteq U x V
```

as the set of pairs on which the descent terminates at a reversed literal.

For a named distribution `nu` on `U x V`, define

```text
defect_nu(C) = Pr_{(u,v)~nu}[(u,v) in Rev_C].
```

This quantity is called the **orientation defect** of the circuit under `nu`.

It is a representation-dependent quantity.  A function-level version is

```text
defect_nu(f,s)
  = min defect_nu(C)
```

where the minimum ranges over circuits `C` of size at most `s` computing `f`.

## 5. Exact protocol statement

### Lemma

Every size-`s` Boolean circuit separating `U` from `V` yields a directed acyclic Karchmer--Wigderson descent protocol with:

1. `O(s+n)` nodes;
2. constant communication per local move, apart from the gate identifier;
3. a valid monotone output on every pair outside `Rev_C`;
4. an orientation-reversed output on every pair in `Rev_C`.

### Proof

Use the negation-normal form construction and the descent rule above.  The maintained `1/0` invariant proves correctness of every transition.  A positive literal is a valid monotone witness, while a negative literal has the reversed orientation.  The protocol DAG has one node per gate of `N(C)`.

## 6. Relation to circuits with local oracles

Krajicek's protocol/CLO framework associates monotone circuits with local oracles to monotone Karchmer--Wigderson protocols that make localized errors.

The desired quantitative theorem for this project is:

> If a polynomial-size circuit has orientation defect at most `mu` under the exact hard-pair measure, then it yields a polynomial-size monotone CLO of union locality `O(mu)` separating the same positive and negative hard sets.

This statement is **not proved here**.  Three issues must be resolved explicitly:

1. the reversed-pair set must be represented by admissible oracle rectangles;
2. DAG sharing must remain polynomial rather than being unfolded into an exponential tree;
3. the resulting CLO must satisfy the additional rectangle restriction used by the available arbitrary-depth CLIQUE lower bound.

## 7. Why this invariant is better than raw NOT count

Canceled negations can increase a circuit's syntactic NOT count without changing its function.  Orientation defect ignores a canceled negation unless it changes the actual descent on a positive--negative pair.

The invariant is therefore closer to the semantic obstruction relevant to monotone lower bounds.

It is still not determined by black-box input-output audits: equivalent circuits may have different descent structures and different defects.  Any use of the invariant must either minimize over equivalent circuits or provide a white-box normalization theorem.

## 8. New central target

The unrestricted route can now be stated as the following falsifiable theorem.

> **Low-defect representation target.**  Assuming a polynomial-size circuit family for the formal layered language, construct an equivalent polynomial-size circuit family whose orientation defect on the CLIQUE hard-pair distribution is below the locality threshold required by a published monotone-CLO lower bound.

This target is weaker than universal monotone simulation and stronger than ordinary output stability.  It precisely measures the missing graph-sensitive structure.

## References

- M. Karchmer and A. Wigderson, monotone communication games and circuit depth.
- J. Krajicek, *Randomized feasible interpolation and monotone circuits with a local oracle*, 2018.
- J. Krajicek and I. C. Oliveira, *On monotone circuits with local oracles and clique lower bounds*, 2018.
