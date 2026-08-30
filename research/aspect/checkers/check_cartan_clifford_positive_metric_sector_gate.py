from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


F = Fraction


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def subtract(left, right):
    return [[x - y for x, y in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def determinant2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def serialize(matrix):
    return [[str(value) for value in row] for row in matrix]


def clifford_generator(a):
    return [[F(0), F(a)], [F(1), F(0)]]


def metric(x, y, a):
    return [[F(x), F(y)], [F(y), F(a) * F(x)]]


def metric_selfadjoint_residual(c, h):
    return subtract(multiply(h, c), multiply(transpose(c), h))


def main():
    positive_a = F(4)
    negative_a = F(-4)
    seam_a = F(0)

    c_positive = clifford_generator(positive_a)
    h_positive = metric(1, 0, positive_a)
    assert metric_selfadjoint_residual(c_positive, h_positive) == [[0, 0], [0, 0]]
    assert h_positive[0][0] > 0 and determinant2(h_positive) > 0

    # H=S^T S with S=diag(1,2); the conjugated carrier is symmetric.
    s = [[F(1), F(0)], [F(0), F(2)]]
    s_inverse = [[F(1), F(0)], [F(0), F(1, 2)]]
    positive_symmetric_carrier = multiply(multiply(s, c_positive), s_inverse)
    assert positive_symmetric_carrier == [[0, 2], [2, 0]]
    assert positive_symmetric_carrier == transpose(positive_symmetric_carrier)

    h_negative = metric(1, 0, negative_a)
    assert metric_selfadjoint_residual(clifford_generator(negative_a), h_negative) == [[0, 0], [0, 0]]
    assert determinant2(h_negative) < 0

    h_seam = metric(1, 0, seam_a)
    assert metric_selfadjoint_residual(clifford_generator(seam_a), h_seam) == [[0, 0], [0, 0]]
    assert determinant2(h_seam) == 0

    # For every symmetric H=[[x,y],[y,z]], HC=C^T H forces z=a*x.
    # Its determinant is a*x^2-y^2, hence positivity implies a>0.
    sample_failures = []
    for a in (F(-4), F(-1), F(0)):
        for x in (F(1), F(2), F(3)):
            for y in (F(-2), F(-1), F(0), F(1), F(2)):
                h = metric(x, y, a)
                assert metric_selfadjoint_residual(clifford_generator(a), h) == [[0, 0], [0, 0]]
                if determinant2(h) > 0:
                    sample_failures.append((a, x, y))
    assert sample_failures == []

    # Collocated Weyl bridge for the positive representative A=[[0,2],[2,0]],
    # v=e0. det(A-zI)=z^2-4 and m(z)=-z/(z^2-4), so the bordered
    # determinant numerator is z.
    result = {
        "schema": "marici.aspect.cartan-clifford-positive-metric-sector-gate.v1",
        "status": "pass",
        "metric_equation": {
            "carrier": "C_a = [[0,a],[1,0]]",
            "general_symmetric_metric": "H = [[x,y],[y,z]]",
            "selfadjointness_condition": "z = a*x",
            "metric_determinant": "a*x^2 - y^2",
            "positive_metric_iff": "a > 0",
        },
        "positive_sector": {
            "a": "4",
            "metric": serialize(h_positive),
            "metric_determinant": str(determinant2(h_positive)),
            "orthonormal_carrier": serialize(positive_symmetric_carrier),
            "collocated_weyl_denominator": "z^2 - 4",
            "collocated_weyl_coefficient": "-z/(z^2 - 4)",
            "bordered_numerator": "z",
        },
        "negative_sector": {
            "a": "-4",
            "metric": serialize(h_negative),
            "metric_determinant": str(determinant2(h_negative)),
            "classification": "indefinite Krein realization only",
        },
        "seam": {
            "a": "0",
            "metric": serialize(h_seam),
            "metric_determinant": "0",
            "classification": "degenerate metric; no uniform positive similarity through the seam",
        },
        "optical_consequence": {
            "passive_reciprocal_pair": "forward-return product is |g|^2 and therefore nonnegative",
            "two_sector_requirement": "negative a needs an active, non-Hermitian, or indefinite-metric realization",
            "forbidden_inference": "one positive collocated Weyl model extends across both half-sectors",
        },
        "claim_boundary": "exact finite two-mode metric and bordered-determinant gate; no source derivation, infinite completion, or theta determinant identification",
    }
    output = Path(__file__).parents[1] / "results" / "cartan_clifford_positive_metric_sector_gate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
