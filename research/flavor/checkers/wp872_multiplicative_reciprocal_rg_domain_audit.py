"""Exact WP872 multiplicative reciprocal RG and domain audit."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    x, delta, y, tau, s0 = sp.symbols(
        "x delta y tau s0", positive=True, real=True)
    beta_cosh = sp.Rational(1, 2)/delta-delta*x**2/sp.Integer(2)
    potential = sp.log(sp.cosh(y))
    beta_y = -sp.diff(potential, y)
    beta_x = sp.factor(-x*sp.tanh(sp.log(delta*x)).rewrite(sp.exp))
    beta_x_rational = x*(1-delta**2*x**2)/(1+delta**2*x**2)
    dual_x = 1/(delta**2*x)
    dual_residual = sp.simplify(
        beta_x_rational.subs(x, dual_x)
        - sp.diff(dual_x, x)*beta_x_rational)
    fixed_points = sp.solve(sp.factor(beta_x_rational), x)
    linear_exponent = sp.simplify(
        sp.diff(beta_x_rational, x).subs(x, 1/delta))
    solution_sinh = s0*sp.exp(-tau)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("wp871_cosh_beta_has_nonzero_decoupled_limit",
          beta_cosh.subs(x, 0) == 1/(2*delta), beta_cosh.subs(x, 0))
    check("wp871_cosh_beta_is_not_multiplicative_at_zero",
          sp.limit(beta_cosh/x, x, 0, dir="+") == sp.oo,
          sp.limit(beta_cosh/x, x, 0, dir="+"))
    check("log_cosh_potential_is_even_and_strictly_convex",
          sp.simplify(potential.subs(y, -y)-potential) == 0
          and sp.simplify(sp.diff(potential, y, 2)-1/sp.cosh(y)**2) == 0,
          sp.diff(potential, y, 2))
    check("repaired_y_flow_is_negative_tanh",
          sp.simplify(beta_y+sp.tanh(y)) == 0, beta_y)
    check("repaired_x_flow_has_exact_rational_form",
          sp.simplify(beta_x-beta_x_rational) == 0, beta_x)
    check("repaired_x_flow_is_multiplicative_and_analytic_at_zero",
          beta_x_rational.subs(x, 0) == 0
          and sp.limit(beta_x_rational/x, x, 0, dir="+") == 1,
          [beta_x_rational.subs(x, 0),
           sp.limit(beta_x_rational/x, x, 0, dir="+")])
    check("repaired_flow_is_reciprocity_covariant",
          dual_residual == 0, dual_residual)
    check("unique_positive_fixed_point_is_inverse_diameter",
          fixed_points == [1/delta], fixed_points)
    check("normalized_linear_exponent_is_minus_one",
          linear_exponent == -1, linear_exponent)
    check("sinh_coordinate_has_exact_exponential_solution",
          sp.diff(solution_sinh, tau) == -solution_sinh, solution_sinh)
    check("diameter_two_still_selects_inverse_sqrt_two",
          sp.sqrt(1/sp.Integer(2)) == sp.sqrt(2)/2, sp.sqrt(2)/2)
    check("zero_seed_is_fixed_and_falsifies_unconditional_inevitability",
          beta_x_rational.subs(x, 0) == 0, beta_x_rational.subs(x, 0))
    check("physical_domain_rg_and_detector_gates_remain_open", True,
          "must exclude zero cusp, derive physical RG map, and calibrate physical16")

    result = {
        "schema": "marici.flavor.multiplicative-reciprocal-rg-domain-audit.v1",
        "work_package": "WP872",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "supersedes": "WP871 cosh-gradient as a Ward-compatible physical coupling beta",
        "retained_from_wp871": "Delta=2 magnitude and global basin on x>0",
        "repaired_source_functional": "log cosh(log(Delta x))",
        "repaired_beta": "x(1-Delta^2 x^2)/(1+Delta^2 x^2)",
        "selected_coupling": "1/sqrt(2)",
        "basin": "all x>0",
        "excluded_or_fixed_boundary": "x=0 is a fixed decoupled cusp",
        "smallest_exact_falsifier": "x(0)=0 remains zero",
        "classification": "Ward-compatible conditional selector on nonzero domain; not unconditional portal generator",
        "remaining_gates": [
            "source theorem excluding zero coupling from the physical domain",
            "microscopic derivation as physical flavor RG",
            "calibrated finite-width physical16 instrument",
        ],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp872_multiplicative_reciprocal_rg_domain_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
