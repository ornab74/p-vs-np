# Certified Orientation Circuit Model

## 1. Motivation

Gate orientation is semantic: it concerns the complete Boolean function computed at an internal gate as a function of the original circuit inputs. A claimed small orientation vector cannot generally be verified merely by inspecting the gate label or by black-box sampling.

This note defines a restricted representation in which a valid orientation upper bound is part of the syntax.

## 2. Positive and complement rails

Let the original input be

```text
x = (x_1,...,x_N).
```

For a set `S subseteq [N]`, expose the rail tuple

```text
R_S(x) = (x_1,...,x_N, (not x_i)_{i in S}).
```

A monotone rail circuit is an AND/OR circuit with no internal NOT gates whose leaves are positive variables `x_i`, selected complement rails `not x_i` for `i in S`, and constants.

Such a circuit computes a function with orientation contained in the characteristic vector of `S`.

## 3. Certified gate representation

A width-`w` certified-oriented circuit consists of an ordinary DAG of named internal gates together with, for every gate `g`:

1. a set `S_g subseteq [N]` with `|S_g| <= w`;
2. an explicit monotone rail circuit `H_g` over `R_{S_g}(x)`;
3. a declaration that the output of gate `g` is exactly `H_g(R_{S_g}(x))`.

The representation is flattened with respect to the original inputs. The circuits `H_g` may share named monotone subcircuits, but their semantics do not rely on unverified orientation claims about other gates.

The output gate's rail circuit computes the represented Boolean function.

## 4. Syntactic verification

A deterministic verifier checks:

1. every `S_g` is explicitly listed and has size at most `w`;
2. every leaf of `H_g` is a constant, a positive input `x_i`, or a complement rail `not x_i` with `i in S_g`;
3. every internal node of `H_g` is AND or OR;
4. references are acyclic and well formed;
5. the designated output is defined.

These checks are polynomial in the total certificate length.

No general circuit-equivalence check is needed because the rail circuits are the representation itself, rather than auxiliary assertions about a separately supplied circuit.

## 5. Certified orientation lemma

### Lemma

For every gate `g` in a width-`w` certified-oriented circuit, the characteristic vector of `S_g` is an orientation of the function computed at `g`.

### Proof

By definition, `H_g` is monotone in all its formal rail inputs. Substituting `not x_i = x_i xor 1` for `i in S_g` and retaining the positive copy of every `x_i` gives

```text
f_g(x) = H_g(x, x xor beta_g),
```

where `beta_g` is supported on `S_g`. Thus `beta_g` is an orientation and has weight at most `w`.

## 6. Complete restricted lower bound

Combining the certified orientation lemma with `SPARSE_ORIENTATION_TRANSFER.md` gives:

> Any bounded-fan-in width-`w` certified-oriented circuit of depth `d` computing the projected layered CLIQUE slice satisfies
>
> ```text
> d(4w+1) = Omega(m).
> ```

Therefore the projected layered language has no certified-oriented circuit family with both polylogarithmic depth and polylogarithmic orientation width.

## 7. Size accounting

Let

```text
L = sum_g size(H_g)
```

be the flattened certificate length. Verification takes time polynomial in `L+N`.

The lower bound concerns represented circuit depth and semantic gate orientations. Flattening can be much larger than an ordinary shared circuit. Consequently this model is a transparent restricted class, not a free normalization of arbitrary circuits.

## 8. Relationship to NOT count

A circuit may have many syntactic NOT gates but small certified orientation width if those NOT gates ultimately depend on only a small set of original variables.

Conversely, a single gate may require a dense orientation even if a particular representation uses few NOT symbols.

Thus orientation width and NOT count are incomparable as raw syntactic measures.

## 9. Relationship to black-box audits

BRC, SRC, SPA, and output resampling tests operate on the computed function. They cannot generate or validate the rail circuit `H_g` for every internal gate.

A bridge from the original audit program to this model would need either:

1. white-box access to the circuit and a constructive rail decomposition algorithm;
2. a proof-carrying circuit format in which the decider is supplied directly as certified-oriented syntax;
3. a canonical reconstruction theorem that builds the rail circuits from independently verified semantic structure.

The current repository proves none of these bridges.

## 10. Value of the model

The model isolates a rigorously verifiable structural property that is strong enough for an existing lower bound. It avoids the impossible claim that black-box tests can bound a supplied circuit's syntax.

It also turns the next research question into a concrete algorithmic problem:

```text
Can the layered identities construct small rail supports S_g and monotone rail circuits H_g without exponential blowup?
```

A positive answer in a sufficiently broad regime would be new circuit-complexity progress.