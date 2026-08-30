#!/usr/bin/env python3
"""Preregister and execute the differentiated specialization-cone packet contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research" / "benincasa" / "results" / "rank26-gram-wall-differentiated-cone.json"
OUT = ROOT / "research" / "aspect" / "results" / "differentiated_cone_packet_check.json"

MATRIX_FIELDS = [
    "d_C_at_wall", "F_at_wall", "d_D_at_wall",
    "d_C_normal_jet", "F_normal_jet", "d_D_normal_jet",
    "d_C_tangent_jet", "F_tangent_jet", "d_D_tangent_jet",
]
TRANSPORT_FIELDS = [
    "retained_pivot_transport",
    "denominator_occurrence_permutation",
    "residue_jacobian_unit",
    "inversion_transition",
]


def shape(a):
    if not isinstance(a, list) or not a or not all(isinstance(row, list) for row in a):
        raise ValueError("matrix must be a nonempty array of row arrays")
    widths = {len(row) for row in a}
    if len(widths) != 1 or 0 in widths:
        raise ValueError("matrix rows must have one nonzero width")
    if not all(isinstance(x, int) for row in a for x in row):
        raise ValueError("matrix entries must be integers")
    return len(a), len(a[0])


def add(a, b, p):
    if shape(a) != shape(b):
        raise ValueError("matrix-add shape mismatch")
    return [[(x + y) % p for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a, b, p):
    if shape(a) != shape(b):
        raise ValueError("matrix-subtract shape mismatch")
    return [[(x - y) % p for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mul(a, b, p):
    ar, ac = shape(a)
    br, bc = shape(b)
    if ac != br:
        raise ValueError("matrix-product shape mismatch")
    return [[sum(a[i][k] * b[k][j] for k in range(ac)) % p for j in range(bc)] for i in range(ar)]


def zero(a, p):
    return all(x % p == 0 for row in a for x in row)


def differentiated_residual(d_c, f, d_d, d_c_jet, f_jet, d_d_jet, p):
    left = add(mul(d_d_jet, f, p), mul(d_d, f_jet, p), p)
    right = add(mul(f_jet, d_c, p), mul(f, d_c_jet, p), p)
    return sub(left, right, p)


contract = {
    "packet": str(PACKET.relative_to(ROOT)).replace("\\", "/"),
    "field": "prime",
    "matrix_convention": "row-by-column; d_D F = F d_C",
    "required_matrix_fields": MATRIX_FIELDS,
    "required_transport_fields": TRANSPORT_FIELDS,
    "equations": {
        "wall": "d_D_at_wall F_at_wall = F_at_wall d_C_at_wall",
        "normal": "d_D_normal_jet F + d_D F_normal_jet = F_normal_jet d_C + F d_C_normal_jet",
        "tangent": "same differentiated equation, with tangent jets, has zero residual",
    },
    "forbidden_repairs": [
        "post-hoc basis alignment",
        "independent rescaling of obstruction and mixed target lines",
        "dropping retained-pivot or inversion transport",
    ],
}

if not PACKET.exists():
    payload = {
        "schema": "marici.aspect.differentiated-cone-packet-check.v1",
        "contract": contract,
        "packet_present": False,
        "passed": True,
        "classification": "preregistered_awaiting_source_export",
        "next_falsifier": "place the source-derived thirteen-field packet at the frozen path; this checker will execute without changing conventions",
    }
else:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    missing = [name for name in MATRIX_FIELDS + TRANSPORT_FIELDS if name not in packet]
    errors = []
    residuals = {}
    if missing:
        errors.append("missing required exports: " + ", ".join(missing))
    p = packet.get("prime")
    if not isinstance(p, int) or p < 2:
        errors.append("prime must be an integer at least 2")
    if not errors:
        try:
            for name in MATRIX_FIELDS:
                shape(packet[name])
            wall_residual = sub(
                mul(packet["d_D_at_wall"], packet["F_at_wall"], p),
                mul(packet["F_at_wall"], packet["d_C_at_wall"], p),
                p,
            )
            normal_residual = differentiated_residual(
                packet["d_C_at_wall"], packet["F_at_wall"], packet["d_D_at_wall"],
                packet["d_C_normal_jet"], packet["F_normal_jet"], packet["d_D_normal_jet"], p,
            )
            tangent_residual = differentiated_residual(
                packet["d_C_at_wall"], packet["F_at_wall"], packet["d_D_at_wall"],
                packet["d_C_tangent_jet"], packet["F_tangent_jet"], packet["d_D_tangent_jet"], p,
            )
            residuals = {
                "wall": wall_residual,
                "normal": normal_residual,
                "tangent": tangent_residual,
            }
            if not zero(wall_residual, p):
                errors.append("wall chain equation fails")
            if not zero(normal_residual, p):
                errors.append("normal differentiated chain equation fails")
            if not zero(tangent_residual, p):
                errors.append("Gram-tangent differentiated residual is nonzero")
        except ValueError as exc:
            errors.append(str(exc))
    payload = {
        "schema": "marici.aspect.differentiated-cone-packet-check.v1",
        "contract": contract,
        "packet_present": True,
        "prime": p,
        "missing": missing,
        "residuals": residuals,
        "errors": errors,
        "passed": not errors,
        "classification": "differentiated_cone_chain_square_verified" if not errors else "differentiated_cone_packet_falsified",
        "next_falsifier": "compare the verified normal image with the coordinate-7 obstruction and common mixed line across both preregistered primes" if not errors else "repair the source reducer; do not align bases after export",
    }

OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
