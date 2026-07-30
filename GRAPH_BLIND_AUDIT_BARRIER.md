# Graph-Blind Audit Barrier

## Statement of the problem

The existing BRC, SRC, and SPA audits alter auxiliary block formulas, masks, assignments, or hash-seed coordinates. They do not inspect the internal use of graph-edge variables by a circuit.

The final lower-bound step, however, needs a monotone or otherwise restricted circuit in the graph-edge variables.

## Invariance principle

Let an audit choose a base input `(H,Z)` and produce transformed inputs

```text
(H, T_1(Z)), ..., (H, T_k(Z)),
```

while holding the graph `H` fixed.

For any Boolean function `D(H)`, the extended function

```text
F(H,Z) := D(H)
```

passes every such invariance test perfectly because its output is independent of `Z`.

This remains true no matter how many negations or other nonmonotone gates occur in the supplied circuit for `D`.

## Consequence

Auxiliary-only semantic audits cannot imply any syntactic restriction on the graph subcircuit. In particular they cannot, by themselves, imply:

1. absence of negated edge variables;
2. few NOT gates on graph computations;
3. bounded negation width;
4. a polynomial-size monotone graph circuit;
5. bounded-locality graph oracles.

## Relation to the hard projection

On the proposed CLIQUE projection, all local formulas, masks, and hash data are fixed to constants. The restricted decider is simply a general Boolean circuit in graph-edge variables computing the projected graph function.

Every auxiliary audit disappears under this restriction. Thus the argument still needs a theorem about the graph circuit that is not supplied by BRC, SRC, or the current SPA identity.

## Functional monotonicity is insufficient

The projected CLIQUE function is monotone as a Boolean function of graph edges. But functional monotonicity does not provide an efficient monotone circuit transformation. Exponential gaps between monotone and unrestricted circuits rule out such a generic argument.

Therefore adding a semantic edge-monotonicity test would also be insufficient unless it yielded an additional special structural property.

## What a useful graph audit must establish

A graph-sensitive component must target a property for which a lower bound is already known or can plausibly be proved. Examples include:

1. at most `r(n)` total negation gates after restriction;
2. negation width at most `w(n)`;
3. sparse orientation in a Karchmer--Wigderson model;
4. a monotone protocol with bounded communication and bounded error rectangles;
5. a monotone-CLO with small union locality.

The theorem must produce the restricted representation, not infer it from black-box monotonicity alone.

## A restricted salvage route

Known results prove superpolynomial lower bounds for CLIQUE circuits having at most roughly `(1/6) log log n` negation gates in particular parameter regimes. Thus a concrete sufficient target would be:

```text
Audits + normalization
=> after the hard projection, at most (1/6) log log n surviving NOT gates.
```

No present audit implies this bound, but it is a mathematically meaningful endpoint covered by existing literature.

## Conclusion

The current audit suite can certify witness preservation and auxiliary-block decomposition. It cannot complete the graph lower-bound step. A new graph-sensitive representation theorem is necessary.
