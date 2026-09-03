# Threshold-anchor conjecture gate: WP1264

## Question

Can an anchor-free microscopic source grammar select the portal-to-sector
production channel?

## DPC resolution

- **Problem:** state the next bold explanation for the microscopic source
  grammar and expose it to falsification.
- **Bold conjecture:** every microscopic source grammar sufficient for the
  flavor selector must carry a dimensionful threshold anchor jointly fixing
  sector basis, amplitude, decay clock, and portal-to-sector channel.
- **Named rivals:** input-erasing replacement channel; source-selected
  nontrivial dilation; stationary-dynamics selection; finite-time transient
  interface; threshold-identified basis and scale; anchor-free microscopic
  grammar.
- **Risky consequences:** WP1178 has a CPTP replacement channel but zero
  sourced portal dynamics; WP1179 has input-dependent dilations and a
  4223-dimensional fixed-output fiber; WP1180 stationary composition erases
  the dilation perturbation; WP1181 has a conditional transient interface but
  zero source-selected interfaces; WP1182 leaves an 87-dimensional
  basis/amplitude fiber; WP1183 leaves an 88-dimensional joint fiber including
  time reparameterization.
- **Strongest falsification attempt:** replay WP1178 through WP1183 and search
  for a source-selected production channel that fixes basis, amplitude, and
  clock without a dimensionful threshold anchor.
- **Exact residual:** no anchor-free source grammar is found; the conjecture
  survives. A dimensionful threshold packet remains unconstructed and
  unfalsified as the required microscopic grammar.
- **Disposition:** threshold-anchor conjecture survives attempted
  falsification; microscopic threshold-anchor packet selected.

## Result

The bold threshold-anchor conjecture **survived** this falsification attempt.
It was not proven. Conditional channels and transient curves exist, but none
is source-selected or dimensionfully anchored.

Checker: `research/flavor/checkers/wp1264_threshold_anchor_conjecture_gate.py`

Result: `results/wp1264_threshold_anchor_conjecture_gate.json`
