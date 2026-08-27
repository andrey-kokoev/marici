"""Exact WP658 composed detector-calibration Jacobian."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
q = sp.symbols("q", real=True)
l, r, t = sp.symbols("ell r t", positive=True, real=True)
a, b = (1+q)/2, (1-q)/2
S = sp.Matrix([[a, b], [b, a]])

# Parameters: source u,v; efficiency nuisances eta_L,eta_R; background beta.
# Records: two signal bins, two independent efficiency controls, one sideband.
J = sp.Matrix([
    [2*a, 2*b, 1, 0, 1],
    [2*b, 2*a, 0, 1, 1],
    [0, 0, l, 0, 0],
    [0, 0, 0, r, 0],
    [0, 0, 0, 0, t],
])
detJ = sp.factor(J.det())
detF = sp.factor((J.T*J).det())

checks = {
    "template_response_determinant_is_q": sp.simplify(S.det()-q) == 0,
    "composed_jacobian_determinant": sp.simplify(detJ-4*q*l*r*t) == 0,
    "composed_fisher_determinant": sp.simplify(detF-16*q**2*l**2*r**2*t**2) == 0,
    "all_positive_controls_and_separation_give_full_rank": J.subs({q: sp.Rational(1, 2), l: 1, r: 1, t: 1}).rank() == 5,
    "zero_template_contrast_loses_rank": J.subs({q: 0, l: 1, r: 1, t: 1}).rank() < 5,
    "missing_left_efficiency_control_loses_rank": J.subs({q: 1, l: 0, r: 1, t: 1}).rank() < 5,
    "missing_right_efficiency_control_loses_rank": J.subs({q: 1, l: 1, r: 0, t: 1}).rank() < 5,
    "missing_sideband_loses_rank": J.subs({q: 1, l: 1, r: 1, t: 0}).rank() < 5,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP658", "status": "PASS", "checks": checks,
    "parameter_packet": ["u", "v", "eta_L", "eta_R", "beta"],
    "record_packet": ["signal_L", "signal_R", "efficiency_control_L", "efficiency_control_R", "background_sideband"],
    "template_contrast": "q=det(S)",
    "composed_jacobian_determinant": "4 q sqrt(k_L k_R tau)",
    "composed_fisher_determinant": "16 q^2 k_L k_R tau",
    "joint_faithfulness_condition": "q != 0 and k_L>0 and k_R>0 and tau>0",
    "completion_stability": "fails when any factor approaches zero",
    "classification": "complete ideal detector-calibration architecture for two magnitude directions; identification only, not selection",
    "smallest_exact_falsifiers": ["q=0", "k_L=0", "k_R=0", "tau=0"],
    "remaining_gate": "bind all five records and their covariance to one actual experiment and verify an uncertainty-stable lower singular bound",
}
(ROOT / "results" / "wp658_composed_detector_calibration.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
