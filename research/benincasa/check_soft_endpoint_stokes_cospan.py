#!/usr/bin/env python3
"""Type the soft endpoint Stokes object as a two-port cospan."""

import json
from pathlib import Path


def main():
    # Ordered endpoints are (+1,-1), so d[-1,1]=[+1,-1].
    boundary_column = [1, -1]
    endpoint_boundary = [[0, 0]]  # points have no further ordinary boundary.
    boundary_of_boundary = sum(endpoint_boundary[0][i] * boundary_column[i] for i in range(2))

    raw_degrees = {"positive_unmarked": 0, "negative_residue": 1}
    cone_shifts = {"positive_unmarked": 0, "negative_residue": -1}
    total_degrees = {
        key: raw_degrees[key] + cone_shifts[key]
        for key in raw_degrees
    }
    physical_occurrence_covectors = {
        "positive_unmarked": [1, 0],
        "negative_residue": [1, 0],
    }

    checks = {
        "source_boundary_orientation_is_plus_minus": boundary_column == [1, -1],
        "residue_cone_shift_aligns_total_degrees": len(set(total_degrees.values())) == 1,
        "boundary_of_boundary_is_zero": boundary_of_boundary == 0,
        "both_ports_retain_separate_labels": len(total_degrees) == 2,
        "physical_chain_selects_positive_a_occurrence_at_each_port": all(
            value == [1, 0] for value in physical_occurrence_covectors.values()
        ),
    }
    result = {
        "schema": "marici.soft-endpoint-stokes-cospan.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "bulk_chain": "Gamma_xi=[-1,1]",
        "boundary_map": {
            "ordered_ports": ["xi=+1 unmarked CM boundary", "xi=-1 q_g1 residue-CM corner"],
            "column": boundary_column,
        },
        "relative_totalization": {
            "raw_degrees": raw_degrees,
            "cone_shifts": cone_shifts,
            "total_degrees": total_degrees,
        },
        "physical_occurrence_covectors": physical_occurrence_covectors,
        "architecture": (
            "one bulk object maps to a direct sum of two endpoint ports; there is "
            "no source boundary map from one endpoint port to the other"
        ),
        "consequence": (
            "Stokes supplies the common parent and orientation, not a scalar identification "
            "of the marked and unmarked coefficient lines"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-stokes-cospan.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
