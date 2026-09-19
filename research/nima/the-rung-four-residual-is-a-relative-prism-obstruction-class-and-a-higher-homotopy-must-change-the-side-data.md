# The rung-four residual is a relative prism obstruction class, and a higher homotopy must change the side data

## Absolute versus relative topology

Let

\[
P=\Delta^1\times\Delta^3.
\]

The prism is contractible, so its positive-degree absolute cohomology vanishes:

\[
H^k(P)=0,
\qquad k>0.
\]

Therefore an arbitrary algebraic top defect can always be written as a
coboundary if one is free to invent or alter side cochains. This formal fact
has no source authority and would amount to fitting a cancelling face.

The actual problem freezes the two end systems and all already sewn lower
faces. It is therefore relative. The oriented four-cell generates

\[
H^4(P,\partial P)\cong\mathbb R
\]

(or the corresponding coefficient module). Evaluation of the fixed boundary
packet on this relative fundamental class gives the obstruction coefficient.

## Current coefficient

In the independent Green target, the coefficient is

\[
[\mathcal R_p]
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z),
\qquad E_p(b_z)>0.
\]

A nonzero value means that no filler exists while every boundary face and its
codomain identification remain fixed.

## Role of the higher equivalence

A Green-system comparison

\[
\eta_G:G_{\rm local}\Longrightarrow G_{\rm ind}
\]

can change the relative boundary datum in an authorized way. Its naturality
cochain contributes

\[
\delta\eta_G
\]

to the four-dimensional prism boundary. The correct closure equation is

\[
\mathcal R_p+\delta\eta_G=0.
\]

This is the homotopy interpretation of a possible opposite-oriented
correction. The correction is not a scalar chosen to equal `-R_p`; it is the
boundary of a source-derived system equivalence whose lower components are
fixed independently.

## Five-dimensional law

For equivalences between complete rung-one-through-rung-four construction
laws, use

\[
Q=\Delta^1\times\Delta^4.
\]

Its boundary contains:

- the two four-dimensional construction laws;
- five homotopy prisms comparing their facets.

The five-dimensional coherence equation says that the alternating sum of these
six boundary components vanishes. The four-dimensional residual can disappear
only as the boundary of one of those independently constructed comparison
prisms.

## Finite acceptance test

A candidate `eta_G` is accepted only if:

1. its vertex and edge components are defined before Xi-zero specialization;
2. its restrictions reproduce the already verified local Green comparisons;
3. its cellular coboundary equals the complete matrix-valued prism defect;
4. the equality holds before scalar evaluation on `b_z`;
5. prime, cutoff, reciprocal, and multiplicity-jet restrictions commute.

Testing only

\[
(\delta\eta_G)(b_z)=-\mathcal R_p(b_z)
\]

after specialization is fitted cancellation and does not fill the relative
class.