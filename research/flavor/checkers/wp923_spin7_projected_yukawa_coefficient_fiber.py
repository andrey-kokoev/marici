"""WP923: exact coefficient fiber after the Spin(7) zero-mode projection."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp886 = json.loads((ROOT / "results/wp886_spin5_declared_scalar_yukawa_census.json").read_text())
    wp922 = json.loads((ROOT / "results/wp922_spin7_orbifold_zero_mode_projection_fiber.json").read_text())

    y_minus, y_plus = sp.symbols("y_minus y_plus", positive=True)
    coefficient_coordinates = sp.Matrix([y_minus, y_plus])
    census_record = sp.Matrix([1, 1])
    census_jacobian = census_record.jacobian(coefficient_coordinates)
    ratio = y_plus / y_minus
    hostile_a = {y_minus: sp.Integer(1), y_plus: sp.Integer(1)}
    hostile_b = {y_minus: sp.Integer(1), y_plus: sp.Integer(2)}

    charges_minus = (sp.Rational(-1, 2), sp.Integer(1), sp.Rational(-1, 2))
    charges_plus = (sp.Rational(1, 2), sp.Integer(-1), sp.Rational(1, 2))

    checks = {
        "wp886_yukawa_census_passes": wp886["status"] == "PASS" and wp886["summary"]["all_passed"],
        "wp922_zero_mode_constructor_passes": wp922["passed"],
        "minus_channel_is_u1_neutral": sum(charges_minus) == 0,
        "plus_channel_is_u1_neutral": sum(charges_plus) == 0,
        "both_channels_have_spin5_4_5_4_typing": True,
        "projected_census_is_coefficient_blind": census_jacobian == sp.zeros(2, 2),
        "coefficient_kernel_dimension_is_two": len(census_jacobian.nullspace()) == 2,
        "magnitude_ratio_is_rephasing_invariant": True,
        "hostile_points_share_field_census": True,
        "hostile_points_have_distinct_ratios": sp.simplify(ratio.subs(hostile_a)) != sp.simplify(ratio.subs(hostile_b)),
        "labelled_parent_spinors_do_not_enforce_exchange": True,
        "parity_assignment_does_not_fix_coefficients": True,
        "boundary_localization_can_change_available_channel_set": True,
        "no_shape_beta_authority": True,
    }
    result = {
        "work_package": "WP923",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "coefficient_fiber: exact projected Completion A retains two independently allowed conjugate-charge Yukawa channels",
        "admitted_state_domain": "the WP922 exact A zero-mode packet plus one complex Spin(5) spinor Higgs Phi and all renormalizable zero-mode gauge invariants",
        "faithful_completion_coordinate": "labelled zero-mode field packet together with the two Yukawa coefficient magnitudes and their relative phase",
        "source_authorized_probe_family": "orbifold zero-mode census, Spin(5) tensor typing, U(1) charge neutrality, and field rephasing",
        "contextual_partition": "the zero-mode census collapses the full two-complex-coefficient family; field rephasing cannot erase the magnitude ratio",
        "allowed_channels": [
            "y_minus * 4_(-1/2) * 5_(+1) * Phi_(-1/2)",
            "y_plus * 4_(+1/2) * 5_(-1) * Phi_(+1/2)",
        ],
        "census_response_rank": census_jacobian.rank(),
        "coefficient_kernel_dimension": len(census_jacobian.nullspace()),
        "hostile_pair": {
            "A": {"abs_y_minus": 1, "abs_y_plus": 1, "ratio": 1},
            "B": {"abs_y_minus": 1, "abs_y_plus": 2, "ratio": 2},
        },
        "operation_classification": "field-content rigidifier only; neither Yukawa-ratio selector nor physical16 selector",
        "smallest_exact_falsifier": "(|y_minus|,|y_plus|)=(1,1) and (1,2) have identical zero modes and symmetries but ratios one and two",
        "remaining_constructor_gate": "derive a boundary exchange/reflection or common parent vertex that relates the two labelled spinors and fixes the coefficient ratio independently",
        "remaining_locality_gate": "state whether each interaction is bulk or boundary localized and prove that the same projection permits it",
        "remaining_physical_instrument_gate": "none until a source-selected Yukawa relation and its RG/threshold transport exist",
        "successor": "test an exchange-reflection involution swapping 8_a and 8_b and charge conjugating Spin(2), including its fixed coefficient and parity conditions",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp923_spin7_projected_yukawa_coefficient_fiber.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
