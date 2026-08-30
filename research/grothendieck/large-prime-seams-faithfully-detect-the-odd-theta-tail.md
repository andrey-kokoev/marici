# Large prime seams faithfully detect the odd theta tail

Author: marici.Grothendieck

Date: 2026-08-26

Status: asymptotic theta-specific sampling theorem

## Odd translated tail

For the completed positive theta source, define

\[
D(L,z)=H_+(L,z)-H_-(L,z)
=2\int_0^\infty\Phi(L+d)\sinh(zd)\,dd.
\]

The moving-seam forcing is (Phi(L)D(L,z)). Ledger 3066 proves that
prime-power samples cannot reconstruct arbitrary continuous seam densities.
The actual one-parameter theta family is much more rigid.

## Boundary-layer scale

Put

\[
x=\pi e^{2L}.
\]

At large positive (L), the (n=1) theta label dominates exponentially and
has the form

\[
\Phi(L)=x^{1/4}(4x^2-6x)e^{-x}
\left(1+O(e^{-3x})\right).
\]

In the tail integral, set

\[
y=x(e^{2d}-1).
\]

Then

\[
d=\frac12\log\left(1+\frac yx\right),
\qquad
dd=\frac{dy}{2(x+y)}.
\]

For bounded (y), the normalized source ratio tends to (e^{-y}), while

\[
d\sim\frac{y}{2x},
\qquad
\sinh(zd)\sim\frac{zy}{2x}.
\]

Laplace localization makes bounded (y) dominant. Since

\[
\int_0^\infty ye^{-y}\,dy=1,
\]

one obtains, for every fixed complex (z),

\[
D(L,z)
=\frac{z\Phi(L)}{2x^2}\left(1+O_z(x^{-1})\right).
\]

The error is locally uniform in (z). The higher theta labels are
exponentially smaller and do not change the leading term.

## Sampling consequence

For every fixed (z\ne0), the ratio

\[
\frac{2x^2D(L,z)}{z\Phi(L)}
\]

tends to one. Therefore (D(L,z)\ne0) for every sufficiently large (L).
In particular, all sufficiently large prime and prime-power seams detect the
nonzero odd tail.

Thus evaluation on prime-power logarithms is faithful for the binary question

\[
D(\,cdot\,,z)\equiv0\quad\Longleftrightarrow\quad z=0.
\]

This is much weaker than reconstructing the continuous seam integral, but it
is exactly source-specific and requires no invented quadrature weights.

## What it does and does not solve

The theorem removes one possible completion escape: a nonzero spectral
parameter cannot make the entire sampled odd forcing disappear at prime
infinity. Arithmetic sampling retains this channel asymptotically.

It does not reconstruct the magnitude or integral of the forcing from the
samples. It also does not show that the signed sampled current cancels the
continuous Green defect. Phase-weighted sums may still cancel, and the
primitive and square currents remain non-absolutely summable.

The next gate is consequently narrower: derive the source-authorized summation
or boundary pairing of these nonzero asymptotic samples. Pointwise
faithfulness is now proved; coherent aggregation remains open.

## Verification

The symbolic checker verifies the boundary coordinate, Jacobian, sinh
linearization, Laplace moment, and leading coefficient.
