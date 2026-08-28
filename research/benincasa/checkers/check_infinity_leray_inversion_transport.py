#!/usr/bin/env python3
"""Audit source-inversion transport of the infinity Gysin Leray covector.

This is a dependency-free exact rational checker.  It distinguishes the
source-normalized horizontal covector from the nonnatural rule that copies
the coordinate row (1,1) into every occurrence chart.
"""
from fractions import Fraction
import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def rowmul(row, matrix):
    return [
        sum((row[k] * matrix[k][j] for k in range(len(row))), Fraction(0))
        for j in range(len(matrix[0]))
    ]


def gysin(x2, y2, e2):
    A = (e2 + y2) / 2
    B = (e2 + x2) / 2
    return [
        [Fraction(1), A, B],
        [Fraction(0), -B, -x2 * A / y2],
    ]


def encode(values):
    return [[str(x) for x in row] for row in values]


samples = [
    # x,y,z = 3,4,5 and its source-inverted occurrence chart.
    (Fraction(9), Fraction(16), Fraction(144)),
    # x,y,z = 5,12,13 with a generic independent total-energy square.
    (Fraction(25), Fraction(144), Fraction(289)),
]

sample_packets = []
all_transport = True
all_covector = True
all_constant_fail = True

for x2, y2, e2 in samples:
    source = gysin(x2, y2, e2)
    target = gysin(y2, x2, e2)
    swap_marks = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(1), Fraction(0)],
    ]
    target_swapped = matmul(target, swap_marks)

    basis_transport = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), y2 / x2],
    ]
    transported_source = matmul(basis_transport, source)
    transport_ok = transported_source == target_swapped

    source_period = [Fraction(1), Fraction(1)]
    target_period = [Fraction(1), x2 / y2]
    source_leray = rowmul(source_period, source)
    target_leray = rowmul(target_period, target_swapped)
    covector_ok = source_leray == target_leray

    copied_target_leray = rowmul([Fraction(1), Fraction(1)], target_swapped)
    copied_constant_fails = copied_target_leray != source_leray

    all_transport &= transport_ok
    all_covector &= covector_ok
    all_constant_fail &= copied_constant_fails
    sample_packets.append({
        "x_squared": str(x2),
        "y_squared": str(y2),
        "E_squared": str(e2),
        "basis_transport": encode(basis_transport),
        "source_leray_covector": [str(v) for v in source_leray],
        "transported_target_period_covector": [str(v) for v in target_period],
        "transported_target_leray_covector": [str(v) for v in target_leray],
        "copied_constant_target_leray_covector": [
            str(v) for v in copied_target_leray
        ],
        "gysin_square_commutes": transport_ok,
        "contragredient_covector_transport_holds": covector_ok,
        "constant_coordinate_copy_fails": copied_constant_fails,
    })

# The symbolic identities used above are:
# M(y,x) P = diag(1,y^2/x^2) M(x,y),
# (1,x^2/y^2) diag(1,y^2/x^2) = (1,1).
checks = {
    "gysin_square_commutes_at_both_exact_samples": all_transport,
    "source_leray_covector_transports_contragrediently": all_covector,
    "constant_coordinate_copy_is_falsified_at_both_samples": all_constant_fail,
    "samples_are_nonsymmetric": all(x2 != y2 for x2, y2, _ in samples),
}
if not all(checks.values()):
    raise SystemExit(
        "failed checks: " + repr([name for name, passed in checks.items() if not passed])
    )

packet = {
    "schema": "marici.infinity_leray_inversion_transport.v1",
    "source_inversion": "(x,y;a,b) -> (y,x;b,a)",
    "master_transport": "e7 fixed; e8 and e9 exchanged",
    "elliptic_basis_transport": "diag(1,y^2/x^2)",
    "period_covector_transport": "(1,1) -> (1,x^2/y^2)",
    "symbolic_transport_identity":
        "M(y,x) P = diag(1,y^2/x^2) M(x,y)",
    "symbolic_dual_identity":
        "(1,x^2/y^2) diag(1,y^2/x^2) = (1,1)",
    "samples": sample_packets,
    "checks": checks,
    "passed": True,
    "conclusion": (
        "The source-normalized infinity Leray covector is a transported dual "
        "section, not a chartwise constant coordinate row.  The explicit "
        "Gysin quotient is occurrence-natural after contragredient period "
        "transport; copying (1,1) into the inverted chart is nonnatural."
    ),
    "scope": (
        "This proves occurrence covariance of the explicit final-four Gysin "
        "readout.  It does not yet extend the covector to the full rank-26 "
        "marked-relative module or construct the physical rank-26 period."
    ),
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "infinity-leray-inversion-transport.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
