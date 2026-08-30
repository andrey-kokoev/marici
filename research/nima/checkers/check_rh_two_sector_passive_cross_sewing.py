from fractions import Fraction
import json
from pathlib import Path


# Exact scalar energy audit. A unitary scalar sewing has J^*J=1.
unitary_j = Fraction(-1)
assert unitary_j * unitary_j == 1

v_plus = Fraction(3)
v_minus = Fraction(-5)
u_minus = unitary_j * v_plus
u_plus = unitary_j * v_minus
boundary_supply = (
    u_plus * u_plus
    + u_minus * u_minus
    - v_plus * v_plus
    - v_minus * v_minus
)
assert boundary_supply == 0

# Positive off-seam defects cannot sum to zero unless both states vanish.
delta_plus = Fraction(2)
delta_minus = Fraction(3)
candidate_states = [
    (Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(2)),
    (Fraction(3), Fraction(-1)),
]
zero_balance_states = []
for g_plus, g_minus in candidate_states:
    defect = delta_plus * g_plus * g_plus + delta_minus * g_minus * g_minus
    if defect == 0:
        zero_balance_states.append((g_plus, g_minus))
assert zero_balance_states == [(Fraction(0), Fraction(0))]

# Hostile gain supplies a nonzero boundary residual.
hostile_j = Fraction(2)
assert hostile_j * hostile_j != 1
hostile_u_minus = hostile_j * v_plus
hostile_u_plus = v_minus / hostile_j
hostile_supply = (
    hostile_u_plus * hostile_u_plus
    + hostile_u_minus * hostile_u_minus
    - v_plus * v_plus
    - v_minus * v_minus
)
assert hostile_supply != 0

# Finite observability can collapse during completion.
observability_floor = [Fraction(1, cutoff * cutoff) for cutoff in range(1, 9)]
assert all(value > 0 for value in observability_floor)

result = {
    "unitary_cross_sewing_boundary_supply": str(boundary_supply),
    "positive_defect_candidate_states_checked": len(candidate_states),
    "zero_balance_states": [[str(a), str(b)] for a, b in zero_balance_states],
    "hostile_gain": str(hostile_j),
    "hostile_boundary_supply": str(hostile_supply),
    "unitary_sewing_forces_zero_defect_state": True,
    "observability_still_required": True,
    "finite_observability_floors": [str(value) for value in observability_floor],
    "global_theta_sewing_unitarity_constructed": False,
    "verdict": "two strict passive sectors with unitary cross-sewing admit no nonzero off-seam closed mode",
}

out = Path(__file__).parents[1] / "results" / "rh-two-sector-passive-cross-sewing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
