# Endpoint-reduced Euler sections are the canonical Hardy carriers

## Why the completed section is the wrong carrier

The completed function

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

has the correct divisor and reciprocal symmetry, but its gamma factor gives
superlinear logarithmic growth along the positive real direction:

\[
\log|\xi(\sigma)|
=
\frac{\sigma}{2}\log\sigma+O(\sigma).
\]

Consequently the usual full-half-plane Nevanlinna characteristic is not
uniformly bounded for the raw completed section. The Hardy factorization used
by the phase observer must not be applied to `xi` without normalization.

## Source-derived endpoint reduction

The endpoint pole and zeta pole already form the canonical acyclic pair
encoded by `(s-1)zeta(s)`. Remove also the harmless rational growth at
infinity. Define

\[
E_+(s)=\frac{s-1}{s}\zeta(s),
\qquad \Re s>\frac12,
\]

and its reciprocal mate

\[
E_-(s)=E_+(1-s)
=
-\frac{s}{1-s}\zeta(1-s),
\qquad \Re s<\frac12.
\]

The apparent singularities at `s=1` and `s=0` are removable. The rational
denominators have no zeros or poles in their respective open sectors.
Therefore

\[
\operatorname{div}_{\Re s>1/2}E_+
=
\operatorname{div}_{\Re s>1/2}\xi,
\]

and analogously for `E_-` in the left sector.

The normalization is source-derived: `(s-1)` is the endpoint--zeta pole
cancellation, `1/s` removes only a nonvanishing rational carrier in the right
sector, and the gamma factor is retained as reciprocal sewing data rather
than as Hardy bulk growth.

## Bounded-type gate

The functions `E_+` and `E_-` are of bounded type in their respective open
half-planes. A direct estimate suffices.

For `1/2 < sigma <= 2`, standard vertical-strip bounds for zeta give

\[
\log^+|E_+(\sigma+it)|
\le C+C'\log(2+|t|),
\]

uniformly after using the removable value at `s=1`. For `sigma >= 2`, the
absolutely convergent Dirichlet series and `(s-1)/s -> 1` give a uniform
bound. Hence

\[
\sup_{\sigma>1/2}
\int_{\mathbb R}
\frac{\log^+|E_+(\sigma+it)|}{1+t^2}\,dt
<\infty.
\]

Reflection gives the same result for `E_-`.

Thus the sectorwise canonical factorization required by the anti-diagonal
Hardy residual is available on a zero-preserving source normalization.

## Singular-inner audit

Each Euler section extends holomorphically through every finite point of the
critical seam. Boundary zeros do not create a singular-inner measure; they
are ordinary boundary zeros in the continued analytic function. The
normalization also has zero half-plane mean type because it approaches `1`
along the interior real ray after the endpoint reduction.

Therefore no independent singular-inner factor is supported on the finite
seam or at half-plane infinity. The remaining sectorwise inner factor is the
Blaschke product of open-sector zeros.

## Exact RH phase gate

For these normalized Euler sections, the anti-diagonal Hardy residual is now
well typed without an unproved analytic proviso. Its residue class vanishes
if and only if both open sectors have empty Blaschke divisors. Since the
completed and Euler-normalized sections have the same open-sector zeros, this
is equivalent to RH.

This is still an equivalence, not a proof. The live explanatory theorem is to
derive vanishing of the relative phase current from labelled theta--Poisson
transport rather than from prior knowledge of the divisor.

## Scope

This packet constructs the zero-preserving bounded-type carriers and removes
the singular-inner ambiguity. It does not derive vanishing of their Blaschke
current from the theta source and does not prove RH.
