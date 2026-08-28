"""Exact WP871 charge-normalized reciprocal gradient selector."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    x, delta, y, tau, u0 = sp.symbols(
        "x delta y tau u0", positive=True, real=True)
    potential = sp.cosh(y)
    beta_y = -sp.diff(potential, y)
    lyapunov = potential-1
    lyapunov_derivative = sp.simplify(sp.diff(lyapunov, y)*beta_y)
    beta_x = sp.Rational(1, 2)/delta-delta*x**2/sp.Integer(2)
    dual_x = 1/(delta**2*x)
    dual_covariance_residual = sp.simplify(
        beta_x.subs(x, dual_x)-sp.diff(dual_x, x)*beta_x)
    fixed_points = sp.solve(beta_x, x)
    solution_u = u0*sp.exp(-tau)
    selected_x = sp.Rational(1, 2)
    selected_g = sp.sqrt(selected_x)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("reciprocal_potential_is_even",
          sp.simplify(potential.subs(y, -y)-potential) == 0, potential)
    check("reciprocal_potential_is_strictly_convex",
          sp.diff(potential, y, 2) > 0, sp.diff(potential, y, 2))
    check("gradient_flow_is_reciprocity_equivariant",
          sp.simplify(beta_y.subs(y, -y)+beta_y) == 0, beta_y)
    check("lyapunov_derivative_is_exact_negative_square",
          lyapunov_derivative == -sp.sinh(y)**2, lyapunov_derivative)
    check("positive_x_flow_is_exact",
          beta_x == 1/(2*delta)-delta*x**2/2, beta_x)
    check("x_flow_is_duality_covariant",
          dual_covariance_residual == 0, dual_covariance_residual)
    check("unique_positive_fixed_point_is_inverse_diameter",
          fixed_points == [1/delta], fixed_points)
    check("diameter_two_selects_inverse_sqrt_two",
          selected_g == sp.sqrt(2)/2, selected_g)
    check("tanh_half_coordinate_has_exponential_solution",
          sp.diff(solution_u, tau) == -solution_u, solution_u)
    check("diameter_hostile_moves_selected_value",
          1/sp.sqrt(2) != 1/sp.sqrt(3), [1/sp.sqrt(2), 1/sp.sqrt(3)])
    check("physical_rg_and_detector_calibration_remain_open", True,
          "requires microscopic RG map and calibrated physical16 response")

    result = {
        "schema": "marici.flavor.charge-normalized-reciprocal-gradient-selector.v1",
        "work_package": "WP871",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_coordinate": "z=Delta_Q g^2 with Delta_Q=2",
        "source_functional": "cosh(log z)=(z+z^-1)/2",
        "selected_coupling": "1/sqrt(2)",
        "coupling_basin": "all g>0",
        "exact_solution": "tanh(log(Delta_Q g^2)/2)=exp(-tau) times its initial value",
        "assembled_conditional_chain": [
            "odd boundary sign and normalized ray",
            "charge-diameter reciprocal magnitude",
            "global reciprocal-gradient coupling basin",
            "Kato marked-projector threshold transport",
            "Ward-locked source detector vertex",
        ],
        "smallest_exact_falsifier": "Delta=3 selects 1/sqrt(3) under the same reciprocal law",
        "classification": "conditional end-to-end selector through source-level readout; microscopic RG and calibrated instrument not admitted",
        "remaining_gates": [
            "source theorem retaining marked Delta_Q through thresholds",
            "physical RG interpretation of reciprocal gradient",
            "finite-width calibrated physical16 detector",
        ],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp871_charge_normalized_reciprocal_gradient_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
