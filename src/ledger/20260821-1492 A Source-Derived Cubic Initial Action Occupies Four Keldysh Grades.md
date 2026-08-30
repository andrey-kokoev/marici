---
author: marici.Benincasa
---

# 1492 — A Source-Derived Cubic Initial Action Occupies Four Keldysh Grades

## Status

Primary-source nonlinear finite-time boundary action from Collins--Holman--
Vardanyan, arXiv:1408.4801v1, Eqs. (4.7)--(4.8).

This is a distinct inflationary \(\zeta\) sector. It is not retroactively
identified with the linearized tadpole block corrected in Entry 1491.

## Frozen cubic initial action

The source introduces a cubic initial action at finite \(t_0\):

\[
S_0^{(3)}
=\mathcal N
\left[
T_C(\zeta_+,\zeta_+,\zeta_+)
-T_{C^*}(\zeta_-,\zeta_-,\zeta_-)
\right],
\]

where \(T_C\) is the source trilinear kernel including the displayed spatial
derivatives, \(\mathcal N\) is the real background normalization, and

\[
\boxed{
C(\mathbf k_1,\mathbf k_2,\mathbf k_3)
=\frac1K\left(\frac1{K\eta_0}-i\right),
\qquad
K=k_1+k_2+k_3.
}
\]

Thus, generically,

\[
C_R=\frac1{K^2\eta_0},
\qquad
C_I=-\frac1K
\]

are both nonzero.

## Keldysh polarization

Set

\[
\zeta_\pm=\zeta_c\pm\frac12\zeta_q,
\qquad
C=C_R+iC_I.
\]

By trilinearity, the real-kernel part is deck anti-invariant:

\[
\begin{aligned}
T_{C_R}(\zeta_+^3)-T_{C_R}(\zeta_-^3)
={}&
\sum_{\text{one }q}
T_{C_R}(\zeta_c,\zeta_c,\zeta_q)\\
&+\frac14T_{C_R}(\zeta_q,\zeta_q,\zeta_q),
\end{aligned}
\]

where the sum retains the three labelled placements of the quantum field.

The imaginary-kernel part is deck invariant:

\[
\begin{aligned}
i\left[
T_{C_I}(\zeta_+^3)+T_{C_I}(\zeta_-^3)
\right]
={}&
2iT_{C_I}(\zeta_c,\zeta_c,\zeta_c)\\
&+\frac{i}{2}
\sum_{\text{two }q}
T_{C_I}(\zeta_c,\zeta_q,\zeta_q).
\end{aligned}
\]

The derivative placements are occurrence labels and are not collapsed in
these sums.

## Four associated grades

The source action therefore has the exact contour-conormal support

\[
\boxed{
\operatorname{gr}_\Delta^m S_0^{(3)}\neq0
\quad\text{for}\quad
m=0,1,2,3,
}
\]

with character decomposition

\[
\boxed{
\begin{array}{c|c|c}
\text{kernel part}&\text{deck character}&\text{grades}\\
\hline
C_R&-1&1,3\\
iC_I&+1&0,2.
\end{array}
}
\]

The odd pair is causal/action-like. The even pair is statistical/density-
matrix data. Both are fixed by one complex source kernel.

## Trace typing

On the contour diagonal \(\zeta_q=0\), the odd part vanishes, while

\[
\Delta^*S_0^{(3)}
=2i\mathcal N T_{C_I}(\zeta_c,\zeta_c,\zeta_c)
\]

survives. This is compatible with density-matrix normalization through the
overall factor \(Z^{-1}\); it is not a unitary action difference and should
not be placed in \(\ker\Delta^*\).

## Architectural consequence

The nonlinear finite-time initial state is not merely a statistical line
feeding a causal block. At cubic order, one source kernel already packages a
deck-graded coefficient object with linked even and odd conormal grades:

\[
\boxed{
\mathcal C_{S_0^{(3)}}
=
\mathcal C_{+}^{(0,2)}
\oplus
\mathcal C_{-}^{(1,3)}.
}
\]

This is sector-specific coefficient complexity on the existing doubled
initial-boundary carrier. No new support stratum is introduced.

## Narrow relation to Entry 1491

Entry 1491 remains correct: the 2005 one-loop tadpole source itself fixes only
first contour grade. The present 2014 source independently demonstrates that
higher odd and even grades occur when a nonlinear initial action is actually
derived. Similar algebra does not establish identity of the two coefficient
objects.

## Next falsifier

Test the finite-time matching condition that fixes \(C\) as a morphism of the
trace/Gysin complex. Determine whether the linked four-grade packet is
preserved by the one-loop two-point correction in Sec. 5.2 or whether an
independent quadratic initial kernel is generated.

## Provenance

- Collins--Holman--Vardanyan, arXiv:1408.4801v1, Eqs. (4.7)--(4.8);
- Entries 1480--1481, 1485, 1487, and 1491;
- allocator claim `seqclaim-8094f482b58f8d325664b3ad`.
- epistemic event `ev-000000001612-6b39582c-a788-45dc-8cc2-1b595df816f2`.
