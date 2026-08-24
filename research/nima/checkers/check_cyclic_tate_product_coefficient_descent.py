#!/usr/bin/env python3
"""Close coefficient descent without fabricating geometric Cech maps."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARICI = ROOT.parents[1]
OCCURRENCE = MARICI / "research" / "benincasa" / "cyclic-occurrence-rees-certificate.json"
LOCAL = ROOT / "results" / "cyclic-tate-lift-cross-product.json"
RESULT = ROOT / "results" / "cyclic-tate-product-coefficient-descent.json"


def main() -> None:
    occurrence = json.loads(OCCURRENCE.read_text(encoding="utf-8"))
    local = json.loads(LOCAL.read_text(encoding="utf-8"))

    assert occurrence["rho_order"] == 3
    assert occurrence["all_source_signs"] == 1
    assert occurrence["cyclic_rees_covariance"] is True
    assert occurrence["cross_sector_cech_maps_source_defined"] is False
    assert occurrence["global_cech_differential_computed"] is False

    products = [tuple(row["cross"]) for row in local["cyclic_adjacent_lift_products"]]
    coefficient_cocycle_closed = len(set(products)) == 1 and products[0] == (1, 1, 1)
    assert coefficient_cocycle_closed

    result = {
        "status": "PASS",
        "local_norm_products": [list(x) for x in products],
        "cyclic_transition_product": "identity",
        "coefficient_cech_cocycle_closed": coefficient_cocycle_closed,
        "geometric_cross_sector_maps_source_defined": False,
        "global_geometric_descent_established": False,
        "remaining_obstruction_type": "source-derived cross-residue-surface overlap morphisms",
        "conclusion": (
            "Coefficient descent is exact. Only geometric Cech/Beck-Chevalley "
            "descent of the local double-Leray constructors remains open."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
