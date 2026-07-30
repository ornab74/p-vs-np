# Black-Box Audits Cannot Bound Circuit Syntax

## Statement

Let an audit be any randomized procedure whose interaction with a candidate implementation consists only of choosing inputs and observing the output bit of the Boolean function computed by that implementation. The procedure may be adaptive, may transform instances, and may use verified witnesses, but it does not inspect the circuit graph.

Then no such audit can imply an upper bound on the number, support, or location of NOT gates in the particular supplied circuit representation.

## Representation-invariance theorem

Let `C(x)` be any Boolean circuit and let `h(x)` be any Boolean subcircuit. Define

```text
C_h(x) = (C(x) AND h(x)) OR (C(x) AND NOT h(x)).
```

For every input `x`,

```text
C_h(x) = C(x) AND (h(x) OR NOT h(x)) = C(x).
```

The added NOT gate lies on a directed path to the output. If `h` depends on two or more graph blocks, the added gate is a mixed graph-dependent NOT gate. Repeating the construction produces, for every integer `r`, a circuit `C^(r)` computing exactly the same function as `C` and containing at least `r` additional graph-dependent NOT gates on output paths.

## Corollary

For every black-box audit `A`, every random seed of `A`, and every input-query transcript,

```text
Transcript(A,C) = Transcript(A,C^(r)).
```

Therefore a conclusion such as

```text
passes A  =>  the supplied circuit has at most q(n) NOT gates
```

is false unless the audit is allowed to inspect a canonical representation or the theorem constructs a new circuit rather than describing the supplied one.

## Consequence for the negation-limited route

The valid target cannot be

```text
semantic audit compliance => original circuit has few NOT gates.
```

It must instead be a constructive normalization theorem:

```text
from the audited function and a small circuit for it,
construct an equivalent polynomial-size circuit with few NOT gates.
```

That constructive theorem is substantially stronger and remains open for the hard CLIQUE projection. It cannot follow from input-output tests alone.

## Relation to prior counterexamples

The earlier masked-gate identity

```text
(x AND h) OR (x AND NOT h) = x
```

is the one-output special case. The theorem here shows that the obstruction is universal: arbitrary canceled negation structure can be inserted around any circuit without changing a single audit response.
