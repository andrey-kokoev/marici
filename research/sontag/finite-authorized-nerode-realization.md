# Finite authorized Nerode realization

## Bounded question

Can a Marici object be reconstructed as the smallest quotient of source states
indistinguishable under all admissible future experiments? If so, does that
quotient automatically carry successor dynamics?

## Toy system

There are six states, one binary output, and one control `a`:

```text
p -a-> u -a-> z0 -a-> z0
q -a-> v -a-> z1 -a-> z1
```

Only `z1` has output one. Every other state has output zero. An observer is not
authorized to apply `a`; a controller is.

For actor alphabet `U` and depth `h`, define two states to be equivalent when
every word over `U` of length at most `h` produces the same complete output
trace. Call the quotient `Q(U,h)`.

## Exact attack

For the controller, `p` and `q` are equivalent at depth one but distinguishable
at depth two. At depth one their successors `u` and `v` are already distinct.
Consequently the depth-one quotient is not a congruence under `a`: successor
dynamics do not descend as an endomap of `Q(U,1)`.

They do descend in the typed form

```text
Q(U,h) --a--> Q(U,h-1).
```

The reason is exact: prepending `a` consumes one unit of the remaining
continuation budget. Once the finite Nerode partition stabilizes, the graded
family becomes stationary and the usual coalgebra on a single quotient
appears.

For the unauthorized observer, the word family contains only the empty word,
so no amount of nominal depth separates `p` from `q`. The minimal realization
is therefore actor-relative.

## What this says about the Marici object

The candidate reconstruction is not one naked quotient. It is initially a
source-indexed and authority-indexed family of quotients:

```text
(source, actor, admitted controls, continuation resource) |-> behavioral state
```

with typed successor maps between resource indices. A stationary carrier is a
derived special case, certified by stabilization or an unbounded
continuation-closed semantics.

This identifies a plausible missing primitive: the residual continuation
resource, or more generally the residual experiment context. Without it, a
finite closed packet can claim a successor operation that is not well-defined.

The claim is deliberately bounded. It does not yet establish that every
Marici realization is finite, stabilizing, deterministic, or representable by
word experiments. It does establish a hostile counterexample to treating a
finite-horizon behavioral quotient as an ordinary stationary state space.

## Verification

Run:

```text
python research/sontag/checkers/finite_authorized_nerode_realization.py
```

The dependency-free checker enumerates all admitted words and exact trace
partitions, tests the failed same-level congruence, tests the graded successor
maps, and tests actor relativity.
