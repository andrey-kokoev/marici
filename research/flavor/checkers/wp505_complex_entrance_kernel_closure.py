"""Exact positive complex neutral entrance-kernel closure for WP505."""

import itertools
import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp504 = load("wp504_complex_entrance_flat_obstruction.json")

a, b = sp.symbols("a b", positive=True)
lambda_u, lambda_d, kappa = sp.symbols("lambda_u lambda_d kappa", positive=True)
alpha_u, alpha_d, rho, eta = sp.symbols("alpha_u alpha_d rho eta", positive=True)
variables = sp.symbols("ur0:3 ui0:3 dr0:3 di0:3", real=True)
ur = sp.Matrix(variables[0:3])
ui = sp.Matrix(variables[3:6])
dr = sp.Matrix(variables[6:9])
di = sp.Matrix(variables[9:12])

norm_u = ur.dot(ur) + ui.dot(ui)
norm_d = dr.dot(dr) + di.dot(di)
hermitian_real = ur.dot(dr) + ui.dot(di)
hermitian_imaginary = ur.dot(di) - ui.dot(dr)

uu_real = ur.dot(ur) - ui.dot(ui)
uu_imaginary = 2 * ur.dot(ui)
dd_real = dr.dot(dr) - di.dot(di)
dd_imaginary = 2 * dr.dot(di)
ud_real = ur.dot(dr) - ui.dot(di)
ud_imaginary = ur.dot(di) + ui.dot(dr)

reality_u = sp.expand(norm_u**2 - uu_real**2 - uu_imaginary**2)
reality_d = sp.expand(norm_d**2 - dd_real**2 - dd_imaginary**2)
reality_u_squares = 4 * sum(
    (ur[i] * ui[j] - ur[j] * ui[i]) ** 2
    for i, j in itertools.combinations(range(3), 2)
)
reality_d_squares = 4 * sum(
    (dr[i] * di[j] - dr[j] * di[i]) ** 2
    for i, j in itertools.combinations(range(3), 2)
)

q = a**2 / b**2
phase_lock = (uu_real - q * dd_real) ** 2 + (uu_imaginary - q * dd_imaginary) ** 2

potential = sp.expand(
    lambda_u * (norm_u - a**2) ** 2
    + lambda_d * (norm_d - b**2) ** 2
    + kappa * (hermitian_real**2 + hermitian_imaginary**2)
    + alpha_u * reality_u
    + alpha_d * reality_d
    + rho * (ud_real**2 + ud_imaginary**2)
    + eta * phase_lock
)

vacuum_ur = sp.Matrix([0, 0, a])
vacuum_dr = sp.Matrix([b, 0, 0])
zero3 = sp.zeros(3, 1)
vacuum_vector = sp.Matrix.vstack(vacuum_ur, zero3, vacuum_dr, zero3)
vacuum = {variable: vacuum_vector[i] for i, variable in enumerate(variables)}

vacuum_energy = sp.simplify(potential.subs(vacuum))
gradient = sp.Matrix([sp.diff(potential, variable) for variable in variables])
vacuum_gradient = sp.simplify(gradient.subs(vacuum))
hessian = sp.simplify(sp.hessian(potential, variables).subs(vacuum))

L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]
row_gauge = [
    sp.Matrix.vstack(generator * vacuum_ur, zero3, generator * vacuum_dr, zero3)
    for generator in L
]
hypercharge_gauge = sp.Matrix.vstack(zero3, vacuum_ur, zero3, vacuum_dr)
gauge_tangents = sp.Matrix.hstack(*(row_gauge + [hypercharge_gauge]))
kernel = sp.Matrix.hstack(*hessian.nullspace())

relative_phase = sp.Matrix.vstack(zero3, vacuum_ur, zero3, -vacuum_dr)
imaginary_u_transverse = sp.Matrix([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
imaginary_d_transverse = sp.Matrix([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
imaginary_cross_kernel = sp.Matrix([0, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, b])
old_physical_flats = sp.Matrix.hstack(
    relative_phase,
    imaginary_u_transverse,
    imaginary_d_transverse,
    imaginary_cross_kernel,
)

checks = {
    "wp504_dependency_passed": wp504["passed"],
    "u_reality_penalty_is_explicit_sum_of_squares": sp.expand(reality_u - reality_u_squares) == 0,
    "d_reality_penalty_is_explicit_sum_of_squares": sp.expand(reality_d - reality_d_squares) == 0,
    "completed_vacuum_has_zero_energy": vacuum_energy == 0,
    "completed_vacuum_is_stationary": vacuum_gradient == sp.zeros(12, 1),
    "completed_hessian_rank_is_eight": hessian.rank() == 8,
    "completed_hessian_nullity_is_four": len(hessian.nullspace()) == 4,
    "row_plus_hypercharge_gauge_rank_is_four": gauge_tangents.rank() == 4,
    "all_gauge_tangents_are_exact_hessian_zeros": hessian * gauge_tangents == sp.zeros(12, 4),
    "gauge_tangents_span_entire_completed_kernel": kernel.row_join(gauge_tangents).rank() == 4,
    "all_four_wp504_physical_flats_are_lifted": (hessian * old_physical_flats).rank() == 4,
    "phase_lock_ratio_has_equal_mass_degree_upstairs_and_downstairs": sp.Poly(a**2, a, b).total_degree() == sp.Poly(b**2, a, b).total_degree(),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP505",
    "domain": "completed complex neutral row-vector source with real SO(3)_E action and common hypercharge, still excluding charged electroweak components",
    "added_invariants": [
        "alpha_u*((u_dagger u)^2-|u_transpose u|^2)",
        "alpha_d*((d_dagger d)^2-|d_transpose d|^2)",
        "rho*|u_transpose d|^2",
        "eta*|u_transpose u-(a^2/b^2)d_transpose d|^2",
    ],
    "positive_parameter_domain": ["alpha_u>0", "alpha_d>0", "rho>0", "eta>0"],
    "vacuum": "u=a e3 and d=b e1, both real, remains a global zero",
    "neutral_hessian": {
        "real_dimension": 12,
        "rank": int(hessian.rank()),
        "nullity": len(hessian.nullspace()),
        "gauge_orbit_dimension": int(gauge_tangents.rank()),
        "physical_kernel_dimension": int(len(hessian.nullspace()) - gauge_tangents.rank()),
    },
    "authority_cost": "The relative-phase locking term contains the predeclared dimensionless norm ratio a^2/b^2. It closes the spectrum but does not derive or select that ratio.",
    "classification": "Exact positive closure of the complex neutral entrance Hessian kernel to the admitted row-plus-hypercharge gauge orbit; conditional spectrum rigidifier, not a numerical selector or complete electroweak pole packet.",
    "selector": False,
    "rigidifier": bool(len(hessian.nullspace()) == gauge_tangents.rank()),
    "instrument": None,
    "smallest_exact_falsifier": "After adding the four declared positive invariants, the twelve-dimensional Hessian has rank eight and its four-dimensional kernel is exactly the row-plus-hypercharge gauge orbit; every WP504 physical-zero witness is lifted.",
    "remaining_gate": "Extend the exact invariant and Hessian audit to all charged and neutral components of the electroweak-doublet triplets, then diagonalize jointly with connector and gauge sectors and derive source-normalized residues and widths without fitting a,b or their ratio.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp505_complex_entrance_kernel_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
