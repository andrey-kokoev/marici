"""Exact WP856 reciprocal endpoint RG and threshold audit."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    a, b, kappa, t, p0 = sp.symbols("a b kappa t p0", positive=True)
    swap = sp.Matrix([[0, 1], [1, 0]])
    generator = sp.Matrix([[-a, b], [a, -b]])
    reciprocal = generator.subs({a: kappa, b: kappa})
    stationary = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
    solution = sp.Rational(1, 2)+(p0-sp.Rational(1, 2))*sp.exp(-2*kappa*t)
    beta = kappa*(1-2*sp.Symbol("p", real=True))
    p = sp.Symbol("p", real=True)
    lyapunov = (p-sp.Rational(1, 2))**2
    lyapunov_dot = sp.diff(lyapunov, p)*kappa*(1-2*p)
    r = sp.symbols("r", real=True)
    threshold = sp.Matrix([[r, 1-r], [1-r, r]])
    current = sp.Matrix([1, -1])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("probability_conserving_generator_has_declared_form",
          sp.Matrix([[1, 1]])*generator == sp.zeros(1, 2), generator)
    exchange_condition = sp.simplify(swap*generator*swap-generator)
    check("endpoint_exchange_covariance_forces_equal_rates",
          sp.solve(list(exchange_condition), [a, b], dict=True) == [{a: b}],
          exchange_condition)
    check("reciprocal_generator_has_unique_uniform_fixed_point",
          reciprocal*stationary == sp.zeros(2, 1)
          and reciprocal.rank() == 1, reciprocal.nullspace())
    check("closed_form_solution_satisfies_rg_equation",
          sp.simplify(sp.diff(solution, t)-kappa*(1-2*solution)) == 0, solution)
    check("zero_seed_is_not_a_fixed_point", beta.subs(p, 0) == kappa, beta.subs(p, 0))
    check("candidate_portal_magnitude_is_inverse_root_two",
          sp.sqrt(stationary[0]) == 1/sp.sqrt(2), sp.sqrt(stationary[0]))
    check("lyapunov_derivative_is_strict_negative_square",
          sp.simplify(lyapunov_dot+4*kappa*(p-sp.Rational(1, 2))**2) == 0,
          sp.factor(lyapunov_dot))
    check("swap_intertwining_threshold_preserves_uniform_packet",
          threshold*stationary == stationary and swap*threshold == threshold*swap,
          threshold*stationary)
    check("threshold_scales_oriented_current_by_exact_eigenvalue",
          threshold*current == (2*r-1)*current, threshold*current)
    check("three_quarter_hostile_preserves_fixed_point_but_halves_current",
          threshold.subs(r, sp.Rational(3, 4))*stationary == stationary
          and threshold.subs(r, sp.Rational(3, 4))*current == current/2,
          threshold.subs(r, sp.Rational(3, 4)))
    check("half_threshold_erases_orientation",
          threshold.subs(r, sp.Rational(1, 2))*current == sp.zeros(2, 1),
          threshold.subs(r, sp.Rational(1, 2))*current)
    check("only_identity_preserves_oriented_current_exactly",
          sp.solve(list(threshold*current-current), r) == {r: 1},
          sp.solve(list(threshold*current-current), r))

    result = {
        "work_package": "WP856",
        "title": "Reciprocal endpoint RG basin and threshold audit",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_domain": "two marked endpoint probability algebra with reciprocal irreducible transport",
        "fixed_point": "p*=1/2",
        "global_basin": "entire interval [0,1] for kappa>0",
        "conditional_portal_magnitude": "|g_n-g_m|=1/sqrt(2) if p is the canonically normalized squared coupling",
        "threshold_family": "T_r=[[r,1-r],[1-r,r]]",
        "smallest_threshold_hostile": "r=3/4 preserves p* but maps J to J/2",
        "classification": "conditional nonzero global magnitude selector; physical RG/coherent lift/threshold authority open",
        "remaining_gates": ["derive endpoint flow as flavor RG", "derive coherent kinetic normalization",
                            "isometric marked-port threshold matching", "WP855 calibrated readout"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp856_reciprocal_endpoint_rg_basin_threshold_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
