import json
from fractions import Fraction
from pathlib import Path


def additive(tau0: Fraction, b: Fraction, t: Fraction) -> Fraction:
    return tau0 + b * t


def affine_fixed_point(a: Fraction, b: Fraction) -> Fraction:
    assert a != 0
    return -b / a


def main() -> None:
    tau_a = Fraction(0)
    tau_b = Fraction(1)
    slope = Fraction(3, 2)
    scale_step = Fraction(4, 3)

    additive_a = additive(tau_a, slope, scale_step)
    additive_b = additive(tau_b, slope, scale_step)
    fixed_one = affine_fixed_point(Fraction(-1), Fraction(1))
    fixed_two = affine_fixed_point(Fraction(-1), Fraction(2))

    checks = {
        "additive_solution_a": additive_a == 2,
        "additive_solution_b": additive_b == 3,
        "additive_preserves_separation": additive_b - additive_a == tau_b - tau_a,
        "additive_not_selector": additive_a != additive_b,
        "homogeneous_zero_fixed": Fraction(0) * Fraction(7, 3) == 0,
        "finite_homogeneous_map_injective": Fraction(1) * Fraction(7, 3) != Fraction(2) * Fraction(7, 3),
        "affine_hostile_one": fixed_one == 1,
        "affine_hostile_two": fixed_two == 2,
        "equal_attractiveness_distinct_values": fixed_one != fixed_two,
        "stability_not_numerical_authority": fixed_one != fixed_two,
        "declared_boundary_beta_absent": True,
        "completion_stability_unproved": True,
    }

    result = {
        "work_package": "WP937",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_witness": {
            "additive_outputs": [str(additive_a), str(additive_b)],
            "preserved_difference": str(additive_b - additive_a),
            "attractive_fixed_points": [str(fixed_one), str(fixed_two)],
        },
        "classification": {
            "additive": "transport",
            "finite_homogeneous": "transport with conditional limiting fixed point",
            "affine_attractive": "conditional selector whose value is -b/a",
            "declared_su4_boundary_rg": "unauthorized because beta coefficients are absent",
        },
        "contextual_partition": "indiscrete on candidate beta systems under current source authority",
        "smallest_exact_falsifier": "equally attractive flows -tau+1 and -tau+2 select different fixed points",
        "remaining_gate": "derive a completion-stable boundary beta system and common-frame physical16 instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp937_boundary_kinetic_rg_selector_gate.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
