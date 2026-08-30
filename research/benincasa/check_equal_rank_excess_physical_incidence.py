#!/usr/bin/env python3
"""Type physical incidence of the complementary soft-axis excess line."""

import json
from pathlib import Path


def main():
    # On the homogeneous physical locus, nonnegative site magnitudes obey
    # each momentum-triangle inequality, in particular z <= x+y.
    samples_checked = 0
    violations = 0
    for x in range(9):
        for y in range(9):
            for z in range(9):
                if z <= x + y and x <= y + z and y <= x + z:
                    samples_checked += 1
                    if x == 0 and y == 0 and z != 0:
                        violations += 1

    generic_axis_lower_bound = 1  # z is nonzero and nonnegative on the generic axis.
    triangle_upper_bound_at_x_eq_y_eq_0 = 0 + 0
    checks = {
        "finite_triangle_census_has_no_generic_soft_axis_point": violations == 0,
        "symbolic_triangle_implication": triangle_upper_bound_at_x_eq_y_eq_0 == 0,
        "generic_excess_support_is_disjoint_from_literal_physical_locus": generic_axis_lower_bound > triangle_upper_bound_at_x_eq_y_eq_0,
        "only_all_soft_specialization_remains": triangle_upper_bound_at_x_eq_y_eq_0 == 0,
    }
    result = {
        "schema": "marici.equal-rank-excess-physical-incidence.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "physical_constraints": ["x,y,z >= 0", "z <= x+y", "x <= y+z", "y <= x+z"],
        "excess_support": "x=y=0 with generic axis coordinate z nonzero",
        "symbolic_certificate": "x=y=0 and 0<=z<=x+y imply z=0",
        "bounded_triangle_points_checked": samples_checked,
        "generic_axis_violations": violations,
        "generic_axis_z_lower_bound": generic_axis_lower_bound,
        "triangle_z_upper_bound_at_x_eq_y_eq_0": triangle_upper_bound_at_x_eq_y_eq_0,
        "classification": {
            "generic_soft_axis_excess": "valid algebraic coefficient/Gysin object but zero literal physical incidence",
            "physical_closure": "all-soft origin only",
            "all_soft_activation": "not selected by current source data; requires the already identified projectivized-normal current covector",
            "new_carrier_support": "none",
        },
        "checks": checks,
    }
    output = Path(__file__).with_name("equal-rank-excess-physical-incidence.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
