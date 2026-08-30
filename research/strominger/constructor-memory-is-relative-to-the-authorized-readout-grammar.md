# Constructor memory is relative to the authorized readout grammar

## Question

Is the 32-entry state

\[
(U_n,V_n)=(C^n,C^{-n})
\]

intrinsic to the neutral-decoration orbit?

## Result

No. The orbit admits three exact presentations:

| retained state | retained coordinates | additional constructor capabilities |
|---|---:|---|
| \(n\in\mathbb Z\) | 1 | integer power and group inverse |
| \(U_n=C^n\in GL(4,\mathbb Z)\) | 16 | group inverse |
| \((U_n,V_n)\in GL(4,\mathbb Z)^2\) | 32 | matrix multiplication only |

All three reconstruct the same magnetic response. Their difference is not
extensional information. It is where executable capability resides.

## Exact factorization

The source supplies a group-valued response, so inversion is part of the
source grammar:

\[
V_n=U_n^{-1}.
\]

Therefore the two-sided state is redundant whenever the readout admits group
inversion. If inversion is withheld from the readout grammar, retaining
\(V_n\) makes the reverse tail available without constructing an inverse.

The exponent-only presentation compresses further:

\[
n\longmapsto C^n\longmapsto (C^n,C^{-n}).
\]

It is exact only relative to an admitted integer-power constructor.

## Hostile deletion result

Capability deletion separates the presentations.

- Delete integer power: the grade-only state no longer constructs a response.
- Delete group inverse: the one-sided matrix no longer constructs the reverse
  tail.
- Delete group inverse while retaining both matrices: the two-sided
  multiplication-only readout remains defined.

Thus equal reconstructible information does not imply equal executable
capability.

## Theorem

For this orbit, state size is not an invariant of the represented source
object. It is an invariant only of a pair:

\[
(\text{state presentation},\text{authorized constructor grammar}).
\]

An absolute claim that the orbit needs 1, 16, or 32 stored coordinates is
ill-typed until the allowed readout operations are declared.

The exact unbounded equivalence follows from

\[
(C^n)^{-1}=C^{-n}
\]

and the fixed anti-representation commutator formula. The checker replays the
three presentations against independently expanded source words for
\(-3\le n\le3\).

## Shift in explanation

The earlier result located a fixed-size integral recurrence. The stronger
view is that storage and capability can be exchanged.

The two-sided state internalizes inversion as data. The one-sided state
delegates inversion to the constructor grammar. The grade-only state delegates
both exponentiation and inversion.

So the explanatory object is not a bare state vector. It is a typed
state--constructor pair.

## Claim boundary

This does not establish an information-theoretic minimum over all possible
encodings. It classifies three source-derived exact presentations and proves
that their coordinate counts cannot be compared without fixing the authorized
operations and their cost model.
