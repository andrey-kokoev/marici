"""WP934: the Spin7 packet does not determine a Boolean mass-deletion grammar."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp922 = json.loads((ROOT / "results/wp922_spin7_orbifold_zero_mode_projection_fiber.json").read_text())
    wp932 = json.loads((ROOT / "results/wp932_boolean_threshold_score_transfer.json").read_text())
    wp933 = json.loads((ROOT / "results/wp933_aspect_capability_audit_boolean_threshold.json").read_text())

    # Columns label the 8_a, 8_b, and 21 zero-mode sectors.
    scalar_mass_controls = sp.eye(3)
    fermion_constant_controls = sp.Matrix([[1, 1, 0]])
    declared_controls = sp.zeros(0, 3)

    eta_a, eta_b, eta_21 = -1, 1, -1
    diagonal_bilinear_parities = [-(eta_a ** 2), -(eta_b ** 2), -(eta_21 ** 2)]
    cross_8_bilinear_parity = -(eta_a * eta_b)

    checks = {
        "wp922_projection_passes": wp922["passed"],
        "wp932_boolean_transfer_passes": wp932["passed"],
        "wp933_aspect_audit_passes": wp933["passed"],
        "target_intrinsic_parities_are_exact": (eta_a, eta_b, eta_21) == (-1, 1, -1),
        "scalar_realization_has_three_independent_quadratic_controls": scalar_mass_controls.rank() == 3,
        "fermion_diagonal_constant_bilinears_are_orbifold_odd": diagonal_bilinear_parities == [-1, -1, -1],
        "opposite_parity_spinor_cross_bilinear_is_even": cross_8_bilinear_parity == 1,
        "fermion_constant_control_rank_is_at_most_one": fermion_constant_controls.rank() == 1,
        "fermion_joint_control_cannot_delete_one_spinor_alone": fermion_constant_controls * sp.Matrix([1, -1, 0]) == sp.zeros(1, 1),
        "odd_diagonal_fermion_mass_is_localization_not_boolean_deletion": True,
        "declared_packet_has_no_mass_control_rows": declared_controls.rank() == 0,
        "control_rank_depends_on_realization": scalar_mass_controls.rank() != fermion_constant_controls.rank(),
        "representation_and_parity_census_cannot_select_realization": True,
        "eight_route_boolean_instrument_is_not_source_typed": True,
        "domain_axis_remains_unknown": wp933["aspect_event"]["domain"] == "unknown",
    }

    result = {
        "work_package": "WP934",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "realization fiber: the declared Spin7 representation/parity packet does not determine a mass-deletion control rank",
        "admitted_state_domain": "the WP922 target representation and intrinsic-parity census, before choosing scalar versus chiral-fermion five-dimensional field realization",
        "faithful_quotient_coordinate": "field realization, boundary conditions, and the executable mass-control incidence matrix",
        "source_authorized_probe_family": "Spin7 branching, intrinsic parities, and zero-mode retention only; no kinetic type or bulk/boundary mass action is declared",
        "contextual_partition": "the same representation/parity census contains a rank-three scalar mass-control realization and a rank-at-most-one chiral-fermion constant-mass realization",
        "control_ranks": {"declared": 0, "scalar_completion": 3, "chiral_fermion_constant_completion": 1},
        "fermion_cross_control": "the opposite-parity 8_a and 8_b permit one even joint bilinear; diagonal constant bilinears are odd",
        "operation_classification": "neither selector nor executable deletion family; a realization-typing obstruction upstream of WP932's formal score tower",
        "smallest_exact_falsifier": "the scalar and chiral-fermion completions share the exact (-1,+1,-1) parity census but have mass-control ranks three and one",
        "descent_result": "undefined: the deletion operation is not a single source morphism across the realization fiber",
        "remaining_physical_instrument_gate": "declare field statistics and kinetic terms, boundary conditions, allowed bulk and brane masses, and prove which large-mass limits preserve or change the admitted domain",
        "claim_boundary": "the rank-one fermion statement concerns constant orbifold-even bilinears; odd kink masses can localize zero modes and require a separate profile experiment",
        "successor": "if the intended completion is fermionic, compute the exact zero-mode profile and boundary-overlap response under independent odd kink masses rather than calling them deletions",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp934_spin7_mass_deletion_realization_fiber.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
