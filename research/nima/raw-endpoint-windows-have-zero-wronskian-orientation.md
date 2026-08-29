# Raw endpoint windows have zero Wronskian orientation

## Polarized Wronskian form

Let

\[
J(h)
=
-2\pi\operatorname{pv}
\int_{\mathbb R}\xi|\widehat h(\xi)|^2\,d\xi.
\]

Its Hermitian polarization is represented in Fourier space by the real
multiplier \(-2\pi\xi\):

\[
\mathcal W(h_1,h_2)
=
-2\pi\operatorname{pv}
\int_{\mathbb R}
\xi\,
\overline{\widehat h_1(\xi)}
\widehat h_2(\xi)\,d\xi,
\]

up to the frozen convention for the linear argument. Then
\(\mathcal W(h,h)=J(h)\).

## Parity of the endpoint windows

The Gaussian tail satisfies

\[
H(-q)=1-H(q).
\]

Hence

\[
W_t(-q)
=
H(-q+t)-H(-q-t)
=
H(q+t)-H(q-t)
=
W_t(q).
\]

Every raw endpoint window \(W_t\) is real and even. Its Fourier transform is
therefore real and even.

For any \(s,t>0\),

\[
\mathcal W(W_s,W_t)
=
-2\pi\operatorname{pv}
\int_{\mathbb R}
\xi\,
\widehat W_s(\xi)
\widehat W_t(\xi)\,d\xi
=
0,
\]

because the integrand is odd.

In particular,

\[
\mathcal W(W_L,W_{2L})=0.
\]

## No-go theorem

The two-dimensional feature plane

\[
\operatorname{span}\{[W_L],[W_{2L}]\}
\]

cannot produce a nonzero reciprocal imaginary Gram coordinate through the
source Wronskian current. Its Wronskian polarization vanishes identically.

Therefore the candidate map

\[
e_{p,k}\mapsto[W_{k\log p}]
\]

constructs only the even endpoint Gram plane. The odd coordinate cannot be
recovered by polarizing those two vectors more carefully.

## Required enlargement

The source odd port lives in the tail--principal-value Fourier plane
\((K,V)\), with

\[
\mathcal FK=V,
\qquad
\mathcal FV=-K.
\]

At least one odd feature must be retained alongside the endpoint windows.
Schematically the local cell must enlarge to

\[
\mathcal F_p^{\mathrm{cell}}
=
\operatorname{span}\{[W_L],[W_{2L}]\}
\oplus
\mathcal F_p^{\mathrm{odd}}
\oplus
\mathcal F_p^{\mathrm{wall/tail}}.
\]

A source incidence map must specify how the primitive--square oriented boundary
couples into \(\mathcal F_p^{\mathrm{odd}}\).

## Correct linking target

The remaining analytic theorem is not

\[
\mathcal W(W_L,W_{2L})
=
J_p^{\mathrm{zero}},
\]

because the left side is zero while the right side is nonzero.

It must instead have the form

\[
\mathcal W
\left(
J_p^{\mathrm{even}}d,
J_p^{\mathrm{odd}}d
\right)
=
J_p^{\mathrm{zero}}
=
\left.\partial_z\log\gamma_p(z)\right|_{z=0},
\]

or an equivalent polarized pairing between the even boundary feature and an
independently source-derived odd seam feature.

## Consequence for the Gram

Writing a nonzero

\[
ih_p
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
\]

directly on the bare endpoint-window plane is an effective compression. It is
source-authorized only after constructing the enlarged odd cell and proving
that its Schur or pushforward compression induces that block.

The full Euler value additionally carries the connected \(k\ge3\) tail, so the
enlarged cell must keep both:

- reciprocal odd orientation;
- higher-grade connected incidence.

## Minimal hostile

Assign the correct nonzero arithmetic \(h_p\) to the bare window Gram while
using the genuine Wronskian representation. Every arithmetic sign test passes,
but the analytic Wronskian of the endpoint vectors is zero. The claimed
quadratic representation theorem fails.

## Refined frontier

The even comparison map is constructed. The arithmetic odd current is
identified exactly. The missing constructor is now one explicit incidence leg:

\[
\text{oriented primitive--square boundary}
\longrightarrow
\text{tail--principal-value odd feature}.
\]

Only after that leg exists can the polarized Wronskian close the
zero-section/Euler/analytic triangle.
