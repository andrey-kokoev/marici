"""Exact SU(3) simple-group moment-map portal and descent audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sqrt3 = sp.sqrt(3)
T3 = sp.diag(sp.Rational(1,2),-sp.Rational(1,2),0)
T8 = sp.diag(1,1,-2)/(2*sqrt3)
weights = [sp.Matrix([T3[i,i],T8[i,i]]) for i in range(3)]
w1,w2,w3 = weights
g2 = sp.symbols("g_squared", positive=True)

def pairing(u,v):
    return sp.simplify(g2*(u.dot(v)))

# Conditional weight-ray assignment: chi and n on w1, m on w2.
gn = pairing(w1,w1)
gm = pairing(w2,w1)
contrast = sp.simplify(gn-gm)
lambda_n = pairing(w1,w1)/2
lambda_m = pairing(w2,w2)/2
lambda_x = pairing(w1,w2)
margin = sp.factor(4*lambda_n*lambda_m-lambda_x**2)
area = sp.det(sp.Matrix.hstack(w1,w2))

# The equally legal channel embedding with n and m exchanged reverses the
# ordered contrast while preserving the simple group, representations, and
# charge Gram.
swapped_gn = pairing(w2,w1)
swapped_gm = pairing(w1,w1)
swapped_contrast = sp.simplify(swapped_gn-swapped_gm)

# A full SU(3) fundamental is complex. One imaginary generator maps a real
# basis vector outside the real three-dimensional slice.
I = sp.I
T2 = sp.Matrix([[0,-I,0],[I,0,0],[0,0,0]])/2
e1 = sp.Matrix([1,0,0])
real_slice_residual = T2*e1

# The common simple-group metric fixes relative normalization but not its
# overall gauge coupling.
scale = sp.symbols("s", positive=True)
scaled_contrast = sp.simplify(contrast.subs(g2,scale*g2))

checks = {
    "fundamental_weights_sum_to_zero": sp.simplify(w1+w2+w3) == sp.zeros(2,1),
    "all_fundamental_weights_have_equal_norm": len({sp.simplify(w.dot(w)) for w in weights}) == 1,
    "conditional_portals_have_opposite_signs": gn == g2/sp.Integer(3) and gm == -g2/sp.Integer(6),
    "conditional_ordered_contrast_is_fixed_ratio": contrast == g2/sp.Integer(2),
    "rank_two_moment_map_has_strict_margin": margin == g2**2/sp.Integer(12),
    "margin_is_weight_area_square": sp.simplify(margin-g2**2*area**2) == 0,
    "swapped_embedding_reverses_ordered_contrast": swapped_contrast == -contrast,
    "swapped_embedding_preserves_unordered_portal_pair": {gn,gm} == {swapped_gn,swapped_gm},
    "real_three_slice_is_not_su3_invariant": real_slice_residual == sp.Matrix([0,I/2,0]),
    "common_gauge_rescaling_changes_magnitude": scaled_contrast == scale*contrast,
    "deliberate_failure_residual_is_nonzero": swapped_contrast-contrast == -g2,
}
checks = {name: bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP746",
    "status": "PASS",
    "checks": checks,
    "source_domain": "SU(3) fundamental complex weight rays with one simple-group Killing metric and a supersymmetric D-term interpretation",
    "faithful_coordinate": "complex three-component carrier and its rank-two Cartan moment map, not the original real irreducible SO(3) triplet",
    "conditional_repair": "weights w_chi=w_n=w1 and w_m=w2 give g_n=g^2/3, g_m=-g^2/6, contrast g^2/2, and strict radial margin g^4/12",
    "classification": "conditional CP-even sign/ratio and radial selector on an enlarged complex domain; neither a physical16 selector nor an absolute-magnitude selector",
    "orientation_fiber": "exchanging the two channel embeddings preserves the unordered source packet and reverses the ordered contrast",
    "descent_obstruction": "the SU(3) fundamental is complex; an imaginary generator maps the real three-slice out of itself, reproducing the WP725 domain-enlargement gate",
    "magnitude_fiber": "common gauge-metric rescaling sends the contrast g^2/2 to s g^2/2",
    "smallest_exact_falsifier": "the equally legal swapped embedding changes the contrast from +g^2/2 to -g^2/2, residual -g^2",
    "remaining_source_gate": "derive an oriented anomaly-free embedding and a mediated descent to physical16, then fix the gauge magnitude and RG clock",
    "remaining_threshold_gate": "prove a nondecoupling supersymmetric or other threshold completion without an independent boundary counterterm",
    "remaining_physical_gate": "construct calibrated representation-labelled channels; Cartan weights are not detector instruments",
}
(ROOT / "results" / "wp746_su3_moment_map_conditional_selector.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
