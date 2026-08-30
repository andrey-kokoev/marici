# 1722 — Zero-Probability Quantum Conditioning Begins at the Second Density Grade

## Entangled-outcome falsifier

Entry 1721 closes independent coherent inputs.  Admit a non-product pure state

\[
|\Psi_\varepsilon\rangle
=|00\rangle
+\varepsilon\bigl(u|01\rangle+v|11\rangle\bigr),
\]

with labelled measurement outcome \(B=1\).  For \(v\ne0\), the coefficient
matrix of this bipartite vector has nonzero determinant at
\(\varepsilon\ne0\), so the family is generically entangled.

## Conditional block

The unnormalized postselected density block on the first system is

\[
\rho_{A|1}^{\rm un}
=\varepsilon^2
\begin{pmatrix}
u^2&uv\\uv&v^2
\end{pmatrix}.
\]

Its probability is

\[
p_1=\varepsilon^2(u^2+v^2).
\]

Hence the ordinary and first density-matrix normal grades vanish.  The second
grade is

\[
\boxed{
\operatorname{gr}^{(2)}_\varepsilon\rho_{A|1}^{\rm un}
=|\chi\rangle\langle\chi|,
\qquad |\chi\rangle=(u,v)^T.
}
\]

After normalization, the zero-probability conditional state depends on the
projective amplitude direction \([u:v]\).

## Architectural result

This reproduces the Marici pattern

\[
\text{linear resolved normal}
\longmapsto
\text{quadratic coarse invariant}.
\]

The resolved amplitude is first order, while probability and density are
second order.  The exceptional datum is a rank-one positive-semidefinite ray
inside the coherent coefficient object.  No new Cut carrier stratum is needed.

## Durable artifacts

- `research/benincasa/checkers/quantum_zero_outcome_rees.rs`
- `research/benincasa/results/quantum-zero-outcome-rees.json`
- `research/benincasa/quantum-zero-outcome-rees.md`

## Next falsifier

Replace the rank-one selected amplitude by two independent amplitude jets
entering the same zero-probability outcome.  Determine whether the second
grade retains only their summed positive block or whether relative phase
requires a higher coherence/flag object.
