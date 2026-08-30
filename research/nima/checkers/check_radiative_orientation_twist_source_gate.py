#!/usr/bin/env python3
"""Bounded provenance gate for the radiative orientation-twist test."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "radiative_orientation_twist_source_gate.json"


def main() -> None:
    # These booleans encode presence in the frozen Strominger source packets,
    # not physical equivalences inferred from suggestive terminology.
    source = {
        "celestial_antipodal_map": True,
        "i_minus_i_plus_antipodal_matching": True,
        "corner_magnetic_parity_condition": True,
        "physical_spatial_parity_action_on_radiative_line": False,
        "physical_time_reversal_action_i_plus_i_minus": False,
        "carrier_road_reflection_comparison": False,
        "carrier_core_exchange_comparison": False,
    }

    forbidden_substitutions = {
        "antipodal_is_spatial_orientation_character": False,
        "magnetic_parity_is_time_reversal_character": False,
        "external_matching_is_derived_carrier_comparison": False,
    }

    required = (
        source["physical_spatial_parity_action_on_radiative_line"],
        source["physical_time_reversal_action_i_plus_i_minus"],
        source["carrier_road_reflection_comparison"],
        source["carrier_core_exchange_comparison"],
    )
    theorem_admitted = all(required)
    assert not theorem_admitted
    assert not any(forbidden_substitutions.values())

    result = {
        "status": "PASS",
        "source_presence": source,
        "forbidden_substitutions": forbidden_substitutions,
        "radiative_cross_sector_twist_theorem_admitted": theorem_admitted,
        "classification": "provenance_gate_open",
        "missing_finite_packet": [
            "P action and character on a named radiative orientation line",
            "T action and character exchanging future and past null infinity",
            "orientation sign in antipodal matching",
            "typed comparison with Carrier road reflection and core exchange",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
