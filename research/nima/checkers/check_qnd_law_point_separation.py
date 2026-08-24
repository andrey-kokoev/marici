"""Exact audit: QND typing fixes the law, not the interaction point."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/qnd-law-point-separation.json"


parameters = (F(0), F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(4, 5))
points = []
for t in parameters:
    c = (1 - t * t) / (1 + t * t)
    s = 2 * t / (1 + t * t)
    points.append((t, c, s))

gates = {
    "all_interactions_are_unitary": all(c * c + s * s == 1 for _t, c, s in points),
    "all_obey_same_complementarity_law": all(c * c + s * s == 1 for _t, c, s in points),
    "typed_source_does_not_select_one_point": len({(c, s) for _t, c, s in points}) > 1,
    "visibility_varies": len({abs(c) for _t, c, _s in points}) > 1,
    "distinguishability_varies": len({abs(s) for _t, _c, s in points}) > 1,
    "frozen_three_four_fifths_point_is_t_half": (
        next((c, s) for t, c, s in points if t == F(1, 2)) == (F(3, 5), F(4, 5))
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.qnd-law-point-separation.v1",
    "rational_unitary_points": [
        {"t": str(t), "visibility": str(abs(c)), "distinguishability": str(abs(s))}
        for t, c, s in points
    ],
    "gates": gates,
    "conclusion": (
        "The controlled-interaction type and unitarity generate the circle "
        "V^2+D^2=1 but do not select a numerical point. The interaction "
        "parameter requires additional dynamical or boundary data."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
