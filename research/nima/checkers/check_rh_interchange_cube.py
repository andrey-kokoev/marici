import json
from pathlib import Path


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


identity = ((1, 0), (0, 1))
X = ((0, 1), (1, 0))
Z = ((1, 0), (0, -1))

omega_sc = X
omega_cr = Z
omega_sr = identity

left_route = matmul(matmul(omega_sc, omega_cr), omega_sr)
right_route = matmul(matmul(omega_sr, omega_cr), omega_sc)

assert left_route == scale(-1, right_route)
assert left_route != right_route

# Each comparison is an involutive invertible cell.
assert matmul(omega_sc, omega_sc) == identity
assert matmul(omega_cr, omega_cr) == identity
assert matmul(omega_sr, omega_sr) == identity

result = {
    "source_composition_cell": omega_sc,
    "composition_reciprocity_cell": omega_cr,
    "source_reciprocity_cell": omega_sr,
    "all_pairwise_cells_invertible": True,
    "first_cube_route": left_route,
    "second_cube_route": right_route,
    "cube_residual": "-I",
    "strict_cube_coherence": False,
    "both_crossed_cells_declared_odd": True,
    "expected_koszul_residual": "-I",
    "koszul_normalized_residual": "I",
    "super_cube_coherence": True,
    "scalar_norm_can_forget_residual": True,
    "verdict": "the raw sign requires parity typing; with both cells odd it is canonical super-interchange",
}

output = Path(__file__).parents[1] / "results" / "rh-interchange-cube.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
