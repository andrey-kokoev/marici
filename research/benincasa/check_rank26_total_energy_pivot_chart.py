"""Pivot-chart audit across the rank-26 total-energy normal line."""

from __future__ import annotations

import hashlib
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))

import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as charts


POINT = (2, 3, -5)
OFFSETS = (-3, -2, -1, 0, 1, 2, 3)
AMBIENT = 12
CUTOFF = 6


def pivot_digest(pivots: dict[int, dict[int, int]]) -> str:
    payload = [
        [pivot, [[column, value] for column, value in sorted(row.items())]]
        for pivot, row in sorted(pivots.items())
    ]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def probe(offset: int) -> dict:
    point = (POINT[0], POINT[1], POINT[2] + offset)
    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = AMBIENT, CUTOFF
    try:
        presentation = charts.presentation(
            base.fiber_data, point, charts.SOURCE_NAMES
        )
    finally:
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
    pivots = presentation["pivots"]
    low_count = len(presentation["low_labels"])
    low_pivots = sorted(pivot for pivot in pivots if pivot < low_count)
    return {
        "offset": offset,
        "point": list(point),
        "total_energy": sum(point),
        "column_count": len(presentation["columns"]),
        "relation_rank": len(pivots),
        "full_cokernel_dimension": len(presentation["columns"]) - len(pivots),
        "low_column_count": low_count,
        "low_pivot_count": len(low_pivots),
        "free_low_count": len(presentation["free_low"]),
        "pivot_columns_digest": hashlib.sha256(
            json.dumps(sorted(pivots)).encode("utf-8")
        ).hexdigest(),
        "normalized_pivot_digest": pivot_digest(pivots),
    }


def main() -> None:
    with ProcessPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(probe, OFFSETS))
    records.sort(key=lambda record: record["offset"])
    special = next(record for record in records if record["offset"] == 0)
    nearby = [record for record in records if record["offset"] != 0]
    rank_stable = all(
        record["relation_rank"] == special["relation_rank"] for record in nearby
    )
    pivot_columns_stable = all(
        record["pivot_columns_digest"] == special["pivot_columns_digest"]
        for record in nearby
    )
    pivot_rows_constant = all(
        record["normalized_pivot_digest"] == special["normalized_pivot_digest"]
        for record in nearby
    )
    payload = {
        "schema": "marici.benincasa.rank26-total-energy-pivot-chart.v1",
        "field": base.PRIME,
        "normal_coordinate": "E_T with (X1,X2) fixed and X3=-X1-X2+E_T",
        "ambient_relation_degree": AMBIENT,
        "low_cutoff": CUTOFF,
        "records": records,
        "relation_rank_stable": rank_stable,
        "pivot_columns_stable": pivot_columns_stable,
        "normalized_pivot_rows_constant": pivot_rows_constant,
        "status": (
            "fixed_pivot_chart_available"
            if rank_stable and pivot_columns_stable
            else "pivot_chart_changes_on_total_energy_support"
        ),
        "scope": (
            "finite-field Laurent relation presentation across seven exact "
            "normal samples; no dual-number derivative or nearby-cycle claim"
        ),
    }
    output = Path(__file__).with_name("rank26-total-energy-pivot-chart.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
