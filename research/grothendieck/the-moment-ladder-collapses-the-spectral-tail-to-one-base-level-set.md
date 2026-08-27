# The moment ladder collapses the spectral tail to one base level set

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact carrier-to-tail intertwiner

## Half-line transform recurrence

For the positive moments (M_k), define

\[
F_k(z)=\int_0^\infty e^{zu}M_k(u)\,du
\]

in its convergence chamber. The source law

\[
DM_k=\left(2k+\frac12\right)M_k-2M_{k+1}
\]

and integration by parts give

\[
2F_{k+1}(z)=\left(z+2k+\frac12\right)F_k(z)+M_k(0).
\]

This is the carrier-to-spectral-tail intertwiner. Its inhomogeneous term is
the seam evaluation, fixed before any zero is considered.

## Collapse of the physical readout

The half-transform of the completed source is

\[
F_\Phi=4F_2-6F_1.
\]

The first two recurrence steps are

\[
2F_1=(z+1/2)F_0+M_0(0),
\]

\[
2F_2=(z+5/2)F_1+M_1(0).
\]

Eliminating (F_1,F_2) gives the exact reduction

\[
F_\Phi(z)
=(z^2-1/4)F_0(z)+(z-1/2)M_0(0)+2M_1(0).
\]

Thus the infinite carrier ladder does not remain infinite after the physical
order-two compression and half-line transform. It becomes one base tail and
two seam coordinates.

## Reciprocal sewing

The bilateral completed transform is

\[
X_\Phi(z)=F_\Phi(z)+F_\Phi(-z).
\]

Writing (X_0(z)=F_0(z)+F_0(-z)), the terms odd in (z) cancel and

\[
X_\Phi(z)
=(z^2-1/4)X_0(z)-M_0(0)+4M_1(0).
\]

Therefore a zero obeys the affine level-set equation

\[
(z^2-1/4)X_0(z)=M_0(0)-4M_1(0).
\]

## The real obstacle

The carrier Gram form and reciprocal boundary cancellation are now fully
transported to the spectral side. They do not orient this final level set.
The remaining RH-bearing theorem must constrain the complex values of the
single base transform (X_0) strongly enough that the displayed equality can
hold only on the critical axis.

This is smaller than constructing an arbitrary infinite Green operator, but
it is not automatically easier. Positivity of (M_0) makes (X_0) a
bilateral Laplace transform of a positive source; the Gaussian-mixture hostile
already shows that such positivity alone does not orient complex level sets.
The missing datum must still use the exact Poisson lattice correspondence.

## Scope

The recurrence, elimination, bilateral sewing, and level-set reduction are
exact in the convergence chamber and continue with the completed transform.
No orientation theorem for (X_0), zero confinement, or RH is proved.
