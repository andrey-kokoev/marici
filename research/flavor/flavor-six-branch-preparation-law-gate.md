# Six-branch preparation-law gate: WP1130

## Question

Can the localized six-sector decomposition independently derive the
preparation law?

## DPC resolution

- **Conjecture:** the localized six-sector decomposition independently
  supplies \(q=(6,8,1,4,2,2)/23\).
- **Rivals:** dimension-weight preparation; parent-branching preparation
  operator; external normalization law; no preparation law.
- **Risky consequences:** an exact six-entry positive rational distribution
  summing to one, a sourced preparation operator, and a source-derived
  normalization map.
- **Falsification attempt:** the dimension distribution is exact, but WP1058
  leaves five independent mass blocks after exchange and supplies no
  preparation operator or normalization map.
- **Residual:** a parent branching or boundary preparation operator may derive
  \(q\) dynamically.
- **Disposition:** retain the dimension-distribution fiber; reject it as a
  preparation law.

## Exact fiber

\[
q=\frac{(6,8,1,4,2,2)}{23},\qquad \sum_b q_b=1.
\]

The decomposition supplies exact branch weights, not dynamics. Sector
dimensions and rational normalization cannot be promoted to preparation.

Checker: `research/flavor/checkers/wp1130_six_branch_preparation_law_gate.py`

Result: `results/wp1130_six_branch_preparation_law_gate.json`
