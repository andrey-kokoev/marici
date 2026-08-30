"""Exact WP838 acceptance certificate for an unavoidable flavor portal."""

import json
from pathlib import Path
import sympy as sp


def fixed_point(a, b, c, d, f):
    a, b, c, d, f = map(sp.Integer, (a, b, c, d, f))
    denominator = a*c-d*f
    return sp.simplify(a*b/denominator), sp.simplify(b*f/denominator)


def main() -> None:
    q = sp.Matrix([1, 2, 3])
    contrast = q[2]-q[1]
    x, y = sp.symbols("x y", nonnegative=True, real=True)
    beta_x = 2*x**2*(-1+3*x-y)
    beta_y = 2*y*(y-x)
    x_star, y_star = fixed_point(1, 1, 3, 1, 1)
    shifted_x, shifted_y = fixed_point(1, 1, 4, 1, 1)
    jacobian = sp.Matrix([beta_x, beta_y]).jacobian([x, y]).subs(
        {x: x_star, y: y_star})
    portal = sp.simplify(contrast*sp.sqrt(x_star))
    labelled = sp.eye(2)
    inclusive = sp.Matrix([[1, 1]])
    contrast_vector = sp.Matrix([1, -1])
    identity_matching = sp.eye(2)
    inclusive_matching = sp.Matrix([[1, 1], [1, 1]])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("primitive_current_fixes_positive_unit_contrast",
          contrast == 1, contrast)
    check("conditional_fixed_point_is_exact",
          (x_star, y_star) == (sp.Rational(1, 2), sp.Rational(1, 2)),
          (x_star, y_star))
    check("fixed_point_solves_both_beta_functions",
          beta_x.subs({x: x_star, y: y_star}) == 0
          and beta_y.subs({x: x_star, y: y_star}) == 0,
          (beta_x.subs({x: x_star, y: y_star}),
           beta_y.subs({x: x_star, y: y_star})))
    check("conditional_portal_sign_and_magnitude_are_fixed",
          portal == 1/sp.sqrt(2) and portal > 0, portal)
    check("local_ir_stability_spectrum_is_positive",
          jacobian.eigenvals() == {sp.Rational(1, 2): 1, sp.Integer(2): 1},
          jacobian.eigenvals())
    check("same_incidence_coefficient_hostile_moves_magnitude",
          (shifted_x, shifted_y) == (sp.Rational(1, 3), sp.Rational(1, 3))
          and shifted_x != x_star,
          ((x_star, y_star), (shifted_x, shifted_y)))
    check("identity_threshold_map_preserves_contrast",
          identity_matching*contrast_vector == contrast_vector,
          identity_matching*contrast_vector)
    check("inclusive_threshold_map_erases_contrast",
          inclusive_matching*contrast_vector == sp.zeros(2, 1),
          inclusive_matching*contrast_vector)
    check("labelled_detector_family_separates_two_channels",
          labelled.rank() == 2 and labelled*contrast_vector != sp.zeros(2, 1),
          labelled.rank())
    check("inclusive_detector_record_erases_contrast",
          inclusive.rank() == 1 and inclusive*contrast_vector == sp.zeros(1, 1),
          inclusive*contrast_vector)

    gates = {
        "oriented_representation": True,
        "source_derived_spectral_action": False,
        "source_derived_beta_coefficients": False,
        "global_selected_rg_basin": False,
        "finite_threshold_survival": False,
        "calibrated_physical16_readout": False,
    }
    check("current_programme_does_not_satisfy_unavoidability_certificate",
          not all(gates.values()), gates)
    check("five_missing_gates_are_explicit",
          sum(not value for value in gates.values()) == 5,
          [key for key, value in gates.items() if not value])

    result = {
        "work_package": "WP838",
        "title": "Single-constructor portal unavoidability certificate",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "candidate_principle": "one source-natural constructor from primitive oriented incidence to representation, finite spectral action, beta system and selected basin, finite threshold map, and calibrated labelled physical16 realization",
        "conditional_prediction": {
            "charge_contrast": "1",
            "fixed_point": ["1/2", "1/2"],
            "portal": "1/sqrt(2)",
            "local_stability_eigenvalues": ["1/2", "2"],
        },
        "gate_status": gates,
        "first_missing_arrow": "primitive incidence plus finite spectral data -> uniquely derived interacting action and beta coefficients",
        "smallest_exact_falsifier": "the same primitive incidence with c=3 and c=4 gives x*=1/2 and x*=1/3",
        "instrument_boundary": "Aspect's comb reference types a common comparison frame but does not select the source value; labelled finite-width physical16 response remains unrealized",
        "classification": "exact acceptance theorem and conditional prediction, not an existing physical source principle",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp838_single_constructor_portal_unavoidability_certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
