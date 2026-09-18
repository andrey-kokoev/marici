# Ratio-profile Mellin transform collapses to a reflection-symmetric gamma factor

Set

$$
x=\frac{s+2}{2},
\qquad
y=\frac{3-s}{2},
\qquad x+y=\frac52.
$$

The three beta terms in `K(s)` share the factor

$$
\frac{\Gamma(x)\Gamma(y)}{\Gamma(9/2)}.
$$

Their polynomial coefficient is

$$
-6y(y+1)+23xy-6x(x+1)
=\frac{35}{4}s(1-s).
$$

Since

$$
\Gamma(9/2)=\frac{105}{16}\sqrt\pi,
$$

the complete Mellin transform simplifies to

$$
\boxed{
K(s)=
\frac{s(1-s)}{\sqrt\pi}
\Gamma\left(\frac{s+2}{2}\right)
\Gamma\left(\frac{3-s}{2}\right)
}.
$$

Consequences include

$$
K(1-s)=K(s),
$$

and the two exact zeros

$$
K(0)=K(1)=0.
$$

Also

$$
K(2)=-2.
$$

The reflection symmetry is precisely centered at the reciprocal seam `Re(s)=1/2`. In the Barnes representation

$$
K(s)\zeta(1+\varepsilon-s)\zeta(\varepsilon+s),
$$

the substitution `s -> 1-s` exchanges the two zeta factors while leaving `K` fixed. At `epsilon=0`, the complete integrand is reflection-invariant.

Thus reciprocal sewing is already visible analytically in the regulated forcing reservoir. Both zeta poles at `s=0,1` are cancelled by the source zeros of `K`; any remaining seam term must arise from contour orientation, gamma poles, or the finite-part regulator rather than an uncancelled zeta pole.

Status: Mellin kernel and reciprocal reflection simplified exactly; regulated contour evaluation remains open.
