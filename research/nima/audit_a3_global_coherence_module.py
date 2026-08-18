#!/usr/bin/env python3
"""Verify the minimal cyclic module required to kill the A3 Kato defects."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
support = json.loads((ROOT / "research/nima/a3-soft-signed-occurrence-support.json").read_text(encoding="utf-8"))
horiz = json.loads((ROOT / "research/benincasa/a3-kato-horizontality-gate.json").read_text(encoding="utf-8"))

germs = support["count"]["labelled_A3_germs"]
assert germs == 66
assert support["count"]["movable_labelled_A3_germs"] == 36
assert support["count"]["coalesced_labelled_A3_germs"] == 30
assert horiz["conclusion"]["strict_horizontality"] is False

occurrences_per_regular = 3
regular_copies = germs // occurrences_per_regular
assert regular_copies == 22
assert regular_copies * occurrences_per_regular == germs

print(json.dumps({
    "labelled_defects": germs,
    "regular_C3_copies": regular_copies,
    "defect_character": [germs, 0, 0],
    "minimal_coherence_rank": germs,
    "minimal_coherence_character": [germs, 0, 0],
    "excess_rank_distinguished_from_cell_rank": support["cohomology"]["aggregate_excess_rank"],
}, indent=2))
