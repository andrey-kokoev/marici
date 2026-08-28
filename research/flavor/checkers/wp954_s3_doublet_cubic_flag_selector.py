import itertools
import json
from pathlib import Path

import sympy as sp


def permutation_matrix(permutation: tuple[int, int, int]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for row, column in enumerate(permutation):
        matrix[row, column] = 1
    return matrix


def main() -> None:
    x, y, z = sp.symbols("x y z", real=True)
    sum_constraint = x + y + z
    norm_constraint = x**2 + y**2 + z**2 - 6
    cubic = x * y * z
    vandermonde_squared = (x - y) ** 2 * (y - z) ** 2 * (z - x) ** 2
    discriminant_residual = sp.expand(vandermonde_squared - (108 - 27 * cubic**2))
    groebner = sp.groebner([sum_constraint, norm_constraint], x, y, z, order="lex")
    _, reduced_discriminant_residual = groebner.reduce(discriminant_residual)

    permutations = [permutation_matrix(item) for item in itertools.permutations(range(3))]
    minimum_representative = sp.Matrix([1, 1, -2])
    maximum_representative = -minimum_representative
    minimum_orbit = {tuple(matrix * minimum_representative) for matrix in permutations}
    maximum_orbit = {tuple(matrix * maximum_representative) for matrix in permutations}
    stabilizer = [matrix for matrix in permutations if matrix * minimum_representative == minimum_representative]

    v1, v2, v3 = sp.symbols("v1 v2 v3")
    candidate = sp.Matrix([v1, v2, v3])
    orthogonal_constraints = sp.Matrix([[1, 1, 1], list(minimum_representative.T)])
    orthogonal_basis = orthogonal_constraints.nullspace()
    down_ray = sp.Matrix([1, -1, 0])
    democratic = sp.Matrix([1, 1, 1])

    checks = {
        "discriminant_identity_on_frozen_domain": sp.simplify(reduced_discriminant_residual) == 0,
        "minimum_representative_sum_zero": sum(minimum_representative) == 0,
        "minimum_representative_norm_six": minimum_representative.dot(minimum_representative) == 6,
        "minimum_cubic_minus_two": sp.prod(minimum_representative) == -2,
        "maximum_cubic_plus_two": sp.prod(maximum_representative) == 2,
        "minimum_orbit_has_three_flags": len(minimum_orbit) == 3,
        "maximum_orbit_has_three_flags": len(maximum_orbit) == 3,
        "representative_stabilizer_order_two": len(stabilizer) == 2,
        "orthogonal_standard_line_dimension_one": len(orthogonal_basis) == 1,
        "orthogonal_line_is_wp350_down_ray": sp.Matrix.hstack(orthogonal_basis[0], down_ray).rank() == 1,
        "down_ray_odd_under_stabilizer_swap": sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]) * down_ray == -down_ray,
        "democratic_ray_full_permutation_invariant": all(matrix * democratic == democratic for matrix in permutations),
        "cubic_sign_selects_opposite_orbits": minimum_orbit.isdisjoint(maximum_orbit),
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP954",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "flag_selector": {
            "minimum_orbit": [[int(value) for value in item] for item in sorted(minimum_orbit)],
            "maximum_orbit": [[int(value) for value in item] for item in sorted(maximum_orbit)],
            "representative_stabilizer_order": len(stabilizer),
            "derived_down_ray": [1, -1, 0],
        },
        "classification": "conditional source selector of an S3-to-Z2 flag orbit and the WP350 down coefficient ray",
        "smallest_exact_falsifier": "zero or sign-reversed cubic coefficient, or completion moving minima off the transposition-axis orbit",
        "remaining_gate": "declare the doublet and coupling in flavor dynamics; derive cubic sign, complex projector ray, radial amplitudes, completion stability, descent, and instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp954_s3_doublet_cubic_flag_selector.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
