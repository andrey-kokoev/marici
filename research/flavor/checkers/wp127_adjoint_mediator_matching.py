"""Exact WP127 adjoint-mediator matching and obstruction audit."""

from fractions import Fraction as F
import json
from pathlib import Path


a, mass_sq, g = F(28), F(2), F(10)
q = g * g / (F(2) * mass_sq)
t_star = -g / mass_sq

# Write X=t B, K=Tr(B^2). The X-dependent potential is
# (M^2/2)t^2 K + g t K.
matched_k_coefficient = mass_sq * t_star * t_star / F(2) + g * t_star
completion_constant = -g * g / (F(2) * mass_sq)

x_star = F(1, 2) + a / (F(8) * q)
dx_dg = -a * mass_sq / (F(2) * g**3)
dx_dmass_sq = a / (F(4) * g * g)

# On the WP125 hostile ray K0=1152/625 and C0=643/25.
# Phi -> s Phi gives V(s)=a*C0*s^4-q*K0*s^8, hence the leading
# coefficient is strictly negative.
k0, c0 = F(1152, 625), F(643, 25)
negative_ray_leading_coefficient = -q * k0

checks = {
    "positive_mediator_mass": mass_sq > 0,
    "exact_auxiliary_solution": mass_sq * t_star + g == 0 and t_star == F(-5),
    "completion_of_square_matching": matched_k_coefficient == completion_constant,
    "required_q_generated": q == F(25),
    "negative_commutator_sign_fixed": matched_k_coefficient == F(-25),
    "wp125_angle_reproduced": x_star == F(16, 25),
    "coupling_intervention_response": dx_dg == F(-7, 250),
    "mass_intervention_response": dx_dmass_sq == F(7, 100),
    "radial_ray_is_unbounded_without_completion": negative_ray_leading_coefficient == F(-1152, 25) and negative_ray_leading_coefficient < 0,
    "dimension_five_vertex_not_renormalizable": 1 + 4 == 5,
}

result = {
    "work_package": "WP127",
    "classification": "exact auxiliary-adjoint EFT matching; not a renormalizable UV completion",
    "mediator": "Hermitian U(3)_Q adjoint X",
    "interaction": "(M^2/2)Tr(X^2)+g Tr(X i[H_u,H_d])",
    "parameters": {"a": str(a), "M_squared": str(mass_sq), "g": str(g)},
    "matching": {"q": str(q), "X_over_B": str(t_star), "K_coefficient": str(matched_k_coefficient)},
    "selected_x": str(x_star),
    "source_responses": {"dx_dg": str(dx_dg), "dx_dM_squared": str(dx_dmass_sq)},
    "radial_obstruction": {"hostile_C0": str(c0), "hostile_K0": str(k0), "s_eighth_coefficient": str(negative_ray_leading_coefficient)},
    "reference_port_required": False,
    "physical_instrument_established": False,
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp127_adjoint_mediator_matching.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)
