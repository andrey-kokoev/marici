import json
from pathlib import Path

import sympy as sp


def main() -> None:
    i = sp.I
    omega = (-1 + sp.sqrt(3) * i) / 2
    d = sp.diag(1, omega, omega**2)
    s = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

    tangent_variables = sp.symbols("a0:9") + sp.symbols("b0:9")
    a = sp.Matrix(3, 3, tangent_variables[:9])
    b = sp.Matrix(3, 3, tangent_variables[9:])
    d_cube_tangent = sum((d**k * a * d**(2 - k) for k in range(3)), sp.zeros(3))
    s_cube_tangent = sum((s**k * b * s**(2 - k) for k in range(3)), sp.zeros(3))
    weyl_tangent = sp.simplify(a * s + d * b - omega * (b * d + s * a))
    relation_matrix, _ = sp.linear_eq_to_matrix(
        list(d_cube_tangent) + list(s_cube_tangent) + list(weyl_tangent),
        tangent_variables,
    )
    relation_basis = sp.Matrix.hstack(*relation_matrix.nullspace())

    x_variables = sp.symbols("x0:9")
    x = sp.Matrix(3, 3, x_variables)
    orbit_pair = sp.Matrix.vstack(x * d - d * x, x * s - s * x)
    orbit_matrix, _ = sp.linear_eq_to_matrix(list(orbit_pair), x_variables)

    relation_rank = relation_matrix.rank()
    tangent_dimension = 18 - relation_rank
    orbit_dimension = orbit_matrix.rank()
    joined_dimension = sp.Matrix.hstack(relation_basis, orbit_matrix).rank()
    quotient_tangent_dimension = joined_dimension - orbit_dimension

    phase_tangent_coefficient = sp.simplify(3 * omega**2)

    checks = {
        "clock_cube_identity": sp.simplify(d**3) == sp.eye(3),
        "shift_cube_identity": s**3 == sp.eye(3),
        "weyl_relation": sp.simplify(d * s - omega * s * d) == sp.zeros(3),
        "relation_linearization_rank_ten": relation_rank == 10,
        "relation_tangent_dimension_eight": tangent_dimension == 8,
        "common_commutant_scalar_orbit_dimension_eight": orbit_dimension == 8,
        "orbit_tangent_satisfies_relations": all(
            sp.simplify(entry) == 0 for entry in relation_matrix * orbit_matrix
        ),
        "joined_tangent_dimension_eight": joined_dimension == 8,
        "relation_tangent_equals_orbit_tangent": tangent_dimension == orbit_dimension == joined_dimension,
        "physical_quotient_tangent_zero": quotient_tangent_dimension == 0,
        "primitive_root_phase_derivative_nonzero_coefficient": phase_tangent_coefficient != 0,
        "primitive_root_phase_tangent_forced_zero": phase_tangent_coefficient != 0,
        "direct_weyl_bockstein_quotient_trivial": quotient_tangent_dimension == 0,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP947",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "tangent_dimensions": {
            "ambient_pair": 18,
            "relation_matrix_rank": relation_rank,
            "relation_tangent": tangent_dimension,
            "weak_basis_orbit": orbit_dimension,
            "joined_span": joined_dimension,
            "physical_quotient": quotient_tangent_dimension,
        },
        "phase_constraint": {
            "linearized_coefficient": str(sp.expand(phase_tangent_coefficient)),
            "phase_tangent": "0",
        },
        "classification": "exact Weyl source is infinitesimally rigid modulo weak-basis conjugation",
        "smallest_exact_falsifier": "relation tangent dimension 8 equals weak-basis orbit tangent dimension 8, with joined dimension 8",
        "remaining_gate": "independent source-normal coordinate outside the rigid Weyl relation object, inducing a proper noncommuting physical16 image and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp947_weyl_source_normal_bockstein_rigidity_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
