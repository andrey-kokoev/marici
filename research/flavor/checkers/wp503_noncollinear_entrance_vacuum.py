"""Exact positive two-vector entrance-vacuum packet for WP503."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp502 = load("wp502_gauged_entrance_triplet_stabilizer.json")

a, b = sp.symbols("a b", positive=True)
lambda_u, lambda_d, kappa = sp.symbols("lambda_u lambda_d kappa", positive=True)
variables = sp.symbols("u0:3 d0:3", real=True)
u = sp.Matrix(variables[:3])
d = sp.Matrix(variables[3:])

square_terms = [
    lambda_u * (u.dot(u) - a**2) ** 2,
    lambda_d * (d.dot(d) - b**2) ** 2,
    kappa * (u.dot(d)) ** 2,
]
potential = sp.expand(sum(square_terms))

vacuum_u = sp.Matrix([0, 0, a])
vacuum_d = sp.Matrix([b, 0, 0])
vacuum = {variables[i]: vacuum_u[i] for i in range(3)}
vacuum.update({variables[i + 3]: vacuum_d[i] for i in range(3)})

vacuum_energy = sp.simplify(potential.subs(vacuum))
gradient = sp.Matrix([sp.diff(potential, variable) for variable in variables])
vacuum_gradient = sp.simplify(gradient.subs(vacuum))
hessian = sp.simplify(sp.hessian(potential, variables).subs(vacuum))

L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]
gauge_tangents = sp.Matrix.hstack(
    *[sp.Matrix.vstack(generator * vacuum_u, generator * vacuum_d) for generator in L]
)

radial_u = sp.Matrix([0, 0, 1, 0, 0, 0])
radial_d = sp.Matrix([0, 0, 0, 1, 0, 0])
relative_angle = sp.Matrix([b, 0, 0, 0, 0, a]) / sp.sqrt(a**2 + b**2)
physical_modes = sp.Matrix.hstack(radial_u, radial_d, relative_angle)
physical_hessian = sp.simplify(physical_modes.T * hessian * physical_modes)
expected_physical_hessian = sp.diag(
    8 * lambda_u * a**2,
    8 * lambda_d * b**2,
    2 * kappa * (a**2 + b**2),
)

kernel = sp.Matrix.hstack(*hessian.nullspace())
kernel_and_gauge_rank = kernel.row_join(gauge_tangents).rank()

checks = {
    "wp502_dependency_passed": wp502["passed"],
    "vacuum_has_zero_energy": vacuum_energy == 0,
    "vacuum_is_stationary": vacuum_gradient == sp.zeros(6, 1),
    "vacuum_vectors_have_declared_norms": vacuum_u.dot(vacuum_u) == a**2 and vacuum_d.dot(vacuum_d) == b**2,
    "vacuum_vectors_are_orthogonal": vacuum_u.dot(vacuum_d) == 0,
    "potential_is_sum_of_three_positive_coefficient_squares": len(square_terms) == 3 and all(
        coefficient.is_positive for coefficient in (lambda_u, lambda_d, kappa)
    ),
    "hessian_rank_is_three": hessian.rank() == 3,
    "hessian_nullity_is_three": len(hessian.nullspace()) == 3,
    "row_gauge_tangent_rank_is_three": gauge_tangents.rank() == 3,
    "all_row_gauge_tangents_are_hessian_zeros": hessian * gauge_tangents == sp.zeros(6, 3),
    "row_gauge_tangents_span_entire_hessian_kernel": kernel_and_gauge_rank == 3,
    "physical_mode_basis_is_orthonormal": sp.simplify(physical_modes.T * physical_modes) == sp.eye(3),
    "physical_modes_are_transverse_to_gauge_orbit": sp.simplify(physical_modes.T * gauge_tangents) == sp.zeros(3),
    "physical_hessian_is_exact_positive_diagonal": physical_hessian == expected_physical_hessian,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP503",
    "domain": "neutral CP-even row-order-parameter subspace of the two entrance triplets, before charged and CP-odd electroweak completion",
    "potential": "lambda_u (u.u-a^2)^2 + lambda_d (d.d-b^2)^2 + kappa (u.d)^2",
    "positive_parameter_domain": ["a>0", "b>0", "lambda_u>0", "lambda_d>0", "kappa>0"],
    "vacuum": {
        "u": ["0", "0", "a"],
        "d": ["b", "0", "0"],
        "energy": str(vacuum_energy),
        "relation": "u and d are nonzero and orthogonal",
    },
    "hessian": {
        "rank": int(hessian.rank()),
        "gauge_kernel_dimension": len(hessian.nullspace()),
        "physical_mass_squared": {
            "u_radial": str(8 * lambda_u * a**2),
            "d_radial": str(8 * lambda_d * b**2),
            "relative_angle": str(2 * kappa * (a**2 + b**2)),
        },
    },
    "selector_rigidifier_split": "The positive source rigidifies the relative angle to orthogonality and the norms to the declared coefficients a and b. It does not select a, b, their ratio, or any flavor clock from deeper dynamics.",
    "classification": "Exact stable noncollinear entrance vacuum modulo the gauged row orbit on the neutral CP-even row subspace; not yet a complete electroweak vacuum theorem.",
    "selector": False,
    "rigidifier": bool(kernel_and_gauge_rank == 3),
    "instrument": None,
    "smallest_exact_falsifier": "The six-by-six Hessian has exactly three zeros, and they are exactly the three common row-rotation gauge tangents; its three physical eigenvalues are strictly positive on the declared domain.",
    "remaining_gate": "Lift this source to the complete complex electroweak-doublet field space, include every symmetry-allowed charged and CP-odd invariant, prove that no additional physical zero or tachyon survives, and then combine its scalar mixing with the fourteen gauge poles and detector response.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp503_noncollinear_entrance_vacuum.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
