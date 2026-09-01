# Dimension-trace preparation gate: WP1132

## Question

Can a dimension-trace ensemble explicitly prepare the six-sector distribution?

## DPC resolution

- **Conjecture:** the normalized dimension-trace ensemble
  \(\rho=\oplus_b I_{d_b}/23\) explicitly prepares
  \(q=(6,8,1,4,2,2)/23\).
- **Rivals:** dimension-trace density operator; sourced UV boundary ensemble;
  microstate-uniform measure; no sourced ensemble.
- **Risky consequences:** \(\rho\) is positive with trace one; sector
  probabilities equal \(d_b/23\); the UV boundary state must match \(\rho\);
  and microstate uniformity must be source-derived.
- **Falsification attempt:** the exact density algebra passes, but no
  boundary-state matching map or microstate-uniform measure is sourced.
- **Residual:** a future UV ensemble may derive the dimension-trace state.
- **Disposition:** construct the conditional dimension-trace preparation
  state; reject current-source authority.

## Exact state

\[
\rho=\bigoplus_b\frac{I_{d_b}}{23},\qquad
\operatorname{Tr}\rho=1,\qquad
\operatorname{Tr}(P_b\rho)=\frac{d_b}{23}.
\]

This gives \(q\) algebraically. Trace one, positivity, and sector weights are
not evidence that the boundary prepared \(\rho\).

Checker: `research/flavor/checkers/wp1132_dimension_trace_preparation_gate.py`

Result: `results/wp1132_dimension_trace_preparation_gate.json`
