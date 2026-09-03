# Absolute boundary-lift gate: WP1287

## Question

Can a boundary template or contact shift substitute for the
determinant-controlled absolute boundary lift?

## DPC resolution

- **Problem:** test whether existing boundary data can close the blocked
  `A1-boundary-lift` leaf.
- **Bold conjecture:** every admissible typed UV packet must carry the
  absolute boundary lift with seven integer exponents, counterterm basis,
  endpoint orientation, direction-labelled boundary coordinates,
  determinant/Schur control, completed closed-range typing, and
  spectral-defect data.
- **Named rivals:** WP1098 contact-counterterm route; WP1106 source bundle;
  WP1109 field fiber; boundary shadow packet; contract shadow; fixture
  packet.
- **Risky consequences:** WP1106 and WP1109 show no admitted packet supplies
  the lift; the Nima analogue requires determinant control through the Schur
  complement; the Grothendieck analogue requires a source-derived
  full-covariance boundary selector; the Aspect analogue requires completed
  closed-range/spectral typing.
- **Strongest falsification attempt:** replay WP1098, WP1106, WP1109, and
  WP1286; compare the v11 and v12 admission contracts; test a boundary
  shadow packet with all v11 fields but no absolute boundary lift.
- **Exact residual:** the boundary shadow packet is rejected and no actual
  packet is admitted. The absolute-boundary-lift necessity conjecture
  survives. The residual is a source-derived seven-channel lift with
  determinant and completed spectral control.
- **Disposition:** absolute-boundary-lift necessity survives attempted
  falsification; owner preparation-packet handoff selected.

## Result

The absolute-boundary-lift necessity conjecture **survived** the attempted
falsification. It remains unproven, and no actual typed packet has been
admitted.

Checker: `research/flavor/checkers/wp1287_absolute_boundary_lift_gate.py`

Result: `results/wp1287_absolute_boundary_lift_gate.json`

Contract: `research/flavor/contracts/flavor-event-production-packet-admission.v12.json`
