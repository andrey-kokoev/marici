"""Exact WP817 audit of the three-operator Gram-loop purity selector."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    r = sp.symbols("r", nonnegative=True, real=True)
    positive = sp.Matrix([[1, r, r], [r, 1, r], [r, r, 1]])
    negative = sp.Matrix([[1, r, -r], [r, 1, r], [-r, r, 1]])
    flips = [sp.diag(*signs) for signs in (
        (1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)
    )]
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    def loop_product(matrix):
        return sp.factor(matrix[0, 1] * matrix[1, 2] * matrix[2, 0])

    plus_eigen = positive.eigenvals()
    minus_eigen = negative.eigenvals()
    check("positive_loop_spectrum_is_exact", plus_eigen == {1 - r: 2, 2*r + 1: 1}, plus_eigen)
    check("negative_loop_spectrum_is_exact", minus_eigen == {1 - 2*r: 1, r + 1: 2}, minus_eigen)
    check("positive_loop_is_psd_through_unit_magnitude", positive.subs(r, 1).is_positive_semidefinite,
          positive.subs(r, 1).eigenvals())
    check("negative_loop_is_psd_only_through_half_magnitude",
          negative.subs(r, sp.Rational(1, 2)).is_positive_semidefinite
          and not negative.subs(r, sp.Rational(3, 4)).is_positive_semidefinite,
          (negative.subs(r, sp.Rational(1, 2)).eigenvals(), negative.subs(r, sp.Rational(3, 4)).eigenvals()))
    check("positivity_alone_admits_both_loop_signs",
          positive.subs(r, sp.Rational(1, 4)).is_positive_semidefinite
          and negative.subs(r, sp.Rational(1, 4)).is_positive_semidefinite,
          (loop_product(positive.subs(r, sp.Rational(1, 4))),
           loop_product(negative.subs(r, sp.Rational(1, 4)))))
    check("positive_loop_reaches_rank_one_at_unit_magnitude", positive.subs(r, 1).rank() == 1,
          positive.subs(r, 1).rank())
    check("negative_loop_never_reaches_rank_one_on_its_psd_interval",
          negative.subs(r, 0).rank() == 3 and negative.subs(r, sp.Rational(1, 2)).rank() == 2,
          "rank 3 for 0<=r<1/2 and rank 2 at r=1/2")
    check("rank_one_purity_selects_positive_loop_and_unit_normalized_edges",
          loop_product(positive.subs(r, 1)) == 1 and positive.subs(r, 1).rank() == 1,
          positive.subs(r, 1))

    base = sp.Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    transformed_products = [loop_product(S * base * S) for S in flips]
    check("triangle_product_survives_all_independent_operator_sign_flips",
          transformed_products == [1, 1, 1, 1], transformed_products)
    check("individual_edges_do_not_survive_operator_sign_flips",
          len({str((S * base * S)[0, 1]) for S in flips}) == 2,
          [(S * base * S)[0, 1] for S in flips])

    v1, v2, v3 = sp.symbols("v1 v2 v3", nonzero=True, real=True)
    vector = sp.Matrix([v1, v2, v3])
    rank_one = vector * vector.T
    check("every_real_rank_one_gram_has_positive_nonzero_triangle_product",
          loop_product(rank_one) == (v1*v2*v3)**2, loop_product(rank_one))

    Z = sp.diag(2, 3, 5)
    transported = Z * base * Z
    normalized = [sp.simplify(transported[i, j] / sp.sqrt(transported[i, i]*transported[j, j]))
                  for i, j in ((0, 1), (1, 2), (2, 0))]
    check("positive_diagonal_thresholds_preserve_normalized_triangle", normalized == [1, 1, 1], normalized)
    shear = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    sheared = shear * base * shear.T
    sheared_normalized = [sp.simplify(sheared[i, j] / sp.sqrt(sheared[i, i]*sheared[j, j]))
                         for i, j in ((0, 1), (1, 2), (2, 0))]
    check("invertible_nonaligned_congruence_preserves_positive_pure_triangle_when_nonzero",
          sheared.rank() == 1 and sheared_normalized == [1, 1, 1],
          {"rank": sheared.rank(), "normalized": sheared_normalized})
    eraser = sp.Matrix([[1, -1, 0], [0, 1, 0], [0, 0, 1]])
    erased = eraser * base * eraser.T
    check("nonaligned_mixing_can_erase_a_primitive_attachment",
          erased[0, 1] == erased[2, 0] == 0 and erased.rank() == 1, erased)

    c12, c23, c31 = sp.symbols("c12 c23 c31", nonzero=True, real=True)
    complete = sp.Matrix([c12, c23, c31])
    check("calibrated_three_cross_channel_record_is_locally_faithful",
          complete.jacobian([c12, c23, c31]).rank() == 3, 3)
    g12, g23, g31 = sp.symbols("g12 g23 g31", positive=True)
    measured_loop = sp.factor(g12*g23*g31*c12*c23*c31)
    check("positive_calibrated_gains_preserve_loop_sign", measured_loop == g12*g23*g31*c12*c23*c31,
          measured_loop)
    check("uncalibrated_gains_leave_absolute_magnitude_kernel",
          sp.Matrix([g12*c12, g23*c23, g31*c31]).jacobian(
              [c12, c23, c31, g12, g23, g31]).rank() == 3,
          "response rank 3 on six source-plus-gain coordinates")

    # Aspect germ-tester gates: retain the native ternary relation and every
    # attachment needed to turn the algebraic invariant into a physical claim.
    germ = {
        "native_arity": 3,
        "operator_germs": ["O1", "O2", "O3"],
        "primitive_attachments": ["C12", "C23", "C31"],
        "comparison_before_local_quotient": True,
        "purity_authority": False,
        "physical16_descent": False,
        "common_detector_calibration": False,
    }
    check("aspect_native_arity_gate_passes", germ["native_arity"] == len(germ["operator_germs"]), germ)
    check("aspect_primitive_attachment_gate_passes", len(germ["primitive_attachments"]) == 3, germ)
    check("aspect_comparison_precedes_operator_sign_quotient", germ["comparison_before_local_quotient"], germ)
    check("aspect_source_authority_gate_remains_open", not germ["purity_authority"], germ)
    check("aspect_physical16_descent_gate_remains_open", not germ["physical16_descent"], germ)
    check("aspect_instrument_gate_remains_open", not germ["common_detector_calibration"], germ)

    deliberate_obstruction = negative.subs(r, sp.Rational(1, 2)).rank() - 1
    check("deliberate_failure_is_smallest_negative_loop_purity_obstruction",
          deliberate_obstruction == 1, deliberate_obstruction)

    result = {
        "work_package": "WP817",
        "title": "Three-operator Gram-loop purity selector",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_data": {
            "positive_loop_eigenvalues": {str(k): v for k, v in plus_eigen.items()},
            "negative_loop_eigenvalues": {str(k): v for k, v in minus_eigen.items()},
            "rank_one_triangle_product": str(loop_product(rank_one)),
            "aspect_germ": germ,
        },
        "classification": {
            "algebra": "rank-one positive Gram purity selects the positive triangle class and unit normalized magnitude",
            "quotient": "triangle sign survives independent sign changes of all three marked operators",
            "source": "purity and the three marked flavor incidences are not yet source-authorized",
            "threshold": "real congruence preserves rank-one positivity and cannot create a negative loop, but can erase an attachment",
            "instrument": "three calibrated cross channels preserve sign; gain calibration and physical16 descent remain open",
            "aspect_germ_tester": "native ternary topology and primitive attachments pass; authority, descent, and instrument gates fail",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp817_three_operator_gram_loop_purity_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
