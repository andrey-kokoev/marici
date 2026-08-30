"""Exact dynamical connector-frame architecture audit for WP483."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp480 = load("wp480_triplicated_messenger_beta_gate.json")
wp482 = load("wp482_port_symmetry_entrance_obstruction.json")

s_variables = sp.symbols("s0:9", real=True)
S = sp.Matrix(3, 3, s_variables)
identity = sp.eye(3)
frame_residual = sp.simplify(S.T * S - identity)
frame_potential = sp.expand(sum(value**2 for value in frame_residual))
vacuum = {s_variables[3 * i + j]: int(i == j) for i in range(3) for j in range(3)}
gradient = [sp.diff(frame_potential, variable).subs(vacuum) for variable in s_variables]
hessian = sp.hessian(frame_potential, s_variables).subs(vacuum)
hessian_spectrum = hessian.eigenvals()

cycle = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
ones = sp.ones(3, 1)
left_transformed = cycle * S
left_potential_residual = sp.simplify(left_transformed.T * left_transformed - S.T * S)
equal_entrance_invariance = sp.simplify(ones.T * cycle - ones.T)

# At the frame vacuum, the three row routes sum to the desired isotropic Gram.
route_gram = sp.simplify(S.T * S)
vacuum_gram = route_gram.subs(vacuum)

ordinary_fundamentals = sp.Integer(6)
stages_per_port = sp.Integer(2)
ports_per_sector = sp.Integer(3)
sm_sectors = sp.Integer(2)
color = sp.Integer(3)
messenger_fundamentals = sp.simplify(
    stages_per_port * ports_per_sector * sm_sectors * color
)
active_fundamentals = ordinary_fundamentals + messenger_fundamentals

CA = sp.Integer(3)
C2F = sp.Rational(4, 3)
C2S = sp.Integer(3)
TF = sp.Rational(1, 2)
S2F = active_fundamentals * TF
S2S = sp.Integer(3) * sp.Integer(3)
b0 = sp.simplify(sp.Rational(11, 3) * CA - sp.Rational(4, 3) * S2F - sp.Rational(1, 6) * S2S)
b1 = sp.simplify(
    sp.Rational(34, 3) * CA**2
    - (4 * C2F + sp.Rational(20, 3) * CA) * S2F
    - (2 * C2S + sp.Rational(1, 3) * CA) * S2S
)
formal_g2 = sp.simplify(-16 * sp.pi**2 * b0 / b1)

checks = {
    "wp480_dependency_passed": wp480["passed"],
    "wp482_dependency_passed": wp482["passed"],
    "frame_potential_is_renormalizable_quartic": sp.Poly(frame_potential, s_variables).total_degree() == 4,
    "unit_frame_has_zero_energy": frame_potential.subs(vacuum) == 0,
    "unit_frame_is_stationary": gradient == [0] * 9,
    "frame_hessian_has_six_positive_modes": hessian_spectrum.get(8) == 6,
    "frame_hessian_has_three_orientation_zeros": hessian_spectrum.get(0) == 3,
    "cyclic_row_action_preserves_frame_gram": left_potential_residual == sp.zeros(3),
    "cyclic_row_action_preserves_equal_entrance": equal_entrance_invariance == sp.zeros(1, 3),
    "vacuum_route_gram_is_isotropic": vacuum_gram == identity,
    "two_stage_repair_adds_thirty_six_messenger_fundamentals": messenger_fundamentals == 36,
    "active_total_is_forty_two_fundamentals": active_fundamentals == 42,
    "active_b0_is_negative_thirty_seven_halves": b0 == -sp.Rational(37, 2),
    "active_b1_is_negative_four_ninety_three": b1 == -493,
    "gauge_only_formal_root_is_negative": formal_g2 == -sp.Rational(296, 493) * sp.pi**2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP483",
    "source_action": {
        "connector_field": "real 3x3 frame S_{alpha i}, gauge singlet, with cyclic row action and oriented-triplet right action",
        "frame_potential": "lambda_S*||S^T S-s^2 I_3||_F^2",
        "two_stage_vertices": [
            "y_H*Qbar*H*A_R_alpha",
            "y_S*Abar_L_alpha*S_alpha_i*B_R_i",
            "y_X*Bbar_L_i*X_i*u_R",
            "M_A*Abar_L_alpha*A_R_alpha",
            "M_B*Bbar_L_i*B_R_i",
        ],
        "all_interaction_vertices_dimension": 4,
    },
    "unit_frame_vacuum": {
        "S": "I_3",
        "energy": 0,
        "hessian_spectrum": {str(value): int(multiplicity) for value, multiplicity in hessian_spectrum.items()},
        "route_gram": [[int(value) for value in row] for row in vacuum_gram.tolist()],
    },
    "relational_groupoid": {
        "old_experiment": "unframed oriented adjoint triplet",
        "new_experiment": "connector frame plus triplet, modulo the stabilizer of S and X",
        "unit_frame_stabilizer": "diagonal cyclic row/right rotations inside C3 x SO(3)",
        "orientation_zeros": 3,
        "meaning": "The frame creates relative port orientation; it does not reveal an absolute orientation of the old experiment.",
    },
    "matter_cost": {
        "messenger_stages_per_port": int(stages_per_port),
        "ports_per_sector": int(ports_per_sector),
        "messenger_dirac_fundamentals": int(messenger_fundamentals),
        "active_dirac_fundamentals": int(active_fundamentals),
        "gauge_only_b0": str(b0),
        "gauge_only_b1": str(b1),
        "formal_g_squared_root": str(formal_g2),
    },
    "classification": "Renormalizable relational connector architecture that conditionally repairs isotropic portal descent; not a numerical selector and not yet a viable spectrum.",
    "selector": False,
    "rigidifier": bool(vacuum_gram == identity),
    "reference_port_required": bool(hessian_spectrum.get(0) == 3),
    "instrument": None,
    "smallest_exact_falsifier": "The frame Hessian has three physical orientation zeros and the enlarged gauge-only root remains negative despite exact isotropic Gram descent.",
    "remaining_gate": "Lift or gauge the connector orientation modes without spoiling S^T S proportional to I, derive all connector/messenger couplings on a complete fixed ray, decouple both messenger stages above the vector poles, and recompute every pole, residue, and width.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp483_connector_frame_architecture.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
