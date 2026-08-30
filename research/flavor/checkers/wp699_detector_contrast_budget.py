"""Exact detector contrast budget for the finite-asymmetry hierarchy."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
t, T = sp.symbols("t T", positive=True)
epsilon, signal, background, eta, beta = sp.symbols(
    "epsilon signal background eta beta", positive=True
)

rho = sp.factor((t-1)**2/(t+1)**2)
contrast = sp.factor(1-rho)
contrast_floor = sp.factor(4*T/(T+1)**2)

yplus = epsilon*signal + background
yminus = epsilon*rho*signal + background
gap = sp.factor(yplus-yminus)
signal_threshold = sp.factor((2*eta+beta)/epsilon/contrast_floor)

checks = {
    "ideal_contrast_exact": contrast == 4*t/(t+1)**2,
    "contrast_reciprocal_symmetry": sp.simplify(contrast.subs(t, 1/t)-contrast) == 0,
    "contrast_increases_to_symmetric_point": sp.simplify(sp.diff(contrast, t)+4*(t-1)/(t+1)**3) == 0,
    "reciprocal_window_endpoint_floor": contrast.subs(t, T) == contrast_floor and sp.simplify(contrast.subs(t, 1/T)-contrast_floor) == 0,
    "common_background_cancels": gap == epsilon*signal*contrast,
    "uniform_signal_threshold_exact": sp.simplify(epsilon*signal_threshold*contrast_floor-(2*eta+beta)) == 0,
    "finite_window_witness": contrast_floor.subs(T, 3) == sp.Rational(3, 4),
    "unbounded_domain_has_zero_uniform_floor": sp.limit(contrast_floor, T, sp.oo) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP699",
    "status": "PASS",
    "checks": checks,
    "admitted_detector_model": "common efficiency epsilon and background B for the two branch hypotheses, per-yield absolute error eta, and residual branch-differential background uncertainty beta",
    "source_support_assumption": "a preregistered reciprocal asymmetry window 1/T <= t <= T with finite T>=1",
    "uniform_contrast_floor": "C_min=4T/(T+1)^2",
    "separation_condition": "epsilon S C_min > 2 eta + beta",
    "minimum_signal_budget": "S > (2 eta+beta)(T+1)^2/(4 epsilon T)",
    "classification": "exact conditional detector budget for the WP698 identifier; no selection authority and no calibration supplied",
    "smallest_exact_falsifier": "without a finite source support bound on t, T tends to infinity and the uniform contrast floor vanishes",
    "remaining_physical_instrument_gate": "derive the compact t support from the complete source, replace common efficiency/background assumptions by calibrated channel response, and include widths, loops, resolution, and correlated uncertainties",
}
(ROOT / "results" / "wp699_detector_contrast_budget.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
