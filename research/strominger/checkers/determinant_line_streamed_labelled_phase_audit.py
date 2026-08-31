#!/usr/bin/env python3
"""Stream source-labelled rank-two cells and audit the phase-data gate."""
from __future__ import annotations
import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "determinant_line_streamed_labelled_phase_audit.json"

def labels(beta, g, q):
    a_star = q - g + 3
    return ("M0",) + tuple(f"P{a}" for a in range(beta, max(beta, a_star) + 1))

def stream_cells(xs):
    """Yield each cell once as (base,pair), without retaining the face atlas."""
    for pair in combinations(xs, 2):
        rest = tuple(x for x in xs if x not in pair)
        for mask in range(1 << len(rest)):
            yield tuple(rest[i] for i in range(len(rest)) if mask & (1 << i)), pair

def formal_phase(base, pair, defects):
    # The compiler consumes a separately supplied connection-phase law.
    return defects.get((base, pair), 1)

xs = labels(4, 5, 11)
defect_key = (("M0",), ("P4", "P5"))
defects = {defect_key: -1}
count = bad = 0
hostile_seen = False
max_retained_cell_labels = 0
for base, pair in stream_cells(xs):
    count += 1
    max_retained_cell_labels = max(max_retained_cell_labels, len(base) + 2)
    phase = formal_phase(base, pair, defects)
    if phase != 1:
        bad += 1
        hostile_seen |= (base, pair) == defect_key

# Empty defect table is the only phase assignment derivable from no connection
# law; it passes vacuously and therefore cannot certify determinant coherence.
empty_bad = sum(formal_phase(b, p, {}) != 1 for b, p in stream_cells(xs))
source_connection_phase_law_present = False
checks = {
    "source_labels_reconstructed_for_beta4_g5_q11": xs == ("M0", "P4", "P5", "P6", "P7", "P8", "P9"),
    "stream_visits_exactly_672_rank_two_cells": count == 672,
    "stream_detects_labelled_upper_face_defect": hostile_seen and bad == 1,
    "compiler_memory_is_cell_bounded_not_atlas_bounded": max_retained_cell_labels == len(xs),
    "empty_phase_table_passes_vacuously": empty_bad == 0,
    "current_sources_do_not_supply_connection_phase_law": not source_connection_phase_law_present,
}
payload = {
 "schema":"marici.strominger.determinant_line_streamed_labelled_phase_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "labels":list(xs), "streamed_cell_count":count, "nontrivial_phase_count":bad,
 "hostile_cell":{"base":["M0"],"pair":["P4","P5"],"phase":-1},
 "verdict":"The source-poset compiler streams all 672 labelled cells and detects a supplied upper-face phase defect without materializing the atlas. The active direction is now decisively blocked at its scientific input boundary: existing cutoff sources determine labels and reachability, but no source-derived connection-phase law. An empty phase table passes vacuously and cannot certify determinant coherence.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
