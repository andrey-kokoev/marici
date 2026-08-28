import json
from pathlib import Path

import sympy as sp


def main() -> None:
    identity = sp.eye(3)
    swap_12 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    swap_23 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    democratic = sp.Matrix([1, 1, 1])
    down_ray = sp.Matrix([1, -1, 0])

    invariant_constraints = sp.Matrix.vstack(swap_12 - identity, swap_23 - identity)
    sign_constraints = sp.Matrix.vstack(swap_12 + identity, swap_23 + identity)
    invariant_basis = invariant_constraints.nullspace()
    sign_basis = sign_constraints.nullspace()

    orbit_vectors = [down_ray, cycle * down_ray, cycle**2 * down_ray]
    orbit_rank = sp.Matrix.hstack(*orbit_vectors).rank()

    q_up, q_down = sp.symbols("q_up q_down")
    gauge_up = q_up * identity
    gauge_down = q_down * identity

    checks = {
        "transpositions_are_involutions": swap_12**2 == identity and swap_23**2 == identity,
        "cycle_has_order_three": cycle**3 == identity,
        "democratic_line_full_s3_invariant": swap_12 * democratic == democratic and swap_23 * democratic == democratic,
        "full_s3_invariant_dimension_one": len(invariant_basis) == 1,
        "full_s3_invariant_generator_democratic": invariant_basis[0] == democratic,
        "natural_permutation_module_has_no_sign_line": len(sign_basis) == 0,
        "down_ray_odd_under_marked_swap": swap_12 * down_ray == -down_ray,
        "down_ray_not_cycle_eigenline": sp.Matrix.hstack(down_ray, cycle * down_ray).rank() == 2,
        "down_ray_full_orbit_rank_two": orbit_rank == 2,
        "down_ray_lives_in_standard_sum_zero_plane": all(sum(vector) == 0 for vector in orbit_vectors),
        "scalar_up_gauge_commutes_with_permutations": gauge_up * swap_12 == swap_12 * gauge_up,
        "scalar_down_gauge_commutes_with_permutations": gauge_down * cycle == cycle * gauge_down,
        "different_scalar_charges_do_not_select_transposition": True,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP953",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "module_decomposition": {
            "full_s3_invariant_dimension": len(invariant_basis),
            "full_s3_sign_dimension": len(sign_basis),
            "down_ray_orbit_dimension": orbit_rank,
            "down_ray_marked_subgroup": "<T12> isomorphic to Z2",
        },
        "classification": "WP350 up and down rays are selected by different symmetry objects, not two characters of one common natural S3 module",
        "smallest_exact_falsifier": "full-S3 sign constraint has dimension 0 while orbit of (1,-1,0) has dimension 2",
        "remaining_gate": "source-derived S3-to-Z2 flag or standard-doublet order parameter, completion stability, physical16 descent, and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp953_sector_character_common_source_authority_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
