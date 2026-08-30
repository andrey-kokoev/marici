# The theta mass may close the half-line shifted-resolvent gate in one estimate

## Uniform Volterra norm

For the half-line history kernel \(\Phi\ge0\), define

\[
M_\Phi
=
\int_0^\infty\Phi(r)\,dr.
\]

Every finite anti-Volterra cutoff \(H_L\) is a compression of one-sided convolution. Young's inequality gives the cutoff-independent bound

\[
\|H_L\|
\le
M_\Phi.
\]

Therefore, if the source normalization satisfies

\[
M_\Phi<1,
\]

then both shifted histories are uniformly invertible by the Neumann series:

\[
(I\pm iH_L)^{-1}
=
\sum_{n\ge0}(\mp iH_L)^n,
\]

and

\[
\|(I\pm iH_L)^{-1}\|
\le
\frac1{1-M_\Phi}.
\]

Consequently,

\[
D_{L,\pm}
=
\frac12(I\pm iH_L)^*(I\pm iH_L)
\ge
\frac{(1-M_\Phi)^2}{2}I
\]

uniformly in cutoff.

This bypasses non-normal finite-section pseudospectra entirely.

## Theta identification

The completed theta source has the cosine representation

\[
\Xi(x)
=
\int_0^\infty\Phi(u)\cos(xu)\,du
\]

up to the frozen normalization convention. At \(x=0\),

\[
M_\Phi=\Xi(0).
\]

Under the conventional completed Riemann normalization, the candidate value is

\[
\Xi(0)=\xi(1/2)\approx0.497120778<1.
\]

If this is exactly the normalization used by the history operator and the coefficient-wall identity has coefficient one, then the auxiliary shifted-resolvent gate is already uniformly solved with explicit margin

\[
c_{\mathrm{hist}}
\ge
1-\Xi(0)
\approx0.502879222.
\]

## Why this is still conditional

Several equal-looking normalizations must not be conflated:

- the theta cosine-transform normalization;
- the history-kernel amplitude;
- the coefficient-wall representation of \(I\);
- prime and grade weights attached before history synthesis;
- any factor two from bilateral versus half-line conventions.

If the actual auxiliary block is

\[
\frac12(\lambda I+H^*H)\pm iT
\]

or the history kernel is scaled by \(\alpha_p\), the relevant criterion becomes

\[
|\alpha_p|M_\Phi<\sqrt{\lambda}
\]

after the corresponding graph-factor normalization, not simply \(M_\Phi<1\).

The numerical value of \(\xi(1/2)\) cannot authorize these identifications.

## Prime-scaled version

If

\[
H_{p,L}=\alpha_p H_L
\]

with source coefficient \(\alpha_p\), then

\[
\|H_{p,L}\|
\le
|\alpha_p|M_\Phi.
\]

A sufficient all-prime bound is

\[
\sup_p|\alpha_p|M_\Phi<1.
\]

For Euler half-density coefficients such as \(p^{-1/2}\), the worst prime is the smallest admitted prime, so the all-prime estimate reduces to a finite extremal check once the exact coefficient placement is frozen.

## Hostiles

1. A hidden bilateral factor two changes \(M_\Phi\) to \(2\Xi(0)\), which is approximately \(0.99424\): still below one but with a drastically smaller margin.
2. A further normalization factor pushes the mass above one; every previous scale-free argument remains valid, but the Neumann closure fails.
3. The scalar cosine transform uses \(\Phi\), while the history operator uses a differentiated or weighted kernel with larger \(L^1\) mass.
4. Prime pushforward applies its coefficient after, rather than before, the shifted-history inversion.

## Immediate executable theorem

Freeze the exact equality among:

\[
\text{wall coefficient},
\quad
\text{history kernel amplitude},
\quad
\Xi(0),
\quad
\text{prime weight}.
\]

Then compute the single dimensionless number

\[
M_{\mathrm{eff}}
=
\sup_p|\alpha_p|
\int_0^\infty\Phi(r)\,dr.
\]

If \(M_{\mathrm{eff}}<1\), the half-line auxiliary positivity and cutoff-uniform resolvent bounds follow immediately. The earliest missing work is now normalization typing, not operator theory.
