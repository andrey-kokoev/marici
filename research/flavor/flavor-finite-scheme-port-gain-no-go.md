# Finite-scheme-port gain no-go: WP1097

## Question

Can the finite-scheme normalization-port theorem supply event reweighting or
the gain law?

## Rank and dimension gate

For ports \(x=(0,1,2)\), the evaluation matrix has Vandermonde determinant

\[
(1-0)(2-0)(2-1)=2.
\]

Thus the three ports are faithful on the rank-three finite-scheme orbit.

The flavor production problem instead has six independent soft-event branches.
Three scheme coordinates cannot supply six branch-to-physical16 rows.

## Gain gate

For the constant normalized response, each port value is \(1\), so evaluation
has gain \(1\), not \(3/2\). Vandermonde invertibility is a coordinate
faithfulness theorem, not a production amplitude or event reweighting law.

## Classification

Negative gate. Three faithful normalization coordinates cannot be promoted to
six event weights, a production kernel, channel selection, or gain \(3/2\).
The remaining gate is a source-derived six-row production kernel with event
weights and gain \(3/2\).

Checker: `research/flavor/checkers/wp1097_finite_scheme_port_gain_no_go.py`

Result: `results/wp1097_finite_scheme_port_gain_no_go.json`
