# Exact Star--Pair Identity on Focused Layered Instances

This note supplies one complete semantic SPA gadget for the formal layered language. It proves an exact language identity with polynomial-time, length-preserving constructors.

The result identifies the focused language as an AND of local satisfiability predicates. It does **not** constrain the internal gates of a circuit computing that language.

## 1. Admissible focused inputs

Fix `t >= 2`. An admissible focused input `I` has:

1. singleton positional masks `A_r={v_r}`;
2. every required edge `{v_r,v_s}` present;
3. every unselected vertex isolated and carrying the canonical padded contradiction;
4. trivial hash width `m=0`;
5. arbitrary selected formulas `phi_{v_r}` and assignment masks `R_{v_r}`.

Define the local predicate

```text
P_r(I)=1
iff
there exists alpha in {0,1}^d obeying R_{v_r} and satisfying phi_{v_r}.
```

Because the selected vertex tuple and graph edges are fixed, the language on this slice is exactly

```text
L(I) = AND_{r=1}^t P_r(I).
```

## 2. Canonical padded replacements

Let `TOP` be the canonical padded tautology of the selected formula width, and let `FREE` be the assignment mask allowing both values at every coordinate.

Replacing a selected block by `(TOP,FREE)` preserves input length and makes its local predicate identically one.

## 3. Pair constructor

For every pair `1 <= r < s <= t`, define `PAIR_{r,s}(I)` by:

- retaining selected blocks `r` and `s` unchanged;
- replacing every other selected formula by `TOP`;
- replacing every other selected assignment mask by `FREE`;
- leaving the singleton vertex masks and selected graph edges unchanged;
- keeping `m=0`.

The constructor scans the padded block encodings and is polynomial-time and length-preserving.

### Lemma 3.1

For every admissible focused input `I`,

```text
L(PAIR_{r,s}(I)) = P_r(I) AND P_s(I).
```

### Proof

All positions other than `r,s` have tautological formulas and unrestricted masks, so they always admit assignments. The fixed graph and vertex checks already pass. Thus the pair instance has a witness exactly when blocks `r` and `s` each admit an allowed satisfying assignment.

## 4. Star constructor

Define

```text
STAR(I)=I.
```

The term "star" records that all selected local predicates meet at the same fixed witness tuple.

### Theorem 4.1: exact star--pair identity

For every admissible focused input `I` with `t>=2`,

```text
L(STAR(I))
=
AND_{1 <= r < s <= t} L(PAIR_{r,s}(I)).
```

### Proof

By the focused-slice identity,

```text
L(STAR(I)) = AND_r P_r(I).
```

By Lemma 3.1, the right side is

```text
AND_{r<s} (P_r(I) AND P_s(I)).
```

If every `P_r=1`, both expressions are one. If some `P_q=0`, the left side is zero and every pair involving `q` is zero, so the right side is zero. Hence the expressions are equal.

## 5. Equivalent single-block identity

For completeness, define `SINGLE_r(I)` by retaining only selected block `r` and replacing every other selected block by `(TOP,FREE)`. Then

```text
L(I) = AND_r L(SINGLE_r(I)).
```

The pair form is useful when testing consistency of two-block interactions; the single form is the minimal exact decomposition.

## 6. What this proves

The previous SPA proposal lacked constructors and an exact identity. The repaired statement now provides:

- explicit star constructor;
- explicit pair constructors;
- fixed admissible domain;
- explicit combining function `F=AND`;
- polynomial runtime;
- exact length preservation;
- complete proof of the language identity.

Therefore SPA is now a valid **semantic audit identity** on the focused trivial-hash slice.

## 7. What this does not prove

The identity is satisfied by the Boolean function, not by a particular parse tree or gate layout. In particular it does not imply:

- that a supplied circuit is literally an AND of pair circuits;
- that internal NOT gates are block-local;
- that mixed gates cannot cancel;
- that the identity yields a polynomial-size monotone representation;
- that graph-edge negations disappear.

A separate representation theorem remains necessary.

## 8. Statistical test version

A statistical SPA test may sample an admissible focused input `I` and compare

```text
f(STAR(I))
```

against

```text
AND_{r<s} f(PAIR_{r,s}(I)).
```

For a worst-case correct decider the equality is pointwise. For an approximate function, its rejection probability is merely a distance from this semantic identity under the named sampling distribution. It still does not reveal circuit syntax.