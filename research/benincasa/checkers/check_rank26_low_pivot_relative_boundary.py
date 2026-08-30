#!/usr/bin/env python3
"""Locate endpoint non-descent among the ten canonical low pivot relations."""
from __future__ import annotations
import contextlib
import io
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CHECKERS = ROOT / "research" / "benincasa" / "checkers"
sys.path.insert(0, str(CHECKERS))
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
os.environ["MARICI_FIELD_PRIME"] = str(P)

with contextlib.redirect_stdout(io.StringIO()):
    import check_rank26_infinity_order2_endpoint_descent as src

base = src.base
pres = src.pres
low_count = len(pres["low_labels"])
low_pivots = sorted(p for p in pres["pivots"] if p < low_count)


def signed(v):
    return v if v <= P // 2 else v - P


def canonical_low_relation(pivot):
    pivot_row = pres["pivots"][pivot]
    assert pivot_row.get(pivot) == 1
    tail = {c: v for c, v in pivot_row.items() if c != pivot}
    other_pivots = {p: r for p, r in pres["pivots"].items() if p != pivot}
    reduced_tail = base.reduce_row(tail, other_pivots)
    relation = {pivot: 1}
    for c, v in reduced_tail.items():
        relation[c] = v
    return relation


def endpoint_value(relation, endpoint):
    value = 0
    unsupported = []
    for column, coefficient in relation.items():
        label = pres["ordered_columns"][column]
        k_pole, *rest = label
        exponent = rest[-1]
        levels = tuple(rest[:-1])
        if k_pole == 0 and levels == (1, 1, 1, 1, 1) and sum(exponent) <= 7:
            value += coefficient * src.raw_endpoint_value(endpoint, exponent)
        else:
            unsupported.append({
                "column": column,
                "label": repr(label),
                "coefficient": signed(coefficient),
            })
    return value % P, unsupported


relations = []
for pivot in low_pivots:
    relation = canonical_low_relation(pivot)
    values = {}
    unsupported_union = []
    for endpoint in ("t=0", "t=-1", "t=infinity"):
        value, unsupported = endpoint_value(relation, endpoint)
        values[endpoint] = signed(value)
        unsupported_union.extend(unsupported)
    relations.append({
        "pivot_column": pivot,
        "pivot_label": repr(pres["ordered_columns"][pivot]),
        "pivot_monomial": list(pres["ordered_columns"][pivot][-1]),
        "term_count": len(relation),
        "all_terms_in_low_simple_pole_sector": not unsupported_union,
        "completed_endpoint_boundary": values,
        "nonzero_endpoint_count": sum(v != 0 for v in values.values()),
        "relation": [
            {
                "column": c,
                "monomial": list(pres["ordered_columns"][c][-1]),
                "coefficient": signed(v),
            }
            for c, v in sorted(relation.items())
        ] if not unsupported_union else [],
        "unsupported_terms": unsupported_union,
    })

offenders = [r for r in relations if r["nonzero_endpoint_count"]]
checks = {
    "physical_quotient_dimension_is_26": len(pres["free_low"]) == 26,
    "ten_canonical_low_relations": len(low_pivots) == 10,
    "all_canonical_relations_close_inside_low_simple_pole_sector": all(
        r["all_terms_in_low_simple_pole_sector"] for r in relations
    ),
    "no_canonical_low_relation_has_relative_boundary": not offenders,
}
packet = {
    "schema": "marici.rank26-low-pivot-relative-boundary.v1",
    "prime": P,
    "external_point": list(src.POINT),
    "low_monomial_count": low_count,
    "free_rank": len(pres["free_low"]),
    "canonical_relation_count": len(low_pivots),
    "offender_count": len(offenders),
    "offenders": offenders,
    "all_relations": relations,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": (
        "All ten canonical relations internal to the rank-26 low quotient have "
        "zero completed endpoint boundary. The earlier non-descent arose only "
        "after ambient reduction followed by unauthorized coordinate truncation."
    ),
}
out = ROOT / "research" / "benincasa" / "results" / f"rank26-low-pivot-relative-boundary-p{P}.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "schema": packet["schema"],
    "prime": P,
    "checks": checks,
    "offender_count": len(offenders),
    "offender_pivots": [
        {"monomial": r["pivot_monomial"], "boundary": r["completed_endpoint_boundary"]}
        for r in offenders
    ],
}, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
