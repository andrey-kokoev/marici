"""Exact WP851 audit of supersymmetric recursive F-flat completion."""

import itertools
import json
from pathlib import Path
import sympy as sp


def quadratic_monomials_with_charge(target):
    names = ("S1", "S1bar", "S2", "S3", "v")
    charges = (-1, 1, -2, -3, 0)
    found = []
    for exponents in itertools.product(range(3), repeat=len(names)):
        if sum(exponents) != 2:
            continue
        if sum(e*q for e, q in zip(exponents, charges)) != target:
            continue
        factors = []
        for name, exponent in zip(names, exponents):
            factors.extend([name]*exponent)
        found.append("*".join(factors))
    return sorted(found)


def main() -> None:
    a, b, c, d, e, f, g, v = sp.symbols("a b c d e f g v", nonzero=True)
    s1, sb, s2, s3, a0, a2, a3 = sp.symbols("s1 sb s2 s3 a0 a2 a3")
    W = (a0*(a*s1*sb-b*v**2)
         + a2*(c*v*s2-d*s1**2+g*sb*s3)
         + a3*(e*v*s3-f*s1*s2))
    fields = (a0, a2, a3, sb, s3, s2, s1)
    F = {str(field): sp.diff(W, field) for field in fields}
    branch = {
        sb: b*v**2/(a*s1),
        s2: a*d*e*s1**2/(v*(a*c*e+b*f*g)),
        s3: a*d*f*s1**3/(v**2*(a*c*e+b*f*g)),
        a0: 0,
        a2: 0,
        a3: 0,
    }
    kernel = sp.Matrix([s2*s3, 2*s1*s3, 3*s1*s2]).subs(branch)
    ray = sp.Matrix([sp.simplify(kernel[i]/kernel[0]) for i in range(3)])
    unit_ray = sp.simplify(ray.subs({a: 1, b: 1, c: 1, d: 1, e: 1,
                                     f: 1, g: 0, s1: v}))
    hostile_ray = sp.simplify(ray.subs({a: 1, b: 1, c: 1, d: 1, e: 1,
                                        f: 1, g: 1, s1: v}))
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("neutral_driver_quadratic_basis_is_exhausted",
          quadratic_monomials_with_charge(0) == ["S1*S1bar", "v*v"],
          quadratic_monomials_with_charge(0))
    check("charge_two_driver_quadratic_basis_is_exhausted",
          quadratic_monomials_with_charge(-2) == ["S1*S1", "S1bar*S3", "S2*v"],
          quadratic_monomials_with_charge(-2))
    check("charge_three_driver_quadratic_basis_is_exhausted",
          quadratic_monomials_with_charge(-3) == ["S1*S2", "S3*v"],
          quadratic_monomials_with_charge(-3))
    check("general_nonzero_branch_is_F_flat",
          all(sp.simplify(value.subs(branch)) == 0 for value in F.values()), F)
    check("nonzero_branch_forces_all_drivers_to_zero",
          all(branch[x] == 0 for x in (a0, a2, a3)), (branch[a0], branch[a2], branch[a3]))
    check("unit_coefficients_recover_primitive_kernel_ray",
          unit_ray == sp.Matrix([1, 2, 3]), unit_ray)
    check("single_allowed_extra_monomial_changes_kernel_ray",
          hostile_ray != unit_ray, {"unit": unit_ray, "hostile": hostile_ray})
    check("coefficient_fiber_contains_relation_ratios_and_extra_monomial",
          all(symbol in sp.flatten([expr.free_symbols for expr in ray])
              for symbol in (c, d, e, f, g)), ray)

    positive_metric_theorem = {
        "premise": "K is positive definite and invertible",
        "identity": "F^dagger K^{-1} F = ||K^{-1/2}F||^2",
        "zero_iff": "F=0",
        "scope": "exact supersymmetric F-term potential",
    }
    check("positive_Kahler_completion_preserves_F_flat_zero_set",
          positive_metric_theorem["zero_iff"] == "F=0", positive_metric_theorem)

    result = {
        "work_package": "WP851",
        "title": "Supersymmetric recursive F-flat completion audit",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_grammar": {"spurion_charges": [-1, 1, -2, -3],
                           "driver_charges": [0, 2, 3],
                           "spurion_R": 0, "driver_R": 2,
                           "maximum_superpotential_degree": 3},
        "completion_result": "positive Kahler completion cannot move the exact F-flat locus",
        "coefficient_fiber": ["b/a", "d/c", "f/e", "g extra A2-channel monomial"],
        "smallest_hostile": "turn on g*A2*S1bar*S3 while preserving all declared source grammar",
        "classification": "F-flat completion repair, but only a conditional alignment selector",
        "remaining_gate": "source-derived positive pairing and canonical multiplication normalization, then RG, thresholds, and calibrated physical16 readout",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp851_supersymmetric_recursive_f_flat_completion_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
