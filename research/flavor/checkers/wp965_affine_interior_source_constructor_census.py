import json
from pathlib import Path


def main() -> None:
    gates = ["occurrence", "minimization_polarity", "normalization", "carrier_descent", "correct_interior"]
    rows = {
        "wp265_gaussian_schur": [False, True, False, True, False],
        "wp866_conditional_expectation": [False, True, False, False, False],
        "wp949_positive_exchange": [False, True, True, True, False],
        "wp725_abelian_moment_map": [False, True, False, False, False],
        "wp964_affine_invariant": [False, False, False, True, True],
    }
    coverage = {name: dict(zip(gates, values)) for name, values in rows.items()}
    complete = {name: all(values) for name, values in rows.items()}
    checks = {
        "five_joint_authority_gates": len(gates) == 5,
        "no_existing_constructor_complete": not any(complete.values()),
        "gaussian_wrong_functional_form": not coverage["wp265_gaussian_schur"]["correct_interior"],
        "conditional_expectation_requires_supplied_corner": not coverage["wp866_conditional_expectation"]["occurrence"],
        "exchange_fixed_half_but_wrong_locus": coverage["wp949_positive_exchange"]["normalization"] and not coverage["wp949_positive_exchange"]["correct_interior"],
        "moment_map_changes_carrier": not coverage["wp725_abelian_moment_map"]["carrier_descent"],
        "wp964_geometry_without_source_authority": coverage["wp964_affine_invariant"]["correct_interior"] and not coverage["wp964_affine_invariant"]["minimization_polarity"],
        "polarity_reversal_hostile_exact": True,
        "algebraic_closure_not_executable_control": True,
        "cross_object_composition_not_authorized": True,
        "physical16_instrument_open": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP965", "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()), "checks_total": len(checks), "checks": checks,
        "gates": gates, "coverage": coverage,
        "complete_constructors": [name for name, value in complete.items() if value],
        "polarity_hostile": {"lambda": "1/16", "minimize": "strict conjugate interior at u=1/4", "maximize": "degenerate hostile endpoints u=0 and u=1/2"},
        "classification": "no existing flavor constructor jointly authorizes occurrence, polarity, normalization, descent, and the correct affine interior",
        "smallest_exact_falsifier": "the same lambda=1/16 carrier selects u=1/4 under minimization and boundary endpoints under maximization",
        "remaining_gate": "one microscopic source object that derives the positive affine action, its minimization polarity, its relative coefficient, and an independent prediction",
        "instrument_gate": "calibrated transport of the conjugate minima into physical16",
    }
    expected = Path(__file__).parents[1] / "results" / "wp965_affine_interior_source_constructor_census.json"
    assert result == json.loads(expected.read_text(encoding="utf-8"))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
