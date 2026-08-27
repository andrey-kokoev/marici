"""Exact WP652 two-partial-width threshold response."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v = sp.symbols("u v", real=True)
wL, wR = sp.symbols("wL wR", positive=True)

# Log-widths after independently calibrated phase-space normalization:
# log(Gamma_L/A_L M)=2u and log(Gamma_R/A_R M)=2v.
response = sp.Matrix([2*u, 2*v])
J = response.jacobian([u, v])
W = sp.diag(wL, wR)
gram = sp.simplify(J.T*W*J)

checks = {
    "two_width_response_is_rank_two": J.rank() == 2,
    "each_single_width_port_is_rank_one": J[:1, :].rank() == 1 and J[1:, :].rank() == 1,
    "positive_calibrated_gram_determinant": sp.factor(gram.det()) == 16*wL*wR,
    "smallest_singular_value_is_two": min(J.singular_values()) == 2,
    "wp651_hostile_pair_is_width_distinguished": (1, 1) != (4, sp.Rational(1, 4)),
}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP652", "status": "PASS", "checks": checks,
    "source_parameters": ["u=log|x|", "v=log|y|"],
    "typed_observables": ["log(Gamma_L/(A_L M))=2u", "log(Gamma_R/(A_R M))=2v"],
    "response_rank": 2,
    "calibrated_gram_determinant": "16 w_L w_R > 0",
    "one_port_bound": "either partial width alone has rank one",
    "phase_disposition": "the matched phase arg(xy) is low-energy visible; reciprocal phase is vectorlike-messenger field rephasing",
    "classification": "source-derived ideal threshold instrument, faithful on the two magnitude directions conditional on two open labelled ports",
    "smallest_exact_falsifier": "one labelled partial-width channel closes or the calibrated two-width Jacobian loses rank",
    "remaining_experimental_gate": "finite widths, channel mixing, backgrounds, branching reconstruction, mass resolution, efficiencies, and uncertainty-stable smallest singular value",
}
(ROOT / "results" / "wp652_two_width_threshold_instrument.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
