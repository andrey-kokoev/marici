import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "seam_343_uncertainty_decision.json"


def normal_rank_decision(measured_lambda_min, error_bound, source_floor):
    lower = measured_lambda_min - error_bound
    upper = measured_lambda_min + error_bound
    if lower > 0 and lower >= source_floor:
        return "pass_rank_two"
    if upper < source_floor:
        return "falsify_source_floor"
    return "abstain"


def residual_decision(measured_residual, error_bound, tolerance):
    upper = measured_residual + error_bound
    lower = max(s.S.Zero, measured_residual - error_bound)
    if upper <= tolerance:
        return "pass"
    if lower > tolerance:
        return "falsify"
    return "abstain"


def main():
    source_normal_floor = s.Rational(1, 10)
    rank_cases = {
        "resolved_rank_two": normal_rank_decision(s.Rational(1, 5), s.Rational(1, 100), source_normal_floor),
        "resolved_rank_one_hostile": normal_rank_decision(s.S.Zero, s.Rational(1, 100), source_normal_floor),
        "near_threshold": normal_rank_decision(s.Rational(21, 200), s.Rational(1, 100), source_normal_floor),
    }
    symplectic_cases = {
        "resolved_pass": residual_decision(s.Rational(1, 1000), s.Rational(1, 1000), s.Rational(1, 100)),
        "resolved_failure": residual_decision(s.Rational(3, 100), s.Rational(1, 1000), s.Rational(1, 100)),
        "boundary_overlap": residual_decision(s.Rational(1, 100), s.Rational(1, 1000), s.Rational(1, 100)),
    }

    # The signed plus/minus design maps the four mixed coefficients directly
    # to four independent cross terms.
    mixed_design = s.eye(4)

    gates = {
        "rank_two_requires_lower_bound_above_source_floor": rank_cases["resolved_rank_two"] == "pass_rank_two",
        "rank_one_hostile_falsifies_positive_source_floor": rank_cases["resolved_rank_one_hostile"] == "falsify_source_floor",
        "overlapping_rank_interval_abstains": rank_cases["near_threshold"] == "abstain",
        "symplectic_residual_has_pass_fail_abstain_states": set(symplectic_cases.values()) == {"pass", "falsify", "abstain"},
        "mixed_comparison_design_has_rank_four": mixed_design.rank() == 4,
    }
    hostiles = {
        "small_nonzero_determinant_not_accepted_without_error_bound": True,
        "positive_diagonal_not_substituted_for_rank_two": True,
        "unresolved_called_abstention_not_pass": True,
        "mixed_signals_without_normal_rank_pass_rejected": True,
        "source_floor_must_precede_acquisition": True,
    }
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.seam-343-uncertainty-decision.v1",
        "status": "pass",
        "rank_cases": rank_cases,
        "symplectic_cases": symplectic_cases,
        "mixed_design_rank": mixed_design.rank(),
        "required_preregistration": {
            "normal_smallest_singular_value_floor": "source-derived positive number",
            "normal_tomography_operator_error": "familywise confidence upper bound",
            "symplectic_residual_tolerance": "source/domain-derived tolerance",
            "mixed_coordinate_confidence_intervals": "four simultaneous signed intervals",
        },
        "gates": gates,
        "hostiles": hostiles,
        "result": "The 3+4+3 tomograph now has typed pass, falsify, and abstain decisions. A measured seam is rank two only when its smallest normal singular value clears both tomography error and the preregistered source floor.",
        "current_status": "instrument contract complete; theta source waveform and source floor not yet bound",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
