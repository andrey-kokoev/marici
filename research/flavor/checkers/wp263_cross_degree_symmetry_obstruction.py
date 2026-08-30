"""WP263: exact obstruction to fixing cross-degree selector coefficients by linear symmetry."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def homogeneous_degrees(polynomial, variables):
    poly = sp.Poly(sp.expand(polynomial), *variables)
    return sorted({sum(monomial) for monomial, _ in poly.terms()})


def main():
    # A generic invertible linear field transformation in two coordinates.
    u, v = sp.symbols("u v")
    p, q, r, s = sp.symbols("p q r s")
    transformed = {u: p * u + q * v, v: r * u + s * v}

    degree_four = (u**2 + v**2) ** 2
    degree_eight = degree_four**2
    degree_four_transformed = sp.expand(degree_four.subs(transformed, simultaneous=True))
    degree_eight_transformed = sp.expand(degree_eight.subs(transformed, simultaneous=True))

    scale = sp.symbols("scale", nonzero=True)
    scale_four = sp.expand(degree_four.subs({u: scale * u, v: scale * v}, simultaneous=True))
    scale_eight = sp.expand(degree_eight.subs({u: scale * u, v: scale * v}, simultaneous=True))

    # No constant k can identify a nonzero degree-four polynomial with a
    # degree-eight one. Coefficient comparison leaves only the zero map.
    k = sp.symbols("k")
    cross_degree_residual = sp.Poly(sp.expand(degree_eight - k * degree_four), u, v)
    coefficient_equations = [sp.Eq(coefficient, 0) for coefficient in cross_degree_residual.coeffs()]
    cross_degree_solutions = sp.solve(coefficient_equations, [k], dict=True)

    checks = {
        "linear_substitution_preserves_degree_four": homogeneous_degrees(degree_four_transformed, (u, v)) == [4],
        "linear_substitution_preserves_degree_eight": homogeneous_degrees(degree_eight_transformed, (u, v)) == [8],
        "uniform_scaling_weight_is_four": sp.simplify(scale_four - scale**4 * degree_four) == 0,
        "uniform_scaling_weight_is_eight": sp.simplify(scale_eight - scale**8 * degree_eight) == 0,
        "no_constant_cross_degree_identification": cross_degree_solutions == [],
        "operator_degree_blocks_are_disjoint": set(homogeneous_degrees(degree_four_transformed, (u, v))).isdisjoint(homogeneous_degrees(degree_eight_transformed, (u, v))),
        "deliberate_linear_exchange_claim_fails": homogeneous_degrees(degree_four_transformed, (u, v)) != homogeneous_degrees(degree_eight, (u, v)),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP263",
        "theorem_domain": "polynomial source actions under invertible linear transformations of the underlying flavon/Gram coordinates",
        "selector_operators": {
            "commutator_invariant": "I4 with homogeneous field degree 4",
            "commutator_square": "I4^2 with homogeneous field degree 8",
        },
        "transformed_degree_support": {
            "I4": homogeneous_degrees(degree_four_transformed, (u, v)),
            "I4_squared": homogeneous_degrees(degree_eight_transformed, (u, v)),
        },
        "cross_degree_identification_solutions": cross_degree_solutions,
        "classification": "ordinary linear source symmetries cannot fix the relative coefficient between the minimal interior-selector operators because they occupy distinct homogeneous-degree blocks",
        "smallest_exact_falsifier": "under uniform field scaling I4 has weight 4 while I4^2 has weight 8, so no nonzero constant linear symmetry exchanges them",
        "remaining_authority_gate": "a dimensionful spurion, nonlinear symmetry, radiative matching relation, or other microscopic constructor that explicitly joins the degree-four and degree-eight coefficient sectors",
        "scope_limit": "does not exclude nonlinear/duality transformations, supersymmetric relations with added multiplets, or a microscopic matching calculation; each is additional source structure",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp263_cross_degree_symmetry_obstruction.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
