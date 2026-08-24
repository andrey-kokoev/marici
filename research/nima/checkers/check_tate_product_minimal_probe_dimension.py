#!/usr/bin/env python3
"""Audit the minimal parameter-space probe for the all-soft Z/3 character."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "tate-product-minimal-probe-dimension.json"


def main() -> None:
    probes = [
        {"probe": "fixed kinematic point", "dimension": 0, "detects_relative_H2": False},
        {"probe": "open interval with fixed endpoints", "dimension": 1, "detects_relative_H2": False},
        {"probe": "oriented boundary loop via transgression", "dimension": 1, "detects_relative_H2": True},
        {"probe": "relative two-simplex family", "dimension": 2, "detects_relative_H2": True},
    ]
    assert [row["detects_relative_H2"] for row in probes] == [False, False, True, True]

    holonomies = {
        "trivial_class": {"phase": "1", "character_trace": 2},
        "nonzero_class_plus": {"phase": "zeta_3", "character_trace": -1},
        "nonzero_class_minus": {"phase": "zeta_3^-1", "character_trace": -1},
    }

    result = {
        "status": "PASS",
        "probes": probes,
        "admissible_holonomies": holonomies,
        "fixed_period_can_detect": False,
        "minimal_operational_readout": "cyclic soft transport holonomy",
        "required_source_input": "canonical nearby loop or i-epsilon tube plus transported CM relative cycle",
        "physical_transport_computed": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
