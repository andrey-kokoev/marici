# Completion descent for metric-transition Markov objects

## Question

Does uniformly bounded framed completion descend to the faithful metric-transition quotient?

## Claim boundary

Every metric \(M_i\) is positive definite with \(\sup_i\lVert M_i\rVert\le C^2\). Edge covariance blocks satisfy the invariant contraction inequality and admit a uniform normalized contraction bound \(\rho<1\). This result does not derive \(\rho\) from pointwise inequalities alone.

## Invariant data

Choose any frames \(M_i=R_iR_i^T\) and define

\[
A_i=R_i^{-1}C_iR_{i+1}^{-T}.
\]

The hypothesis is \(\lVert A_i\rVert\le\rho<1\). A different frame choice changes \(A_i\) by orthogonal conjugation at its endpoints, so this norm condition is quotient-invariant.

Long blocks are defined without retaining a frame:

\[
K_{ij}=C_iM_{i+1}^{-1}C_{i+1}\cdots M_{j-1}^{-1}C_{j-1}.
\]

They equal \(R_i(A_i\cdots A_{j-1})R_j^T\), hence

\[
\lVert K_{ij}\rVert\le C^2\rho^{|i-j|}.
\]

The block Schur test yields

\[
\lVert K\rVert\le C^2\frac{1+\rho}{1-\rho}.
\]

Positivity follows from finite metric-transition kernels.

## Descent coherence

Every finite compression, contiguous Beck–Chevalley cell, associator, and completion comparison is expressed by the invariant blocks \((M_i,C_i)\). Orthogonal changes of reconstruction frame therefore induce identity comparisons on the quotient. Completion descends independently of a persistent frame choice.

A uniformly bounded GL congruence family with uniformly bounded inverse acts on quotient data by

\[
M_i\mapsto S_iM_iS_i^T,
\qquad
C_i\mapsto S_iC_iS_{i+1}^T,
\]

and preserves completed companion/conjoint structure.

## Hostile boundary

Bounded metrics alone do not provide geometric off-diagonal decay. Pointwise normalized contraction with supremum one is refused. Unbounded metrics are also refused even when all normalized transfers vanish, because diagonal block norms then diverge.

## Disposition

Uniform framed completion descends to the metric-transition quotient, preserving positivity, GL congruence, contiguous Beck–Chevalley, and companion/conjoint completion cells. The remaining analytic gate is general noncontiguous pullback/amalgamation.

## Verification

- `research/voevodsky/checkers/check_metric_transition_markov_completion.py`
- `research/voevodsky/results/metric_transition_markov_completion.json`
