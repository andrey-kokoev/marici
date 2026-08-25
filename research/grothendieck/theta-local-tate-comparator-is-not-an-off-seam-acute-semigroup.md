# The local Tate comparator is not an off-seam acute semigroup

## Bounded hostile test

Nima sharpened the geometric-algebra proposal: orientation is insufficient;
an off-seam comparison would need to lie in a distinguished acute or positive
Clifford semigroup whose scalar projection cannot vanish. Test that claim
against the already source-derived local transition

\[
 \gamma_p(s)=\frac{1-p^{-s}}{1-p^{s-1}}.
\]

## Exact scalar geometry

Write

\[
 s=\frac12+\sigma+it,
 \qquad
 r_+=p^{-1/2-\sigma},
 \qquad
 r_-=p^{-1/2+\sigma},
 \qquad
 \theta=t\log p.
\]

Inside the critical strip, `0<r_+,r_-<1` and

\[
 r_+r_-=p^{-1}.
\]

The transition is

\[
 \gamma_p
 =\frac{1-r_+e^{-i\theta}}{1-r_-e^{i\theta}}.
\]

Multiply by the conjugate denominator. Since its squared modulus is positive,
the sign of the scalar projection is the sign of

\[
 F_p(c)
 =1-(r_++r_-)c+p^{-1}(2c^2-1),
 \qquad c=\cos\theta.
\]

Thus the acute-cone question is an exact quadratic minimization on
`-1<=c<=1`; no separate phase bounds need be combined.

## Prime two is the sharp immediate falsifier

Put `S=r_++r_-`. For `p=2`,

\[
 F_2(c)=\frac12-Sc+c^2.
\]

Its critical point is `c=S/2`. Throughout the open critical strip,
`sqrt(2)<=S<3/2`, so this critical point lies in `[-1,1]` and

\[
 \min_{-1\le c\le1}F_2(c)=\frac12-\frac{S^2}{4}.
\]

On the seam `sigma=0`,

\[
 r_+=r_-=2^{-1/2},
 \qquad
 r_+^2+r_-^2=1,
\]

and the minimum is zero. For every nonzero `sigma` still inside the critical
strip,

\[
 r_+^2+r_-^2
 =2^{-1-2\sigma}+2^{-1+2\sigma}>1
\]

by strict arithmetic--geometric mean, so `S^2>2`. Hence

\[
 \boxed{
 \min_{\theta}\operatorname{Re}\gamma_2(1/2+\sigma+it)<0
 \qquad(0<|\sigma|<1/2).}
\]

There are therefore spectral phases for which the source-derived local
prime-two transition has negative scalar projection off the critical seam.

## Disposition

The conjecture

\[
 \text{each local off-seam Tate comparator lies in an acute Clifford cone}
\]

is false. Nonunitarity is not the same as a hyperbolic boost with positive
scalar part. The local comparator generally contains both dilation and
elliptic phase.

This does not falsify a **completed** acute-semigroup theorem. It proves that
any such cone can arise only after retaining and sewing:

\[
 \text{all prime labels}
 +\text{primitive and square boundary currents}
 +\text{archimedean completion}
 +\text{reciprocal dual sector}.
\]

A global theorem may not be established by multiplying primewise positive
scalar parts, because those parts are not primewise positive.

## New target

Construct the full completed two-sector Clifford comparison before projecting
to local factors. Then ask whether modular/archimedean sewing maps its total
geometric product into an acute semigroup on each open half-plane.

The smallest falsifier remains prime two: any proposed global cone proof must
show explicitly how the negative local scalar phases are paired or transported
without deleting their bivector and boundary data.
