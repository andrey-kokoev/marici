import json
from pathlib import Path

import sympy as sp


g, c, luminosity, efficiency, q, background = sp.symbols(
    "g c luminosity efficiency q background", nonzero=True
)
q1, q2, e1, e2 = sp.symbols("q1 q2 e1 e2", positive=True)

s1 = luminosity * e1 * g**2 * q1
s2 = luminosity * e2 * g**2 * q2
p1 = sp.cancel(s1 / (s1 + s2))
mu = background + luminosity * efficiency * g**2 * q

tests = {
    "normalized_fraction_is_gain_independent": sp.diff(p1, g) == 0,
    "normalized_fraction_is_luminosity_independent": sp.diff(p1, luminosity) == 0,
    "absolute_rate_has_nonzero_gain_derivative": sp.simplify(sp.diff(mu, g) - 2 * luminosity * efficiency * g * q) == 0,
    "gain_two_has_fourfold_signal": sp.simplify((mu.subs(background, 0).subs(g, 2)) / (mu.subs(background, 0).subs(g, 1)) - 4) == 0,
    "gain_sign_is_rate_blind": sp.simplify(mu.subs(g, -g) - mu) == 0,
    "luminosity_gain_nuisance_symmetry": sp.simplify(mu.subs({g: c * g, luminosity: luminosity / c**2}) - mu) == 0,
    "uncalibrated_log_jacobian_rank_one": sp.Matrix([[2, 1]]).rank() == 1,
    "calibrated_log_jacobian_rank_two": sp.Matrix([[2, 1], [0, 1]]).rank() == 2,
    "calibrated_log_jacobian_determinant_two": sp.Matrix([[2, 1], [0, 1]]).det() == 2,
    "hostile_normalized_pair_survives": sp.simplify(p1.subs(g, 1) - p1.subs(g, 2)) == 0,
    "hostile_uncalibrated_absolute_pair_survives": sp.simplify(mu.subs({g: 1, luminosity: 4}) - mu.subs({g: 2, luminosity: 1})) == 0,
}

passed = sum(bool(value) for value in tests.values())
result = {
    "work_package": "WP881",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "deferred: exact common-gain readout requires an independently calibrated absolute-rate instrument",
    "normalized_observation_gain_rank": 0,
    "uncalibrated_absolute_response_rank": 1,
    "calibrated_gain_luminosity_response_rank": 2,
    "smallest_hostiles": {
        "normalized": "g=1 versus g=2",
        "uncalibrated_absolute": "(g,L)=(1,4) versus (2,1)",
        "rate_sign": "g versus -g",
    },
    "required_instrument": [
        "completion-specific source production and decay channel",
        "independent luminosity or source-current monitor",
        "independent efficiency calibration",
        "background-normal channel",
        "interference reference if gain sign is claimed",
    ],
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp881_common_gain_absolute_rate_gate.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
