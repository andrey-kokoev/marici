# Todd and Euler are two boundary localizations of one global scale current

## The exact distributive law

Let

\[
E(r)=-\log(1-r)
\]

be the Euler occupation potential, and let

\[
\tau(t)=\frac{t}{e^t-1}
\]

be the Todd normalization germ. Relate the scale coordinates by

\[
r=e^{-t}.
\]

Then

\[
r\frac{d}{dr}E(r)=\frac{r}{1-r}=\frac1{e^t-1},
\]

and therefore

\[
\tau(-\log r)
=
(-\log r),r\frac{d}{dr}E(r).
\]

Todd normalization is the logarithmic-scale derivative of the Euler
occupation potential, multiplied by the scale distance \(-\log r\).

## Why the coefficient supports looked incompatible

Near \(r=0\), the Euler chart is

\[
E(r)=\sum_{k\geq1}\frac{r^k}{k}.
\]

Every positive occupation grade is visible. The logarithmic derivative acts
diagonally:

\[
r\frac{d}{dr}E(r)=\sum_{k\geq1}r^k.
\]

Near \(t=0\), equivalently \(r=1\), the same derived current is singular.
Multiplication by \(t=-\log r\) removes that singularity and produces the
regular Todd/Bernoulli germ.

Thus the two coefficient systems belong to different formal
neighbourhoods:

- Euler prime-power grades are the expansion at \(r=0\);
- Todd boundary jets are the regularized expansion at \(r=1\).

Their different coefficient supports are not a contradiction. They are
shadows of one global scale current viewed from opposite boundary charts.

## The missing categorical level

The correct carrier is the compactified scale interval with both ends
retained. It contains:

- the dilute occupation boundary \(r=0\);
- the continuum/lattice collision boundary \(r=1\);
- the open transition \(r=e^{-t}\);
- the Euler potential \(E\);
- its logarithmic current \(rD_rE\);
- the Todd-regularized boundary value \((-\log r)rD_rE\).

Neither local formal germ can reconstruct this whole object by itself. Their
agreement is a descent statement on the overlap, not equality of Taylor
coefficients.

## Connection to the two-sector intuition

This is a literal instance of two sectors pretending to be one scalar
formula. The Euler and Todd presentations are not alternative expressions in
one local ring. They are complementary localizations of a global scale
object.

That distinction explains several earlier surprises:

- finite part is necessary at the \(r=1\) boundary;
- every prime-power grade remains visible at \(r=0\);
- centering removes the local singular term without deleting the remote
  Euler grades;
- scalar analytic continuation hides which boundary chart supplied which
  datum.

## Reciprocal sewing target

Reciprocal Fourier–Tate sewing should now be formulated on this two-boundary
scale object. A valid sewing morphism must preserve the Euler occupation
expansion at one end, the Todd finite-part germ at the other, and the
logarithmic derivative relation on their overlap.

The finite falsifier is a failure of the overlap identity after inserting
the source-labelled prime, square, and archimedean channels. Agreement only
after scalar summation is insufficient because it forgets which boundary
localization carried each term.

## Scope

The identity is exact and repairs the earlier coefficient-support puzzle. It
does not yet provide the Fourier–Tate sewing morphism, a completed Green
current, or zero confinement.

## Result

Todd normalization and Euler occupation are two boundary localizations of
one global scale current. The Euler chart at \(r=0\) exposes all
prime-power grades; the Todd chart at \(r=1\) regularizes the collision with
the continuum. Their exact transition is logarithmic differentiation under
\(r=e^{-t}\). The next pullback is the global two-boundary scale object on
which both charts descend.
