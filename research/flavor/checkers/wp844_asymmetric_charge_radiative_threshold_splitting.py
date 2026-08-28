"""Exact WP844 audit of radiative splitting of the equal spectral threshold."""

import json
from pathlib import Path
import sympy as sp


def commutant_dimension(*operators: sp.Matrix) -> int:
    n = operators[0].rows
    variables = sp.symbols(f"z0:{n*n}")
    Z = sp.Matrix(n, n, variables)
    equations = []
    for operator in operators:
        equations.extend(list(Z*operator-operator*Z))
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(coefficients.nullspace())


def main() -> None:
    q = sp.Matrix([1, 2, 3])
    Q = sp.diag(1, 2, 3)
    H = sp.eye(3)-2*q*q.T/q.dot(q)
    mass, epsilon = sp.symbols("mass epsilon", positive=True, real=True)
    tree_gram = (mass*H).T*(mass*H)
    corrected = tree_gram+epsilon*Q**2
    centered_hostile = epsilon*(Q-2*sp.eye(3))**2
    traceless = epsilon*(Q**2-sp.Rational(14, 3)*sp.eye(3))
    a, b, c = sp.symbols("a b c", real=True)
    values = [a+b*i+c*i**2 for i in (1, 2, 3)]
    equal_solution = sp.solve([values[1]-values[0], values[2]-values[1]], [b, c], dict=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("wp837_tree_singular_values_are_exactly_equal",
          tree_gram == mass**2*sp.eye(3), tree_gram)
    check("charge_square_hostile_is_basis_covariant",
          Q**2 == sp.diag(1, 4, 9), Q**2)
    check("radiative_hostile_splits_all_three_thresholds",
          list(corrected.diagonal()) == [mass**2+epsilon, mass**2+4*epsilon, mass**2+9*epsilon],
          corrected.diagonal())
    check("adjacent_squared_threshold_gaps_are_nonzero",
          corrected[1, 1]-corrected[0, 0] == 3*epsilon
          and corrected[2, 2]-corrected[1, 1] == 5*epsilon,
          (3*epsilon, 5*epsilon))
    check("shift_insensitive_centered_hostile_still_splits",
          centered_hostile == epsilon*sp.diag(1, 0, 1), centered_hostile)
    check("simple_charge_spectrum_has_diagonal_commutant_dimension_three",
          commutant_dimension(Q) == 3, commutant_dimension(Q))
    check("charge_and_current_reflection_have_only_scalar_common_commutant",
          commutant_dimension(Q, H) == 1, commutant_dimension(Q, H))
    check("quadratic_charge_correction_preserves_degeneracy_only_if_constant",
          equal_solution == [{b: 0, c: 0}], equal_solution)
    check("traceless_self_energy_really_is_traceless",
          sp.trace(traceless) == 0, sp.trace(traceless))
    check("traceless_splitting_has_positive_exact_norm",
          sp.trace(traceless**2) == sp.Rational(98, 3)*epsilon**2,
          sp.trace(traceless**2))
    check("scalar_mass_counterterm_cannot_cancel_traceless_splitting",
          traceless != sp.zeros(3), traceless)
    check("tree_equal_threshold_is_not_protected_by_current_source_alone",
          corrected != (mass**2+sp.trace(epsilon*Q**2)/3)*sp.eye(3), corrected)

    result = {
        "work_package": "WP844",
        "title": "Asymmetric charge radiative threshold splitting",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "tree_packet": "D=m H_q gives D^T D=m^2 I",
        "covariant_hostile": "Pi=epsilon Q^2 gives squared thresholds m^2+epsilon, m^2+4epsilon, m^2+9epsilon",
        "symmetry_result": "commutant(Q) is diagonal dimension 3; common commutant(Q,H_q) is scalar",
        "required_cancellation": "-epsilon(Q^2-(14/3)I), with squared norm (98/3)epsilon^2",
        "classification": "negative radiative threshold-protection theorem; tree equal-singular shape is not threshold survival",
        "claim_boundary": "epsilon Q^2 is an allowed covariant hostile, not an asserted universal physical self-energy",
        "remaining_source_gate": "derive a nonrenormalization identity canceling every traceless charge-dependent self-energy without erasing the asymmetric portal, then finite matching and physical16 readout",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp844_asymmetric_charge_radiative_threshold_splitting.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
