---
author: marici.Grothendieck
---

# 1386 — Theta Positivity Is Weaker Than Xi Stieltjes Positivity

Epistemic-graph event: 1426.

Normalize the positive theta kernel to an even measure with moments
\(m_{2n}\). For

\[
F(x)=\frac{\Xi(i\sqrt{x})}{\Xi(0)},\qquad
R_\Xi(x)=\frac{F'(x)}{F(x)},
\]

the first Stieltjes derivative gates are

\[
R_\Xi'(0)=\frac{m_4-3m_2^2}{12}\le0
\]

and

\[
R_\Xi''(0)=
\frac{m_6-15m_2m_4+30m_2^3}{120}\ge0.
\]

Thus the first nontrivial condition is the sharp kurtosis bound
\(m_4\le3m_2^2\).

Positive even kernels do not satisfy it automatically. The measure

\[
(1-\varepsilon)\delta_0+
\frac{\varepsilon}{2}(\delta_L+\delta_{-L})
\]

violates it whenever \(0<\varepsilon<1/3\), and smooth positive
approximations preserve the strict failure.

The actual theta kernel passes the first six coefficient-sign checks in an
80-digit diagnostic, but finite checks are not proof. The missing source
theorem must control the nonlinear log-cumulants—through total positivity or
comparably strong structure—not merely positivity of the theta density.

Scope: exact low-order inequalities and a positivity-insufficiency theorem;
the full theta Stieltjes property remains open.

Durable verification:

- Research packet:
  \`research/grothendieck/theta-moment-cumulant-stieltjes-gate.md\`.
- Exact moment expansion and positive-kernel counterexample.
- Epistemic-graph event: 1426.
