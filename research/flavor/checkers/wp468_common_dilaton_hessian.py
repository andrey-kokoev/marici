"""Exact full Hessian audit for the WP467 common-dilaton portal."""

import json
from pathlib import Path

import sympy as sp


I = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]]) / sp.sqrt(2),
    sp.diag(1, 0, -1),
]


def norm_squared(matrix):
    return sp.simplify(sp.trace(matrix.conjugate().T * matrix))


z = sp.symbols("z0:24", real=True)
h = sp.symbols("h0:4", real=True)
sigma = sp.symbols("sigma", real=True)
coordinates = z + h + (sigma,)
X = [sum((z[8 * k + i] * lambdas[i] for i in range(8)), sp.zeros(3)) for k in range(3)]
pairs = [(0, 1, 2, 1), (0, 2, 1, -1), (1, 2, 0, 1)]
square_terms = [X[i] * X[j] - X[j] * X[i] - I * sign * sigma * X[k] for i, j, k, sign in pairs]
flavor_norm = sum(sp.trace(matrix * matrix) for matrix in X)
higgs_norm = sum(component**2 for component in h) / 2
potential = sp.expand(
    sum(norm_squared(term) for term in square_terms)
    + (flavor_norm - 6 * sigma**2) ** 2
    + (higgs_norm - sigma**2) ** 2
)

vacuum = {coordinate: 0 for coordinate in coordinates}
vacuum[sigma] = 1
vacuum[h[3]] = sp.sqrt(2)
for k in range(3):
    for i in range(8):
        vacuum[z[8 * k + i]] = sp.simplify(sp.trace(J[k] * lambdas[i]) / 2)

hessian = sp.hessian(potential, coordinates).subs(vacuum)
spectrum = hessian.eigenvals()
rank = hessian.rank()
nullity = len(coordinates) - rank

gauge_tangents = []
for generator in lambdas:
    vector = []
    for matrix in J:
        delta = I * (generator * matrix - matrix * generator)
        vector.extend([sp.simplify(sp.trace(delta * basis) / 2) for basis in lambdas])
    vector.extend([0] * 5)
    gauge_tangents.append(vector)
flavor_gauge_rank = sp.Matrix(gauge_tangents).T.rank()

ew_tangents = []
for index in range(3):
    vector = [0] * 29
    vector[24 + index] = 1
    ew_tangents.append(vector)
ew_rank = sp.Matrix(ew_tangents).T.rank()

dilation = []
for k in range(3):
    dilation.extend([vacuum[z[8 * k + i]] for i in range(8)])
dilation.extend([vacuum[item] for item in h])
dilation.append(vacuum[sigma])
dilation_vector = sp.Matrix(dilation)

# Canonically normalized flavor-radial, Higgs-radial, and singlet directions.
flavor_radial = sp.Matrix([*dilation[:24], 0, 0, 0, 0, 0]) / sp.sqrt(3)
higgs_radial = sp.Matrix([0] * 27 + [sp.sqrt(2), 0]) / sp.sqrt(2)
singlet_radial = sp.Matrix([0] * 28 + [1])
radial_basis = sp.Matrix.hstack(flavor_radial, higgs_radial, singlet_radial)
radial_block = sp.simplify(radial_basis.T * hessian * radial_basis)
radial_spectrum = radial_block.eigenvals()
radial_projectors = {}
projector_matrices = []
for eigenvalue in sorted(radial_spectrum, key=lambda value: float(sp.N(value))):
    projector = sp.eye(3)
    for other in radial_spectrum:
        if other != eigenvalue:
            projector = sp.simplify(projector * (radial_block - other * sp.eye(3)) / (eigenvalue - other))
    radial_projectors[str(eigenvalue)] = {
        "flavor_radial": str(sp.simplify(projector[0, 0])),
        "higgs_radial": str(sp.simplify(projector[1, 1])),
        "singlet_radial": str(sp.simplify(projector[2, 2])),
    }
    projector_matrices.append(projector)

checks = {
    "potential_is_quartic": sp.Poly(potential, coordinates).total_degree() == 4,
    "vacuum_energy_is_zero": potential.subs(vacuum) == 0,
    "vacuum_is_stationary": all(sp.diff(potential, item).subs(vacuum) == 0 for item in coordinates),
    "flavor_gauge_rank_is_eight": flavor_gauge_rank == 8,
    "electroweak_goldstone_rank_is_three": ew_rank == 3,
    "dilation_is_null": hessian * dilation_vector == sp.zeros(29, 1),
    "nullity_is_twelve": nullity == 12,
    "all_nonzero_modes_positive": all(value > 0 for value in spectrum if value != 0),
    "radial_projectors_are_idempotent": all(sp.simplify(p * p - p) == sp.zeros(3) for p in projector_matrices),
    "radial_projectors_are_orthogonal": all(
        sp.simplify(projector_matrices[i] * projector_matrices[j]) == sp.zeros(3)
        for i in range(len(projector_matrices))
        for j in range(i + 1, len(projector_matrices))
    ),
    "radial_projectors_are_complete": sp.simplify(sum(projector_matrices, sp.zeros(3)) - sp.eye(3)) == sp.zeros(3),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP468",
    "benchmark": {"lambda": 1, "rho": 1, "eta": 1, "y": 1, "a": 1, "sigma": 1},
    "real_field_dimension": len(coordinates),
    "hessian_rank": rank,
    "hessian_nullity": nullity,
    "expected_null_sectors": {
        "flavor_gauge": flavor_gauge_rank,
        "electroweak_goldstone": ew_rank,
        "common_dilation": 1,
    },
    "hessian_spectrum": {str(value): int(multiplicity) for value, multiplicity in spectrum.items()},
    "canonically_normalized_radial_block": [[str(value) for value in row] for row in radial_block.tolist()],
    "radial_diagonal_residues": radial_projectors,
    "instrument": None,
    "remaining_gate": "lift or type the physical massless dilaton, then recompute mass eigenstate vertices and widths before detector composition",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp468_common_dilaton_hessian.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
