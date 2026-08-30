# Opposite-momentum Gaussian correlations force a compatibility-domain assignment

At a translationally invariant anomalous support such as \(q=-p\), the
observed mode and one internal occurrence can already form a two-mode squeezed
Gaussian state.  In scaled quadratures, use the standard covariance blocks

\[
V_{pq}
=
\begin{pmatrix}
aI&cZ\\
cZ&aI
\end{pmatrix},
\qquad
c^2=a^2-1,
\qquad a>1.
\]

This is the pure two-mode-squeezed family.  Attempt a state-independent
assignment that keeps the environment block \(aI\) and correlation block
\(cZ\) fixed while replacing the observed covariance by \(xI\).

Even ordinary block positivity requires the Schur condition

\[
xa-c^2\geq0,
\qquad
x\geq a-\frac1a.
\]

For every integer \(a\geq2\), the physical observed vacuum \(x=1\) violates
this condition.  Hence the fixed correlated assignment is not positive on the
full observed state space.  Quantum uncertainty can only strengthen this
restriction.

The reduced evolution derived from this initial state is therefore defined on
a compatibility domain of observed marginals, not by a state-independent CP
channel acting on arbitrary observed inputs.  The natural typed object is an
initial-correlation assignment/process tensor retaining the supported partner.

The checker verifies the source family, vacuum failures, and ordinary
compatibility gate exactly for \(2\leq a\leq64\).
