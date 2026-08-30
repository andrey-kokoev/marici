#!/usr/bin/env python3
"""Audit the cyclic Leray-frame cocycle and its e6 logarithmic edge."""

import json
from pathlib import Path

import sympy as sp


x1, x2, x3, v = sp.symbols("X1 X2 X3 v", nonzero=True)

# Cyclic relabelings of Entry 304's source-fixed common wall normalization.
n12 = -sp.Rational(1, 2) / (x1 * x2)
n23 = -sp.Rational(1, 2) / (x2 * x3)
n31 = -sp.Rational(1, 2) / (x3 * x1)

transitions = {
    "G12_to_G23": sp.factor(n23 / n12),
    "G23_to_G31": sp.factor(n31 / n23),
    "G31_to_G12": sp.factor(n12 / n31),
}

cocycle = sp.factor(sp.prod(transitions.values()))

# Homogeneous q_G12 chart: X1=1, X2=(v-2)/2, X3=-v/2.
subs = {x1: 1, x2: (v - 2) / 2, x3: -v / 2}
selected_edge = sp.factor(transitions["G31_to_G12"].subs(subs))
edge_log = sp.factor(sp.diff(sp.log(selected_edge), v))
candidate_log = sp.factor(sp.diff(sp.log(v / (v - 2)), v))


def residue(expr, point):
    return sp.factor(sp.residue(expr, v, point))


checks = {
    "transition_12_23": transitions["G12_to_G23"] == x1 / x3,
    "transition_23_31": transitions["G23_to_G31"] == x2 / x1,
    "transition_31_12": transitions["G31_to_G12"] == x3 / x2,
    "cech_cocycle_closes": cocycle == 1,
    "homogeneous_edge": sp.simplify(selected_edge + v / (v - 2)) == 0,
    "logarithmic_edge_equals_candidate": sp.simplify(edge_log - candidate_log) == 0,
    "residue_v0": residue(edge_log, 0) == 1,
    "residue_v2": residue(edge_log, 2) == -1,
}

packet = {
    "schema": "marici.benincasa.cyclic_leray_transition_torsor.v1",
    "source_frames": {
        "G12": str(n12),
        "G23": str(n23),
        "G31": str(n31),
        "provenance": "Entry 304 normalization plus Entries 756 and 764 labelled occurrence transport",
    },
    "transition_functions": {key: str(value) for key, value in transitions.items()},
    "cocycle_product": str(cocycle),
    "homogeneous_G31_to_G12": {
        "transition": str(selected_edge),
        "logarithmic_connection": str(edge_log),
        "residue_vector_v0_v2": [str(residue(edge_log, 0)), str(residue(edge_log, 2))],
    },
    "C2": "-1/8",
    "checks": checks,
    "verdict": (
        "The primitive e6 logarithmic candidate is exactly C2 times the "
        "G31-to-G12 cyclic Leray-frame transition connection."
    ),
    "typing_limit": (
        "This derives occurrence-descent provenance for the logarithmic class. "
        "It does not yet prove that the rank-twelve source reduction chooses "
        "this class as its off-diagonal extension coordinate."
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

out = Path(__file__).resolve().parents[1] / "results" / "cyclic_leray_transition_torsor.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
