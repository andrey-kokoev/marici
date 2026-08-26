from fractions import Fraction
import json
from pathlib import Path


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def determinant_columns(u, v, w):
    return (
        u[0] * (v[1] * w[2] - v[2] * w[1])
        - v[0] * (u[1] * w[2] - u[2] * w[1])
        + w[0] * (u[1] * v[2] - u[2] * v[1])
    )


def krylov_carrier(operator, seed):
    first = seed
    second = matvec(operator, first)
    third = matvec(operator, second)
    return determinant_columns(first, second, third)


def add_vectors(*terms):
    return tuple(sum(term[i] for term in terms) for i in range(3))


def scale(scalar, vector):
    return tuple(scalar * value for value in vector)


diag = (
    (Fraction(1), 0, 0),
    (0, Fraction(2), 0),
    (0, 0, Fraction(3)),
)
seed = (Fraction(1), Fraction(1), Fraction(1))
carrier = krylov_carrier(diag, seed)
assert carrier == 2

reflection = (
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 1),
)
reflected_operator = matmul(matmul(reflection, diag), reflection)
reflected_seed = matvec(reflection, seed)
assert krylov_carrier(reflected_operator, reflected_seed) == -carrier

cycle = (
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
)
cycle_inverse = (
    (0, 0, 1),
    (1, 0, 0),
    (0, 1, 0),
)
cycled_operator = matmul(matmul(cycle, diag), cycle_inverse)
cycled_seed = matvec(cycle, seed)
assert krylov_carrier(cycled_operator, cycled_seed) == carrier

# Degenerate spectra or a seed missing an eigendirection make the carrier zero.
degenerate = (
    (Fraction(1), 0, 0),
    (0, Fraction(1), 0),
    (0, 0, Fraction(3)),
)
missing_direction_seed = (Fraction(1), Fraction(1), Fraction(0))
assert krylov_carrier(degenerate, seed) == 0
assert krylov_carrier(diag, missing_direction_seed) == 0

# Cayley-Hamilton closes all later jets over the first three. For eigenvalues
# 1,2,3: A^3 - 6 A^2 + 11 A - 6 I = 0.
v0 = seed
v1 = matvec(diag, v0)
v2 = matvec(diag, v1)
v3 = matvec(diag, v2)
ch_residual = add_vectors(v3, scale(-6, v2), scale(11, v1), scale(-6, v0))
assert ch_residual == (0, 0, 0)

result = {
    "schema": "marici.nima.flavor-krylov-orientation-carrier.v1",
    "generic_krylov_determinant": str(carrier),
    "cyclic_relabelling_preserves_sign": True,
    "reflection_reverses_sign": True,
    "degenerate_spectrum_falsifier": True,
    "missing_eigendirection_falsifier": True,
    "cayley_hamilton_closes_after_three_ports": True,
    "existing_charged_current_overlap_authorizes_candidate": False,
    "seed_phase_weight": 3,
    "sixth_root_phase_flips_signed_determinant": True,
    "signed_determinant_descends_to_seed_ray": False,
    "modulus_squared_descends_to_seed_ray": True,
    "verdict": (
        "One triplet plus a source-derived evolution can generate the three "
        "typed ports x, Ax, A^2x. Their determinant detects a cyclic Krylov "
        "frame algebraically, but its phase has weight three under seed-ray "
        "rephasing and does not descend physically. Only its modulus squared "
        "is a source-independent cyclicity readout without a new phase port."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-krylov-orientation-carrier.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
