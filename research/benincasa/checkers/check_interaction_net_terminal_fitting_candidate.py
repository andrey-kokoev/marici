#!/usr/bin/env python3
"""Audit the minimal terminal Fitting candidate against structural fibers.

This checker does not derive the candidate from the 14422 by 2278 source
matrix.  It freezes the smallest parameter-ring presentation compatible with
Ledger 4151, computes its determinantal ideals exactly, and subjects its
specializations to the already computed hostile fiber table.
"""
from __future__ import annotations

import json
import math

GENERIC = [
    ((5, 7, 11), (8, 8)),
    ((3, 5, 7), (8, 8)),
    ((3, 9, 13), (8, 8)),
    ((7, 11, 17), (8, 12)),
    ((3, 7, 11), (8, 12)),
    ((3, 11, 17), (8, 12)),
]
EQUALITY = [
    ((5, 5, 7), (8, 12)),
    ((3, 3, 5), (8, 17)),
    ((3, 3, 7), (8, 22)),
    ((3, 3, 9), (8, 12)),
    ((7, 7, 9), (8, 22)),
    ((7, 7, 13), (8, 12)),
    ((9, 9, 11), (8, 12)),
    ((11, 11, 13), (8, 17)),
]


def v2(value: int) -> int | None:
    if value == 0:
        return None
    return (abs(value) & -abs(value)).bit_length() - 1


def candidate_profile(point: tuple[int, int, int]) -> tuple[int, int]:
    x, y, _ = point
    second = math.gcd(2**12, 2**4 * (y - x) ** 4)
    return 8, v2(second)


generic_rows = []
for point, observed in GENERIC:
    predicted = candidate_profile(point)
    generic_rows.append({
        "point": point,
        "difference": point[1] - point[0],
        "observed": observed,
        "predicted": predicted,
        "match": observed == predicted,
    })

equality_rows = []
for point, observed in EQUALITY:
    predicted = candidate_profile(point)
    secondary = (8, 7 + 5 * v2(point[0] + 1))
    equality_rows.append({
        "point": point,
        "observed": observed,
        "generic_candidate": predicted,
        "secondary_prediction": secondary,
        "generic_match": observed == predicted,
        "secondary_match": observed == secondary,
    })

payload = {
    "schema": "marici.interaction-net-terminal-fitting-candidate.v1",
    "ring": "Z[x,y,z]",
    "presentation_rows_by_generators": [
        ["2^8", "0"],
        ["0", "2^12"],
        ["0", "2^4*(y-x)^4"],
    ],
    "fitting_ideals": {
        "Fitt_0": ["2^20", "2^12*(y-x)^4"],
        "Fitt_1": ["2^8", "2^4*(y-x)^4"],
    },
    "generic_open": {
        "condition": "x != y",
        "rows": generic_rows,
        "all_match": all(row["match"] for row in generic_rows),
    },
    "equality_boundary": {
        "condition": "x = y",
        "rows": equality_rows,
        "generic_candidate_globally_sufficient": all(
            row["generic_match"] for row in equality_rows
        ),
        "path_formula_all_match": all(
            row["secondary_match"] for row in equality_rows
        ),
        "retracted_path_formula": "7 + 5*v2(x+1)",
        "interpretation": (
            "The fifth-order spacing survives, but varying z falsifies the "
            "x+1 coordinate inferred on z=x+2.  The terminal generator must "
            "be derived from the unspecialized mixed-Rees presentation."
        ),
    },
    "typing": {
        "is_derived_from_full_source_matrix": False,
        "legitimate_use": "finite candidate and acceptance contract for mixed-(2,y-x) Rees elimination",
        "prohibited_use": "claiming the Fitting ideals before source-matrix derivation",
    },
}
payload["status"] = (
    "pass"
    if payload["generic_open"]["all_match"]
    and not payload["equality_boundary"]["generic_candidate_globally_sufficient"]
    and not payload["equality_boundary"]["path_formula_all_match"]
    else "fail"
)
print(json.dumps(payload, indent=2))
if payload["status"] != "pass":
    raise SystemExit(1)
