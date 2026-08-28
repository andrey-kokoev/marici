"""Exact WP835 audit of a combined Ward-spectral positive functional."""

import json
from pathlib import Path
import sympy as sp


def commutant_dimension(*operators: sp.Matrix) -> int:
    n = operators[0].rows
    variables = sp.symbols(f"x0:{n*n}")
    X = sp.Matrix(n, n, variables)
    equations = []
    for operator in operators:
        equations.extend(list(X*operator-operator*X))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(coefficient_matrix.nullspace())


def main() -> None:
    Q3 = sp.diag(1, 2, 3)
    D3 = sp.Matrix([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 2]])
    Q4 = sp.diag(1, 2, 3, 0)
    D4 = sp.Matrix([[0, 1, 0, 1],
                    [1, 1, 1, 0],
                    [0, 1, 2, 1],
                    [1, 0, 1, 3]])
    alpha, beta, scale, clock = sp.symbols(
        "alpha beta scale clock", positive=True, real=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    ward3 = sp.trace(Q3**2)
    ward4 = sp.trace(Q4**2)
    spectral3 = sp.trace(D3**2)
    spectral4 = sp.trace(D4**2)
    inverse4 = sp.trace(D4.inv()**2)
    check("base_and_neutral_completion_share_ward_index",
          ward3 == ward4 == 14, (ward3, ward4))
    check("spectral_square_detects_neutral_completion_at_fixed_scale",
          spectral3 == 9 and spectral4 == 22 and spectral4-spectral3 == 13,
          (spectral3, spectral4))

    F3 = ward3+alpha*spectral3
    F4 = ward4+alpha*scale**2*spectral4
    check("combined_functional_is_strictly_positive_on_fixed_neutral_scale",
          sp.diff(F4, scale) > 0 and sp.simplify(F4.subs(scale, 1)-F3) == 13*alpha,
          F4)
    check("spectral_scaling_preserves_operator_irreducibility",
          commutant_dimension(Q4, scale*D4) == 1,
          commutant_dimension(Q4, scale*D4))
    check("neutral_penalty_has_unattained_zero_scale_infimum",
          sp.limit(F4, scale, 0, dir="+") == 14
          and sp.solve(sp.Eq(sp.diff(F4, scale), 0), scale) == [],
          (sp.limit(F4, scale, 0, dir="+"), sp.diff(F4, scale)))

    equalizing_scale = sp.Rational(3)/sp.sqrt(22)
    check("base_and_neutral_completion_have_exact_equal_score_fiber",
          sp.simplify(F4.subs(scale, equalizing_scale)-F3) == 0,
          equalizing_scale)
    check("relative_weight_and_spectral_units_have_common_rescaling_fiber",
          sp.simplify((alpha/clock**2)*sp.trace((clock*D4)**2)
                      -alpha*spectral4) == 0,
          (clock*D4, alpha/clock**2))

    stabilized = ward4+alpha*spectral4*scale**2+beta*inverse4/scale**2
    stationary_scale_fourth = sp.simplify(beta*inverse4/(alpha*spectral4))
    check("inverse_spectral_term_creates_coefficient_controlled_scale",
          inverse4 == sp.Rational(37, 16)
          and stationary_scale_fourth == 37*beta/(352*alpha),
          stationary_scale_fourth)
    check("changing_positive_weight_changes_selected_spectral_scale",
          sp.simplify(stationary_scale_fourth.subs({alpha: 16, beta: 1})
                      -stationary_scale_fourth.subs({alpha: 1, beta: 1})/16) == 0,
          (stationary_scale_fourth.subs({alpha: 1, beta: 1}),
           stationary_scale_fourth.subs({alpha: 16, beta: 1})))

    lower_bound = sp.symbols("lower_bound", positive=True, real=True)
    check("external_gap_bound_selects_only_its_boundary",
          sp.diff(F4, scale) > 0
          and sp.simplify(F4.subs(scale, lower_bound)
                          -(14+22*alpha*lower_bound**2)) == 0,
          F4.subs(scale, lower_bound))
    check("combined_score_does_not_fix_rg_neutral_coordinate",
          F4.free_symbols == {alpha, scale}, F4.free_symbols)

    result = {
        "work_package": "WP835",
        "title": "Ward-spectral positive-functional scale fiber",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "candidate_functional": "F_alpha(Q,D)=Tr(Q^2)+alpha Tr(D^2)",
        "exact_data": {
            "base": {"ward_index": 14, "spectral_square": 9},
            "neutral_completion": {"ward_index": 14, "spectral_square": 22,
                                   "inverse_spectral_square": "37/16"},
            "equal_score_scales": {"base": "1", "neutral_completion": "3/sqrt(22)"},
            "stabilized_stationary_scale_fourth": "37 beta/(352 alpha)",
        },
        "classification": {
            "faithfulness": "at a fixed common spectral scale and fixed alpha, the functional sees the neutral completion",
            "scale_fiber": "independent positive rescaling of D preserves irreducibility and can equalize scores",
            "weight_fiber": "alpha is an inverse-square clock; simultaneous D and alpha rescaling leaves the score invariant",
            "minimizer": "the quadratic spectral penalty has an unattained zero-scale infimum on irreducible positive-scale packets",
            "selector_or_rigidifier": "a source-fixed common clock makes F a comparison functional; without it F is a scale rigidifier, not a spectrum selector",
            "physical_instrument": "no admitted experiment measures the combined Ward and finite-Dirac score with one calibrated relative metric",
        },
        "smallest_exact_falsifier": "the base at scale 1 and neutral completion at scale 3/sqrt(22) have identical F_alpha for every alpha>0",
        "remaining_source_gate": "derive the charged-neutral relative metric and absolute spectral clock from one action, prove its minimizer exists and is unique over all physical completions, then transport that minimizer through RG, thresholds, and a common instrument",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp835_ward_spectral_positive_functional_scale_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
