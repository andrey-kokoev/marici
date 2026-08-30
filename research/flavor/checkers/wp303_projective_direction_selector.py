"""WP303: exact projective selector and normalization-lift obstruction."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def projective_coordinate(vector):
    if vector[1] == 0:
        raise ValueError("declared affine chart requires second coordinate nonzero")
    return sp.simplify(vector[0] / vector[1])


def normalized_lift(direction, radius):
    norm = sp.sqrt((direction.T * direction)[0])
    return sp.simplify(radius * direction / norm)


def main():
    first = sp.Matrix([1, 1])
    second = sp.Matrix([2, 2])
    off_direction = sp.Matrix([1, 2])
    projective_first = projective_coordinate(first)
    projective_second = projective_coordinate(second)
    projective_off = projective_coordinate(off_direction)
    unit_lift = normalized_lift(first, 1)
    double_lift = normalized_lift(first, 2)

    checks = {
        "rival_amplitudes_define_same_projective_point": projective_first == projective_second == 1,
        "off_direction_is_separated_projectively": projective_off == sp.Rational(1, 2) and projective_off != projective_first,
        "swap_fixed_projective_locus_is_singleton_in_chart": projective_coordinate(sp.Matrix([sp.symbols("lambda", positive=True)] * 2)) == 1,
        "different_normalizations_lift_to_distinct_physical_points": unit_lift != double_lift,
        "unit_lift_has_declared_norm": sp.simplify((unit_lift.T * unit_lift)[0]) == 1,
        "double_lift_has_declared_norm": sp.simplify((double_lift.T * double_lift)[0]) == 4,
        "both_lifts_retain_selected_projective_coordinate": projective_coordinate(unit_lift) == projective_coordinate(double_lift) == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP303",
        "admitted_projective_domain": "positive two-coordinate rays modulo x~lambda*x for lambda>0, in the chart x_2 nonzero",
        "projective_selector": "swap symmetry selects the singleton ray [1:1]",
        "projective_hostile_packets": {
            "first_vector": ["1", "1"],
            "second_vector": ["2", "2"],
            "shared_projective_coordinate": str(projective_first),
        },
        "normalization_lifts": [
            {"radius": "1", "point": [str(value) for value in unit_lift]},
            {"radius": "2", "point": [str(value) for value in double_lift]},
        ],
        "descent": "the direction selector descends under positive rescaling only on the explicitly changed projective groupoid",
        "classification": "genuine projective ratio selector and direction rigidifier; not a full physical16 selector until a source-derived physical normalization lifts the ray",
        "smallest_exact_falsifier": "the rays represented by (1,1) and (2,2) are identical projectively but give distinct normalized physical lifts at radii 1 and 2",
        "first_missing_arrow": "selected projective ray -> source-normalized physical16 point",
        "remaining_physical_instrument_gate": "show that positive rescaling is an admitted redundancy for the targeted flavor lens, then derive and calibrate the normalization radius if absolute masses or magnitudes are physical",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp303_projective_direction_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
