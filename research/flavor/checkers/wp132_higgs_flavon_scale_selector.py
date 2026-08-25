"""Exact WP132 Higgs-flavon scale-selector audit."""

from fractions import Fraction as F
import json
from pathlib import Path


lambda_h, lambda_f, kappa = F(1), F(4), F(-2)


def potential(h2, r2):
    return lambda_h * h2 * h2 / 4 + lambda_f * r2 * r2 / 4 + kappa * h2 * r2 / 2


def gradients_over_fields(h2, r2):
    return lambda_h * h2 + kappa * r2, lambda_f * r2 + kappa * h2


def hessian(h2, r2):
    # At a nonzero stationary point, diagonal entries simplify to
    # 2 lambda_h h^2 and 2 lambda_f r^2.
    # r/h is not rational for r^2/h^2=1/2; determinant/rank use products.
    diagonal_product = (2 * lambda_h * h2) * (2 * lambda_f * r2)
    cross_squared = 4 * kappa * kappa * h2 * r2
    return diagonal_product, cross_squared


h2_a, r2_a = F(1), F(1, 2)
h2_b, r2_b = F(100), F(50)
grad_a = gradients_over_fields(h2_a, r2_a)
grad_b = gradients_over_fields(h2_b, r2_b)
diag_prod_a, cross_sq_a = hessian(h2_a, r2_a)

ratio = r2_a / h2_a
flat_condition = lambda_h * lambda_f - kappa * kappa

checks = {
    "bounded_quartic_saturates_condition": kappa < 0 and flat_condition == 0,
    "first_nonzero_stationary_point": grad_a == (0, 0),
    "second_scale_related_stationary_point": grad_b == (0, 0),
    "stationary_ratio_exact": ratio == F(1, 2),
    "potential_flat_at_first_point": potential(h2_a, r2_a) == 0,
    "potential_flat_at_second_point": potential(h2_b, r2_b) == 0,
    "hessian_determinant_zero": diag_prod_a - cross_sq_a == 0,
    "hessian_has_one_positive_direction": 2 * lambda_h * h2_a + 2 * lambda_f * r2_a > 0,
    "absolute_scale_not_selected": h2_a != h2_b and ratio == r2_b / h2_b,
    "threshold_scale_changes": h2_b / h2_a == 100 and r2_b / r2_a == 100,
}

result = {
    "work_package": "WP132",
    "classification": "Higgs-flavon portal selects a conditional scale ratio but not an absolute threshold scale",
    "potential": "lambda_h*h^4/4 + lambda_f*R^4/4 + kappa*h^2*R^2/2",
    "couplings": {"lambda_h": str(lambda_h), "lambda_f": str(lambda_f), "kappa": str(kappa)},
    "stationary_ratio_R2_over_h2": str(ratio),
    "flat_condition_lambda_product_minus_kappa_squared": str(flat_condition),
    "hostile_scale_pair": {
        "point_A_h2_R2": [str(h2_a), str(r2_a)],
        "point_B_h2_R2": [str(h2_b), str(r2_b)],
        "common_ratio": str(ratio),
        "threshold_mass_scale_factor": "10",
    },
    "hessian_rank": 1,
    "absolute_scale_selected": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp132_higgs_flavon_scale_selector.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
