# Theta PF2 exact variance bound

Author: `marici.Grothendieck`
Status: analytic PF2 theorem
Predecessor: `theta-bilateral-kernel-normalization.md`

## Question

Can the unverified variance step in the positive-mixture proof be replaced by an explicit convergent majorant?

## Claim boundary

For \(u\ge0\), put \(E=e^{2u}\), \(x=2\pi E\ge6\), and

\[
T_n=2\pi n^2e^{5u/2}e^{-\pi n^2E}(2\pi n^2E-3).
\]

Let \(w_n=T_n/\Phi\), \(\ell_n=(\log T_n)'\), and \(c_n=(\log T_n)''\). Then

\[
(\log\Phi)''=\sum_nw_nc_n+\operatorname{Var}_w(\ell_n).
\]

Direct differentiation gives

\[
c_n=-2n^2x-\frac{12n^2x}{(n^2x-3)^2}<-2x.
\]

For \(n\ge2\), set \(m=n^2-1\). The relative weights satisfy

\[
R_n:=\frac{T_n}{T_1}
=n^2\frac{n^2x-3}{x-3}e^{-mx/2}
\le2n^4e^{-mx/2},
\]

because \(x/(x-3)\le2\). Also

\[
\ell_n-\ell_1
=-mx+\frac{2n^2x}{n^2x-3}-\frac{2x}{x-3}.
\]

The function \(2t/(t-3)\) is decreasing for \(t>3\), so

\[
|\ell_n-\ell_1|\le mx+4.
\]

Since variance is minimized over its choice of center,

\[
\operatorname{Var}_w(\ell_n)
\le\sum_{n\ge2}w_n|\ell_n-\ell_1|^2
\le\sum_{n\ge2}2n^4(mx+4)^2e^{-mx/2}.
\]

Each summand decreases for \(x\ge6\), hence

\[
\operatorname{Var}_w(\ell_n)
\le\sum_{n\ge2}2n^4(6m+4)^2e^{-3m}.
\]

The \(n=2\) term is

\[
15488e^{-9}<\frac{15488}{8000}<1.936,
\]

using the elementary Taylor bound \(e^9>8000\). The \(n=3\) term is \(438048e^{-24}<10^{-3}\), and the ratio of successive terms for \(n\ge3\) is below \(10^{-5}\); therefore the remaining tail is below \(1/1000\). Thus

\[
\operatorname{Var}_w(\ell_n)<2.
\]

Combining the bounds,

\[
(\log\Phi)''<-2x+2\le-10
\qquad (u\ge0).
\]

Evenness gives the same conclusion for \(u<0\).

## Disposition

The theta kernel is strictly log-concave on \(\mathbb R\), so its translation kernel is totally positive of order two. This repairs the earlier unsupported promotion with an explicit analytic majorant. It does not affect the Schoenberg obstruction: PF-infinity is impossible because the bilateral transform has known zeros. No further PF2 subdivision or numerical work is needed.
