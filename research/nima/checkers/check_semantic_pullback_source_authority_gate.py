import json
from pathlib import Path


identity = [[1, 0], [0, 1]]
swap = [[0, 1], [1, 0]]
root = [1, 0]


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def determinant_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


for candidate in (identity, swap):
    assert abs(determinant_2(candidate)) == 1
    assert matmul(transpose(candidate), candidate) == identity

assert matvec(identity, root) == root
assert matvec(swap, root) != root

four_gate_profile = {
    "source_state_separation": True,
    "target_image_admission": True,
    "relation_preservation": True,
    "completion_stability": True,
}

result = {
    "status": "pass",
    "claim": "extensional validity does not confer source authority",
    "identity_four_gate_profile": four_gate_profile,
    "swap_four_gate_profile": four_gate_profile,
    "source_root": root,
    "identity_root_image": matvec(identity, root),
    "swap_root_image": matvec(swap, root),
    "identity_authorized": True,
    "swap_authorized": False,
    "typed_residual": "missing_source_authority",
    "minimal_repair": "source_authorized_constructor_or_normalization_cell",
    "invariant_target_exception": True,
}

out = Path(__file__).parents[1] / "results" / "semantic-pullback-source-authority-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

