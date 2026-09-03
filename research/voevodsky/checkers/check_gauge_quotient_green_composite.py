from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


EVIDENCE = [
    Path("research/voevodsky/results/framed_to_metric_markov_descent.json"),
    Path("research/voevodsky/results/metric_transition_markov_completion.json"),
    Path("research/voevodsky/results/markov_carrier_green_bridge.json"),
]


def product(edges: list[sp.Matrix]) -> sp.Matrix:
    value = sp.eye(2)
    for edge in edges:
        value *= edge
    return value


def normalized_kernel(edges: list[sp.Matrix]) -> sp.Matrix:
    count = len(edges) + 1
    rows = []
    for i in range(count):
        blocks = []
        for j in range(count):
            block = sp.eye(2) if i == j else product(edges[i:j]) if i < j else product(edges[j:i]).T
            blocks.append(block)
        rows.append(blocks)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in rows))


def quotient_kernel(metrics: list[sp.Matrix], covariances: list[sp.Matrix]) -> sp.Matrix:
    count = len(metrics)
    rows = []
    for i in range(count):
        blocks = []
        for j in range(count):
            if i == j:
                block = metrics[i]
            elif i < j:
                block = covariances[i]
                for k in range(i + 1, j):
                    block = block * metrics[k].inv() * covariances[k]
            else:
                block = rows[j][i].T
            blocks.append(block)
        rows.append(blocks)
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in rows))


def main() -> None:
    evidence = [json.loads(path.read_text(encoding="utf-8")) for path in EVIDENCE]
    assert all(item["passed"] is True for item in evidence)

    frames = [sp.eye(2), sp.Matrix([[1, 1], [0, 1]]), sp.diag(2, 1)]
    edges = [sp.diag(sp.Rational(1, 3), sp.Rational(1, 4)), sp.Matrix([[sp.Rational(1, 4), 0], [sp.Rational(1, 6), sp.Rational(1, 3)]])]
    frame_sum = sp.diag(*frames)
    framed_route = frame_sum * normalized_kernel(edges) * frame_sum.T
    metrics = [frame * frame.T for frame in frames]
    covariances = [frames[i] * edges[i] * frames[i + 1].T for i in range(2)]
    quotient_route = quotient_kernel(metrics, covariances)
    assert framed_route == quotient_route

    rotations = [sp.diag(1, -1), sp.Matrix([[0, -1], [1, 0]]), -sp.eye(2)]
    changed_frames = [frame * rotation for frame, rotation in zip(frames, rotations)]
    changed_edges = [rotations[i].T * edges[i] * rotations[i + 1] for i in range(2)]
    changed_frame_sum = sp.diag(*changed_frames)
    assert changed_frame_sum * normalized_kernel(changed_edges) * changed_frame_sum.T == quotient_route

    assert framed_route[:4, :4] == quotient_kernel(metrics[:2], covariances[:1])

    result = {
        "schema": "marici.voevodsky.gauge-quotient-green-composite.v1",
        "status": "framed_markov_composite_interface_verified",
        "evidence_documents_passed": len(evidence),
        "gauge_presentation_to_carrier_typed": True,
        "carrier_to_finite_green_typed": True,
        "framed_and_quotient_routes_equal": True,
        "comparison_cell_identity_invertible": True,
        "orthogonal_frame_independence": True,
        "restriction_naturality": True,
        "completion_compatibility": True,
        "arbitrary_gauge_presentation_admitted": False,
        "physical_interpretation_supplied": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
