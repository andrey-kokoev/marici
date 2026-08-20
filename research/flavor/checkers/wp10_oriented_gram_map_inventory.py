"""Inventory sector-labelled Gram-map complexity for all 36 nine-link classes.

Classify each sector support by row-overlap multiplicities. An off-diagonal
Gram entry is monomial in edge variables only when the corresponding row pair
shares at most one column. Multiple shared columns require a phase-sensitive
sum and must retain the loop coefficient in any Jacobian calculation.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SLOTS = [(i, j) for i in range(3) for j in range(3)]


def slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def sector_signature(mask):
    ss = slots(mask)
    row_degrees = tuple(sorted(sum(i == r for i, _ in ss)
                               for r in range(3)))
    col_degrees = tuple(sorted(sum(j == c for _, j in ss)
                               for c in range(3)))
    overlaps = tuple(sorted(sum((i, c) in ss and (j, c) in ss
                                for c in range(3))
                            for i in range(3) for j in range(i+1, 3)))
    return {
        "edge_count": len(ss),
        "row_degrees": row_degrees,
        "column_degrees": col_degrees,
        "row_pair_shared_column_counts": overlaps,
        "phase_sensitive_offdiagonal": max(overlaps) >= 2,
    }


original = json.loads((RESULTS / "wp7_ensemble.json").read_text())
oriented_inputs = [
    {"orientation": "original", "orbit": rec["orbit_index"],
     "mask_u": rec["mask_u"], "mask_d": rec["mask_d"]}
    for rec in original["orbits"]
]
for orbit in range(18):
    rec = json.loads(
        (RESULTS / f"wp10_sector_swapped_orbit{orbit}_pilot.json").read_text())
    oriented_inputs.append({
        "orientation": "sector_swapped", "orbit": orbit,
        "mask_u": rec["mask_u"], "mask_d": rec["mask_d"],
    })

rows = []
signatures = {}
for row in oriented_inputs:
    mu, md = row["mask_u"], row["mask_d"]
    su, sd = sector_signature(mu), sector_signature(md)
    key = (su["edge_count"], su["row_degrees"], su["column_degrees"],
           su["row_pair_shared_column_counts"],
           sd["edge_count"], sd["row_degrees"], sd["column_degrees"],
           sd["row_pair_shared_column_counts"])
    sid = signatures.setdefault(key, len(signatures))
    rows.append({
        "orientation": row["orientation"],
        "orbit": row["orbit"],
        "mask_u": mu, "mask_d": md,
        "signature_id": sid,
        "up": su, "down": sd,
        "requires_phase_in_gram_map":
            su["phase_sensitive_offdiagonal"] or
            sd["phase_sensitive_offdiagonal"],
    })

out = {
    "schema": "marici.flavor.oriented_gram_map_inventory.v1",
    "status": "complete",
    "oriented_classes": len(rows),
    "distinct_signatures": len(signatures),
    "purely_monomial_gram_classes":
        sum(not r["requires_phase_in_gram_map"] for r in rows),
    "phase_sensitive_gram_classes":
        sum(r["requires_phase_in_gram_map"] for r in rows),
    "signature_multiplicities": {
        str(sid): sum(r["signature_id"] == sid for r in rows)
        for sid in range(len(signatures))
    },
    "rows": rows,
}
(RESULTS / "wp10_oriented_gram_map_inventory.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=2))
