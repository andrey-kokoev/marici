# Two four-presentation phases form a homotopy prism whose top cell can carry the rung-four residual

## Correct combinatorial object

One phase with four presentation vertices

\[
[S,A,C,G]
\]

is naturally organized as a tetrahedron `Delta^3`. Two phases do not form an
eight-vertex simplex. They form the prism

\[
\Delta^1\times\Delta^3,
\]

with eight vertices

\[
X_-,X_+,
\qquad X\in\{S,A,C,G\}.
\]

Its dimension is

\[
1+3=4.
\]

The two tetrahedral ends are the backward and forward coherence systems. The
side cells compare their vertices, edges, and triangle coherences.

## Homotopy equation

Let `F_-` and `F_+` denote the two complete four-presentation systems. A prism
filler is a homotopy `H` satisfying

\[
F_+-F_-=\partial H+H\partial.
\]

At lower dimensions this equation supplies:

- four vertex comparisons;
- six edge homotopies;
- four triangle modifications;
- one top prism coherence.

The top equation is exactly where a residual left after separate rung-four
sewing can live.

## Interpretation of the defect

The crossing defect

\[
\Delta=U_{\rm G4}-T_{\rm PB}
\]

should therefore be treated as the difference of the two end systems. The
rung-four scalar

\[
\mathcal R_p(b_z)
=(1-p^{-2\operatorname{Re}z})E_p(b_z)
\]

is a candidate evaluation of the unfilled top prism boundary, rather than an
extra vertex or an omitted scalar correction.

An oppositely oriented value, such as the sign reversal of the observed Evans
projection, is then naturally the other orientation of the same prism face.
It is not inserted as a cancelling coefficient.

## Next coherence level

There are two distinct promotions:

1. comparing two tetrahedral presentation systems uses the four-dimensional
   prism `Delta^1 x Delta^3`;
2. comparing two complete rung-one-through-rung-four construction laws uses
   `Delta^1 x Delta^4`, a five-dimensional homotopy-of-constructions object.

The second is the genuine next-level law: an equivalence between the systems
that generate all four rungs, not another response inside one system.

## Nonautomatic closure

Passing to the prism does not make the residual vanish. It relocates the
problem from equality

\[
F_+=F_-
\]

to construction of a source-derived homotopy `H`. If the side homotopies are
already supplied by the sewn lower cells, their oriented top boundary is a
well-typed candidate for the missing rung-four relation. If no such `H` is
source-derived, the prism records the obstruction without removing it.

## Concrete next test

Inventory the existing lower sewing maps as faces of `Delta^1 x Delta^3` and
compute its cellular boundary. The test succeeds only if every side face is an
already authorized comparison and the sole unmatched top component evaluates
to `R_p(b_z)` with its existing orientation.