#!/usr/bin/env python3
"""Typed census of diagnostic -> capability <- policy across four sectors."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "nima" / "results" / "cross_sector_diagnostic_capability_policy.json"


def main():
    rows = {
        "scattering": {
            "diagnostic": True,
            "capability_fiber": True,
            "source_policy_section": True,
            "evidence": "Cut event/no-event effect; U sqrt(E_empty) completion fiber; oriented Cut plus boundary jet derives elastic S",
            "scope": "instrument_density_before_laboratory_wavepacket_exposure",
        },
        "topology": {
            "diagnostic": True,
            "capability_fiber": True,
            "source_policy_section": False,
            "evidence": "syndrome record; multiple recovery chains; no source noise/cost decoder",
            "scope": "finite_toric_code",
        },
        "cosmology": {
            "diagnostic": True,
            "capability_fiber": False,
            "source_policy_section": False,
            "evidence": "connected boundary-score response exposes hidden contact packet; no state-updating successor instrument",
            "scope": "generic_transverse_contact_grade",
        },
        "flavor": {
            "diagnostic": False,
            "capability_fiber": False,
            "source_policy_section": False,
            "evidence": "faithful quotient and ambiguity census exist, but no source-derived record-producing instrument or proper-image task",
            "scope": "declared_texture_and_rg_source",
        },
    }
    assert [sum((r["diagnostic"], r["capability_fiber"], r["source_policy_section"]))
            for r in rows.values()] == [3, 2, 1, 0]
    for r in rows.values():
        assert not r["source_policy_section"] or r["capability_fiber"]
        assert not r["capability_fiber"] or r["diagnostic"]
    result = {
        "schema": "marici.cross-sector-diagnostic-capability-policy.v1",
        "criteria_order": ["diagnostic", "capability_fiber", "source_policy_section"],
        "rows": rows,
        "stage_counts": [3, 2, 1, 0],
        "verdict": "One common ordered lifting skeleton survives; only scattering currently realizes the full triple, and only at instrument-density scope.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
