# Nontrivial portal-dilation gate: WP1179

## Question

Can a nontrivial portal-to-sector dilation exist?

## DPC resolution

- **Conjecture:** an input-dependent CPTP dilation can fix the dark input and
  produce the dimension-trace state.
- **Rivals:** input-erasing replacement channel; rank-one Choi perturbation;
  fixed-point channel fiber; source dynamics.
- **Risky consequences:** with epsilon \(1/100\), the Choi margin is
  \(77/2300\); vacuum and even inputs receive different outputs; the
  fixed-output fiber has dimension \(4223\).
- **Falsification attempt:** the explicit perturbation is trace-annihilating
  and completely positive by operator-norm margin, but no source dynamics
  selects it.
- **Residual:** a source law must choose a channel from the high-dimensional
  conditional fiber.
- **Disposition:** accept conditional nontrivial dilation; reject sourced
  selection.

Checker: `research/flavor/checkers/wp1179_nontrivial_portal_dilation_gate.py`

Result: `results/wp1179_nontrivial_portal_dilation_gate.json`
