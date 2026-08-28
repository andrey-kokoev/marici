# An off-sector zero is a quantized Poisson phase delay

## Boundary signature of one interior zero

Let `w=a+ib` with `a>0` and use the right-half-plane Blaschke factor

\[
b_w(z)=\frac{z-w}{z+\overline w}.
\]

On the seam `z=it`, set `x=t-b`. Direct logarithmic differentiation gives

\[
\frac{d}{dt}\arg b_w(it)
=-\frac{2a}{a^2+(t-b)^2}.
\]

The sign reflects the chosen boundary orientation. Its absolute density is a
Poisson kernel, and its total phase change is

\[
\int_{-\infty}^{\infty}
\frac{d}{dt}\arg b_w(it)\,dt=-2\pi.
\]

Thus one interior zero contributes one quantized unit of smooth boundary
phase delay while changing no boundary magnitude.

## The inner residual

Under the standard Hardy or bounded-type hypotheses, the outer factor's phase
is determined by its boundary log-magnitude through harmonic conjugation,
up to the usual normalization constants. Define the residual schematically
as

\[
\kappa_F(t)
=\partial_t\arg F(it)
-\mathcal H\bigl(\partial_t\log|F(it)|\bigr),
\]

with the sign of the Hilbert transform fixed by the half-plane convention.
For a finite Blaschke product, `kappa_F` is exactly the sum of the oriented
Poisson kernels of its interior zeros. Singular-inner contributions require
an additional boundary measure and must be audited separately.

This is the explicit inner-factor record missing from the adjoint Gramian.
It is phase/path data, not another positivity statistic.

## Source interpretation

The theta/Tate source already constructs two real quadratures of its boundary
value before modulus compression. The missing theorem is not their existence.
It is that their transported phase has no residual beyond the outer phase
forced by the source magnitude and declared seam normalization.

Equivalently, after removing known factors and fixing the correct function
class, one seeks

\[
\kappa_X=0
\]

as a source identity in each open sector. This would exclude every interior
Blaschke factor at once.

## Stable inverse formulation

The same condition can be expressed operationally. A normalized causal
source filter whose transfer function and inverse both admit stable
source-authorized realizations has no interior zero. A Blaschke factor is
stable in the forward direction but its inverse has a pole at `w` and cannot
be a stable inverse in the same sector.

Reciprocal Fourier--Tate reflection does not automatically supply this
inverse: it gives the reflected transform, not `1/F`. Treating reflection as
inversion would be another authority error. The next constructor question is
therefore whether theta/Tate operations build a genuine sectorwise inverse or
an equivalent zero-inner-phase transport law.

## Hostile test

Given a proposed phase law, multiply the normalized transform by `b_w` or by
a reciprocal/conjugate packet of Blaschke factors preserving the scalar
functional equation. The boundary magnitude remains unchanged, while
`kappa_F` gains the corresponding Poisson packet. A source law that cannot
detect this modification contains no RH force.

## Scope

This makes the missing winding information explicit and finitely falsifiable.
It does not establish the Hardy normalization for the completed theta
transform, construct a stable inverse, prove that `kappa_X` vanishes, or prove
RH.
