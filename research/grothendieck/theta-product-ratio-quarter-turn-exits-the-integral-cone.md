# The product--ratio quarter-turn exits the integral cone

## Bounded question

Does reciprocal sewing define an internal unitary intertwiner exchanging the
product and ratio characters on the faithful integral pair-label space?

## Logarithmic coordinates

Put

\[
 a=\log n,
 \qquad b=\log m,
\]

and define signed product--ratio coordinates

\[
 P=a+b=\log(nm),
 \qquad
 R=b-a=\log(m/n).
\]

The character variance distinction of packet 131 is

\[
 e^{-ixP}=(nm)^{-ix},
 \qquad
 e^{-ixR}=(m/n)^{-ix}.
\]

Exchanging product and ratio means

\[
 (P,R)\longmapsto(R,P).
\]

Returning to the original coordinates gives

\[
 a'=\frac{R-P}{2}=-a,
 \qquad
 b'=\frac{R+P}{2}=b.
\]

Therefore

\[
 \boxed{(n,m)\longmapsto(n^{-1},m).}
\]

## Integral-cone obstruction

The map is not an endomorphism of `N x N` unless `n=1`.  At the first hostile
product fiber,

\[
\begin{array}{c|c}
(1,6)&(1,6)\\
(2,3)&(1/2,3)\\
(3,2)&(1/3,2)\\
(6,1)&(1/6,1)
\end{array}
\]

so three of the four branches exit the integral label space.  In particular,
there is no internal `2x2` operator on the two even product-six ports that can
implement the required product--ratio quarter-turn.

The proposed finite Gram test is therefore ill-typed before its determinant
is formed.

## Valuation-cone form

For every prime `p`, write

\[
 \alpha_p=v_p(n)\ge0,
 \qquad
 \beta_p=v_p(m)\ge0.
\]

The product and ratio valuations are

\[
 c_p=\alpha_p+\beta_p,
 \qquad
 d_p=\beta_p-\alpha_p.
\]

Their exchange sends

\[
 (\alpha_p,\beta_p)\longmapsto(-\alpha_p,\beta_p).
\]

Thus the integral valuation cone `N_0^2` is mapped to an oppositely polarized
rational cone.  Their common face is `alpha_p=0`.

This supplies an exact two-sector geometry:

\[
 \boxed{
 \text{integral cone}
 \xleftrightarrow{\text{quarter-turn}}
 \text{inverse-integral cone}.}
\]

The two analytic half-planes can now be understood as Mellin shadows of these
oppositely polarized valuation sectors rather than two regions of one
pre-existing scalar label space.

## Required enlargement

The quarter-turn is a bijection on

\[
 \mathbb Q_{>0}\times\mathbb Q_{>0},
\]

where inversion is allowed.  Therefore the correct operator is not internal
to the theta integer labels.  It must be a correspondence between an integral
sector and a rational/dual sector inside the adelic completion.

This is a candidate primal--dual doubling of the kind anticipated by Poisson
sewing. A source-authority caution is essential: additive Fourier duality fixes
the compact-open vacuum `1_Zp`; it does not by itself implement multiplicative
inversion of valuation labels. The full Tate functional equation or another
explicit source correspondence must be shown to supply the opposite cone.
That source lift is not proved here.

## Disposition and next gate

The internal product--ratio Gram-intertwiner conjecture is falsified.  Its
correct successor is a two-space correspondence

\[
 \ell^2(\mathbb N^2)
 \longleftrightarrow
 \ell^2(\mathbb N^{-1}\times\mathbb N)
\]

embedded in the rational adelic label space, with a relative pairing on their
overlap and seam.

The next test is the one-prime valuation model: construct the two cones
`alpha>=0` and `alpha<=0`, their common face `alpha=0`, and the reflection
`alpha->-alpha`. Determine whether the compact-open local vacuum supplies a
positive relative Green form after the two cones are sewn.

The smallest falsifier is an entering arrow across the common face that is not
paired by reflection or whose pull--push norm disagrees with the local
stabilizer.
