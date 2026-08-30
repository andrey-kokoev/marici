#!/usr/bin/env python3
"""Audit the first source/typing gate of the coupling-necessity conjecture."""

from __future__ import annotations

import json
from pathlib import Path


NIMA = Path(__file__).resolve().parents[1]
MARICI = NIMA.parents[1]
RESULT = NIMA / "results" / "physical-coupling-necessity-gate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    relative = load(NIMA / "results" / "positive-simplex-relative-tate-product.json")
    radial = load(MARICI / "research" / "benincasa" / "all-soft-radial-strict-transform.json")
    lift = load(NIMA / "results" / "supported-norm-integral-lift.json")
    comparison = load(NIMA / "results" / "norm-grade-to-a2-discriminant-comparison.json")
    linking = load(NIMA / "results" / "a2-discriminant-linking-readout.json")

    supported_class_ready = bool(
        relative["relative_class_nonzero"] and relative["supported_product_nonzero"]
    )
    coefficient_readout_ready = all(
        packet["status"].lower() == "pass" for packet in (lift, comparison, linking)
    )
    physical_pairing_ready = bool(relative["physical_fiberwise_pairing_established"])
    radial_physical_status = radial["classification"]["physical_level"]
    source_selects_specialization = "unselected" not in radial_physical_status

    checks = {
        "supported_relative_class_ready": supported_class_ready,
        "coefficient_readout_ready": coefficient_readout_ready,
        "physical_pairing_not_established": not physical_pairing_ready,
        "radial_source_does_not_select_specialization": not source_selects_specialization,
        "defect_calculation_not_authorized_without_composition_square": True,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.physical-coupling-necessity-gate.v1",
        "status": "pass",
        "classification": "source_underdetermined",
        "supported_class": "established",
        "coefficient_readout": "established",
        "physical_chain_comparison": "not established",
        "uncoupled_defect": "not yet typed",
        "zero_coupling_conclusion_authorized": False,
        "next_admissible_input": (
            "source-defined relative chain map or a legal composition square "
            "whose missing coherence cell targets the all-soft supported class"
        ),
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
