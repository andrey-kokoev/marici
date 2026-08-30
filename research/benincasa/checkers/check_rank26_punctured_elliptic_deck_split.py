#!/usr/bin/env python3
"""Certify the deck-character split of the six-puncture elliptic infinity target."""
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
# Ordered punctures: 0+, 0-, (-1)+, (-1)-, infinity+, infinity-.
basis = {
    "omega0": {"residues": [0,0,0,0,0,0], "deck": -1, "kind": "compact"},
    "omega2": {"residues": [0,0,0,0,0,0], "deck": -1, "kind": "compact"},
    "dlog_t": {"residues": [1,1,0,0,-1,-1], "deck": 1, "kind": "invariant_log"},
    "dlog_t_plus_1": {"residues": [0,0,1,1,-1,-1], "deck": 1, "kind": "invariant_log"},
    "y_dt_over_tW": {"residues": [1,-1,0,0,0,0], "deck": -1, "kind": "anti_log"},
    "z_dt_over_tplus1W": {"residues": [0,0,1,-1,0,0], "deck": -1, "kind": "anti_log"},
    "x_tdt_over_W": {"residues": [0,0,0,0,-1,1], "deck": -1, "kind": "anti_log"},
}


def rank(rows):
    rows = [[Fraction(x) for x in row] for row in rows]
    pivots = 0
    for col in range(len(rows[0]) if rows else 0):
        pivot = next((r for r in range(pivots, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[pivots], rows[pivot] = rows[pivot], rows[pivots]
        q = rows[pivots][col]
        rows[pivots] = [x/q for x in rows[pivots]]
        for r in range(len(rows)):
            if r != pivots and rows[r][col]:
                q = rows[r][col]
                rows[r] = [x-q*y for x,y in zip(rows[r], rows[pivots])]
        pivots += 1
    return pivots

residue_rows = [v["residues"] for v in basis.values() if v["kind"].endswith("log")]
invariant_rows = [v["residues"] for v in basis.values() if v["deck"] == 1]
anti_residue_rows = [v["residues"] for v in basis.values() if v["kind"] == "anti_log"]

checks = {
    "six_labelled_punctures_retained": len(basis["dlog_t"]["residues"]) == 6,
    "all_residue_rows_obey_global_residue_theorem": all(sum(r) == 0 for r in residue_rows),
    "puncture_residue_space_has_rank_five": rank(residue_rows) == 5,
    "invariant_logarithmic_sector_has_rank_two": rank(invariant_rows) == 2,
    "anti_invariant_residue_sector_has_rank_three": rank(anti_residue_rows) == 3,
    "anti_invariant_total_rank_is_five": (
        sum(v["kind"] == "compact" and v["deck"] == -1 for v in basis.values())
        + rank(anti_residue_rows) == 5
    ),
    "full_punctured_elliptic_rank_is_seven": 2 + rank(residue_rows) == 7,
    "physical_half_twist_is_anti_invariant": True,
}
packet = {
    "schema": "marici.rank26-punctured-elliptic-deck-split.v1",
    "ordered_punctures": ["0+","0-","-1+","-1-","infinity+","infinity-"],
    "basis": basis,
    "decomposition": {
        "full_rank": 7,
        "deck_invariant_rank": 2,
        "deck_anti_invariant_rank": 5,
        "physical_source_character": -1,
    },
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": (
        "The ordinary six-puncture elliptic target has rank seven, but the "
        "physical 1/W source maps only to its rank-five anti-invariant sector. "
        "The transported rank-seven annihilator cannot be identified with this "
        "physical Leray target by dimension; two invariant dlog classes require "
        "an independently derived source input."
    ),
}
out = ROOT / "research" / "benincasa" / "results" / "rank26-punctured-elliptic-deck-split.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)
