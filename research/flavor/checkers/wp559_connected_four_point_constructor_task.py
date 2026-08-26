"""Exact source-derived connected four-point task for the WP133 hostile."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp133 = load("wp133_physical_instrument_open_world_audit.json")
wp558 = load("wp558_constructor_fiber_pole_descent.json")

phi, mass_squared, quartic = sp.symbols("phi m2 lambda")
potential = mass_squared * phi**2 / 2 + quartic * phi**4 / 4
two_point = sp.diff(potential, phi, 2).subs(phi, 0)
four_point = sp.diff(potential, phi, 4).subs(phi, 0)

lambda_pair = (sp.Integer(0), sp.Integer(1))
two_point_pair = [two_point.subs(quartic, value) for value in lambda_pair]
four_point_pair = [four_point.subs(quartic, value) for value in lambda_pair]

# WP133's exact normalized two-point response on four constructors, followed
# by the action-derived normalized fourth derivative.
two_point_response = sp.Matrix(
    [
        [1, 0, 0, 1],
        [1, 2, 0, 1],
        [0, 0, 1, 0],
    ]
)
source_four_point_row = sp.Matrix([[0, 0, 0, four_point_pair[1] / 6]])
joint_response = two_point_response.col_join(source_four_point_row)
hostile_constructor_difference = sp.Matrix([1, 0, 0, -1])

checks = {
    "dependencies_passed": bool(wp133["all_pass"] and wp558["passed"]),
    "two_point_operation_is_source_derived": two_point == mass_squared,
    "four_point_operation_is_source_derived": four_point == 6 * quartic,
    "isospectral_pair_has_equal_two_point_response": two_point_pair[0]
    == two_point_pair[1],
    "quartic_pair_has_distinct_four_point_response": four_point_pair
    == [0, 6],
    "two_point_rank_matches_wp133": two_point_response.rank()
    == wp133["expanded_family"]["two_point_rank"]
    == 3,
    "two_point_kernel_matches_wp133": len(two_point_response.nullspace())
    == wp133["expanded_family"]["two_point_kernel_dimension"]
    == 1,
    "hostile_difference_is_two_point_null": two_point_response
    * hostile_constructor_difference
    == sp.zeros(3, 1),
    "four_point_row_detects_hostile": source_four_point_row
    * hostile_constructor_difference
    != sp.zeros(1, 1),
    "joint_response_has_rank_four": joint_response.rank()
    == wp133["expanded_family"]["formal_four_point_rank"]
    == 4,
    "joint_kernel_is_zero": joint_response.nullspace() == [],
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP559",
    "domain": "WP133's bounded four-constructor family, with the two-adjoint isospectral hostile represented by one canonically normalized source coordinate and a frozen quadratic-plus-quartic action grammar.",
    "source_operation": {
        "potential": "V(phi)=m2*phi^2/2+lambda*phi^4/4",
        "two_point_vertex": str(two_point),
        "four_point_vertex": str(four_point),
        "rival_quartics": [str(value) for value in lambda_pair],
        "rival_two_point_responses": [str(value) for value in two_point_pair],
        "rival_four_point_responses": [str(value) for value in four_point_pair],
    },
    "contextual_partition": {
        "two_point": [
            ["two_adjoint", "isospectral_nonlinear_two_adjoint"],
            ["single_auxiliary_adjoint"],
            ["direct_EFT_contact"],
        ],
        "two_plus_four_point": [
            ["two_adjoint"],
            ["isospectral_nonlinear_two_adjoint"],
            ["single_auxiliary_adjoint"],
            ["direct_EFT_contact"],
        ],
    },
    "rank": {
        "two_point": int(two_point_response.rank()),
        "two_plus_four_point": int(joint_response.rank()),
        "joint_kernel_dimension": int(len(joint_response.nullspace())),
    },
    "classification": "Source-derived constructor-sensitive multipoint operation and exact bounded-family separator; not an executed instrument or selector.",
    "selector": bool(wp558["selector"]),
    "rigidifier": bool(joint_response.rank() == 4),
    "instrument": "Absent. Requires production of the source excitations, calibrated four-channel kinematics, scattering or amputated-vertex readout, finite-width and mixing transport, backgrounds, detector response, and covariance.",
    "smallest_exact_falsifier": "At common m2, lambda=0 and lambda=1 have identical Hessians but fourth derivatives 0 and 6. The difference lies in the two-point kernel and outside the four-point kernel.",
    "remaining_gate": "Derive an accessible portal from the frozen constructor grammar, propagate the four-point task through masses, widths, mixing and detector acceptance, and prove calibrated rank on a predeclared open rival class. Numerical source selection remains independent.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp559_connected_four_point_constructor_task.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
