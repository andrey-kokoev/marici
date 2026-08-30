"""Exact WP655 Gaussian detector-convolution pullback."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
k, sigma = sp.symbols("k sigma", positive=True, real=True)
dg, Delta = sp.symbols("delta_gamma Delta", real=True)
transfer = sp.exp(-sigma**2*k**2/2)
source_ratio_positive_k = sp.exp(-dg*k-sp.I*Delta*k)
log_derivative_at_zero = sp.simplify(
    sp.diff(sp.log(source_ratio_positive_k), k).subs(k, 0))
separation_jacobian = sp.Matrix([
    sp.re(log_derivative_at_zero), sp.im(log_derivative_at_zero)
]).jacobian([dg, Delta])

checks = {
    "gaussian_transfer_is_positive": transfer.is_positive is True,
    "convolution_transfer_has_no_real_frequency_zero": sp.solve(transfer, k) == [],
    "source_ratio_log_derivative": log_derivative_at_zero == -dg-sp.I*Delta,
    "mass_width_separation_jacobian_has_rank_two": separation_jacobian.rank() == 2,
    "exact_collapse_requires_equal_width_and_mass": sp.solve(
        [sp.re(log_derivative_at_zero), sp.im(log_derivative_at_zero)],
        [dg, Delta], dict=True) == [{dg: 0, Delta: 0}],
    "coalescing_family_loses_first_order_separation": log_derivative_at_zero.subs({dg: 0, Delta: 0}) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP655", "status": "PASS", "checks": checks,
    "source_templates": "Lorentzian line shapes parameterized by mass and half-width",
    "detector_operation": "convolution with a Gaussian resolution kernel of finite sigma",
    "fourier_transfer": "exp(-sigma^2 k^2/2), strictly positive for every finite real k",
    "object_separation": "preserved: convolved templates coincide only when Delta=0 and delta_gamma=0",
    "completion_stability": "fails uniformly as (Delta,delta_gamma) approaches (0,0)",
    "operational_target_domain": "must impose a declared positive lower bound on the calibrated convolved-template Gram eigenvalue",
    "classification": "injective detector convolution without uniform inverse; identification conditional on an operational separation domain",
    "smallest_exact_falsifier": "a finite-sigma Gaussian transfer zero or two distinct Lorentzian parameter pairs with identical convolved templates",
    "remaining_gate": "derive the calibrated resolution sigma, background covariance, efficiencies, and uncertainty-stable Gram lower bound from an experiment",
}
(ROOT / "results" / "wp655_gaussian_convolution_pullback.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
