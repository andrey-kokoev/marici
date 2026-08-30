# Phase-Preserving Completion Is an Oriented Blow-Up

Write a nonzero complex coupling as

\[
z=ru,
\qquad
r>0,
\quad
u\in U(1).
\]

The ordinary Euclidean completion of \(\mathbf C^\times\) adds one point at
zero and identifies every phase approaching it. If phase provenance must
survive amplitude collapse, the appropriate source completion is instead

\[
\widetilde{\mathbf C}
=[0,\infty)\times U(1),
\]

with blow-down map

\[
\pi(r,u)=ru.
\]

The map is one-to-one over \(\mathbf C^\times\) and collapses the boundary

\[
\pi^{-1}(0)=\{0\}\times U(1)
\]

to the scalar zero. Thus a phase-preserving zero is not one extra bit or one
extra point; it is a full (U(1)) boundary fiber.

## Completion theorem

Give the polar source the product metric

\[
d_{\mathrm{pol}}((r,u),(s,v))
=|r-s|+|u-v|.
\]

The completion of \((0,\infty)\times U(1)\) is exactly
\([0,\infty)\times U(1)\), since the radial half-line completes by adjoining
zero and (U(1)) is compact and complete.

The blow-down is continuous on every bounded radial set, because

\[
|ru-sv|
\le
|r-s|+s|u-v|.
\]

The inverse polar map is not continuous at scalar zero. Distinct boundary
phases remain separated in (d_{\mathrm{pol}}) while their scalar images
coalesce.

For example,

\[
x_N=(1/N,1),
\qquad
y_N=(1/N,i).
\]

Then

\[
|\pi(x_N)-\pi(y_N)|=\sqrt2/N\to0,
\]

but

\[
d_{\mathrm{pol}}(x_N,y_N)=\sqrt2.
\]

The phase-sensitive completion is strictly finer than the scalar analytic
completion.

## Which scalar Cauchy sequences are rejected

Let (r_N\to0) while (u_N) alternates between (1) and (-1). Then
(z_N=r_Nu_N\) is Cauchy in \(\mathbf C\) and converges to zero. The polar
sequence is not Cauchy because successive phase distances remain two.

Therefore retaining phase through completion is not merely adding metadata
after scalar completion. It changes which source sequences are Cauchy. A
phase-preserving source must either require phase convergence or enlarge its
boundary further with a weaker object such as a phase measure; the latter is
a different coefficient lens.

## Real locus

For a real coupling, the angular group is

\[
S^0=\{+1,-1\}\simeq C_2.
\]

The oriented real blow-up replaces zero by two boundary points. Hence the
earlier (C_2) sheet bit is exactly the real one-dimensional boundary fiber.
The generic complex lens enlarges it to (U(1)).

This explains when a torsor bit is sufficient: only after a source-derived
real structure reduces the angular coefficient group.

## Decoder consequence

The boundary phase can retain provenance or coherent orientation, but it does
not create a nonzero amplitude. Any decoder containing (1/r) still diverges
at the boundary. Blow-up resolves direction, not invertibility.

The typed hierarchy is therefore

\[
\text{scalar zero}
\longleftarrow
\text{phase-labelled zero}
\longleftarrow
\text{nonzero coupling},
\]

where the left arrow forgets boundary orientation and neither arrow supplies
a lower radial bound.

## Authority boundary and falsifiers

The oriented blow-up is an abstract coefficient completion. It does not prove
that a theta/Fock source retains boundary phase, nor that the scalar defect
model has room for the (U(1)) fiber. Such retention needs a source-derived
phase channel or matrix/internal-state lift.

Falsifiers are:

- replacing a complex zero by only a (C_2) fiber without a real structure;
- calling blow-up topology identical to scalar Euclidean topology;
- completing scalars first and claiming the lost phase was canonically
  recovered afterward;
- admitting oscillatory phase-collapse sequences as polar Cauchy sequences;
- using boundary phase as evidence for a positive radial lower bound;
- importing the blow-up into theta completion without a source phase law.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to identify the exact topology behind completion-stable
phase provenance.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Phase retention is an oriented blow-up: (C_2) on a real locus,
(U(1)) for a complex coefficient, and strictly finer than scalar completion.
