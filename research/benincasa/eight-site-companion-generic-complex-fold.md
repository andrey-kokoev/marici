# Generic complex C8 companion walls are rank-one folds

## Question

Entry 1916 excludes all 36 reduced companion walls from the real-Euclidean routing cone. It does not determine whether their complex coefficient geometry is genuine.

For the four source-base-reduced cover maps

\[
F=(F_1,F_2,F_3,F_4),
\qquad
J=\frac{\partial F}{\partial(a,b,c,d)},
\]

let \(H\) be the corresponding companion factor of \(\det J\). At a generic point of \(H=0\), choose a nonzero adjugate column \(v\) and the corresponding left kernel covector \(\lambda\). A corank-one critical point is a fold when

\[
\lambda D^2F(v,v)\ne0.
\]

Equivalently, up to a nonzero adjugate normalization, the kernel-transversality polynomial is \(v\cdot\nabla H\).

## Exact factorization

For family A, one exact rank-three minor is

\[
-\frac1{16}bcd\,k^2(2k-3)(7k+6)^2
(2k^2-6kl-k-6l-6),
\]

and the kernel-transversality polynomial is

\[
-\frac14abcd\,k^2(2k-3)(7k+6)^2F_A(k,l),
\]

where

\[
\begin{aligned}
F_A={}&8k^4+8k^3l+12k^3+16k^2l^2+16k^2l-130k^2\\
&+136kl^2+182kl-179k+114l^2+228l+114.
\end{aligned}
\]

For all three B-patterns, one exact rank-three minor is

\[
\frac1{16}bcd\,k^2(7k+6)^2(6k-8l+7)
(2k^2-5k+2l-1),
\]

while kernel transversality is, up to the occurrence orientation sign,

\[
\frac18abcd\,k^2(7k+6)^2(6k-8l+7)F_B(k,l),
\]

with

\[
F_B=8k^3-28k^2+8kl+14k-4l^2+4l-1.
\]

These are nonzero polynomials. Hence on the generic companion divisor, away from the explicitly displayed residual intersections, \(J\) has rank three and its kernel is transverse to the critical divisor.

## Result

\[
\boxed{
\text{Every labelled reduced C8 companion family is generically an }A_1\text{ fold over complex routing.}
}
\]

Its local anti-invariant vanishing-cycle coefficient therefore has rank one. The edge-4 orientation sign changes the labelled generator, not its rank.

This is a coefficient theorem. It does not establish a nonzero intersection with the analytically continued Bunch--Davies relative chain.

## Artifacts

- `checkers/eight_site_companion_fold_samples.py`
- `checkers/eight_site_companion_symbolic_fold.py`
- `results/eight-site-companion-fold-samples.json`
- `results/eight-site-companion-symbolic-fold.json`

