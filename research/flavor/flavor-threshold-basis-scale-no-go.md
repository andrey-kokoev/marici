# Threshold basis/scale no-go: WP1183

## Question

Can the conditional transient interface derive a threshold basis and scale?

## DPC resolution

- **Conjecture:** the conditional sector curve selects its basis, amplitude,
  and decay scale.
- **Rivals:** fixed \(U(23)\) basis; fixed epsilon gain; fixed kappa clock;
  reparametrized conditional curve.
- **Risky consequences:** the sector-basis orbit has dimension 86, epsilon has
  one dimension, and kappa has one time-reparametrization dimension.
- **Falsification attempt:** for every positive \(\kappa'\), the substitution
  \(t'=\kappa t/\kappa'\) maps the old curve to the new one, while the basis
  and epsilon fiber remain open.
- **Residual:** a dimensionful threshold anchor and sector-basis packet remain
  absent.
- **Disposition:** reject threshold basis/scale derivation.

Checker: `research/flavor/checkers/wp1183_threshold_basis_scale_no_go.py`

Result: `results/wp1183_threshold_basis_scale_no_go.json`
