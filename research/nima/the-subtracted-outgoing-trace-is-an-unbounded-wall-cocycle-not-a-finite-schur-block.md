# The subtracted outgoing trace is an unbounded wall cocycle, not a finite Schur block

> **Withdrawn for the completed centered constructor.** Its formal
> \(1/\log p\) column was inherited from the incomplete uncentered pairing
> corrected in
> `correction-the-centered-joint-cut-column-has-a-bounded-common-mode-not-an-unbounded-outgoing-wall-column.md`.
> It must not be identified with the primitive determinant anomaly. The actual
> centered common mode is bounded by \(\sum_p1/(p\log p)<\infty\).

## Trace subtraction revisited

The primitive mixed pairing with the raw twisted history has asymptotic

\[
\langle b_p,H_-\Phi\rangle
\longrightarrow c_-\ne0.
\]

After source-metric adjunction, the outgoing trace contribution is the formal
coefficient packet

\[
w_p=
\frac{c_-}{\log p}.
\]

The zero-trace relative representative removes exactly this packet from the
mixed return.

## Failure as a Hilbert source vector

Its arithmetic norm is

\[
\|w\|_U^2
=
|c_-|^2
\sum_p\frac1{\log p}
=
\infty.
\]

Thus the removed wall contribution is not a vector in \(U_{\rm ar}\). It
cannot be restored by adjoining one ordinary scalar wall coordinate and a
bounded rank-one map

\[
\mathbb C_{\rm wall}\to U_{\rm ar}.
\]

The corresponding column would be unbounded.

## Consequence for Schur equivalence

At finite cutoff \(X\), raw and relative mixed blocks differ by a rank-one
wall column \(w_X\). Its norm diverges as \(X\to\infty\). Therefore the finite
trace subtraction is not implemented in the completed Hilbert pencil by a
bounded triangular change of variables.

In particular, one may not conclude automatically that the raw and relative
Schur determinants differ by a nowhere-zero finite-dimensional determinant.
That conclusion would require a completed bounded equivalence which does not
exist on the current source metric.

## Correct determinant-line type

The outgoing trace contribution instead belongs to a boundary anomaly line or
descent cocycle. Its finite-cutoff transitions are exponentials of the removed
primitive cumulant. Completion must be performed as determinant-line descent,
not by treating the wall trace as another ordinary dynamic block.

The reciprocal channel supplies a second transition. Reciprocal symmetry can
relate the two transitions but does not prove their product is a coboundary or
a nowhere-zero global unit.

## No double counting

A valid compiler must choose one of two equivalent descriptions and prove the
transition between them:

1. raw finite-cutoff pencil plus its divergent outgoing wall columns;
2. zero-trace relative pencil plus a separately normalized primitive anomaly
   frame.

It may not retain the raw wall columns and multiply by the anomaly factor, nor
remove the columns and omit the anomaly. Either error changes the determinant
section.

## Required source calculation

Let \(a_X^\pm(s)\) be the two reciprocal outgoing-trace increments. The next
finite audit must compute them from the Wronskian moments and verify, on every
completion-chart cycle,

\[
a_{ij}^\pm+a_{jk}^\pm+a_{ki}^\pm=0.
\]

Only then do chart potentials exist. Their exponentials must also remain
holomorphic and nowhere zero on the comparison domain.

## Effect on the dressed scalar

The relative scalar

\[
F_\theta^{\rm rel}
\]

is a well-typed local section after trace subtraction. It is not yet a global
scalar function with the Xi divisor. The desired comparison is a
line-section identity

\[
F_\theta^{\rm rel}
=
E_\theta\tau
\]

only after both sides are placed in the same determinant-line frame.

## Disposition

Outgoing half-density subtraction repairs the mixed seam pairing but produces
an unbounded primitive wall cocycle. This cocycle cannot be reincorporated as
a bounded finite Schur port on the current arithmetic Hilbert space. G4 now
requires explicit primitive anomaly descent before any scalar divisor
comparison. No RH conclusion is authorized.
