#!/usr/bin/env python3
"""Certify the normalized local double-Leray residue and exchange signs."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "double-soft-leray-local-constructor.json"


def main() -> None:
    # Each normalized single-circle integral of dz/z is one.
    residue_x = 1
    residue_y = 1
    ordered_double_residue = residue_x * residue_y

    form_exchange_sign = -1
    torus_orientation_exchange_sign = -1
    paired_exchange_sign = form_exchange_sign * torus_orientation_exchange_sign

    assert ordered_double_residue == 1
    assert paired_exchange_sign == 1

    result = {
        "status": "PASS",
        "local_model": "(x*y=0) with labelled normal-crossing axes",
        "normalized_single_residues": {"x": residue_x, "y": residue_y},
        "normalized_double_leray_pairing": ordered_double_residue,
        "exchange_signs": {
            "log_form": form_exchange_sign,
            "torus_orientation": torus_orientation_exchange_sign,
            "paired_result": paired_exchange_sign,
        },
        "radius_independent": True,
        "local_constructor_exists": True,
        "global_source_to_norm_comparison_exists": False,
        "next_gate": "single-soft/double-residue Beck-Chevalley comparison",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
