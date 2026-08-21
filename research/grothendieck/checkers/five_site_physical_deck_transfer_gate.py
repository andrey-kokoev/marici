#!/usr/bin/env python3
"""Exact gate for admitting finite-deck transfer as a five-site physical readout."""

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/grothendieck/results/five-site-physical-deck-transfer-gate.json"


def main() -> None:
    sheets = tuple(range(32))
    delta0 = tuple(int(h == 0) for h in sheets)
    trace_pairing = tuple(1 for _ in sheets)
    average_pairing = tuple(Fraction(1, 32) for _ in sheets)

    simultaneous_transport_checks = sum(
        int((g == h) == ((g ^ k) == (h ^ k)))
        for g in sheets for h in sheets for k in sheets
    )
    result = {
        "schema": "marici.grothendieck.five_site_physical_deck_transfer_gate.v1",
        "deck_group": "(C2)^5",
        "deck_order": 32,
        "sheet_pairing": "<e_g,Gamma_h>=delta_(g,h)",
        "simultaneous_transport_checks": simultaneous_transport_checks,
        "selected_pairing": list(delta0),
        "orbit_trace_pairing": list(trace_pairing),
        "orbit_trace_mismatches": sum(a != b for a, b in zip(trace_pairing, delta0)),
        "normalized_average_pairing": [str(x) for x in average_pairing],
        "normalized_average_mismatches": sum(a != b for a, b in zip(average_pairing, delta0)),
        "algebraic_collapse_transfer": "For phi:(C2)^5->1, phi_!(delta_0)=1.",
        "physical_admission": False,
        "obstruction": (
            "The source-selected Gamma_+ is a local chamber vector. Replacing it by "
            "sum_g Gamma_g or its average changes the observable."
        ),
        "missing_resource": (
            "A source-derived finite deck map together with a relative-cycle trace/Gysin "
            "map fixing orientation, support, multiplicity, endpoint regularization, and normalization."
        ),
        "verdict": (
            "Unnormalized fiber-sum is canonical algebraically, but is not presently admitted "
            "as a five-site physical transfer."
        ),
    }
    assert simultaneous_transport_checks == 32 ** 3
    assert result["orbit_trace_mismatches"] == 31
    assert result["normalized_average_mismatches"] == 32
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
