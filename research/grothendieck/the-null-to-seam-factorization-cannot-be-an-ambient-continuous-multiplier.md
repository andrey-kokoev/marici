# The null-to-seam factorization cannot be an ambient continuous multiplier

## Tempting strengthening

Let

\[
d(z)=(P-C)M_z\Omega
\]

be the reciprocal–real comparison effect. The desired implication is

\[
X(z)=0\Longrightarrow d(z)=0.
\]

A tempting construction would seek a continuous vector-valued multiplier
(K(z)) satisfying

\[
d(z)=K(z)X(z)
\]

on a neighborhood of the critical seam.

## Directional obstruction at a simple seam zero

Let (z_0=i\gamma) be a simple seam zero of (X). Write (z=x+i t).

Along the seam (x=0), the comparison effect vanishes identically:

\[
d(i t)=0.
\]

For nearby (t\ne\gamma), (X(it)\ne0), so any identity (d=KX) forces

\[
K(it)=0.
\]

Continuity would therefore give (K(z_0)=0).

Along the normal path (z=x+i\gamma), however,

\[
d(x+i\gamma)
=-2x,u e^{-i\gamma u}\Omega(u)+O(x^2),
\]

while simplicity gives

\[
X(x+i\gamma)=xX'(z_0)+O(x^2).
\]

Hence

\[
\lim_{x\to0}\frac{d(x+i\gamma)}{X(x+i\gamma)}
=
-\frac{2u e^{-i\gamma u}\Omega(u)}{X'(z_0)},
\]

which is a nonzero source vector. This contradicts the tangential limit.

## Consequence

At every simple seam zero, no continuous ambient multiplier can realize the
null-to-comparison factorization. In particular, the missing witness cannot
be:

- a bounded repair channel multiplying (X);
- a continuous vector quotient (d/X);
- a Schur complement whose only input is the scalar section;
- or a natural transformation defined on the whole parameter neighborhood
  by scalar divisibility.

## Correct categorical level

The factorization (Z_0\to S) is a morphism defined on the null pullback,
not an extension across the ambient parameter plane. A proof must use
additional structure available when the scalar boundary condition is imposed.
A Green identity, deficiency-state condition, or exact boundary complex has
the correct type: it can turn null incidence into path equality without
asserting (d=KX) away from the null locus.

## Scope

The obstruction is conditional at a simple seam zero. It is sufficient to
reject the proposed universal continuous-multiplier architecture. It does not
construct the required incidence-specific factorization and does not prove
RH.
