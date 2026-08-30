#!/usr/bin/env python3
"""Audit projective-infinity decay of the frozen localized C9 contour."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "nine-site-canonical-contour-packet.json"
TARGET = ROOT / "results" / "c9-contour-infinity-decay.json"


def main() -> None:
    packet = json.loads(SOURCE.read_text(encoding="utf-8"))
    localization = packet["localization_basis"]
    free = localization["unfixed_contour_variables"]
    rows = []
    for index, variable in enumerate(free):
        dependent = [
            denominator["contour_variable"]
            for denominator in localization["localized_denominators"]
            if denominator["unfixed_coefficients"][index] != "0"
        ]
        denominator_degree = 1 + len(dependent)  # includes dc/(c-i epsilon)
        vanishing_order = denominator_degree - 2  # c=1/s and dc=-ds/s^2
        rows.append(
            {
                "variable": variable,
                "own_pole_count": 1,
                "dependent_localized_poles": dependent,
                "denominator_degree": denominator_degree,
                "projective_infinity_vanishing_order": vanishing_order,
                "infinity_residue": "zero" if vanishing_order >= 0 else "possible",
            }
        )
    assert len(rows) == 9
    assert all(row["denominator_degree"] == 4 for row in rows)
    assert all(row["projective_infinity_vanishing_order"] == 2 for row in rows)
    result = {
        "schema": "marici.c9_contour_infinity_decay.v1",
        "source": str(SOURCE.relative_to(ROOT.parent.parent)),
        "source_equations": ["arXiv:2305.19686v2 (4.1)-(4.4)"],
        "contour": "R^9 with each variable closed in UHP or LHP",
        "variables": rows,
        "all_infinity_residues_zero": True,
        "scope": "the frozen scalar canonical contour; no claim about a differently typed carrier-parameter relative chain",
    }
    TARGET.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"variables": 9, "vanishing_order": 2, "all_infinity_residues_zero": True}))


if __name__ == "__main__":
    main()
