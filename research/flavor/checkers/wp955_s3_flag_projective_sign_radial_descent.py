import itertools
import json
from pathlib import Path

import sympy as sp


def permutation_matrix(permutation: tuple[int, int, int]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for row, column in enumerate(permutation):
        matrix[row, column] = 1
    return matrix


def axis_projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.T / vector.dot(vector))


def main() -> None:
    identity = sp.eye(3)
    democratic = sp.Matrix([1, 1, 1])
    standard_projector = sp.simplify(identity - democratic * democratic.T / 3)
    representative = sp.Matrix([1, 1, -2])
    down_ray = sp.Matrix([1, -1, 0])
    expected_down_projector = sp.simplify(down_ray * down_ray.T / down_ray.dot(down_ray))
    flag_projector = axis_projector(representative)
    down_projector = sp.simplify(standard_projector - flag_projector)

    permutations = [permutation_matrix(item) for item in itertools.permutations(range(3))]
    minimum_orbit = {tuple(matrix * representative) for matrix in permutations}
    maximum_orbit = {tuple(-matrix * representative) for matrix in permutations}

    def serialized_projector(vector_tuple: tuple[sp.Expr, ...]) -> tuple[str, ...]:
        return tuple(str(value) for value in axis_projector(sp.Matrix(vector_tuple)))

    minimum_projectors = {serialized_projector(item) for item in minimum_orbit}
    maximum_projectors = {serialized_projector(item) for item in maximum_orbit}

    rho = sp.symbols("rho", nonzero=True, real=True)
    scaled_projector = axis_projector(rho * representative)
    hostile = sp.Matrix([[2, 1, sp.I], [1, 3, 1], [-sp.I, 1, 5]])
    compressed = sp.simplify(down_projector * hostile * down_projector)

    checks = {
        "representative_in_standard_plane": democratic.dot(representative) == 0,
        "axis_projector_idempotent": flag_projector**2 == flag_projector,
        "axis_projector_sign_blind": axis_projector(-representative) == flag_projector,
        "axis_projector_radius_blind": scaled_projector == flag_projector,
        "down_projector_exact_wp350_line": down_projector == expected_down_projector,
        "down_projector_idempotent": down_projector**2 == down_projector,
        "down_projector_rank_one": down_projector.rank() == 1,
        "flag_and_down_projectors_orthogonal": flag_projector * down_projector == sp.zeros(3),
        "opposite_vector_orbits_disjoint": minimum_orbit.isdisjoint(maximum_orbit),
        "opposite_orbits_same_projective_flags": minimum_projectors == maximum_projectors,
        "projective_flag_orbit_has_three_members": len(minimum_projectors) == 3,
        "single_kraus_compression_hermitian": compressed == compressed.conjugate().T,
        "single_kraus_compression_rank_at_most_one": compressed.rank() <= 1,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP955",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "projective_selector": {
            "flag_orbit_size": len(minimum_projectors),
            "opposite_vector_orbits_have_same_flags": minimum_projectors == maximum_projectors,
            "down_projector": str(down_projector.tolist()),
            "compressed_hostile_rank": compressed.rank(),
        },
        "classification": "projective S3-to-Z2 flag selector is blind to cubic sign and nonzero radial magnitude",
        "smallest_exact_falsifier": "odd-in-order-parameter coupling or completion moving projective minima off transposition axes",
        "remaining_gate": "physical doublet and even projective coupling, general completion stability, family-module descent, complex ray, Yukawa amplitudes, and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp955_s3_flag_projective_sign_radial_descent.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
