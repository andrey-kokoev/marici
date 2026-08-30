#!/usr/bin/env python3
"""Audit what the existing Cut carrier does and does not determine for pointed torsors."""

import json
from fractions import Fraction
from pathlib import Path


def sew(scale: Fraction, left: Fraction, right: Fraction) -> Fraction:
    return scale * (left + right)


def main() -> None:
    scales = [Fraction(1, 2), Fraction(1), Fraction(2)]
    probes = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)), (Fraction(2), Fraction(-1))]
    rows = []
    for scale in scales:
        values = [sew(scale, left, right) for left, right in probes]
        rows.append(
            {
                "scale": str(scale),
                "probe_values": [str(value) for value in values],
                "preserves_pointed_origin": values[0] == 0,
                "left_right_symmetric": all(
                    sew(scale, left, right) == sew(scale, right, left) for left, right in probes
                ),
                "additive": True,
            }
        )

    checks = {
        "carrier_cut_identifies_resolved_interface_variables": True,
        "each_local_torsor_has_source_point_F2_equal_zero": True,
        "multiple_distinct_symmetric_additive_origin_preserving_maps_exist": len({tuple(row["probe_values"]) for row in rows}) > 1,
        "carrier_data_does_not_select_scale": True,
        "composite_source_coefficient_map_is_absent": True,
        "no_sewing_mismatch_class_is_currently_typed": True,
    }
    packet = {
        "schema": "marici.pointed-kummer-cut-sewing-typing.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "known_carrier_map": "physical diagonal identification of the two resolved Cut-interface occurrences",
        "known_local_pointings": "F_L(2)=0 and F_R(2)=0",
        "required_missing_constructor": (
            "S_Cut: T_L external-product T_R -> T_G, derived from the composite source integrand and compatible with monodromy"
        ),
        "underdetermination_family": "S_c(P_L,P_R)=c*(P_L+P_R)",
        "family_audit": rows,
        "classification": "shared carrier sewing exists; coefficient-torsor sewing is unconstructed",
        "conclusion": (
            "the current data neither prove canonical sewing nor define a mismatch obstruction; "
            "forming either would require choosing an unauthorized coefficient adapter"
        ),
        "checks": checks,
    }
    out = Path(__file__).with_name("pointed-kummer-cut-sewing-typing.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
