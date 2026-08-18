#!/usr/bin/env python3
"""Verify the evidence packet for conditional closure of the A3 branch."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


grade = load("research/benincasa/a3-soft-signed-nearby-complex.json")
horiz = load("research/benincasa/a3-kato-horizontality-gate.json")
chambers = load("research/benincasa/a3-source-regulator-chambers.json")
exact = load("research/nima/a3-regulator-chamber-separation.json")
global_cells = load("research/nima/a3-global-coherence-module.json")

assert grade["complex"]["rank_over_Q"] == 3
assert grade["complex"]["support_symbol_rank"] == 2
assert horiz["conclusion"]["strict_horizontality"] is False
assert chambers["conclusion"]["unique_labelled_thimble_system"] is False
assert exact["separator"]["contained_in_discriminant"] is True
assert global_cells["minimal_coherence_module"]["dimension"] == 66

print(json.dumps({
    "carrier_geometry": "sufficient",
    "de_Rham_associated_grade": "sufficient",
    "strict_quotient_local_system": "refuted",
    "physical_coherence_cell": "unselected",
    "new_carrier_stratum": "unsupported",
    "reopening_condition": "source-derived contour-to-energy regulator image contained in one A3 chamber",
}, indent=2))
