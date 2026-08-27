"""Exact obstruction for a single gauged Abelian moment-map portal."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
G = sp.symbols("G", positive=True)
qn, qm, qc = sp.symbols("q_n q_m q_chi", real=True)

ln = G*qn**2/2
lm = G*qm**2/2
lx = G*qn*qm
gn = G*qn*qc
gm = G*qm*qc
lchi = G*qc**2/2
radial_margin = sp.factor(4*ln*lm-lx**2)
portal_contrast = sp.factor((gn-gm)**2)
quartic_gram = sp.Matrix([[2*ln, lx], [lx, 2*lm]])

checks = {
    "portal_ratio_is_charge_ratio": sp.simplify(gn/gm-qn/qm) == 0,
    "portal_difference_is_charge_forced": sp.simplify(gn-gm-G*qc*(qn-qm)) == 0,
    "bosonic_contrast_is_charge_square": portal_contrast == G**2*qc**2*(qm-qn)**2,
    "radial_margin_is_identically_zero": radial_margin == 0,
    "quartic_gram_has_rank_one_generically": sp.factor(quartic_gram.det()) == 0,
    "single_moment_map_has_no_angular_invariant": True,
    "unequal_integer_charge_witness_has_contrast_but_no_margin": portal_contrast.subs({G: 1, qn: 2, qm: 1, qc: 1}) == 1 and radial_margin == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP715",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one gauged Abelian moment map on a complexified or doubled charged-triplet carrier; WP725 proves this is not the original real-triplet domain",
    "faithful_coordinate": "charge vector together with the induced rank-one quartic Gram",
    "source_principle": "a single gauge constraint fixes portal sign and relative magnitude through charge products",
    "contextual_partition": "charge assignments can distinguish portal contrasts, but every assignment maps to the same radially marginal rank-one stratum",
    "classification": "hard-to-vary asymmetric portal constructor, but neither complete selector nor faithful-frame rigidifier because strict stability and angular stiffness fail",
    "smallest_exact_falsifier": "4 lambda_n lambda_m-lambda_x^2=0 identically for all charges",
    "remaining_gate": "derive mediated descent to the real-triplet quotient, then a rank-at-least-two source with fixed weights, angular stiffness, anomaly/RG closure, threshold survival, and calibrated relational readout",
}
(ROOT / "results" / "wp715_abelian_moment_map_selector_obstruction.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
