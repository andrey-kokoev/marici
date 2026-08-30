# Tail-flow polarization constructs the two-height boundary pairing

Author: `marici.Nima`

Date: 2026-08-26

Status: exact source-forward Green identity and isolated forcing reservoir

## Source tail equation

For a spectral parameter (zeta), let the source tail satisfy

\[
(\partial_q+\zeta)G_\zeta(q)=-f_\zeta(q).
\]

This is the forward-derived tail equation obtained from the source integral,
not an equation manufactured from the completed scalar section.

For a second parameter (eta), differentiate the mixed product. Direct use
of the two tail equations gives

\[
\partial_q
\left(
G_\eta(q)^*G_\zeta(q)
\right)
=
-(\zeta+\bar\eta)
G_\eta(q)^*G_\zeta(q)
-f_\eta(q)^*G_\zeta(q)
-G_\eta(q)^*f_\zeta(q).
\]

Hence the polarized local conservation identity is

\[
(\zeta+\bar\eta)
G_\eta^*G_\zeta
=
-\partial_q(G_\eta^*G_\zeta)
-f_\eta^*G_\zeta
-G_\eta^*f_\zeta.
\]

## Integrated boundary pairing

Assume the tails vanish at infinity. Integration over the half-line yields

\[
(\zeta+\bar\eta)
K_H(\eta,\zeta)
=
G_\eta(0)^*G_\zeta(0)
-\mathcal F(\eta,\zeta),
\]

where

\[
K_H(\eta,\zeta)
=
\int_0^\infty
G_\eta(q)^*G_\zeta(q)\,dq
\]

is a positive kernel and

\[
\mathcal F(\eta,\zeta)
=
\int_0^\infty
\left(
f_\eta(q)^*G_\zeta(q)
+G_\eta(q)^*f_\zeta(q)
\right)dq
\]

is the exact mixed forcing reservoir.

Thus the half-plane boundary pairing is already constructed:

\[
\mathcal B(\eta,\zeta)
=
G_\eta(0)^*G_\zeta(0)
-\mathcal F(\eta,\zeta).
\]

The remaining problem is not to guess (mathcal B). It is to express the
forcing reservoir through the typed modular boundary currents and factor the
result as input Gram minus output Gram.

## Relation to the doubled system

For reciprocal sheets, apply the identity to each tail and sum after
transporting both into the common Clark frame. The established Clark
polarization supplies the positive bulk kernel. The difference between the
two forcing reservoirs is the mixed modular current isolated in the doubled
calculation.

Primitive, square, seam, and archimedean terms must therefore arise as a
source decomposition of (mathcal F), not as extra positive ports appended
afterward.

## Exact exponential model

Take a real source

\[
f(q)=e^{-\beta q}
\]

with (eta) larger than the real parts of both parameters. Then

\[
G_\zeta(q)=\frac{e^{-\beta q}}{\beta-\zeta}.
\]

The integrated identity becomes an exact rational equality. This model
verifies the signs, endpoint orientation, and both mixed forcing terms without
numerical quadrature.

## Conservative-factorization gate

To obtain a lurking isometry, the source must now prove

\[
G_\eta(0)^*G_\zeta(0)
-\mathcal F(\eta,\zeta)
=
I-\Theta(\eta)^*\Theta(\zeta).
\]

The right side cannot be fitted from the left. Input and output boundary ports
must be independently supplied by the theta/Tate construction.

The finite residual is

\[
\mathcal Q_X(\eta,\zeta)
=
\mathcal F_X(\eta,\zeta)
-\mathcal F_X^{(1)}(\eta,\zeta)
-\mathcal F_X^{(2)}(\eta,\zeta)
-\mathcal F_X^{(\mathrm{seam})}(\eta,\zeta)
-\mathcal F_X^{(\infty)}(\eta,\zeta).
\]

One nonzero typed residual disproves the proposed modular decomposition.

## Completion gate

Even exact finite decomposition must survive the source topology. The
primitive term may exist only on an exponential test space, the square term
on a tempered or Hilbert level, and the seam on its independent carrier. Their
sum must define the boundary pairing without pretending that the individual
scalar readouts share one ordinary domain.

This is precisely the singular boundary vessel identified earlier.

