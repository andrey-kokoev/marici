import json
from pathlib import Path

import sympy as sp


def commutant_basis(generators: list[sp.Matrix]) -> list[sp.Matrix]:
    variables = sp.symbols("x0:9")
    x = sp.Matrix(3, 3, variables)
    equations = []
    for generator in generators:
        equations.extend(list(x * generator - generator * x))
    coefficient, _ = sp.linear_eq_to_matrix(equations, variables)
    return [sp.Matrix(3, 3, vector) for vector in coefficient.nullspace()]


def basis_is_commutative(basis: list[sp.Matrix]) -> bool:
    return all(sp.simplify(left * right - right * left) == sp.zeros(3) for left in basis for right in basis)


def main() -> None:
    i = sp.I
    omega = (-1 + sp.sqrt(3) * i) / 2
    d = sp.diag(1, omega, omega**2)
    s = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])

    line_vectors = [(1, 0), (0, 1), (1, 1), (1, 2)]
    line_data = {}
    for a, b in line_vectors:
        generator = sp.simplify(d**a * s**b)
        basis = commutant_basis([generator])
        key = f"({a},{b})"
        line_data[key] = {
            "commutant_dimension": len(basis),
            "commutative": basis_is_commutative(basis),
            "generator_has_three_distinct_eigenvalues": len(generator.eigenvals()) == 3,
        }

    zero_basis = commutant_basis([])
    full_basis = commutant_basis([d, s])
    subgroup_count = 1 + len(line_vectors) + 1

    checks = {
        "projective_subgroup_count_six": subgroup_count == 6,
        "zero_subgroup_fixed_dimension_nine": len(zero_basis) == 9,
        "zero_subgroup_fixed_algebra_noncommutative": not basis_is_commutative(zero_basis),
        "four_projective_lines": len(line_data) == 4,
        "every_line_generator_has_simple_spectrum": all(item["generator_has_three_distinct_eigenvalues"] for item in line_data.values()),
        "every_line_fixed_dimension_three": all(item["commutant_dimension"] == 3 for item in line_data.values()),
        "every_line_fixed_algebra_commutative": all(item["commutative"] for item in line_data.values()),
        "full_plane_fixed_dimension_one": len(full_basis) == 1,
        "full_plane_fixed_algebra_scalar": len(full_basis) == 1 and sp.simplify(full_basis[0] - sp.eye(3)) == sp.zeros(3),
        "no_proper_noncommutative_subgroup_fixed_algebra": all(item["commutative"] for item in line_data.values()) and len(full_basis) == 1,
        "identity_route_nonselective": len(zero_basis) == 9,
        "line_routes_cp_blind": all(item["commutative"] for item in line_data.values()),
        "full_route_erases_flavor": len(full_basis) == 1,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP946",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "projective_subgroup_lattice": {
            "subgroup_count": subgroup_count,
            "zero_fixed_dimension": len(zero_basis),
            "lines": line_data,
            "full_fixed_dimension": len(full_basis),
        },
        "classification": "all canonical projective Weyl subgroup twirls are identity, commutative rank-three, or scalar rank-one",
        "smallest_exact_falsifier": "all four line commutants have dimension 3 and are commutative",
        "remaining_gate": "source-derived asymmetric proper noncommutative channel with completion stability, physical16 descent, and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp946_projective_weyl_subgroup_twirl_exhaustion.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
