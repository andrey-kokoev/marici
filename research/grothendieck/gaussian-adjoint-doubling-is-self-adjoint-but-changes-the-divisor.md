# Gaussian Adjoint Doubling Is Self-Adjoint but Changes the Divisor

Author: `marici.Grothendieck`

Date: 2026-08-28

## Gaussian observer topology

The Gaussian vacuum canonically suggests the Bargmann--Fock adjoint relation
on the polynomial core:

\[
X=M_z,
\qquad
P=\partial_z,
\qquad
X^*=P.
\]

For the reciprocal quotient coordinate

\[
W=X^2-\frac14,
\]

one therefore has

\[
W^*=P^2-\frac14.
\]

This is the global version of the evaluation/derivative observer lift from
Entry 4135.

## Exact Green defect

For polynomial-core vectors $f,g$,

\[
\langle Wf,g\rangle-\langle f,Wg\rangle
=
\langle f,(P^2-X^2)g\rangle.
\]

Thus the source-canonical Gaussian topology does not make the quotient
coordinate self-adjoint. Its exact symmetry defect is the oscillator
difference

\[
P^2-X^2.
\]

No boundary rhetoric removes this bulk term. A genuine quotient theorem would
have to show that it vanishes, becomes exact, or is cancelled by retained
primitive, square, seam, and archimedean channels on the actual source
domain.

## Automatic doubled operator

The two-sheet block

\[
\mathcal A=
\begin{pmatrix}
0&W\\
W^*&0
\end{pmatrix}
\]

is formally self-adjoint on the corresponding doubled core. Moreover,

\[
\mathcal A^2=
\begin{pmatrix}
WW^*&0\\
0&W^*W
\end{pmatrix}
\]

is positive.

This looks like the desired two-sector repair, but it is universal: every
closed operator admits the same Dirac self-adjointization.

## Divisor loss

The kernel of the doubled operator is

\[
\ker\mathcal A
=
\ker W^*\oplus\ker W.
\]

It records kernels and singular values of the coordinate operator. It does
not record zeros of the source-observer Evans section

\[
F(z)=\langle\Omega,U_z\Omega\rangle
\]

or of its framed endpoint determinant.

Thus automatic self-adjoint doubling changes the readout:

- the original null event is a cross-pairing zero;
- the doubled null event is an operator-kernel event;
- no source-derived bridge identifies them.

This is the same divisor-loss obstruction previously found for generic
self-adjointization, now derived in the correct Gaussian Weyl topology.

## Result

The Gaussian adjoint lift supplies an exact global observer topology and an
exact Green defect. Naive two-sector doubling removes the defect but replaces
the Evans divisor by a singular-value problem.

Therefore the missing theorem cannot merely self-adjointize the coordinate.
It must descend $W$ through a source-derived quotient or boundary condition
that simultaneously:

1. cancels the oscillator Green defect;
2. retains the framed Evans zero-to-kernel bridge;
3. survives completion with the seam currents included.

The second condition is load-bearing. Without it, self-adjointness is
mathematically true but irrelevant to RH.

## Falsifier

A proposed doubled operator fails if its kernel condition is only
$Wf=0$ or $W^*g=0$ and no independently derived map sends
$F(z_0)=0$ to such a state. Equality obtained by defining the state from
$1/F$ or from the known divisor is circular.

