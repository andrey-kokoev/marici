#!/usr/bin/env python3
"""Audit whether Entry 304's Leray interval can select the e6 soft torsor."""

import json
from pathlib import Path

import sympy as sp


v = sp.symbols("v")
x = sp.Integer(1)
y = (v - 2) / 2

# Entry 304's common normalized coefficient on the homogeneous u=0 chart.
leray_normalization = sp.factor(-1 / (2 * x * y))

# Entry 3315's primitive logarithmic torsor, stripped of C2=-1/8.
torsor_log_form = sp.factor(sp.diff(sp.log(v / (v - 2)), v))


def residue(expr, point):
    return sp.factor(sp.residue(expr, v, point))


checks = {
    "homogeneous_normalization": sp.simplify(leray_normalization + 1 / (v - 2)) == 0,
    "endpoints_are_parameter_constant": True,  # d_v(+/-1)=0
    "leray_residue_v0_zero": residue(leray_normalization, 0) == 0,
    "leray_residue_v2_minus_one": residue(leray_normalization, 2) == -1,
    "torsor_residue_v0_plus_one": residue(torsor_log_form, 0) == 1,
    "torsor_residue_v2_minus_one": residue(torsor_log_form, 2) == -1,
    "support_vectors_differ": (
        residue(leray_normalization, 0), residue(leray_normalization, 2)
    )
    != (residue(torsor_log_form, 0), residue(torsor_log_form, 2)),
}

packet = {
    "schema": "marici.benincasa.moving_wall_leray_base_boundary.v1",
    "source": {
        "ledger_entry": 304,
        "fiber_endpoints": {"p_minus": "r=-1", "p_plus": "r=1"},
        "orientation": "p_minus to p_plus",
        "common_normalization": str(leray_normalization),
    },
    "homogeneous_chart": {
        "u": "0",
        "X1": "1",
        "X2": str(y),
        "X3": "-v/2",
        "soft_divisors": {"s3": "v=0", "s2": "v=2"},
    },
    "residue_vectors_ordered_s3_s2": {
        "entry_304_leray_normalization": [
            str(residue(leray_normalization, 0)),
            str(residue(leray_normalization, 2)),
        ],
        "candidate_primitive_torsor": [
            str(residue(torsor_log_form, 0)),
            str(residue(torsor_log_form, 2)),
        ],
    },
    "checks": checks,
    "verdict": (
        "Entry 304's fixed-endpoint moving-wall Leray family cannot select the "
        "candidate primitive base-soft torsor: it has no v=0 residue."
    ),
    "scope": (
        "This excludes only the established two-wall Leray interval as the "
        "selection map. It does not exclude a separately source-derived "
        "parameter-space relative chain or another occurrence sector."
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[k for k, ok in checks.items() if not ok]}")

out = Path(__file__).resolve().parents[1] / "results" / "moving_wall_leray_base_boundary.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
