"""Exact WP591 common-clock coupling audit for the FDM-1 CP scale."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp87 = json.loads(
    (ROOT / "results" / "wp87_dynamical_cp_breaking_constructor.json").read_text(
        encoding="utf-8"
    )
)

s, sigma, chi, y, coupling = sp.symbols(
    "s sigma chi y kappa", positive=True, real=True
)

lock_potential = coupling * (s**2 - chi * sigma**2) ** 2 / 4
flavor_norm_sq = 6 * y**2 * sigma**2
vacuum_s_sq = chi * sigma**2
normalized_cp_ratio = sp.simplify(vacuum_s_sq / flavor_norm_sq)

hostile_unit = normalized_cp_ratio.subs({chi: 1, y: 1})
hostile_quadruple = normalized_cp_ratio.subs({chi: 4, y: 1})

checks = {
    "lock_is_cp_even": sp.expand(lock_potential.subs(s, -s) - lock_potential)
    == 0,
    "lock_is_nonnegative_square": sp.simplify(
        lock_potential - coupling * (chi * sigma**2 - s**2) ** 2 / 4
    )
    == 0,
    "vacuum_shell_annihilates_lock": sp.simplify(
        lock_potential.subs(s**2, vacuum_s_sq)
    )
    == 0,
    "common_scale_cancels": sigma not in normalized_cp_ratio.free_symbols,
    "normalized_ratio_is_chi_over_six_y_squared": normalized_cp_ratio
    == chi / (6 * y**2),
    "ratio_retains_chi_response": sp.diff(normalized_cp_ratio, chi)
    == 1 / (6 * y**2),
    "ratio_retains_y_response": sp.diff(normalized_cp_ratio, y)
    == -chi / (3 * y**3),
    "hostile_models_differ_by_factor_four": hostile_unit == sp.Rational(1, 6)
    and hostile_quadruple == sp.Rational(2, 3),
    "qualitative_cp_prediction_still_survives_ensemble": wp87["prediction"][
        "passes"
    ]
    == wp87["prediction"]["sheets_tested"]
    == 1210,
}

if not all(checks.values()):
    raise SystemExit(f"WP591 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP591",
    "status": "PASS",
    "checks": checks,
    "coupled_source_term": "kappa*(s^2-chi*sigma^2)^2/4",
    "common_clock_relation": "f^2=6*y^2*sigma^2",
    "selected_dimensionless_relation": "s^2/f^2=chi/(6*y^2)",
    "hard_to_vary_gain": "the independent dimensionful CP scale is removed and the common dilation cancels",
    "easy_to_vary_remainder": "the dimensionless Wilson ratio chi/y^2 remains continuously free under the same symmetries and positivity",
    "ensemble_disposition": "the inherited qualitative prediction J!=0 still passes all 1210 sheets; no numerical prediction is preregistered because chi/y^2 is unfixed",
    "classification": "relational scale selector and qualitative CP selector, but not a hard-to-vary numerical flavor explanation",
    "smallest_exact_falsifier": "chi=1 and chi=4 at y=1 satisfy the same source typing but give s^2/f^2=1/6 and 2/3",
    "remaining_explanatory_gate": "derive chi/y^2 from a symmetry, anomaly, fixed point, or microscopic matching theorem independent of fitted flavor data",
    "remaining_experiment_gate": "joint calibrated readout of the CP invariant and flavor clock in one source model after chi/y^2 is fixed",
}

out = ROOT / "results" / "wp591_common_clock_cp_normalization_migration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
