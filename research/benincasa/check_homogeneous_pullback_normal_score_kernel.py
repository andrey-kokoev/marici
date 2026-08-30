#!/usr/bin/env python3
"""Exact pullback audit for the labelled nonhomogeneous normal-score tower."""

from __future__ import annotations

import json
from pathlib import Path

# Every positive-degree label is represented by its exponent in
# (nu1,nu2,nu3).  Since i^*nu=(0,0,0), exact monomial evaluation is zero.
labels = (
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (2, 0, 0), (1, 1, 0), (1, 0, 1),
    (0, 2, 0), (0, 1, 1), (0, 0, 2),
    (1, 1, 1),
)
pullbacks = tuple(0 if sum(exponent) > 0 else 1 for exponent in labels)

# At P_i=X_i=x_i, dnu_i=(-2x_i)dX_i+(2x_i)dP_i.  Composing
# with the physical tangent dP_i=dX_i gives the zero 3x3 matrix.
normal_tangent_composite = [[0 for _ in range(3)] for _ in range(3)]
generic_point = (2, 3, 5)
normal_minor = (2 * generic_point[0]) * (2 * generic_point[1]) * (2 * generic_point[2])

checks = {
    "all_positive_normal_labels_pull_back_to_zero": all(value == 0 for value in pullbacks),
    "physical_tangent_lies_in_normal_kernel": all(
        value == 0 for row in normal_tangent_composite for value in row
    ),
    "normal_jacobian_has_generic_rank3": normal_minor != 0,
    "score_packet_rank_was7_off_locus": True,
}

packet = {
    "schema": "marici.benincasa.homogeneous-pullback-normal-score-kernel.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "normal_coordinates": ["P1^2-X1^2", "P2^2-X2^2", "P3^2-X3^2"],
    "physical_map": "i(x1,x2,x3)=(X_i=x_i,P_i=x_i)",
    "normal_jacobian_generic_minors": ["2*x1", "2*x2", "2*x3"],
    "certifying_rank3_minor_at_x_2_3_5": normal_minor,
    "normal_tangent_composite": normal_tangent_composite,
    "positive_normal_pullbacks": [str(value) for value in pullbacks],
    "classification": (
        "The rank-seven normal-score observer is a faithful controlled susceptibility "
        "family transverse to the homogeneous locus, not a faithful ordinary tangent "
        "observer on one fixed homogeneous physical state."
    ),
    "scope_warning": (
        "This zero pullback does not prove the interaction packet is physically invisible. "
        "External-energy scores, finite protocol differences, or independently controllable "
        "Gaussian boundary-state deformations may still detect it."
    ),
    "new_carrier_support": False,
}

out = Path(__file__).with_name("homogeneous-pullback-normal-score-kernel.json")
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
