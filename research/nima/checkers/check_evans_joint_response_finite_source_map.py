import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/evans-joint-response-finite-source-map.json"


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def stack(a, b):
    return a + b


def rank(a):
    m = [row[:] for row in a]
    rows, cols, r = len(m), len(m[0]), 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        d = m[r][c]
        m[r] = [x / d for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                f = m[i][c]
                m[i] = [m[i][j] - f * m[r][j] for j in range(cols)]
        r += 1
    return r


def enc(a):
    return [[str(x) for x in row] for row in a]


# Fixed forcing vector phi=(1,2).  C is a finite correlation fixture.
C = [[Q(1), Q(2)], [Q(2), Q(1)]]
# u -> phi tensor u, ordered (phi_1 u_1, phi_2 u_1, phi_1 u_2, phi_2 u_2).
T = [[Q(1), Q(0)], [Q(2), Q(0)], [Q(0), Q(1)], [Q(0), Q(2)]]
J = stack(C, T)
S = [[Q(0), Q(1)], [Q(1), Q(0)]]
# Transport on separation and tensor legs, derived by conjugation / block swap.
Cinv = [[Q(-1, 3), Q(2, 3)], [Q(2, 3), Q(-1, 3)]]
Ssep = matmul(matmul(C, S), Cinv)
Stensor = [[Q(0), Q(0), Q(1), Q(0)],
           [Q(0), Q(0), Q(0), Q(1)],
           [Q(1), Q(0), Q(0), Q(0)],
           [Q(0), Q(1), Q(0), Q(0)]]
R = [[Q(0) for _ in range(6)] for _ in range(6)]
for i in range(2):
    for j in range(2):
        R[i][j] = Ssep[i][j]
for i in range(4):
    for j in range(4):
        R[i + 2][j + 2] = Stensor[i][j]

# Fixed-marginal hostile: reverse only the tensor leg.  Component Gramians are
# unchanged, but it is not the graph of the declared joint source operation.
J_hostile = stack(C, [[-x for x in row] for row in T])
hostile_residual = [[J_hostile[i][j] - J[i][j] for j in range(2)] for i in range(6)]

checks = {
    "both_response_coordinates_retained": len(J) == 6,
    "haar_tensor_leg_is_injective": rank(T) == 2,
    "joint_source_map_is_injective": rank(J) == 2,
    "translation_transport_intertwines": matmul(R, J) == matmul(J, S),
    "translation_composition_closes": matmul(S, S) == [[Q(1), Q(0)], [Q(0), Q(1)]],
    "fixed_marginal_hostile_preserves_component_ranks": rank(C) == rank(J_hostile[:2]) and rank(T) == rank(J_hostile[2:]),
    "fixed_marginal_hostile_has_nonzero_joint_residual": any(x for row in hostile_residual for x in row),
}
assert all(checks.values()), checks

result = {
    "schema": "marici.nima.evans-joint-response-finite-source-map.v1",
    "claim_strength": "finite-cutoff source-realization fixture",
    "source_operation": "fixed-forcing correlation paired with the based tensor embedding",
    "matrices": {"correlation": enc(C), "tensor": enc(T), "joint": enc(J), "source_transport": enc(S), "joint_transport": enc(R)},
    "checks": checks,
    "hostile": {
        "kind": "fixed_marginals_changed_cross_coupling",
        "joint_residual": enc(hostile_residual),
        "disposition": "rejected_by_based_graph_relation",
    },
    "unsupported": [
        "endpoint-Euler-archimedean determinant-line clutching",
        "cutoff completion",
        "determinant monodromy",
        "relative-Haar energy-cycle vanishing",
    ],
    "passed": True,
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"checks": checks, "unsupported": result["unsupported"], "passed": True}, indent=2))
