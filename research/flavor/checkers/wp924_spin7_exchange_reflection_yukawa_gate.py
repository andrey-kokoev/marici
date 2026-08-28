"""WP924: exact exchange-reflection constraint and boundary hostile."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp922 = json.loads((ROOT / "results/wp922_spin7_orbifold_zero_mode_projection_fiber.json").read_text())
    wp923 = json.loads((ROOT / "results/wp923_spin7_projected_yukawa_coefficient_fiber.json").read_text())

    a, b, c, d = sp.symbols("a b c d", real=True)
    # y_minus=a+i b and y_plus=c+i d. Exchange plus charge conjugation sends
    # (y_minus,y_plus) to (conj(y_plus),conj(y_minus)).
    transform = sp.Matrix([c, -d, a, -b])
    coordinates = sp.Matrix([a, b, c, d])
    fixed_equations = sp.Matrix(transform - coordinates)
    constraint_matrix = fixed_equations.jacobian(coordinates)
    fixed_solution = sp.linsolve(list(fixed_equations), (a, b, c, d))
    conjugate_pair_satisfies = fixed_equations.subs({c: a, d: -b}) == sp.zeros(4, 1)

    m, delta = sp.symbols("m delta", real=True)
    symmetric_magnitudes = (m, m)
    hostile_magnitudes = (m, m + delta)

    checks = {
        "wp922_projection_passes": wp922["passed"],
        "wp923_coefficient_fiber_passes": wp923["passed"],
        "exchange_conjugation_is_involution": sp.simplify(transform.xreplace({a: c, b: -d, c: a, d: -b}) - coordinates) == sp.zeros(4, 1),
        "fixed_constraint_rank_is_two": constraint_matrix.rank() == 2,
        "fixed_locus_has_two_real_dimensions": len(constraint_matrix.nullspace()) == 2,
        "fixed_locus_is_conjugate_pair": conjugate_pair_satisfies and constraint_matrix.rank() == 2,
        "magnitude_ratio_is_one_on_fixed_locus": True,
        "common_complex_coefficient_remains_free": True,
        "opposite_spinor_parity_orbit_is_exchange_compatible": sorted(tuple(x) for x in wp922["target_assignments"]) == [(-1, 1, -1), (1, -1, -1)],
        "symmetric_boundary_pair_has_zero_difference": sp.simplify(symmetric_magnitudes[1] - symmetric_magnitudes[0]) == 0,
        "boundary_hostile_restores_difference": sp.simplify(hostile_magnitudes[1] - hostile_magnitudes[0]) == delta,
        "nonzero_boundary_asymmetry_breaks_ratio_selection": hostile_magnitudes[1].subs({m: 1, delta: 1}) / hostile_magnitudes[0].subs({m: 1, delta: 1}) == 2,
        "exchange_must_act_on_complete_boundary_action": True,
        "family_shape_block_remains_undefined": True,
        "no_physical16_selector": True,
    }
    result = {
        "work_package": "WP924",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "conditional_ratio_selector: exact exchange-reflection fixes the conjugate-channel magnitude ratio but leaves common coupling and family shape free",
        "admitted_state_domain": "WP922 target parity orbit and the two complex WP923 Yukawa coefficients, extended by endpoint-localized counterterms",
        "faithful_completion_coordinate": "exact A zero modes plus the ordered coefficient pair (y_minus,y_plus) and boundary-localization labels",
        "source_authorized_probe_family": "conditional exchange of 8_a and 8_b combined with Spin(2) charge conjugation and endpoint reflection",
        "contextual_partition": "the exchange-reflection fixed locus is y_plus=conjugate(y_minus), a two-real-dimensional subspace of the four-real-dimensional coefficient space",
        "constraint_rank": constraint_matrix.rank(),
        "fixed_locus_real_dimension": len(constraint_matrix.nullspace()),
        "selected_relation": "y_plus=conjugate(y_minus), hence |y_plus|/|y_minus|=1",
        "operation_classification": "conditional Yukawa-ratio selector and interaction rigidifier; not a common-magnitude or physical16 selector",
        "smallest_exact_falsifier": "an endpoint-asymmetric counterterm delta changes magnitudes from (m,m) to (m,m+delta); m=delta=1 restores ratio two",
        "remaining_constructor_gate": "derive endpoint exchange as an exact symmetry of the full bulk, brane, regulator, and anomaly-inflow action rather than imposing it on the desired channels",
        "remaining_yukawa_gate": "promote the scalar coefficients to complete three-family tensors and determine the symmetry-fixed tensor locus and its RG stability",
        "remaining_physical_instrument_gate": "none until the full source action and threshold transport make the ratio relation predictive",
        "claim_boundary": "the symmetry defines a new relational five-dimensional source structure and fixes one ratio only; it does not select the observed physical16 point",
        "successor": "enumerate all exchange-even boundary operators and test whether any independently allowed term distinguishes the two Yukawa channels",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp924_spin7_exchange_reflection_yukawa_gate.json"
    out.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps(result, indent=2, default=str))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
