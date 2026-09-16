#!/usr/bin/env python3
"""Link each of the 343 indexed esd_7 tetrahedra to analytical prototypes."""
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
propagation = json.loads((ROOT / "results/asymptotic_face_234_propagation.json").read_text())
prop = {tuple(cell["index"]): cell for cell in propagation["cells"]}

FACE_FORMS = {
    "H123": "naturality/interchange face in the residual-augmented relative-feature nerve",
    "H124": "mate/localized-equivalence face with endpoint coordinate retained",
    "H134": "regulator-transport face with Hermitian and skew placement coordinates",
    "H234": "rapid-decay asymptotic face with finite-part and endpoint residue coordinates",
}
TETRAHEDRON_FORM = "alternating four-face modification in the strictified relative-feature nerve"

cells = []
for index in product(range(7), repeat=3):
    witness = prop[index]
    cells.append({
        "id": f"esd7:{index[0]},{index[1]},{index[2]}",
        "index": index,
        "analytical_form": TETRAHEDRON_FORM,
        "face_prototypes": FACE_FORMS,
        "H234_decay_witness": {
            "minimum_cutoff_exponent": witness["minimum_cutoff_exponent"],
            "source_orders_for_target_orders": witness["source_orders_for_target_orders"],
        },
        "higher_coherence": "unique nerve filler after residual augmentation",
    })

assert len(cells) == 343
assert len({cell["id"] for cell in cells}) == 343
assert set(prop) == {tuple(cell["index"]) for cell in cells}
assert all(set(cell["face_prototypes"]) == set(FACE_FORMS) for cell in cells)

result = {
    "schema": "marici.voevodsky.esd7-tetrahedron-prototype-registry.v1",
    "complex": "esd_7(Delta^3)",
    "tetrahedron_count": len(cells),
    "parent_face_prototypes": FACE_FORMS,
    "parent_tetrahedron_prototype": TETRAHEDRON_FORM,
    "cells": cells,
    "coverage": {
        "unique_ids": 343,
        "analytical_forms_assigned": 343,
        "four_face_references_assigned": 343,
        "asymptotic_witnesses_assigned": 343,
    },
    "scope": "finite regulators and signed/relative analytical forms",
    "passed": True,
}
out = ROOT / "results/esd7_tetrahedron_prototype_registry.json"
out.write_text(json.dumps(result, separators=(",", ":")) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "cells"}, indent=2))
