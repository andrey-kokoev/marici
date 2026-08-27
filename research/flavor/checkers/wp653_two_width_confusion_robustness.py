"""Exact WP653 detector-confusion robustness for two width ports."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
e = sp.symbols("e", real=True)
C = sp.Matrix([[1-e, e], [e, 1-e]])
J = 2*C
gram = sp.simplify(J.T*J)
e0, delta = sp.Rational(1, 10), sp.Rational(1, 20)
robust_lower = sp.simplify(2*(abs(1-2*e0)-2*delta))

checks = {
    "confusion_matrix_preserves_total_rate": C*sp.ones(2, 1) == sp.ones(2, 1),
    "response_determinant": sp.simplify(J.det()-4*(1-2*e)) == 0,
    "gram_determinant": sp.simplify(gram.det()-16*(1-2*e)**2) == 0,
    "rank_is_two_away_from_half_confusion": J.subs(e, sp.Rational(1, 10)).rank() == 2,
    "half_confusion_collapses_to_rank_one": J.subs(e, sp.Rational(1, 2)).rank() == 1,
    "benchmark_uncertainty_interval_avoids_collapse": abs(1-2*e0) > 2*delta,
    "benchmark_robust_singular_lower_bound": robust_lower == sp.Rational(7, 5),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP653", "status": "PASS", "checks": checks,
    "detector_response": "J_det=2[[1-e,e],[e,1-e]] for symmetric labelled-channel confusion e",
    "rank_condition": "e != 1/2",
    "gram_determinant": "16(1-2e)^2",
    "uncertainty_condition": "|1-2e0|>2 delta_e",
    "robust_singular_lower_bound": "2(|1-2e0|-2 delta_e)",
    "exact_benchmark": {"e0": "1/10", "delta_e": "1/20", "lower_bound": "7/5"},
    "classification": "conditional detector-robust identification theorem; no experimental calibration value is yet admitted",
    "smallest_exact_falsifier": "e=1/2, where both reconstructed channels are identical and response rank is one",
    "remaining_gate": "supply a detector-derived confusion matrix and uncertainty set, then include finite-width overlap, backgrounds, efficiencies, and mass resolution",
}
(ROOT / "results" / "wp653_two_width_confusion_robustness.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
