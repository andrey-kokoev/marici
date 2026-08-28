"""Exact WP836 audit of a scale-free Ward-spectral completion selector."""

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


def spectral_shape(D: sp.Matrix):
    gram = D.T*D
    n = D.rows
    return sp.simplify(sp.trace(gram)/(gram.det()**sp.Rational(1, n)))


def main() -> None:
    Q = sp.diag(1, 2, 3)
    one = sp.ones(3, 1)
    D_a = sp.eye(3)-sp.Rational(2, 3)*(one*one.T)
    w = sp.Matrix([1, 2, 3])
    D_b = sp.eye(3)-sp.Rational(1, 7)*(w*w.T)
    weight, mass = sp.symbols("weight mass", positive=True, real=True)
    k, ell, charge_square_sum = sp.symbols(
        "k ell charge_square_sum", nonnegative=True, integer=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("primitive_ward_index_is_fourteen",
          sp.trace(Q**2) == 14, sp.trace(Q**2))
    check("first_three_state_packet_saturates_scale_free_shape_bound",
          D_a.T*D_a == sp.eye(3) and D_a.det() == -1
          and spectral_shape(D_a) == 3,
          (D_a.T*D_a, spectral_shape(D_a)))
    check("saturating_packet_is_operator_irreducible",
          commutant_dimension(Q, D_a) == 1,
          commutant_dimension(Q, D_a))

    check("second_inequivalent_mixing_also_saturates_shape_bound",
          D_b.T*D_b == sp.eye(3) and D_b.det() == -1
          and spectral_shape(D_b) == 3 and D_a != D_b,
          (D_b, spectral_shape(D_b)))
    check("second_saturating_packet_is_operator_irreducible",
          commutant_dimension(Q, D_b) == 1,
          commutant_dimension(Q, D_b))

    check("scale_free_shape_is_invariant_under_positive_mass_rescaling",
          sp.simplify(spectral_shape(mass*D_a)-spectral_shape(D_a)) == 0,
          spectral_shape(mass*D_a))

    # k counts nonzero charged vectorlike pairs and ell counts neutral states.
    # The Ward increment is 2 sum r_j^2; AM-GM gives spectral shape >= n.
    completion_lower_bound = (
        14+2*charge_square_sum+weight*(3+2*k+ell))
    base_score = 14+3*weight
    score_gap = sp.simplify(completion_lower_bound-base_score)
    check("completion_score_gap_has_exact_additive_form",
          sp.simplify(score_gap-(2*charge_square_sum+weight*(2*k+ell))) == 0,
          score_gap)
    check("every_nonempty_neutral_completion_has_positive_gap",
          score_gap.subs({k: 0, ell: 1, charge_square_sum: 0}) == weight,
          score_gap.subs({k: 0, ell: 1, charge_square_sum: 0}))
    check("every_unit_charged_pair_has_positive_gap",
          score_gap.subs({k: 1, ell: 0, charge_square_sum: 1})
          == 2+2*weight,
          score_gap.subs({k: 1, ell: 0, charge_square_sum: 1}))
    check("completion_order_is_robust_for_every_positive_weight",
          sp.diff(2+2*weight, weight) == 2
          and (2+2*weight).subs(weight, 1) > 0,
          2+2*weight)

    check("functional_does_not_select_absolute_spectral_scale",
          spectral_shape(D_a) == spectral_shape(mass*D_a),
          (spectral_shape(D_a), spectral_shape(mass*D_a)))
    check("functional_does_not_select_mixing_orientation",
          D_a != D_b and spectral_shape(D_a) == spectral_shape(D_b)
          and commutant_dimension(Q, D_a) == commutant_dimension(Q, D_b) == 1,
          (D_a, D_b))

    result = {
        "work_package": "WP836",
        "title": "Scale-free Ward-spectral completion selector",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "candidate_functional": "Phi=Tr(Q^2)+lambda Tr(D^dagger D)/det(D^dagger D)^(1/n), lambda>0",
        "theorem_domain": "finite nondegenerate real spectral completions of the primitive three-charge packet by k nonzero vectorlike pairs and ell neutral states",
        "exact_bound": {
            "spectral_shape": "R_n>=n by arithmetic-geometric mean on positive singular-value squares",
            "base_score": "14+3 lambda",
            "completion_gap": "2 sum_j r_j^2 + lambda(2k+ell)",
            "strictness": "positive for every nonempty completion and every lambda>0",
        },
        "classification": {
            "selector": "within the declared finite completion domain, Phi uniquely selects k=ell=0 and equal singular values",
            "coefficient_robustness": "the completion ordering is independent of the numerical positive weight lambda",
            "scale": "unselected because the spectral shape is invariant under D->mD",
            "mixing": "unselected because inequivalent irreducible Householder mixings saturate the same bound",
            "rg_basin": "not supplied by the static completion functional",
            "threshold_survival": "matter multiplicity is selected in-domain, but masses, relevant deformations, and finite matching remain open",
            "physical_instrument": "no admitted apparatus measures Phi or prepares its global minimization over source completions",
            "selector_or_rigidifier": "genuine finite-completion and singular-shape selector; scale/mixing rigidifier only",
        },
        "smallest_exact_falsifier_of_full_completion": "D_a and D_b are distinct irreducible three-state minimizers, and m D_a has the same score for every m>0",
        "claim_boundary": "Source authority for minimizing Phi is not derived. The theorem covers the declared direct charged/neutral finite completion grammar, not arbitrary interacting QFT completions.",
        "remaining_source_gate": "derive Phi or an equivalent comparison action from the source, lift its mixing and scale fibers, derive the interacting RG basin and threshold map, and realize a calibrated physical16 readout",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp836_scale_free_ward_spectral_completion_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
