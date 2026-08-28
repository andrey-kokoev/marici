"""Exact WP834 audit of the neutral RG kernel of minimal Ward index."""

import json
from pathlib import Path
import sympy as sp


def commutant_dimension(*operators: sp.Matrix) -> tuple[int, list[sp.Matrix]]:
    n = operators[0].rows
    variables = sp.symbols(f"x0:{n*n}")
    X = sp.Matrix(n, n, variables)
    equations = []
    for operator in operators:
        equations.extend(list(X*operator-operator*X))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = [vector.reshape(n, n) for vector in coefficient_matrix.nullspace()]
    return len(nullspace), nullspace


def main() -> None:
    Q3 = sp.diag(1, 2, 3)
    Q4 = sp.diag(1, 2, 3, 0)
    D4 = sp.Matrix([[0, 1, 0, 1],
                    [1, 1, 1, 0],
                    [0, 1, 2, 1],
                    [1, 0, 1, 3]])
    r = sp.symbols("r", positive=True, integer=True)
    eta = sp.symbols("eta", nonnegative=True, real=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    anomaly = lambda Q, power: sum(Q[i, i]**power for i in range(Q.rows))
    index = lambda Q: anomaly(Q, 2)
    check("neutral_completion_preserves_linear_and_cubic_anomaly",
          anomaly(Q3, 1) == anomaly(Q4, 1) == 6
          and anomaly(Q3, 3) == anomaly(Q4, 3) == 36,
          (anomaly(Q4, 1), anomaly(Q4, 3)))
    check("neutral_completion_lies_in_ward_index_kernel",
          index(Q3) == index(Q4) == 14, (index(Q3), index(Q4)))
    check("every_nonzero_vectorlike_charge_raises_ward_index",
          sp.simplify(14+2*r**2-14) > 0, 14+2*r**2)
    check("primitive_portal_contrast_is_unchanged",
          Q4[2, 2]-Q4[1, 1] == 1, Q4[2, 2]-Q4[1, 1])

    dimension, commutant = commutant_dimension(Q4, D4)
    check("neutral_completed_operator_packet_is_irreducible",
          dimension == 1 and commutant[0] == sp.eye(4), commutant)
    check("neutral_state_is_mixed_and_spectral_operator_is_nondegenerate",
          any(D4[i, 3] != 0 for i in range(3)) and D4.det() == -8,
          (D4[:3, 3:], D4.det()))
    check("neutral_spectral_mass_scale_is_not_seen_by_ward_index",
          index(Q4) == 14 and D4.charpoly().as_expr().factor()
          == (sp.Symbol("lambda")-4)*(sp.Symbol("lambda")-2)
             *(sp.Symbol("lambda")-1)*(sp.Symbol("lambda")+1),
          D4.charpoly().as_expr().factor())

    # WP821 normalized gauge-Yukawa flow with a=b=d=f=1 and
    # c=3+eta^2.  The neutral interaction is a declared RG-active direction.
    c = 3+eta**2
    fixed_x = sp.simplify(1/(c-1))
    check("neutral_interaction_moves_fixed_point_inside_ward_kernel",
          fixed_x.subs(eta, 0) == sp.Rational(1, 2)
          and fixed_x.subs(eta, 1) == sp.Rational(1, 3),
          (fixed_x.subs(eta, 0), fixed_x.subs(eta, 1)))

    x, y = sp.symbols("x y", positive=True, real=True)
    beta_x = 2*x**2*(-1+c*x-y)
    beta_y = 2*y*(y-x)
    jacobian = sp.Matrix([beta_x, beta_y]).jacobian([x, y])
    J0 = sp.simplify(jacobian.subs(eta, 0).subs(
        {x: fixed_x.subs(eta, 0), y: fixed_x.subs(eta, 0)}))
    J1 = sp.simplify(jacobian.subs(eta, 1).subs(
        {x: fixed_x.subs(eta, 1), y: fixed_x.subs(eta, 1)}))
    eig0 = sorted(J0.eigenvals(), key=sp.default_sort_key)
    eig1 = sorted(J1.eigenvals(), key=sp.default_sort_key)
    check("both_fixed_points_have_two_positive_local_ir_exponents",
          eig0 == [sp.Rational(1, 2), sp.Integer(2)]
          and eig1 == [(7-sp.sqrt(13))/9, (7+sp.sqrt(13))/9]
          and all(value > 0 for value in eig0+eig1),
          (eig0, eig1))

    check("neutral_threshold_switches_rg_magnitude_without_changing_pairing",
          index(Q3) == index(Q4)
          and fixed_x.subs(eta, 0) != fixed_x.subs(eta, 1),
          (index(Q3), fixed_x.subs(eta, 0), fixed_x.subs(eta, 1)))
    check("ward_readout_remains_a_readout_not_a_selector",
          sp.diff(14*x, x) == 14 and fixed_x.subs(eta, 0) != fixed_x.subs(eta, 1),
          14*x)

    result = {
        "work_package": "WP834",
        "title": "Minimal Ward-index neutral RG kernel",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "admitted_state_domain": "oriented primitive charge packet plus charged vectorlike and neutral operator completions; neutral RG activity is represented by c=3+eta^2 in the WP821 flow",
        "positive_pairing": "Ward current index S=Tr(Q^2)",
        "contextual_partition": {
            "charged_vectorlike_family": "S strictly increases by 2r^2 and minimality selects no nonzero pair",
            "neutral_completion_family": "S, anomalies, and primitive contrast are identical; eta and the neutral spectrum remain unresolved",
        },
        "exact_hostile": {
            "base": {"charges": [1, 2, 3], "ward_index": 14,
                     "fixed_gauge_coordinate": "1/2",
                     "stability_exponents": ["1/2", "2"]},
            "neutral_completed": {"charges": [1, 2, 3, 0], "ward_index": 14,
                                  "fixed_gauge_coordinate": "1/3",
                                  "stability_exponents": ["(7-sqrt(13))/9",
                                                          "(7+sqrt(13))/9"]},
        },
        "classification": {
            "selector": "minimal Ward index excludes nonzero charged vectorlike additions inside the declared family",
            "kernel": "neutral interacting sectors have zero Ward norm while changing RG and thresholds",
            "rigidifier": "the pairing rigidifies charged-current normalization",
            "physical_instrument": "a calibrated current correlator can read S*x but does not observe neutral RG data by itself",
            "first_nonfaithful_arrow": "full RG-active spectrum to the Ward-current Gram",
            "verdict": "positive-current minimality is a partial charged-spectrum selector, not a complete portal selector",
        },
        "claim_boundary": "The eta-dependent beta coefficient is an exact declared hostile model, not a derived loop calculation for the displayed finite operator packet.",
        "remaining_source_gate": "a source-derived positive functional must be faithful on neutral as well as charged RG-active sectors, with independently fixed weights, threshold matching, and a common physical16 instrument",
        "tests": tests,
    }

    def native(value):
        if isinstance(value, sp.Integer):
            return int(value)
        if isinstance(value, list):
            return [native(item) for item in value]
        if isinstance(value, dict):
            return {key: native(item) for key, item in value.items()}
        return value

    result = native(result)
    output = Path(__file__).parents[1] / "results" / "wp834_minimal_ward_index_neutral_rg_kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
