"""Exact WP829 hostile test for scheme descent of RG curvature anchors."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    u = sp.symbols("u", real=True)
    rate = sp.symbols("rate", positive=True, real=True)
    beta_u = rate * u * (1-u)
    v = sp.expand(u + sp.Rational(1, 2)*u*(1-u))
    dv_du = sp.diff(v, u)
    beta_v = sp.factor(dv_du * beta_u)
    acceleration_v = sp.factor(beta_u * sp.diff(beta_v, u))
    anchor_polynomial = 24*u**3 - 48*u**2 + 26*u - 3
    acceleration_derivative = sp.factor(sp.diff(acceleration_v, u))
    old_lower = (3-sp.sqrt(3))/6
    old_upper = (3+sp.sqrt(3))/6
    reflected_polynomial = sp.expand(anchor_polynomial.subs(u, 1-u))
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("scheme_map_fixes_both_endpoints",
          v.subs(u, 0) == 0 and v.subs(u, 1) == 1,
          (v.subs(u, 0), v.subs(u, 1)))
    check("scheme_map_is_strictly_monotone_on_unit_interval",
          dv_du.subs(u, 0) > 0 and dv_du.subs(u, 1) > 0
          and sp.diff(dv_du, u) < 0,
          dv_du)
    check("transformed_beta_is_chain_rule_pushforward",
          sp.simplify(beta_v-rate*u*(u-1)*(u-sp.Rational(3, 2))) == 0,
          beta_v)

    # Linearized eigenvalues at a fixed point are invariant under a regular
    # one-dimensional coordinate change.  Compute d beta_v / d v by division.
    linearized_v = sp.cancel(sp.diff(beta_v, u)/dv_du)
    check("endpoint_critical_exponents_are_preserved",
          sp.simplify(linearized_v.subs(u, 0)-rate) == 0
          and sp.simplify(linearized_v.subs(u, 1)+rate) == 0,
          (linearized_v.subs(u, 0), linearized_v.subs(u, 1)))
    check("same_physical_portal_is_carried_to_new_coordinate",
          v.subs(u, sp.Rational(1, 2)) == sp.Rational(5, 8),
          v.subs(u, sp.Rational(1, 2)))

    check("new_curvature_extrema_obey_cubic_anchor_equation",
          sp.simplify(acceleration_derivative
                      + rate**2*anchor_polynomial/2) == 0,
          acceleration_derivative)
    check("old_curvature_anchors_are_not_new_curvature_anchors",
          sp.simplify(anchor_polynomial.subs(u, old_lower)-sp.sqrt(3)/3) == 0
          and sp.simplify(anchor_polynomial.subs(u, old_upper)+sp.sqrt(3)/3) == 0,
          (anchor_polynomial.subs(u, old_lower),
           anchor_polynomial.subs(u, old_upper)))
    check("new_anchor_equation_has_exactly_two_internal_roots",
          sp.count_roots(anchor_polynomial, 0, 1) == 2
          and sp.count_roots(anchor_polynomial, 1, sp.oo) == 1,
          (sp.count_roots(anchor_polynomial, 0, 1),
           sp.count_roots(anchor_polynomial, 1, sp.oo)))
    check("new_internal_anchors_are_not_reflection_complements",
          sp.resultant(anchor_polynomial, reflected_polynomial, u) == 110592
          and sp.gcd(anchor_polynomial, reflected_polynomial) == 1,
          sp.resultant(anchor_polynomial, reflected_polynomial, u))

    old_ratio = 2+sp.sqrt(3)
    check("unit_rate_old_equal_spacing_prediction_does_not_descend",
          anchor_polynomial.subs(u, old_lower) != 0
          and anchor_polynomial.subs(u, old_upper) != 0,
          old_ratio)

    result = {
        "work_package": "WP829",
        "title": "RG curvature-anchor scheme-descent no-go",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_flow": {"coordinate": "u", "beta": str(beta_u),
                        "old_anchors": [str(old_lower), str(old_upper)]},
        "admissible_reparameterization": {
            "map": str(v), "derivative": str(dv_du),
            "transformed_beta": str(beta_v),
            "same_portal_coordinate": "5/8",
            "new_anchor_polynomial": str(anchor_polynomial),
            "internal_root_count": 2,
            "external_root_count_above_one": 1,
        },
        "classification": {
            "preserved": ["fixed endpoints", "oriented orbit", "RG time",
                          "endpoint critical exponents", "physical portal event"],
            "not_preserved": ["coordinate acceleration extrema",
                              "reflection-paired anchor states",
                              "equal-spacing scale ratio"],
            "first_nonfaithful_arrow": "physical RG trajectory to chosen coupling-coordinate acceleration jet",
            "threshold_implication": "a finite matching redefinition can move the curvature anchors without changing the underlying trajectory",
            "required_repair": "derive a physically normalized coupling observable and one source-authorized matched instrument before differentiating its record",
            "verdict": "WP827 curvature anchors are chart rigidifiers unless the coupling coordinate and matching scheme are physically frozen",
        },
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp829_rg_curvature_scheme_descent_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
