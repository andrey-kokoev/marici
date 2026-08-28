#!/usr/bin/env python3
"""Flat mixed transport does not force a distinguished line to be horizontal."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "aspect" / "results" / "flat_mixed_cell_nonhorizontal_line_hostile.json"

# V=<b,q_x,q_y>, with distinguished Bockstein line L=<b>.
# A_x(b)=q_x and A_y(b)=q_y; both operators kill the quotient plane.
AX = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
AY = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


curvature = sub(mul(AX, AY), mul(AY, AX))
b = [1, 0, 0]
ax_b = [sum(AX[i][j] * b[j] for j in range(3)) for i in range(3)]
ay_b = [sum(AY[i][j] * b[j] for j in range(3)) for i in range(3)]
qx = ax_b[1:]
qy = ay_b[1:]

checks = {
    "mixed_cell_commutes_exactly": curvature == [[0, 0, 0]] * 3,
    "x_quotient_defect_is_nonzero": qx != [0, 0],
    "y_quotient_defect_is_nonzero": qy != [0, 0],
    "bidual_quotient_defects_are_independent": qx == [1, 0] and qy == [0, 1],
    "distinguished_line_is_not_horizontal": ax_b[1:] != [0, 0] and ay_b[1:] != [0, 0],
}
payload = {
    "schema": "marici.aspect.flat-mixed-cell-nonhorizontal-line-hostile.v1",
    "basis": ["b", "q_x", "q_y"],
    "distinguished_line": "span(b)",
    "A_x": AX,
    "A_y": AY,
    "curvature": curvature,
    "quotient_defects": {"x": qx, "y": qy},
    "checks": checks,
    "passed": all(checks.values()),
    "consequence": "Mixed commutation, at any number of labelled generators, does not imply horizontality of the Bockstein line. The quotient defects must be computed explicitly in both parameter directions.",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
