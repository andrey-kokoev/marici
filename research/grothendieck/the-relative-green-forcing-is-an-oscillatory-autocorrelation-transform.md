# The Relative Green Forcing Is an Oscillatory Autocorrelation Transform

## One-sided forcing

Let \(f\) be a real nonnegative source on the positive chart and define

\[
G_z(q)
=
e^{-(z-1/2)q}
\int_q^\infty f(v)e^{(z-1/2)v}\,dv.
\]

The source-derived Green identity contains the forcing scalar

\[
\Psi_z
=
2\operatorname{Re}
\int_0^\infty e^{-q}f(q)\overline{G_z(q)}\,dq.
\]

Write \(z=x+iy\).

## Exact two-copy reduction

Define the one-sided weighted autocorrelation

\[
A_f(d)
=
\int_0^\infty e^{-q}f(q)f(q+d)\,dq,
\qquad d\geq0.
\]

It is nonnegative. Expanding the tail integral and setting \(v=q+d\) gives

\[
\Psi_z
=
2\int_0^\infty
A_f(d)e^{-d/2}e^{xd}\cos(yd)\,dd.
\]

The reciprocal spectral point is

\[
z^\vee=-\overline z=-x+iy.
\]

Therefore

\[
\Psi_{z^\vee}
=
2\int_0^\infty
A_f(d)e^{-d/2}e^{-xd}\cos(yd)\,dd,
\]

and the relative forcing residual is

\[
\mathcal R_f(x,y)
=
\Psi_z-\Psi_{z^\vee}
=
4\int_0^\infty
A_f(d)e^{-d/2}\sinh(xd)\cos(yd)\,dd.
\]

This is the independently computed dynamic top cell. It is a bulk
autocorrelation transform, not the degree-zero corona boundary.

## Coupled zero-state identity

Let

\[
E_z=\int_0^\infty e^{-q}|G_z(q)|^2\,dq.
\]

Assume reciprocal completion makes both scalar endpoints vanish at a paired
zero:

\[
G_z(0)=G_{z^\vee}(0)=0.
\]

The two one-sided Green identities then give

\[
2x(E_z+E_{z^\vee})
=
-\mathcal R_f(x,y).
\]

For \(x\neq0\), division by \(2x\) yields

\[
E_z+E_{z^\vee}
=
-2\int_0^\infty
A_f(d)e^{-d/2}
\frac{\sinh(xd)}{x}
\cos(yd)\,dd.
\]

The left side is strictly positive for a nonzero zero-state, while

\[
\frac{\sinh(xd)}{x}>0
\]

for \(d>0\). Hence a sufficient zero-confinement theorem is the
theta-specific orientation

\[
\int_0^\infty
A_f(d)e^{-d/2}
\frac{\sinh(xd)}{x}
\cos(yd)\,dd
\geq0
\]

throughout the required open domain.

## Meaning

The preceding categorical construction performs two real tasks:

- it preserves the full residue-tree state through completion;
- it supplies the legitimate alternating boundary sign.

It does not make the forcing states a relative cycle. Their mismatch is the
explicit oscillatory transform above. Positivity of \(A_f\) alone is
insufficient because the cosine changes sign.

Thus the programme has not reduced RH to a formal boundary cancellation. It
has isolated the exact remaining source law:

> modular and arithmetic completion must orient the cosine transform of the
> source-derived weighted autocorrelation.

This is narrower than the original scalar problem because the measure
\(A_f(d)e^{-d/2}dd\) is fixed before spectral evaluation and comes directly
from the Green forcing.

## Falsifier

A generic positive source can have a negative cosine transform. Such a source
passes positivity of \(A_f\), the local Fourier square, the split relative
corona complex, and additive bulk-energy positivity while failing the required
orientation.

The next source-specific attack is to insert the labelled theta decomposition
into \(A_f\), retain its reciprocal residue-tree labels, and determine whether
Poisson sewing pairs the negative cosine lobes with positive labelled
contributions. Any residual label packet with negative oriented transform
closes the route.
