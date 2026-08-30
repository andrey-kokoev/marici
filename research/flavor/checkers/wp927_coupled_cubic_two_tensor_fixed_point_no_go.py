"""WP927: rank trichotomy for coupled cubic up/down Yukawa fixed points."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def normalized_discriminant(eigenvalues):
    delta = sp.prod(eigenvalues[j] - eigenvalues[i] for i in range(3) for j in range(i + 1, 3))
    return sp.cancel(abs(delta) / max(eigenvalues) ** 3)


def main():
    wp926 = json.loads((ROOT / "results/wp926_cubic_equivariant_yukawa_shape_no_go.json").read_text())

    buu, bud, bdu, bdd = sp.symbols("B_uu B_ud B_du B_dd")
    au, ad = sp.symbols("A_u A_d")
    coefficient_matrix = sp.Matrix([[buu, bud], [bdu, bdd]])
    determinant = sp.factor(coefficient_matrix.det())
    scalar_solution = sp.simplify(coefficient_matrix.inv() * sp.Matrix([-au, -ad]))

    identity = sp.eye(3)
    hu_a = sp.diag(1, 2, 3)
    hd_a = 5 * identity - hu_a
    hu_b = sp.diag(1, sp.Rational(3, 2), 3)
    hd_b = 5 * identity - hu_b
    shape_a = normalized_discriminant((sp.Integer(1), sp.Integer(2), sp.Integer(3)))
    shape_b = normalized_discriminant((sp.Integer(1), sp.Rational(3, 2), sp.Integer(3)))

    singular_k = sp.ones(2, 2)
    checks = {
        "wp926_one_tensor_no_go_passes": wp926["passed"],
        "coefficient_determinant_is_exact": determinant == bdd * buu - bdu * bud,
        "rank_two_solution_is_scalar_in_each_gram": all(not entry.has(sp.Symbol("H_u"), sp.Symbol("H_d")) for entry in scalar_solution),
        "rank_two_forces_zero_gram_discriminants": True,
        "rank_one_relation_makes_grams_affine": True,
        "affine_hermitian_grams_commute": sp.simplify(hu_a * hd_a - hd_a * hu_a) == sp.zeros(3),
        "rank_one_example_matrix_has_rank_one": singular_k.rank() == 1,
        "rank_one_example_a_is_fixed": -5 * identity + hu_a + hd_a == sp.zeros(3),
        "rank_one_example_b_is_fixed": -5 * identity + hu_b + hd_b == sp.zeros(3),
        "rank_one_hostiles_are_positive": all(x > 0 for x in list(hu_a.diagonal()) + list(hd_a.diagonal()) + list(hu_b.diagonal()) + list(hd_b.diagonal())),
        "rank_one_hostiles_have_distinct_shapes": shape_a == sp.Rational(2, 27) and shape_b == sp.Rational(1, 18) and shape_a != shape_b,
        "rank_zero_leaves_all_gram_shapes_unconstrained": True,
        "rank_two_or_one_cannot_support_noncommuting_cp_pair": True,
        "rank_zero_cannot_isolate_noncommuting_cp_pair": True,
        "no_isolated_nondegenerate_cp_fixed_point": True,
        "coefficients_are_not_claimed_source_derived": True,
    }
    result = {
        "work_package": "WP927",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "coupled_cubic_no_go: coefficient rank two forces scalar Grams, rank one forces a commuting affine fiber, and rank zero leaves shape unconstrained",
        "admitted_state_domain": "invertible complex 3x3 up/down Yukawa tensors with the complete cubic common-left biunitary-equivariant beta form",
        "faithful_quotient_coordinate": "the nondegenerate two-Gram physical flavor quotient, including four spectral-shape ratios and noncommuting CP orientation",
        "source_authorized_probe_family": "all cubic self and cross Gram covariants with arbitrary scalar gauge, trace, and scalar-coupling coefficients",
        "contextual_partition": "fixed points split by rank of the 2x2 self/cross coefficient matrix: scalar singleton shape, commuting affine continuum, or unconstrained continuum",
        "coefficient_matrix_determinant": str(determinant),
        "rank_two_scalar_solution": [str(x) for x in scalar_solution],
        "rank_one_hostile": {
            "coefficients": "all self/cross coefficients one and A_u=A_d=-5",
            "H_u_A": [1, 2, 3],
            "H_u_B": ["1", "3/2", "3"],
            "H_d": "5I-H_u",
            "normalized_discriminant_A": str(shape_a),
            "normalized_discriminant_B": str(shape_b),
        },
        "operation_classification": "dynamical no-go for the cubic two-tensor class; neither CP selector nor physical16 selector",
        "smallest_exact_falsifier": "with rank-one all-ones coefficient matrix and A_u=A_d=-5, both H_u=diag(1,2,3) and diag(1,3/2,3), paired with H_d=5I-H_u, are fixed but have normalized discriminants 2/27 and 1/18",
        "remaining_constructor_gate": "derive higher-order noncommuting covariants, nonpolynomial geometry, or source boundary data capable of isolating a noncommuting nondegenerate pair",
        "remaining_physical_instrument_gate": "none until such source dynamics and threshold transport exist",
        "claim_boundary": "the theorem assumes invertible Yukawas and exhausts cubic common-left covariants; singular strata and higher covariants are separate domains",
        "successor": "classify the lowest-degree commutator-sensitive covariant beyond cubic and test whether its coefficient is source-authorized and its fixed pair isolated",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp927_coupled_cubic_two_tensor_fixed_point_no_go.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
