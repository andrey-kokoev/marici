#!/usr/bin/env python3
"""Little-group character obstruction for the scaffolded A3^YM polynomial."""

import json
from pathlib import Path


scaffold_weight = (0, 0, 0)
ym_mhv_weight = (2, 2, -2)      # A3(1-,2-,3+)
ym_anti_mhv_weight = (-2, -2, 2)  # A3(1+,2+,3-)


def equivariant_hom_exists(source, target):
    return source == target


assert not equivariant_hom_exists(scaffold_weight, ym_mhv_weight)
assert not equivariant_hom_exists(scaffold_weight, ym_anti_mhv_weight)
assert tuple(-x for x in ym_mhv_weight) == ym_anti_mhv_weight

result = {
    "status": "PASS",
    "scaffold_mandelstam_weight": scaffold_weight,
    "ym_mhv_weight": ym_mhv_weight,
    "ym_anti_mhv_weight": ym_anti_mhv_weight,
    "equivariant_map_to_mhv": False,
    "equivariant_map_to_anti_mhv": False,
    "required_coefficient_weights": [ym_mhv_weight, ym_anti_mhv_weight],
    "conclusion": "the scalar-scaffolded residue requires an external polarization character line to lift to helicity amplitudes",
}

out = Path(__file__).resolve().parents[1] / "results" / "scaffold_helicity_weight_obstruction.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
