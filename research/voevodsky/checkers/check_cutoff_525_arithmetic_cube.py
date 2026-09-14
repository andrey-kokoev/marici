#!/usr/bin/env python3
"""Exact square and cube decomposition at the first one-probe rank step."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/voevodsky/the_cutoff_525_probe_rank_step_is_a_completed_arithmetic_cube.md"
RESULT = ROOT / "research/voevodsky/results/cutoff_525_arithmetic_cube.json"


def primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for q in range(p * p, n + 1, p):
                sieve[q] = False
    return [i for i, value in enumerate(sieve) if value]


def structure(cutoff):
    ps = primes(cutoff // 2 + 2)
    edges = []
    for shell, (p, q) in enumerate(zip(ps, ps[1:]), 1):
        for k in range(1, cutoff // (p * q) + 1):
            edges.append((k * p * q, shell, k, k * p, k * q, p, q))
    edges.sort()
    vertices = sorted({e[3] for e in edges} | {e[4] for e in edges})
    vi = {v: i for i, v in enumerate(vertices)}
    ei = {(e[3], e[4], e[1]): i for i, e in enumerate(edges)}
    boundary = s.zeros(len(vertices), len(edges))
    for col, edge in enumerate(edges):
        boundary[vi[edge[3]], col] = -1
        boundary[vi[edge[4]], col] = 1
    squares, metadata = [], []
    outgoing = {}
    for edge in edges:
        outgoing[(edge[3], edge[1])] = edge
    for source in vertices:
        available = [edge for edge in edges if edge[3] == source]
        for ai, first in enumerate(available):
            for second in available[ai + 1:]:
                if first[1] == second[1]:
                    continue
                upper_second = outgoing.get((first[4], second[1]))
                upper_first = outgoing.get((second[4], first[1]))
                if upper_second and upper_first and upper_second[4] == upper_first[4]:
                    target = upper_second[4]
                    vector = s.zeros(len(edges), 1)
                    indices = [
                        ei[(source, first[4], first[1])],
                        ei[(first[4], target, second[1])],
                        ei[(source, second[4], second[1])],
                        ei[(second[4], target, first[1])],
                    ]
                    vector[indices[0]] = vector[indices[1]] = 1
                    vector[indices[2]] = vector[indices[3]] = -1
                    squares.append(vector)
                    metadata.append((source, target, first[1], second[1], indices))
    square_matrix = s.Matrix.hstack(*squares) if squares else s.zeros(len(edges), 0)
    return edges, vertices, boundary, square_matrix, metadata


def keyed(metadata, source, target, shell_a, shell_b):
    for index, item in enumerate(metadata):
        if item[:4] == (source, target, shell_a, shell_b):
            return index
    raise KeyError((source, target, shell_a, shell_b))


data = {}
checks = {}
for cutoff in (522, 525):
    edges, vertices, boundary, squares, metadata = structure(cutoff)
    weights = s.diag(*[s.Rational(5, 6) ** edge[1] for edge in edges])
    joint = boundary.col_join(boundary * weights)
    cycles = len(edges) - boundary.rank()
    blind = joint.nullspace()
    square_rank = squares.rank()
    data[cutoff] = (edges, vertices, boundary, weights, squares, metadata, blind)
    checks[f"squares_are_cycles_{cutoff}"] = boundary * squares == s.zeros(boundary.rows, squares.cols)
    checks[f"squares_span_cycles_{cutoff}"] = square_rank == cycles
    checks[f"blind_dimension_{cutoff}"] = len(blind) == (0 if cutoff == 522 else 1)
    checks[f"square_count_{cutoff}"] = squares.cols == (21 if cutoff == 522 else 23)
    checks[f"square_rank_{cutoff}"] = square_rank == (21 if cutoff == 522 else 22)

edges, vertices, boundary, weights, squares, metadata, blind = data[525]
z = blind[0]
relation = squares.nullspace()[0]
expected_faces = {
    (30, 75, 1, 2): s.Integer(1),
    (30, 63, 1, 3): s.Integer(-1),
    (30, 70, 2, 3): s.Integer(1),
    (42, 105, 1, 2): s.Integer(-1),
    (45, 105, 2, 3): s.Integer(-1),
    (50, 105, 1, 3): s.Integer(1),
}
actual_relation = {metadata[i][:4]: relation[i] for i in range(squares.cols) if relation[i]}
checks["unique_six_face_relation"] = squares.cols - squares.rank() == 1 and actual_relation == expected_faces
checks["cube_vertices_exact"] = {30, 42, 45, 50, 63, 70, 75, 105}.issubset(set(vertices))

expected_decomposition = {
    (30, 75, 1, 2): s.Rational(5, 6),
    (30, 70, 2, 3): s.Integer(-1),
    (42, 105, 1, 2): s.Rational(-5, 6),
    (45, 105, 2, 3): s.Integer(1),
}
reconstructed = s.zeros(len(edges), 1)
for face, coefficient in expected_decomposition.items():
    reconstructed += coefficient * squares[:, keyed(metadata, *face)]
checks["blind_cycle_four_face_decomposition"] = reconstructed == z or reconstructed == -z
checks["blind_cycle_twelve_edge_support"] = sum(1 for value in z if value) == 12
checks["blind_cycle_ordinary_cancellation"] = boundary * z == s.zeros(boundary.rows, 1)
checks["blind_cycle_modulated_cancellation"] = boundary * weights * z == s.zeros(boundary.rows, 1)

new_edges = [edge for edge in edges if edge[0] == 525]
checks["grade_525_edges"] = [(e[1], e[3], e[4]) for e in new_edges] == [(2, 105, 175), (3, 75, 105)]
text = PACKET.read_text()
checks["finite_cubical_boundary_stated"] = "finite 1-skeletal cubical model" in text
checks["physical_nonpromotion_stated"] = "supplies no physical realization" in text
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "schema": "marici.voevodsky.cutoff-525-arithmetic-cube.v1",
    "packet_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest(),
    "checks": checks,
    "passed": all(checks.values()),
    "transition": {
        "522": {"edges": 148, "vertices": 165, "cycle_dimension": 21, "square_count": 21, "square_rank": 21, "blind_dimension": 0},
        "525": {"edges": 150, "vertices": 166, "cycle_dimension": 22, "square_count": 23, "square_rank": 22, "blind_dimension": 1},
    },
    "cube": {
        "source": 30,
        "target": 105,
        "vertices": [30, 42, 45, 50, 63, 70, 75, 105],
        "shells": [[2, 3], [3, 5], [5, 7]],
        "face_relation": [{"source": a, "target": b, "shell_pair": [i, j], "coefficient": str(c)} for (a, b, i, j), c in expected_faces.items()],
    },
    "blind_cycle": {
        "setting": "5/6",
        "edge_support_size": 12,
        "square_support_size": 4,
        "square_decomposition": [{"source": a, "target": b, "shell_pair": [i, j], "coefficient": str(c)} for (a, b, i, j), c in expected_decomposition.items()],
    },
    "disposition": "the first one-probe rank defect is a square-generated cycle organized by one arithmetic cube boundary relation",
}
RESULT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"passed": result["passed"], "checks": len(checks), "square_rank_step": [21, 22], "cube_relation_dimension": 1}))
raise SystemExit(0 if result["passed"] else 1)
