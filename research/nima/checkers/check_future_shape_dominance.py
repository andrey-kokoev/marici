"""Exact countermodel to physical-weight monotonicity under future-shape dominance."""

import json
from pathlib import Path
import sympy as sp


# Finite depth-indexed extension towers. Restriction maps point toward depth 0.
A = {
    0: {"A"},
    1: {"a0", "a1"},
    2: {"a00", "a10"},
}
B = {
    0: {"B"},
    1: {"b0"},
    2: {"b00"},
}
A_res = {1: {"a0": "A", "a1": "A"}, 2: {"a00": "a0", "a10": "a1"}}
B_res = {1: {"b0": "B"}, 2: {"b00": "b0"}}
eta = {0: {"B": "A"}, 1: {"b0": "a0"}, 2: {"b00": "a00"}}

# Naturality and injectivity of B -> A at every depth.
for depth in (0, 1, 2):
    assert set(eta[depth]) == B[depth]
    assert len(set(eta[depth].values())) == len(B[depth])
    assert set(eta[depth].values()) <= A[depth]
for depth in (1, 2):
    for b in B[depth]:
        assert A_res[depth][eta[depth][b]] == eta[depth-1][B_res[depth][b]]
assert len(A[1]) > len(B[1]) and len(A[2]) > len(B[2])

# Exact normalized preparation: the strictly dominant A alternative has lower
# source weight than B.
psi = sp.Matrix([1/sp.sqrt(10), 3/sp.sqrt(10)])
weights = [sp.simplify(v**2) for v in psi]
assert sum(weights) == 1
assert weights == [sp.Rational(1, 10), sp.Rational(9, 10)]

# Lawful isometric future channel. A reaches record labels r0 and r1; B reaches
# r0 only, with an orthogonal environment tag preserving isometry.
V = sp.Matrix([
    [1/sp.sqrt(2), 0],
    [1/sp.sqrt(2), 0],
    [0, 1],
])
assert sp.simplify(V.T*V) == sp.eye(2)

# Joint present-alternative / future-record table after forgetting environment.
P = sp.Matrix([
    [sp.Rational(1, 20), sp.Rational(1, 20)],  # A -> r0,r1
    [sp.Rational(9, 10), 0],                   # B -> r0
])
assert sum(P) == 1
dependence_minor = sp.factor(P.det())
assert dependence_minor != 0  # r1 is connected to A, not spectator noise.

result = {
    "status": "PASS",
    "tower_cardinalities_A": [len(A[d]) for d in range(3)],
    "tower_cardinalities_B": [len(B[d]) for d in range(3)],
    "natural_embedding_B_into_A": True,
    "strict_dominance": True,
    "source_weights": {"A": str(weights[0]), "B": str(weights[1])},
    "isometry_residual": [[str(v) for v in row] for row in (V.T*V-sp.eye(2)).tolist()],
    "joint_dependence_minor": str(dependence_minor),
    "dominance_weight_monotonicity": False,
    "conclusion": (
        "A has a strictly larger, naturally embedded and causally connected "
        "future-extension tower, yet a valid normalized positive preparation "
        "assigns it lower source weight. Future-shape dominance does not force "
        "weight monotonicity in the admitted state/effect calculus."
    ),
}
out = Path(__file__).parents[1] / "results" / "future_shape_dominance.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
