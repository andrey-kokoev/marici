# SU(6) is the first unitary parent with enough spectral budget, but it retains the boundary modulus: WP774

## Question

What is the smallest simple unitary extension of the \(SU(4)\) gauge-link
parent whose vector sector can keep the \(32\)-degree portal operand packet in
the bulk without reversing the half-twist spectral sign?

## Exact vector budget

For \(SU(n)\),

\[
N_V=n^2-1.
\]

With the bulk portal operands,

\[
\kappa(n)=2+(n^2-1)-32=n^2-31.
\]

Therefore

\[
\kappa(5)=-6,
\qquad
\kappa(6)=5.
\]

\(SU(6)\) is the first group in the \(SU(n)\) chain with positive index.
Its adjoint branching under \(SU(4)\times SU(2)\times U(1)\) has dimensions

\[
35=15+3+1+8+8.
\]

The original \(SU(4)\) gauge-link parent is present as the fifteen-dimensional
block, while twenty additional vector degrees repair the portal-operand
spectral budget.

## Two surviving obstructions

First, the compulsory mediator packet costs another \(48\) degrees. If it is
also bulk,

\[
\kappa=2+35-32-48=-43.
\]

Second, group enlargement does not alter the orbifold operator typing.
Residual gauge symmetry still permits the exchange-even boundary kinetic
coefficient

\[
g_{\mathrm{eff}}^2=\frac{1}{C+\tau}.
\]

At \(C=1\), the legal packets \(\tau=0\) and \(\tau=1\) retain the same
\(SU(6)\) parent and positive portal-operand spectral sign but change the
WP771 contrast from \(1/10\) to \(1/20\).

## Classification

\(SU(6)\) is a minimal vector-budget candidate, not yet a source-selected
theory. Minimality inside a chosen \(SU(n)\) scan does not explain why nature
chooses that chain, representation embedding, or localization. A genuine
successor must derive the enlargement from anomaly and chirality constraints,
place the required mediator sector without reversing the complete spectral
measure, and fix the common orbifold kinetic coefficient through a boundary
source law.

The resulting finite response must still be realized by actual physical16
production and decay channels satisfying the WP770 two-port uncertainty gate.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp774_minimal_su6_vector_budget_boundary_modulus.py

Generated result:
research/flavor/results/wp774_minimal_su6_vector_budget_boundary_modulus.json
