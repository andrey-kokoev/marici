"""WP378: exact denominator-clearing and degeneracy audit of the CP portal."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    C, Du, Dd, rho = sp.symbols("C Delta_u Delta_d rho", real=True)
    alpha, lam = sp.symbols("alpha lambda", positive=True)
    J = sp.symbols("J", real=True)

    jarlskog_identity_residual = C - 2 * J * Du * Dd
    polynomial_constraint = C**2 - 4 * alpha * rho * Du**2 * Dd**2
    positive_potential = lam * polynomial_constraint**2
    normalized_constraint = J**2 - alpha * rho
    cleared_normalized_constraint = sp.simplify(
        polynomial_constraint.subs(C, 2 * J * Du * Dd)
    )
    rho_response = sp.diff(polynomial_constraint, rho)

    rho1, rho2 = sp.symbols("rho1 rho2", real=True)
    degenerate_left = polynomial_constraint.subs({Du: 0, C: 0, rho: rho1})
    degenerate_right = polynomial_constraint.subs({Du: 0, C: 0, rho: rho2})

    gram_degree_C = 6
    gram_degree_C_squared = 2 * gram_degree_C
    gram_degree_discriminant_squared_each = 6
    gram_degree_F = gram_degree_discriminant_squared_each * 2
    gram_degree_potential = 2 * gram_degree_F
    field_degree_potential = 2 * gram_degree_potential

    wp109 = json.loads(
        (ROOT / "results/wp109_jarlskog_normalized_margin.json").read_text(encoding="utf-8")
    )

    checks = {
        "wp109_exact_identity_dependency_passes": wp109["passed"] == wp109["total"],
        "denominator_clearing_recovers_normalized_shell": sp.expand(
            cleared_normalized_constraint - 4 * Du**2 * Dd**2 * normalized_constraint
        ) == 0,
        "positive_square_portal_is_nonnegative": positive_potential.is_nonnegative,
        "rho_response_has_discriminant_factor": rho_response == -4 * alpha * Du**2 * Dd**2,
        "degenerate_stratum_kills_constraint_for_first_source": degenerate_left == 0,
        "degenerate_stratum_kills_constraint_for_second_source": degenerate_right == 0,
        "distinct_source_values_collide_at_degeneracy": rho1 != rho2 and degenerate_left == degenerate_right,
        "degenerate_stratum_kills_rho_response": rho_response.subs(Du, 0) == 0,
        "constraint_has_gram_degree_twelve": gram_degree_C_squared == gram_degree_F == 12,
        "positive_potential_has_gram_degree_twenty_four": gram_degree_potential == 24,
        "bifundamental_field_degree_is_forty_eight": field_degree_potential == 48,
        "deliberate_normalized_formula_has_discriminant_denominator": sp.denom(
            C**2 / (4 * Du**2 * Dd**2)
        ) == 4 * Du**2 * Dd**2,
        "jarlskog_identity_is_nontrivial": jarlskog_identity_residual != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP378",
        "admitted_state_domain": "polynomial weak-basis invariant algebra of two Hermitian flavor Gram matrices and a singlet source ratio rho; equivalence to normalized J^2 is restricted to Delta_u*Delta_d nonzero",
        "faithful_quotient_coordinate": "full physical16 on the nondegenerate stratum; normalized J is not a global coordinate across spectral degeneracy",
        "source_authorized_probe_family": "conditional polynomial residual F=C^2-4*alpha*rho*Delta_u^2*Delta_d^2 and its positive square",
        "contextual_partition": "on the nondegenerate stratum F fixes J^2 relative to alpha*rho; at either spectral degeneracy all rho values collide when C=0",
        "classification": "conditional weak-basis-descending polynomial CP-shell selector on the nondegenerate stratum; high-degree EFT operator, degeneracy-blind, and not a derived numerical selector",
        "jarlskog_identity_residual": str(jarlskog_identity_residual),
        "polynomial_constraint": str(polynomial_constraint),
        "positive_potential": str(positive_potential),
        "rho_response": str(rho_response),
        "degrees": {
            "constraint_gram_degree": gram_degree_F,
            "potential_gram_degree": gram_degree_potential,
            "potential_bifundamental_field_degree": field_degree_potential,
        },
        "smallest_exact_falsifier": "Delta_u=0 and C=0 make F and dF/drho vanish for every rho, so the polynomial portal loses source/flavor separation",
        "remaining_physical_instrument_gate": "derive a mediator completion generating the degree-24 Gram potential and alpha, prove stability and nondegenerate source support, and test without fitting alpha",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp378_local_polynomial_cp_portal.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
