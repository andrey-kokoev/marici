import json
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/three-prime-permutohedral-braid.json"

length = {"p": 1, "q": 2, "r": 4}
labels = tuple(length)
total = sum(length.values())


def partition_matrix(word):
    rows = []
    start = 0
    for a in word:
        end = start + length[a]
        rows.append([Q(1) if start <= j < end else Q(0) for j in range(total)])
        start = end
    return rows


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def swap(word, i):
    w = list(word)
    w[i], w[i+1] = w[i+1], w[i]
    return tuple(w)


def enc(a):
    return [[str(x) for x in row] for row in a]

P = {w: partition_matrix(w) for w in permutations(labels)}
start = ("p", "q", "r")
path_left = [start]
for i in (0, 1, 0):
    path_left.append(swap(path_left[-1], i))
path_right = [start]
for i in (1, 0, 1):
    path_right.append(swap(path_right[-1], i))
# Source transport on the seven atomic unit intervals is identity; every vertex
# readout is obtained by reaggregation P_w after retaining that common source.
x = [[Q(0)], [Q(1)], [Q(-1)]] + [[Q(0)] for _ in range(total-3)]
initial = mm(P[start], x)
first_swapped = mm(P[path_left[1]], x)
checks = {
    "both_braid_words_have_same_endpoint": path_left[-1] == path_right[-1] == ("r", "q", "p"),
    "braid_transport_agrees_on_common_atomic_carrier": P[path_left[-1]] == P[path_right[-1]],
    "every_vertex_preserves_total_interval": all([sum(row[j] for row in P[w]) for j in range(total)] == [Q(1)]*total for w in P),
    "three_port_initial_packet_has_hidden_refinement_kernel": initial == [[Q(0)], [Q(0)], [Q(0)]],
    "adjacent_order_detects_hidden_ratio_content": first_swapped != [[Q(0)], [Q(0)], [Q(0)]],
}
assert all(checks.values()), checks
result = {
    "schema": "marici.nima.three-prime-permutohedral-braid.v1",
    "claim_strength": "finite-cutoff source-typed braid coherence",
    "source_operation": "reaggregation of one retained common interval refinement",
    "length_fixture": length,
    "left_braid_path": ["".join(w) for w in path_left],
    "right_braid_path": ["".join(w) for w in path_right],
    "endpoint_matrix": enc(P[path_left[-1]]),
    "checks": checks,
    "hostile": {
        "atomic_state": [str(v[0]) for v in x],
        "initial_readout": [str(v[0]) for v in initial],
        "first_swapped_readout": [str(v[0]) for v in first_swapped],
        "disposition": "three-port quotient_before_transport_rejected",
    },
    "unsupported": ["determinant-line image of ratio faces", "order-three anomaly comparison", "all-prime completion"],
    "passed": True,
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
