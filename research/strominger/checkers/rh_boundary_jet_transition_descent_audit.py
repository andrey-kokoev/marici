#!/usr/bin/env python3
"""Transition/descent audit for the growing RH boundary-jet tower."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_boundary_jet_transition_descent_audit.json"


def trunc(v, g):
    return v[:g]


def zero_extend(v):
    return v + [Fraction(0)]


def source_top(g):
    # Source-normalized order-g boundary current from the Laurent audits.
    return [Fraction(0) for _ in range(g - 1)] + [Fraction(1)]


def norm2(v, r):
    # Boundary-jet source-radius graph norm: order k+1 costs (1-r)^-(k+1).
    return sum(x * x * (1 - r) ** (-(k + 1)) for k, x in enumerate(v))

rows = []
for g in range(1, 8):
    old = source_top(g)
    new = source_top(g + 1)
    lifted_old = zero_extend(old)
    r = Fraction(g + 1, g + 2)
    rows.append({
        "g": g,
        "old": old,
        "new": new,
        "trunc_new": trunc(new, g),
        "lifted_old": lifted_old,
        "new_top_lost_by_truncation": new[-1],
        "old_norm": norm2(old, r),
        "lifted_old_norm": norm2(lifted_old, r),
        "new_norm": norm2(new, r),
    })

# Candidate maps:
# 1. truncation g+1 -> g is natural but forgets the new top current;
# 2. zero-extension g -> g+1 is bounded and section-like but misses the source
#    order-(g+1) current;
# 3. any finite stabilization would require all later source_top rows to lie in
#    a fixed finite image, which they do not.
truncation_natural = all(trunc(row["lifted_old"], row["g"]) == row["old"] for row in rows)
truncation_loses_new_current = all(row["trunc_new"] == [Fraction(0) for _ in range(row["g"])] and row["new_top_lost_by_truncation"] == 1 for row in rows)
zero_extension_bounded_on_old = all(row["lifted_old_norm"] == row["old_norm"] for row in rows)
zero_extension_misses_new_source_current = all(row["lifted_old"] != row["new"] for row in rows)
new_norms_grow = all(rows[i]["new_norm"] < rows[i + 1]["new_norm"] for i in range(len(rows) - 1))

# A source-derived descent transition would need a declared law assigning the
# new top coefficient from old data.  The exact hostile is two sources with the
# same old truncation and different new top coefficient.
same_old = [Fraction(1), Fraction(-1)]
extension_a = same_old + [Fraction(0)]
extension_b = same_old + [Fraction(1)]
old_data_equal = trunc(extension_a, 2) == trunc(extension_b, 2)
new_data_differs = extension_a[2] != extension_b[2]
old_data_cannot_determine_new_top = old_data_equal and new_data_differs

checks = {
    "truncation_bonding_is_natural_on_zero_extension": truncation_natural,
    "truncation_forgets_each_new_source_current": truncation_loses_new_current,
    "zero_extension_is_bounded_but_only_on_old_data": zero_extension_bounded_on_old,
    "zero_extension_misses_new_source_current": zero_extension_misses_new_source_current,
    "new_top_graph_norms_grow_with_grade_at_source_radius_prefix": new_norms_grow,
    "old_boundary_data_does_not_determine_new_top_current": old_data_cannot_determine_new_top,
}

payload = {
    "schema": "marici.strominger.rh_boundary_jet_transition_descent_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "rows": [
        {
            "g": row["g"],
            "old": [str(x) for x in row["old"]],
            "new": [str(x) for x in row["new"]],
            "trunc_new": [str(x) for x in row["trunc_new"]],
            "old_norm": str(row["old_norm"]),
            "new_norm": str(row["new_norm"]),
        }
        for row in rows
    ],
    "hostile_same_old_different_new_top": {
        "extension_a": [str(x) for x in extension_a],
        "extension_b": [str(x) for x in extension_b],
    },
    "verdict": (
        "The finite transition/descent candidates are exhausted. Truncation is "
        "natural but forgets every new source-declared top boundary current; "
        "zero-extension is bounded on old data but misses the new current. Old "
        "boundary data cannot determine the next top coefficient without an "
        "extra source law. Since the top-jet graph norm keeps growing toward the "
        "source radius, the needed transition is not a formal tower map but an "
        "independently derived Poisson/archimedean/seam descent relation that "
        "supplies the new coefficient while preserving the adjoint pairing."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
