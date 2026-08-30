"""Exact WP590 Deutschian explanatory-scope audit of FDM-1."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp87 = json.loads(
    (ROOT / "results" / "wp87_dynamical_cp_breaking_constructor.json").read_text(
        encoding="utf-8"
    )
)

s, a, coupling, j = sp.symbols("s a lambda j", positive=True, real=True)
potential = coupling * (s**2 - a**2) ** 2 / 4
gradient = sp.diff(potential, s)
hessian = sp.diff(gradient, s)

stationary = sp.solve(sp.Eq(gradient, 0), s)
positive_vacuum_hessian = sp.simplify(hessian.subs(s, a))
cp_conserving_hessian = sp.simplify(hessian.subs(s, 0))
j_magnitude = a * j

unit_model = {a: 1, coupling: 1, j: 1}
double_model = {a: 2, coupling: 1, j: 1}

checks = {
    "potential_is_cp_even": sp.expand(potential.subs(s, -s) - potential) == 0,
    "positive_domain_stationary_points_are_zero_and_a": stationary == [a],
    "positive_vacuum_is_stable": positive_vacuum_hessian
    == 2 * a**2 * coupling,
    "cp_conserving_point_is_unstable": cp_conserving_hessian
    == -a**2 * coupling,
    "vacuum_j_magnitude_depends_on_free_scale": sp.diff(j_magnitude, a) == j,
    "unit_and_double_models_keep_cp_breaking": j_magnitude.subs(unit_model) != 0
    and j_magnitude.subs(double_model) != 0,
    "unit_and_double_models_predict_different_magnitudes": j_magnitude.subs(
        unit_model
    )
    == 1
    and j_magnitude.subs(double_model) == 2,
    "wp87_tested_complete_ensemble": wp87["prediction"]["sheets_tested"] == 1210,
    "wp87_qualitative_prediction_survived": wp87["prediction"]["passes"] == 1210,
    "wp87_declared_magnitude_unconstrained": wp87["prediction"]["predeclared"]
    == "J != 0; sign and magnitude unconstrained",
}

if not all(checks.values()):
    raise SystemExit(f"WP590 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP590",
    "status": "PASS",
    "checks": checks,
    "source_family": "V_{a,lambda}(s)=lambda*(s^2-a^2)^2/4 with a>0 and lambda>0",
    "hard_to_vary_core": "CP-even dynamics with an unstable CP-conserving point and two stable CP-conjugate vacua",
    "robust_prediction": "J is nonzero for every admitted initial state outside the separatrix",
    "easy_to_vary_content": "|J|=a*j(q); changing a preserves the mechanism while continuously changing the magnitude",
    "physical16_scope": "one qualitative CP attribute is restricted; the remaining 15 local quotient coordinates are untouched",
    "ensemble_test": {
        "sheets": wp87["prediction"]["sheets_tested"],
        "passes": wp87["prediction"]["passes"],
        "min_abs_J": wp87["prediction"]["min_abs_J"],
        "max_abs_J": wp87["prediction"]["max_abs_J"],
    },
    "classification": "genuine qualitative CP-breaking selector, but not an explanation of the observed physical16 flavor relations",
    "smallest_exact_falsifier": "an admitted CP-conserving physical flavor point refutes the robust class; a measured magnitude refutes only a fixed-a member",
    "remaining_explanatory_gate": "derive an independently normalized relation locking a and the untouched quotient moduli, then preregister numerical physical16 consequences",
}

out = ROOT / "results" / "wp590_fdm1_deutschian_scope.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
