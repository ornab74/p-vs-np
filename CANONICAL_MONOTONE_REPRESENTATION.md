# Canonical Monotone Representation and the Compression Gap

This note addresses the representation component directly. It gives an exact monotone representation for the trivial-hash layered language and isolates why that representation does not yet yield a lower bound contradiction.

## 1. Trivial-hash layered language

Set `m=0` and define, for each vertex `v`, the local oracle bit

```text
Y_v = 1
iff
there exists an assignment obeying R_v and satisfying phi_v.
```

For a positional tuple

```text
q=(v_1,...,v_t),  v_r in A_r,
```

define its graph monomial

```text
M_q(H,Y)
=
(AND_{r<s} E_{v_r,v_s})
AND
(AND_r Y_{v_r}).
```

All occurrences of graph-edge variables and local-oracle variables are positive.

## 2. Exact monotone DNF

### Theorem 2.1

The trivial-hash layered language is exactly

```text
L_layer^0(H,Phi,A,R)
=
OR_{q in A_1 x ... x A_t} M_q(H,Y).
```

### Proof

If a term `M_q` is one, the selected tuple has all required cross-layer edges and every selected block admits an allowed satisfying assignment, so the tuple and assignments form a witness. Conversely, every witness determines a tuple whose edge and local-oracle literals are all one, making its term one.

Thus the language has a monotone circuit with local SAT-oracle inputs.

## 3. Size

The DNF has at most

```text
product_r |A_r| <= B^t
```

terms, each of size `O(t^2+t)`.

This is polynomial only when `t` is constant. In regimes where monotone CLIQUE lower bounds are superpolynomial, `B^t` is itself superpolynomial.

Therefore the canonical representation does not contradict known lower bounds; it merely restates exhaustive witness search.

## 4. The required compression theorem

To use an assumed polynomial-size nonmonotone decider, the project needs a theorem of the following form.

### Open representation theorem

Assume the full layered language has a polynomial-size circuit family satisfying the exact audit identities. Construct a circuit

```text
C_mon(H, Y, O_1,...,O_s)
```

such that:

1. `C_mon` is monotone in graph-edge variables and all displayed oracle inputs;
2. `C_mon` has polynomial size;
3. each `O_i` has a precisely defined positive-negative rectangle;
4. the union oracle locality is quantitatively bounded;
5. `C_mon` agrees pointwise with the required graph projection on the positive and negative hard-instance sets.

The canonical DNF proves existence without item 2. The unresolved task is polynomial compression with controlled oracles.

## 5. Why semantic audits do not provide compression automatically

WV, FOCUS, BRC, SRC, and the exact SPA identity constrain values of the computed Boolean function on related inputs. They do not describe how a nonmonotone circuit shares intermediate computations among the exponentially many witness tuples.

A correct circuit may use negated graph-edge variables internally even though the graph projection is a monotone Boolean function. There is no general polynomial-size conversion from an arbitrary nonmonotone circuit for a monotone function into a monotone circuit; proving such a conversion for CLIQUE would itself resolve the central monotone-versus-general circuit gap used by the proposed argument.

## 6. Graph-negation obstruction

The current BRC and SRC audits resample formulas, assignment masks, or unused seed blocks while holding the graph fixed. Consequently they give no direct control over how the circuit uses graph-edge variables.

The exact SPA identity is also a function identity on focused formula blocks. It does not prohibit a circuit from computing the graph component through arbitrary negations.

Thus any valid representation theorem needs at least one new ingredient specifically governing graph-edge dependence, such as:

- a two-sided graph-edge audit with a proved language identity;
- an interpolation theorem tailored to the reduction;
- a proof-complexity translation producing a monotone separator;
- or a direct monotone-CLO construction with locality bounds.

## 7. Focused slice versus global graph projection

On a focused instance with a fixed selected tuple, the representation collapses to

```text
AND_r Y_{v_r},
```

which is a size-`O(t)` monotone circuit. This is useful for identifying the local block function, but all graph-search complexity has been removed by fixing the tuple.

On the global slice where every `Y_v=1`, the function becomes `t`-partite CLIQUE:

```text
OR_{q} AND_{r<s} E_{v_r,v_s}.
```

This is exactly where the exponential number of candidate tuples and the monotone lower bound live.

A proof cannot simultaneously use focus to remove tuple search and then invoke a lower bound whose hardness comes from tuple search. The representation theorem must operate before that information is destroyed.

## 8. Status

Completed:

- exact monotone DNF with local SAT-oracle inputs;
- exact size accounting;
- exact identification of the polynomial-compression gap;
- explicit graph-negation obstruction.

Open:

- polynomial-size monotone or monotone-CLO representation derived from an assumed small general circuit;
- oracle locality bound;
- rectangle condition for known arbitrary-depth CLO lower bounds;
- lower-bound-compatible hard projection.