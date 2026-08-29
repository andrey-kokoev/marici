# The Euler packet is a Hilbert--Schmidt Schur operator, not a scalar Schur sum

The scattering route becomes exact after choosing the seam coordinate with the opposite orientation:
\[
z=i\left(s-\frac12\right).
\]
Then
\[
\operatorname{Im}z=\operatorname{Re}s-\frac12,
\]
so the right off-seam sector maps to the upper half-plane, and
\[
p^{-s}
=
p^{-1/2}e^{iz\log p}.
\]

Define the prime-diagonal operator on \(\ell^2(\mathcal P)\):
\[
S(z)e_p
=
r_p(z)e_p,
\qquad
r_p(z)=p^{-1/2}e^{iz\log p}.
\]
For \(\operatorname{Im}z>0\),
\[
|r_p(z)|
=
p^{-1/2-\operatorname{Im}z}<1,
\]
and therefore
\[
\|S(z)\|
=
\sup_p |r_p(z)|
<1.
\]
This is a genuine operator-valued Schur function. Prime assembly is a direct sum of passive delay channels, not a scalar sum.

The ideal class is exactly informative. One has
\[
\|S(z)\|_{\mathfrak S_2}^{2}
=
\sum_p p^{-1-2\operatorname{Im}z},
\]
which converges for every \(\operatorname{Im}z>0\). Thus \(S(z)\) is Hilbert--Schmidt throughout the right half of the critical strip.

But
\[
\|S(z)\|_{\mathfrak S_1}
=
\sum_p p^{-1/2-\operatorname{Im}z}
\]
converges only when
\[
\operatorname{Im}z>\frac12,
\]
equivalently \(\operatorname{Re}s>1\). Therefore the ordinary Fredholm determinant
\[
\det(I-S(z))
=
\prod_p(1-p^{-s})
\]
is directly authorized only in the classical Euler half-plane.

Inside
\[
\frac12<\operatorname{Re}s\le1,
\]
the canonical operator determinant is instead the second regularized determinant
\[
\det_2(I-S)
=
\prod_p(1-r_p)e^{r_p}.
\]
Its logarithm retains the prime-power terms with \(k\ge2\):
\[
\log\det_2(I-S)
=
-\sum_p\sum_{k\ge2}\frac{r_p^k}{k}.
\]
The omitted term is precisely the primitive prime channel
\[
\sum_p r_p.
\]

This recovers the programme's primitive-versus-square typing from operator ideals:

- primitive \(k=1\) channel: not trace class in the critical strip and must remain distributional or wall-routed;
- square and higher \(k\ge2\) channels: Hilbert--Schmidt regularization makes them determinant-class;
- full Euler determinant: requires a separately authorized primitive boundary value.

The exact factorization at finite cutoff is
\[
\det(I-S_X)
=
\det_2(I-S_X)
\exp\bigl(-\operatorname{tr}S_X\bigr).
\]
At completion, the second factor cannot be interpreted as an ordinary convergent scalar in the strip. It is the missing primitive seam object, not a disposable renormalization.

This produces a sharper constructor architecture:
\[
\text{prime-diagonal Schur operator }S
\to
\det_2(I-S)\text{ for }k\ge2
\quad+\quad
\text{primitive trace distribution}
\to
\text{completed Euler boundary packet}.
\]

It also explains why the square channel was Hilbert-continuous at the seam while the primitive channel was not. The distinction is the threshold between \(\mathfrak S_2\) and \(\mathfrak S_1\).

The immediate theorem now has two parts:

1. prove that the source valuation/Fock carrier realizes the diagonal Schur operator \(S(z)\) and its cutoff-compatible passive dilation;
2. prove that the source wall/primitive history supplies the missing regularized trace term needed to pass from \(\det_2\) to the completed Euler determinant.

The minimal hostile simply drops \(\operatorname{tr}S_X\). It produces a perfectly analytic Hilbert--Schmidt determinant in the critical strip, but it encodes only prime powers \(k\ge2\) and therefore cannot be identified with \(\zeta(s)^{-1}\).

A second hostile assigns an arbitrary analytic continuation to the primitive trace. That restores the scalar Euler determinant but has no constructor authority and may import the desired zero set.

This is the first exact ideal-class explanation of the primitive/square split: RH lives precisely where the Euler scattering operator is Hilbert--Schmidt but not trace class.
