# Positive self-Fourier Poisson sewing still allows off-critical Mellin zeros

## Bounded question

Does positivity of the continuous carrier together with exact Fourier
self-duality and completed primal--dual Poisson sewing restrict the Mellin
orbit enough to confine its zeros?

## Starting Fourier-fixed direction

Let (t=\pi x^2). Nima's exact degree-twelve construction supplies a real
polynomial (P(t)) such that

\[
p(x)=e^{-\pi x^2}P(\pi x^2)
\]

is Fourier-fixed. Its normalized Mellin window is

\[
A(y)=r(2r-1)H(y),
\qquad
y=\left(r-\frac14\right)^2,
\]

where

\[
H(y)=\frac{256y^2+5920y+87325}{81920}.
\]

The discriminant of (H) is negative. This was the earlier signed
self-Fourier hostile carrier.

## Positive Fourier-fixed deformation

For (delta>0), put

\[
f_\delta(x)
=
e^{-\pi x^2}\left[1+\delta P(\pi x^2)\right].
\]

Both summands are Fourier-fixed, so (f_\delta) is Fourier-fixed. The
polynomial (P) has positive leading coefficient, hence it has a finite
minimum (m) on ([0,\infty)). Therefore (f_\delta) is strictly positive
whenever

\[
0<\delta<
\begin{cases}
-1/m,&m<0,\\
\infty,&m\ge0.
\end{cases}
\]

It is also even and Schwartz.

## Off-critical zeros persist for small positive deformation

After removing the common zero-free gamma factor, the Mellin window of
(f_\delta) is

\[
Q_\delta(y)=1+\delta A(y).
\]

Since

\[
r(2r-1)=2\left(y-\frac1{16}\right),
\]

(A(y)) is a real cubic with positive leading coefficient. Write

\[
A(y)=ay^3+by^2+cy+d,
\qquad a>0.
\]

The coefficients of (Q_\delta) are

\[
\delta a,
\quad
\delta b,
\quad
\delta c,
\quad
1+\delta d.
\]

Its cubic discriminant therefore has the small-(delta) expansion

\[
\operatorname{Disc}(Q_\delta)
=
-27a^2\delta^2+O(\delta^3).
\]

Consequently the discriminant is negative for every sufficiently small
positive (delta). The window then has one real (y)-root and a nonreal
conjugate pair. For either nonreal root,

\[
r=\frac14\pm\sqrt y
\]

has real part different from (1/4). Thus the Mellin transform of the
strictly positive Fourier-fixed carrier (f_\delta) has off-critical zeros.

The positivity and negative-discriminant conditions are both open at
(delta=0^+), so one (delta) satisfies them simultaneously.

## Exact Poisson sewing

Because (f_\delta) is Fourier-fixed, Poisson summation supplies the exact
primal--dual relation for its lattice orbit. This is not merely the scalar
reflection metadata of an arbitrary transform: the carrier itself belongs to
the fixed orbit of the Fourier operation and its comb evaluation is sewn by
the standard Poisson correspondence.

Therefore the following package is still insufficient for critical-line
Mellin orientation:

1. a strictly positive even Schwartz carrier;
2. Fourier self-duality at the source level;
3. exact primal--dual Poisson sewing;
4. positive lattice samples;
5. complete finite polarized label tomography;
6. the scalar functional equation induced by sewing.

## Meaning of the falsifier

Completed Poisson sewing does restrict the admitted orbit, but its fixed-point
space contains positive Hermite excitations as well as the Gaussian vacuum.
That orbit restriction is therefore too large. It transports primal and dual
descriptions coherently without selecting the Mellin divisor.

The next theta-specific discriminator must distinguish the Gaussian vacuum
from positive Fourier-fixed excitations before Mellin aggregation. Natural
candidates are the source heat-semigroup ground-state law, annihilation by the
oscillator lowering operator, or an arithmetic boundary current that couples
that vacuum law to the labelled comb. Merely adding more Poisson, moment, or
tomographic outputs cannot help.

## Next falsifier

Derive the proposed vacuum-selection operation without naming the Gaussian as
its desired solution. Then apply it to (f_\delta). A valid operation must
reject the hostile excitation at source level while remaining compatible with
the labelled comb, Mellin transport, and completion. If it accepts
(f_\delta), it has no zero-confinement force.
