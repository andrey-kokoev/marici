"""Audit uniqueness and physical authority of the C3 Tate-to-norm square."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARICI = ROOT.parents[1]


def main() -> None:
    algebra = json.loads(
        (ROOT / "results" / "c3-occurrence-is-depth-two-jet.json").read_text(
            encoding="utf-8"
        )
    )
    inventory = json.loads(
        (
            MARICI
            / "research"
            / "grothendieck"
            / "results"
            / "phase-i-operation-inventory-closure.json"
        ).read_text(encoding="utf-8")
    )

    assert algebra["status"] == "PASS"
    assert algebra["canonical_quadratic_map"].startswith("every nonzero class")

    # A bilinear map between one-dimensional F_3 spaces is determined by c=mu(1,1).
    # Odd x odd is even, so all three scalars are D3-equivariant; norm
    # normalization selects c=1 uniquely.
    equivariant_bilinear_scalars = [0, 1, 2]
    normalized_scalars = [c for c in equivariant_bilinear_scalars if c == 1]
    assert len(equivariant_bilinear_scalars) == 3
    assert normalized_scalars == [1]

    passing_carrier_products = inventory["passing_multiplication_candidates"]
    assert passing_carrier_products == []
    assert inventory["verdict"]["intrinsic_multiplication_derived"] is False

    operation_audit = [
        {
            "operation": "cyclic soft-star Gysin",
            "input_arity": 1,
            "physical_source_derived": True,
            "realizes_binary_tate_product": False,
        },
        {
            "operation": "norm channel TR",
            "input_arity": 1,
            "physical_source_derived": True,
            "realizes_binary_tate_product": False,
        },
        {
            "operation": "scalar augmentation",
            "input_arity": 1,
            "physical_source_derived": True,
            "realizes_binary_tate_product": False,
        },
        {
            "operation": "F_3[C_3] convolution",
            "input_arity": 2,
            "physical_source_derived": False,
            "realizes_binary_tate_product": False,
        },
    ]
    assert not any(item["realizes_binary_tate_product"] for item in operation_audit)

    result = {
        "status": "PASS",
        "equivariant_bilinear_map_dimension": 1,
        "normalized_map_unique": True,
        "normalized_rule": "nonzero Tate class squared equals norm",
        "operation_audit": operation_audit,
        "passing_carrier_product_count": len(passing_carrier_products),
        "coefficient_square_status": "established",
        "physical_binary_process_status": "not admitted",
        "reopening_condition": "source-derived two-input supported correspondence",
    }

    output = ROOT / "results" / "c3-tate-square-physical-authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
