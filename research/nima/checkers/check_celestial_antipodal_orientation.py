#!/usr/bin/env python3
"""Exact Jacobian sign of the celestial antipodal map."""

import json
import sympy as sp
from pathlib import Path


x, y = sp.symbols("x y", real=True)
r2 = x**2 + y**2
xp, yp = -x / r2, -y / r2
J = sp.Matrix([xp, yp]).jacobian([x, y])
detJ = sp.factor(J.det())

assert sp.simplify(detJ + 1 / r2**2) == 0

result = {
    "status": "PASS",
    "map": [str(xp), str(yp)],
    "jacobian_determinant": str(detJ),
    "sign_away_from_chart_origin": -1,
    "degree_on_S2": -1,
    "establishes": "celestial_spatial_orientation_character_only",
    "does_not_establish": [
        "physical time-reversal character",
        "null-infinity coorientation character",
        "Carrier-to-radiative comparison map",
    ],
}

out = Path(__file__).resolve().parents[1] / "results" / "celestial_antipodal_orientation.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
