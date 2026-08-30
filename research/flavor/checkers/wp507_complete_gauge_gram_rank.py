"""Exact complete coupled gauge-tangent Gram rank for WP507."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp488 = load("wp488_flavor_clock_normalization_correction.json")
wp502 = load("wp502_gauged_entrance_triplet_stabilizer.json")
wp506 = load("wp506_full_doublet_hessian_attempt.json")

I = sp.I
mu, s, a, b = sp.symbols("mu s a b", positive=True)
g_f, g_p, g_e, g_2, g_y = sp.symbols("g_F g_P g_E g_2 g_Y", positive=True)

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
L = [
    sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
    sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
]
pauli = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.diag(1, -1),
]

S0 = s * sp.eye(3)
U0 = sp.zeros(3, 2)
D0 = sp.zeros(3, 2)
U0[2, 1] = a
D0[0, 1] = b


def adjoint_coordinates(matrix):
    return [sp.simplify(sp.trace(matrix * basis) / 2) for basis in lambdas]


def complex_coordinates(matrix):
    expanded = matrix.applyfunc(sp.expand_complex)
    return [sp.simplify(sp.re(value)) for value in expanded] + [
        sp.simplify(sp.im(value)) for value in expanded
    ]


def field_vector(delta_s, delta_x, delta_u, delta_d):
    vector = list(delta_s)
    for matrix in delta_x:
        vector.extend(adjoint_coordinates(matrix))
    vector.extend(complex_coordinates(delta_u))
    vector.extend(complex_coordinates(delta_d))
    return sp.Matrix(vector)


zero_s = sp.zeros(3)
zero_x = [sp.zeros(3) for _ in range(3)]
zero_u = sp.zeros(3, 2)
zero_d = sp.zeros(3, 2)
tangents = []

for generator in lambdas:
    delta_x = [I * g_f * mu * (generator * matrix - matrix * generator) for matrix in J]
    tangents.append(field_vector(zero_s, delta_x, zero_u, zero_d))

for generator in L:
    delta_x = [
        g_p * mu * sum((generator[i, j] * J[j] for j in range(3)), sp.zeros(3))
        for i in range(3)
    ]
    tangents.append(field_vector(-g_p * S0 * generator, delta_x, zero_u, zero_d))

for generator in L:
    tangents.append(
        field_vector(
            g_e * generator * S0,
            zero_x,
            g_e * generator * U0,
            g_e * generator * D0,
        )
    )

for generator in pauli:
    tangents.append(
        field_vector(
            zero_s,
            zero_x,
            I * g_2 * U0 * generator.T / 2,
            I * g_2 * D0 * generator.T / 2,
        )
    )

tangents.append(field_vector(zero_s, zero_x, I * g_y * U0 / 2, I * g_y * D0 / 2))

tangent_matrix = sp.Matrix.hstack(*tangents)
gram = sp.simplify(tangent_matrix.T * tangent_matrix)
flavor_row_block = gram[:14, :14]
electroweak_block = gram[14:, 14:]
cross_block = gram[:14, 14:]

photon = sp.zeros(18, 1)
photon[16] = 1 / g_2
photon[17] = 1 / g_y
gram_nullspace = gram.nullspace()
nullspace_matrix = sp.Matrix.hstack(*gram_nullspace)

v_squared = a**2 + b**2
expected_electroweak_block = v_squared * sp.Matrix(
    [
        [g_2**2 / 4, 0, 0, 0],
        [0, g_2**2 / 4, 0, 0],
        [0, 0, g_2**2 / 4, -g_2 * g_y / 4],
        [0, 0, -g_2 * g_y / 4, g_y**2 / 4],
    ]
)
electroweak_block_difference = (electroweak_block - expected_electroweak_block).applyfunc(sp.simplify)

checks = {
    "wp488_dependency_passed": wp488["passed"],
    "wp502_dependency_passed": wp502["passed"],
    "wp506_dependency_passed": wp506["passed"],
    "generator_count_is_eighteen": tangent_matrix.cols == 18,
    "field_tangent_coordinate_count_is_fifty_seven": tangent_matrix.rows == 57,
    "flavor_port_row_block_has_rank_fourteen": flavor_row_block.rank() == 14,
    "electroweak_block_has_rank_three": electroweak_block.rank() == 3,
    "row_electroweak_cross_block_vanishes_at_real_neutral_vacuum": cross_block == sp.zeros(14, 4),
    "electroweak_block_has_standard_exact_form": electroweak_block_difference == sp.zeros(4),
    "complete_gauge_gram_has_rank_seventeen": gram.rank() == 17,
    "complete_gauge_gram_nullity_is_one": len(gram_nullspace) == 1,
    "declared_photon_is_exact_null_vector": sp.simplify(gram * photon) == sp.zeros(18, 1),
    "declared_photon_spans_full_nullspace": nullspace_matrix.row_join(photon).rank() == 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP507",
    "gauge_group": "SU(3)_F x SO(3)_P x SO(3)_E x SU(2)_L x U(1)_Y",
    "vacuum": "X_i=mu J_i, S=s I_3, U_3=(0,a), D_1=(0,b)",
    "tangent_gram": {
        "field_coordinate_dimension": int(tangent_matrix.rows),
        "generator_count": int(tangent_matrix.cols),
        "rank": int(gram.rank()),
        "nullity": len(gram_nullspace),
        "flavor_port_row_rank": int(flavor_row_block.rank()),
        "electroweak_rank": int(electroweak_block.rank()),
        "row_electroweak_cross_rank": int(cross_block.rank()),
    },
    "photon": {
        "generator_coordinates": "T3/g_2 + Y/g_Y",
        "unique": bool(len(gram_nullspace) == 1),
        "unbroken_stabilizer": "U(1)_em",
    },
    "electroweak_subblock": "(a^2+b^2)/4 times the standard charged diagonal and neutral [[g_2^2,-g_2 g_Y],[-g_2 g_Y,g_Y^2]] block",
    "normalization_scope": "Exact Euclidean tangent-coordinate Gram in the WP484 adjoint/frame convention and direct real-imaginary doublet coordinates. Rank and kernel are invariant; absolute canonical pole normalization must retain the declared kinetic metrics when composed with WP488.",
    "classification": "Exact complete gauge-support and kernel theorem. Seventeen gauge directions are massive and the photon is the unique null direction; numerical pole values remain functions of unselected couplings and vev scales.",
    "selector": False,
    "rigidifier": bool(gram.rank() == 17),
    "instrument": None,
    "smallest_exact_falsifier": "The eighteen-generator tangent Gram has rank seventeen, and its one-dimensional kernel is exactly T3/g_2+Y/g_Y; the fourteen-dimensional flavor-port-row block is nonsingular.",
    "remaining_gate": "Apply the canonical kinetic metric, diagonalize the fourteen massive flavor-port-row poles and three electroweak poles, derive their current residues, and enumerate every scalar, fermion, and vector decay channel before assigning total widths or detector reach.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp507_complete_gauge_gram_rank.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
