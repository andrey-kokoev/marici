import json
from pathlib import Path


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def scale(value, matrix):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


identity = ((1, 0), (0, 1))
X = ((0, 1), (1, 0))
Z = ((1, 0), (0, -1))

assert matmul(X, X) == identity
assert matmul(Z, Z) == identity

xz = matmul(X, Z)
zx = matmul(Z, X)
assert xz == scale(-1, zx)
assert xz != zx

# A scalar projection that forgets central sign cannot distinguish the two
# projective composites by absolute quadratic norm.
probe = (1, 0)


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


def norm_squared(vector):
    return sum(entry * entry for entry in vector)


assert norm_squared(matvec(xz, probe)) == norm_squared(matvec(zx, probe))

result = {
    "abstract_relations": ["p^2=1", "q^2=1", "pq=qp"],
    "source_realization_p": X,
    "source_realization_q": Z,
    "individual_involutions_valid": True,
    "realized_pq": xz,
    "realized_qp": zx,
    "mixed_interchange_phase": -1,
    "strict_interchange_valid": False,
    "scalar_norm_projection_detects_failure": False,
    "verdict": "forward composition and source realization require an independent mixed interchange cell",
}

output = Path(__file__).parents[1] / "results" / "rh-two-tower-interchange.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

