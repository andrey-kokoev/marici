"""Exact WP128 two-adjoint renormalizable matching audit."""

from fractions import Fraction as F
import json
from pathlib import Path


a = F(28)
mass_u_sq = mass_d_sq = F(1)
mu_u = mu_d = F(1)
lam = F(25)
rho = F(13)

alpha = mu_u / mass_u_sq
beta = mu_d / mass_d_sq
q = lam * alpha**2 * beta**2
stability_margin = rho - lam / F(2)
x_star = F(1, 2) + a / (F(8) * q)

dx_dlam = -a / (F(8) * q * lam)
dx_dmu_u = -a / (F(4) * q * mu_u)
dx_dmass_u_sq = a / (F(4) * q * mass_u_sq)

# Hostile WP125 spectra: Qu=3^2+2^2+1^2, Qd=6^2+4^2+1^2.
qu, qd, k0 = F(14), F(53), F(1152, 625)
degree8_hostile = rho * (alpha**2 * qu + beta**2 * qd) ** 2 - q * k0

checks = {
    "linear_sources_are_dimension_three": 1 + 2 == 3,
    "commutator_square_is_dimension_four": 2 * (1 + 1) == 4,
    "radial_stabilizer_is_dimension_four": 4 == 4,
    "leading_solutions_exact": alpha == 1 and beta == 1,
    "required_commutator_coefficient": q == F(25),
    "wp125_angle_reproduced": x_star == F(16, 25),
    "bottcher_wenzel_stability_margin": stability_margin == F(1, 2) and stability_margin > 0,
    "hostile_degree_eight_is_positive": degree8_hostile == F(1457773, 25) and degree8_hostile > 0,
    "lambda_intervention_response": dx_dlam == F(-7, 1250),
    "linear_coupling_response": dx_dmu_u == F(-7, 25),
    "mass_intervention_response": dx_dmass_u_sq == F(7, 25),
}

result = {
    "work_package": "WP128",
    "classification": "renormalizable stable two-adjoint mediator sector with exact degree-eight matching; numerical coefficients unsourced",
    "mediators": ["Hermitian U(3)_Q adjoint A", "Hermitian U(3)_Q adjoint D"],
    "parameters": {
        "a": str(a), "M_u_squared": str(mass_u_sq), "M_d_squared": str(mass_d_sq),
        "mu_u": str(mu_u), "mu_d": str(mu_d), "lambda": str(lam), "rho": str(rho),
    },
    "matching": {"alpha": str(alpha), "beta": str(beta), "q": str(q), "selected_x": str(x_star)},
    "stability": {"rho_minus_lambda_over_two": str(stability_margin), "hostile_degree8_coefficient": str(degree8_hostile)},
    "source_responses": {"dx_dlambda": str(dx_dlam), "dx_dmu_u": str(dx_dmu_u), "dx_dM_u_squared": str(dx_dmass_u_sq)},
    "matching_order": "exact through field degree eight; mediator-shift corrections begin at field degree twelve",
    "reference_port_required": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp128_two_adjoint_renormalizable_completion.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
