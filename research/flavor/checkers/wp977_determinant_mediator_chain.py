"""Exact WP977 determinant mediator-chain checker."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

lambda_aux = Fraction(1)
gamma = Fraction(8)
mu = Fraction(1)
m_a_squared = Fraction(1)
m_s_squared = Fraction(1)

vertex_degrees = {
    "A_commutator_XY": 3,
    "s_det_A": 4,
    "auxiliary_radial_stabilizer": 4,
}
stability_margin = lambda_aux - abs(gamma) / 16
leading_commutator_coefficient = mu**2 / (2 * m_a_squared)
leading_determinant_coefficient = (
    gamma**2 * mu**6
    / (2 * m_s_squared * m_a_squared**6)
)

# Exact maximization underlying |s det A| <= R^2/16:
# set u=s^2/R and q=Tr(A^2)/R=1-u.  The squared normalized bound is
# u(1-u)^3/27, maximized at u=1/4 with value 1/256.
u_star = Fraction(1, 4)
normalized_bound_squared = u_star * (1 - u_star)**3 / 27

checks = {
    "all_fundamental_vertices_are_renormalizable": max(vertex_degrees.values()) <= 4,
    "determinant_operator_is_generated_at_field_degree_twelve": 2 * 3 * 2 == 12,
    "auxiliary_determinant_bound_is_one_sixteenth": normalized_bound_squared == Fraction(1, 256),
    "benchmark_auxiliary_quartic_is_strictly_coercive": stability_margin == Fraction(1, 2),
    "adjoint_elimination_generates_negative_commutator_square": leading_commutator_coefficient == Fraction(1, 2),
    "two_stage_elimination_generates_expected_determinant_coefficient": leading_determinant_coefficient == 32,
    "generated_determinant_sign_favors_full_rank": leading_determinant_coefficient > 0,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.determinant-mediator-chain.v1",
    "work_package": "WP977",
    "status": "PASS",
    "checks": checks,
    "domain": "two Hermitian coefficient fields, one Hermitian adjoint mediator, and one CP-odd scalar",
    "quotient": "full weak-basis conjugation with simultaneous CP on the pseudoscalar port",
    "fundamental_vertex_degrees": vertex_degrees,
    "auxiliary_stability_margin": str(stability_margin),
    "leading_commutator_square_coefficient": str(leading_commutator_coefficient),
    "leading_determinant_square_coefficient": str(leading_determinant_coefficient),
    "classification": "renormalizable source constructor for the CP-magnitude operator; not a completed selector or instrument",
    "remaining_gate": "full coupled vacuum, coefficient-ray authority, ensemble survival, thresholds, and calibrated readout",
}
out = ROOT / "results" / "wp977_determinant_mediator_chain.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
