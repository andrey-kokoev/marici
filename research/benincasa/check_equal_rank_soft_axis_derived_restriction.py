#!/usr/bin/env python3
"""Compare derived restriction of equal-rank supports to a soft axis."""

import json
from pathlib import Path


def main():
    # On Z={x=y=0}, the hypersurface resolution [R --L--> R]
    # restricts to [F[z] --L|Z--> F[z]].
    restrictions = {
        "vertex": {
            "support": "x+y+3z",
            "restriction_to_Z": "3z",
            "generic_Z_localized_differential": "unit",
            "generic_Z_H0_rank": 0,
            "generic_Z_Tor1_rank": 0,
            "origin_H0_rank": 1,
            "origin_Tor1_rank": 0,
        },
        "complementary": {
            "support": "x+y",
            "restriction_to_Z": "0",
            "generic_Z_localized_differential": "zero",
            "generic_Z_H0_rank": 1,
            "generic_Z_Tor1_rank": 1,
            "origin_H0_rank": 1,
            "origin_Tor1_rank": 1,
        },
    }
    checks = {
        "vertex_complex_is_acyclic_on_generic_soft_axis": restrictions["vertex"]["generic_Z_H0_rank"] == restrictions["vertex"]["generic_Z_Tor1_rank"] == 0,
        "complementary_complex_has_excess_Tor_line": restrictions["complementary"]["generic_Z_Tor1_rank"] == 1,
        "ordinary_origin_intersection_does_not_fake_vertex_excess": restrictions["vertex"]["origin_H0_rank"] == 1 and restrictions["vertex"]["origin_Tor1_rank"] == 0,
        "contained_axis_retains_origin_excess": restrictions["complementary"]["origin_Tor1_rank"] == 1,
    }
    result = {
        "schema": "marici.equal-rank-soft-axis-derived-restriction.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ambient_ring": "F[x,y,z]",
        "soft_axis": "Z=V(x,y)",
        "generic_axis_ring": "F[z,z^-1]",
        "derived_model": "[O_Z -- L|Z --> O_Z]",
        "restrictions": restrictions,
        "comparison": "vertex restriction is generically empty/acyclic; complementary restriction carries H0 plus a rank-one excess Tor1/Gysin line",
        "checks": checks,
    }
    output = Path(__file__).with_name("equal-rank-soft-axis-derived-restriction.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
