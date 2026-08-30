"""Exact mirror-completion audit for chiral source selection."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp785 = json.loads(
    (ROOT / "results" / "wp785_orientation_odd_bias_reference_port_no_go.json")
    .read_text(encoding="utf-8")
)

# Smallest standard five-charge genuinely chiral anomaly-free U(1) witness.
charges = (-9, -5, -1, 7, 8)
mirror = tuple(-q for q in charges)

def moments(packet):
    return {power: sum(q**power for q in packet) for power in range(1, 5)}

moments_source = moments(charges)
moments_mirror = moments(mirror)
has_vectorlike_pair = any(-q in charges for q in charges)

delta, a, b, z, ell = sp.symbols("delta a b z ell", real=True)
beta = delta * (a + b * delta**2)
beta_mirror_residual = sp.simplify(beta.subs(delta, -delta) + beta)

# Mirror-equivariant finite threshold matching and two readouts.
delta_low = z * delta
width = sp.expand(delta_low**2)
parity_readout = sp.expand(ell * delta_low)
threshold_mirror_residual = sp.simplify(
    delta_low.subs(delta, -delta) + delta_low
)
width_mirror_residual = sp.simplify(width.subs(delta, -delta) - width)
parity_mirror_residual = sp.simplify(
    parity_readout.subs(delta, -delta) + parity_readout
)

# The local critical exponent agrees at paired nonzero fixed points.
v = sp.symbols("v", positive=True)
paired_beta = delta * (delta**2 - v**2)
critical = sp.diff(paired_beta, delta)
critical_plus = sp.simplify(critical.subs(delta, v))
critical_minus = sp.simplify(critical.subs(delta, -v))

# A normalized binary parity instrument separates the pair when ell*z != 0.
response = sp.Matrix([[ell * z], [-ell * z]])
response_gram = sp.simplify((response.T * response)[0])

checks = {
    "wp785_dependency_passed": wp785["status"] == "PASS"
    and all(wp785["checks"].values()),
    "witness_is_genuinely_chiral": not has_vectorlike_pair,
    "source_linear_anomaly_cancels": moments_source[1] == 0,
    "source_cubic_anomaly_cancels": moments_source[3] == 0,
    "mirror_linear_anomaly_cancels": moments_mirror[1] == 0,
    "mirror_cubic_anomaly_cancels": moments_mirror[3] == 0,
    "quadratic_rg_weight_is_mirror_even": moments_source[2]
    == moments_mirror[2]
    == 220,
    "quartic_threshold_weight_is_mirror_even": moments_source[4]
    == moments_mirror[4],
    "odd_portal_beta_is_mirror_equivariant": beta_mirror_residual == 0,
    "paired_fixed_points_have_same_critical_exponent": critical_plus
    == critical_minus
    == 2 * v**2,
    "threshold_matching_transports_but_does_not_select_sign":
        threshold_mirror_residual == 0,
    "inclusive_width_is_mirror_blind": width_mirror_residual == 0,
    "parity_readout_flips_and_can_separate": parity_mirror_residual == 0
    and response_gram == 2 * ell**2 * z**2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP786",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP785",
    "admitted_state_domain": (
        "a genuinely chiral anomaly-free five-charge source and its complete "
        "charge-conjugate mirror, an exchange-odd portal coordinate, "
        "mirror-equivariant RG and finite threshold maps, and inclusive and "
        "parity-sensitive readouts"
    ),
    "faithful_coordinate": (
        "the signed portal contrast delta together with the full labelled "
        "chiral charge packet; delta squared is explicitly nonfaithful"
    ),
    "source_authorized_probe_family": (
        "linear and cubic anomaly tests, even charge moments entering ordinary "
        "RG/threshold responses, an odd equivariant beta field, and finite "
        "multiplicative matching"
    ),
    "contextual_partition": (
        "anomaly cancellation, even RG weights, critical exponents, threshold "
        "survival, and inclusive widths identify a source with its mirror; a "
        "parity-sensitive labelled instrument separates the two signs"
    ),
    "selector_result": (
        "none of the admitted source consistency or transport operations "
        "selects a mirror branch; parity readout identifies a realized branch "
        "but has no backward authority to select it"
    ),
    "smallest_exact_falsifier": (
        "the chiral packets (-9,-5,-1,7,8) and (9,5,1,-7,-8) both have "
        "vanishing linear and cubic anomalies and equal quadratic weight 220, "
        "while their signed parity responses are opposite"
    ),
    "instrument_result": (
        "two labelled parity responses have positive Gram value "
        "2*(ell*z)^2 when ell*z is nonzero; the inclusive width remains blind"
    ),
    "deutschian_status": (
        "a theory that merely permits one chiral packet also permits its mirror "
        "under the tested source laws; explaining the sign requires a "
        "non-mirror-completable source boundary, not post-selection by the "
        "instrument"
    ),
    "remaining_gate": (
        "construct an independently oriented boundary or incidence object whose "
        "mirror is not an admitted source state, then derive from that same "
        "object the continuous normalization, fixed RG trajectory, threshold "
        "map, and calibrated parity-labelled physical16 instrument"
    ),
}
(ROOT / "results" / "wp786_mirror_completion_sign_selection_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
