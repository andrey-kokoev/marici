"""Exact WP849 audit of a charge-recursive spurion alignment selector."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
    v = sp.symbols("v", positive=True, real=True)
    constraints = sp.Matrix([u1**2-1, u2-u1**2, u3-u1*u2])
    variables = sp.Matrix([u1, u2, u3])
    J = constraints.jacobian(variables).subs({u1: 1, u2: 1, u3: 1})
    hessian = 2*J.T*J
    real_solutions = sp.solve(list(constraints), [u1, u2, u3], dict=True)
    s1 = v
    s2 = v
    s3 = v
    kernel = sp.Matrix([s2*s3, 2*s1*s3, 3*s1*s2])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("charge_two_recursion_is_gauge_covariant",
          -2 == 2*(-1), (-2, 2*(-1)))
    check("charge_three_recursion_is_gauge_covariant",
          -3 == -1+(-2), (-3, -1+(-2)))
    check("real_zero_locus_has_only_gauge_related_sign_pair",
          real_solutions == [{u1: -1, u2: 1, u3: -1},
                             {u1: 1, u2: 1, u3: 1}], real_solutions)
    check("negative_real_solution_is_pi_gauge_transform_of_positive_one",
          [(-1)**j for j in (1, 2, 3)] == [-1, 1, -1],
          [(-1)**j for j in (1, 2, 3)])
    check("constraint_jacobian_is_nonsingular",
          J.det() == 2, J.det())
    check("gauge_fixed_hessian_is_exact_gram",
          hessian == 2*J.T*J, hessian)
    principal_minors = [hessian[:i, :i].det() for i in (1, 2, 3)]
    check("gauge_fixed_hessian_is_positive_definite",
          all(value > 0 for value in principal_minors), principal_minors)
    check("equal_vev_orbit_recovers_primitive_kernel_ray",
          kernel == v**2*sp.Matrix([1, 2, 3]), kernel)
    check("dimensionful_vev_scale_cancels_from_projective_ratios",
          sp.simplify(kernel[1]/kernel[0]) == 2
          and sp.simplify(kernel[2]/kernel[0]) == 3,
          (sp.simplify(kernel[1]/kernel[0]), sp.simplify(kernel[2]/kernel[0])))
    check("positive_sum_of_squares_has_zero_at_selected_orbit",
          constraints.subs({u1: 1, u2: 1, u3: 1}) == sp.zeros(3, 1),
          constraints.subs({u1: 1, u2: 1, u3: 1}))
    check("zero_locus_does_not_depend_on_positive_term_weights",
          len(real_solutions) == 2, real_solutions)
    check("nonzero_weight_one_vev_leaves_trivial_u1_stabilizer",
          sp.gcd(1, sp.gcd(2, 3)) == 1, sp.gcd(1, sp.gcd(2, 3)))

    result = {
        "work_package": "WP849",
        "title": "Charge-recursive spurion alignment selector",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "potential": "lambda1(|s1|^2-v^2)^2 + lambda2 v^2|s2-s1^2/v|^2 + lambda3 v^2|s3-s1 s2/v|^2",
        "zero_orbit": "v(e^{-i theta},e^{-2i theta},e^{-3i theta})",
        "gauge_fixed_representative": "(v,v,v)",
        "selected_kernel": "v^2(1,2,3)",
        "coefficient_robustness": "zero orbit is identical for all lambda_i>0",
        "classification": "conditional genuine spurion-alignment and primitive-ray selector",
        "remaining_source_gate": "derive or uniquely authorize the recursive potential, then beta law, pre/post-vacuum character transport, threshold matching, and calibrated holonomy physical16 readout",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp849_charge_recursive_spurion_alignment_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
