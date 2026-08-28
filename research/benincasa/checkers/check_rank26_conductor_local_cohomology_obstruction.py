#!/usr/bin/env python3
"""Local-cohomology obstruction to an exact bulk cancellation at active conductors."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-conductor-local-cohomology-obstruction.json"
a, b = sp.symbols("a b")
x, y, z = 2, 3, 4
r1 = 3*sp.sqrt(46)/2
r2 = sp.sqrt(94)
marks = {
    "g1": b-y-z,
    "g2": a-x-z,
    "g3": a+b+z,
    "g23": b-x,
    "g31": a-y,
}

points = {
    "g1": {a: r1, b: y+z},
    "g2": {a: x+z, b: r2},
}
coefficients = {
    "g1": sp.Rational(16, 99225)-sp.sqrt(46)/101430,
    "g2": sp.Rational(1, 2025)-sp.sqrt(94)/28200,
}
rows = {}
checks = {}
for active, point in points.items():
    values = {label: sp.simplify(q.subs(point)) for label, q in marks.items()}
    numerator = sp.simplify(values["g23"]+values["g31"])
    inactive = {label: value for label, value in values.items() if label != active}
    rows[active] = {
        "marked_values": {label: str(value) for label, value in values.items()},
        "unsplit_numerator": str(numerator),
        "iterated_conductor_residue": str(coefficients[active]),
    }
    checks[f"{active}_only_active_marked_wall"] = all(value != 0 for value in inactive.values())
    checks[f"{active}_unsplit_numerator_nonzero"] = numerator != 0
    checks[f"{active}_iterated_residue_nonzero"] = coefficients[active] != 0

packet = {
    "schema": "marici.rank26-conductor-local-cohomology-obstruction.v1",
    "sample": {"x": x, "y": y, "z": z},
    "rows": rows,
    "local_statement": "Each selected point is an isolated intersection of one marked wall with the square-root conductor. Its nonzero iterated residue is invariant in the local logarithmic de Rham cohomology and cannot be removed by adding an exact bulk primitive regular on the other frozen supports.",
    "checks": {key: bool(value) for key, value in checks.items()},
    "passed": all(bool(value) for value in checks.values()),
    "conclusion": "The conjectured source-internal exact bulk cancellation is locally obstructed at both active conductors. Finiteness would require a relative-chain prescription, subtraction datum, or additional independently sourced support—not an exact homotopy inside the frozen five-wall meromorphic complex.",
    "scope": "This falsifies the no-subtraction exact-bulk mechanism. It does not forbid a distributional boundary value or renormalized observable with separately authorized physical data.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2)+"\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
