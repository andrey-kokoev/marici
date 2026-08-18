---
id: 451
date: 2026-08-18
title: Neither Euler Generator Is First-Order Soft Torsion
---

# Neither Euler Generator Is First-Order Soft Torsion

Entry 449 identifies the characteristic-zero Euler-resonance quotient
\[
T=\mathbb Q\langle[1],[a^7(b+1)]\rangle
\]
after dividing the universal \(a^4\) factor. The parallel Entry 449 shows
that ordinary fiber multiplication does not descend to this quotient, and
Entry 450 finds that the complete first soft deformation is nonflat in the
ordinary polynomial-degree filtration and mixes the resonance plane with the
quartic tail.

The remaining elementary alternative was that either distinguished resonance
class simply becomes torsion under the soft parameter. This can be tested
without choosing a connection or multiplying cokernel representatives.

Write the complete exact operator along the source-fixed physical soft arc
\[
X_2=t,\qquad E=0
\]
as
\[
D(t)=D_0+tD_1\pmod {t^2}.
\]
For a special-fiber class \(y\), the equation that \(t y\) be exact over
\(\mathbf F[t]/(t^2)\) is
\[
D_0x_0=0,
\qquad
D_1x_0+D_0x_1=y.
\]
This uses all four exact sectors and both exact columns before taking the
cokernel.

For the undivided representatives
\[
y_0=a^4,
\qquad
y_1=a^{11}(b+1),
\]
the block systems are inconsistent at both tested cutoffs:

\[
\begin{array}{c|c|c|c}
D&y&\operatorname{rank}A&\operatorname{rank}[A\mid y]\\ \hline
16&a^4&427&428\\
16&a^{11}(b+1)&427&428\\
20&a^4&611&612\\
20&a^{11}(b+1)&611&612
\end{array}
\]

Therefore neither canonical generator is killed by one power of the soft
parameter in the frozen dual-number exact complex:
\[
\boxed{t[a^4]\ne0,\qquad t[a^{11}(b+1)]\ne0\pmod {t^2}.}
\]

This does not contradict Entry 450. The complete filtered cokernel is still
nonflat; the result only excludes the simpler explanation that its defect is
obtained by making either canonical Euler generator first-order torsion.
The surviving architecture is:
\[
\text{persistent resonance classes}
\quad+\quad
\text{first-order mixing with the quartic tail}.
\]

The next finite test is the one prescribed by Entry 450: pull the complete
dual-number exact complex to \(\operatorname{Bl}_{(t,a)}\), derive the
exceptional filtration shifts from the transformed source operators, and
recompute flatness. No logarithmic Gauss--Manin action is defined before that
test.

The executable audit is the dlog-soft-axis-dual-number-resonance mode of
research/benincasa/marici-gm/src/bin/marked_tangency_support.rs; its bounded
output is
research/benincasa/soft-axis-dual-number-resonance-certificate.json.
