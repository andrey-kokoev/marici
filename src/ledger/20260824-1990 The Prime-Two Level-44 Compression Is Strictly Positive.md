# The Prime-Two Level-44 Compression Is Strictly Positive

Sequence claim: `seqclaim-c921b83ae4d9583c688e3daa`

The finite gamma truncation at the Burnol support boundary has kernel

\[
T_{44}
=d_{44}I+e^{|x-y|/2}
-\sum_{n=1}^{43}e^{-(2n+1/2)|x-y|}
\]

on an interval of length \(L=\log2\), with

\[
d_{44}
=-\log\pi-\gamma-\frac\pi2-3\log2
+4\sum_{n=0}^{43}\frac1{4n+1}.
\]

It is strictly positive. Level 43 is not: directed ball propagation places an
even eigenvalue in \((-10^{-4},0)\). Since every added gamma channel is
positive semidefinite, level 44 is the first positive truncation.

## Odd sector

Put

\[
B(t)=K_{44}(L)-K_{44}(t),
\qquad
\phi(x)=xe^{-7x^2-32x^4}.
\]

The folded odd kernel is positive:

\[
B_-(x,y)=K_{44}(x+y)-K_{44}(|x-y|)\ge0.
\]

Directed FLINT/Arb analytic integration, including the removable center
limit, certifies

\[
\sup_{0<x\le L/2}\frac{(B_-\phi)(x)}{\phi(x)}<d_{44}.
\]

Weighted Schur therefore proves strict positivity of the odd sector.

## Even sector

The labelled auxiliary system has the exact positive symmetrizer

\[
H=\operatorname{diag}
\left(1,\frac1{2a_1},\ldots,\frac1{2a_{43}}\right).
\]

In symmetric coordinates its coefficient matrix is

\[
\widetilde M(\lambda)
=\operatorname{diag}(a_n^2)
-\frac{qq^T}{d_{44}-\lambda}.
\]

The center Dirichlet-to-Neumann response satisfies

\[
P'(\lambda)\succeq0
\]

between Riccati poles. Directed ball congruence certifies

\[
\operatorname{inertia}P(0)=(43-,1+),
\]

which equals its exact decoupled inertia at \(\lambda\to-\infty\).

There are no intervening poles. A pole at a shortened interval of length
\(\ell\) would require

\[
F=\frac1{d_{44}-\lambda}C_\ell F,
\]

but the channel Green functions give exactly

\[
C_\ell(s,t)=K_{44}(s+t)-K_{44}(|s-t|).
\]

This is the restriction of the already certified positive odd kernel, so

\[
\|C_\ell\|<d_{44}\le d_{44}-\lambda
\qquad(\lambda\le0).
\]

The pole equation is impossible. Loewner monotonicity and equal endpoint
inertia therefore exclude every nonpositive even eigenvalue.

Hence

\[
\boxed{T_{44}>0.}
\]

## Rank-one interpretation

The exact endpoint decomposition is

\[
T_{44}=A+c|1\rangle\langle1|,
\qquad
c=\frac{5+4^{-43}}{3\sqrt2}.
\]

Directed integration gives

\[
\frac{\langle1,B1\rangle}{\|1\|^2}
=3.2837698479145955\ldots>d_{44},
\]

so \(A=d_{44}I-B\) has a negative direction. Since its rank-one completion
is strictly positive, \(A\) has exactly one negative direction and

\[
\boxed{
1+c\langle1,A^{-1}1\rangle<0.
}
\]

Thus forty-three decaying gamma channels leave one even coherence defect, and
the source-fixed endpoint channel repairs exactly that defect. This theorem is
a finite prime-two positivity result. It does not prove positivity of the full
theta/Stieltjes tower or the Riemann hypothesis.

## Evidence

- `research/nima/burnol-prime-two-boundary-scout.md`
- `research/nima/checkers/check_burnol_odd_schur_acb.py`
- `research/nima/checkers/check_burnol_44_channel_arb.py`
- `research/nima/checkers/check_burnol_b_kernel_tp2_counterexample.py`
- commits `707724eb`, `6c474d78`, and `1c48d217`
