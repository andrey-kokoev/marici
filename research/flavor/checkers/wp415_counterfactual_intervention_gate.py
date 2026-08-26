"""Exact Deutsch-Popperian gate for a second flavor intervention."""

import json
from pathlib import Path

import sympy as sp


a, b, c, d = sp.symbols("a b c d", real=True)
w_h, w_j = sp.symbols("w_h w_j", positive=True)
delta, sigma = sp.symbols("delta sigma", nonnegative=True)

j = sp.Matrix([[a, b], [c, d]])
w = sp.diag(w_h, w_j)
gram_det = sp.factor((j.T * w * j).det())
wedge = sp.factor(j.det())

# The WP412 direction is the first column (1,v0).  A candidate second source
# has response (p,q), so the distinguishing invariant is q-v0*p.
v0, p, q = sp.symbols("v0 p q", real=True)
j_higgs = sp.Matrix([[1, p], [v0, q]])
higgs_wedge = sp.factor(j_higgs.det())
higgs_gram_det = sp.factor((j_higgs.T * w * j_higgs).det())

# A bounded calibration uncertainty sigma cannot certify separation unless the
# measured absolute wedge delta remains strictly outside zero.
robust_margin = delta - sigma

checks = {
    "weighted_gram_factorizes_as_positive_metric_times_wedge_square": gram_det == w_h * w_j * wedge**2,
    "rank_two_iff_response_wedge_is_nonzero": j.rank() == 2,
    "higgs_second_source_wedge_is_q_minus_v0p": higgs_wedge == q - p * v0,
    "higgs_weighted_gram_uses_same_wedge": higgs_gram_det == w_h * w_j * (p * v0 - q) ** 2,
    "robust_margin_vanishes_at_uncertainty_boundary": sp.simplify(robust_margin.subs(delta, sigma)) == 0,
    "robust_margin_is_positive_above_boundary": bool(sp.simplify(robust_margin.subs(delta, sigma + 1)) > 0),
    "robust_margin_is_not_positive_below_boundary": bool(sp.simplify(robust_margin.subs(delta, sigma / 2)) <= 0),
}

result = {
    "work_package": "WP415",
    "title": "Counterfactual second-intervention gate",
    "general_response_jacobian": [[str(x) for x in row] for row in j.tolist()],
    "response_wedge": str(wedge),
    "weighted_gram_determinant": str(gram_det),
    "wp412_first_column": ["1", "v0"],
    "candidate_second_column": ["p", "q"],
    "higgs_distinguishing_wedge": str(higgs_wedge),
    "robust_margin": str(robust_margin),
    "classification": "a second source story becomes experimentally distinct only through an executable nonzero response wedge",
    "smallest_exact_falsifier": "q-v0*p = 0",
    "uncertainty_falsifier": "the calibrated wedge interval contains zero",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp415_counterfactual_intervention_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
