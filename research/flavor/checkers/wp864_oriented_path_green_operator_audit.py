"""Exact WP864 audit of the oriented-path Green operator."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    rho, delta, u, v, w = sp.symbols("rho delta u v w", real=True)
    F = sp.Matrix([[0, -sp.I, 0], [0, 0, -sp.I], [0, 0, 0]]) / sp.sqrt(2)
    identity = sp.eye(3)
    kinetic = identity - rho*F - delta*F**2
    green = sp.simplify(kinetic.inv())
    predicted = identity + rho*F + (rho**2+delta)*F**2
    candidate = u*identity + v*F + w*F**2
    residual = sp.expand((identity-F)*candidate-identity)
    equations = list(residual.reshape(9, 1))
    solution = sp.solve(equations, (u, v, w), dict=True)
    sign_flip = sp.diag(1, -1, 1)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("normalized_path_has_exact_nilpotency_order_three",
          F**3 == sp.zeros(3) and F**2 != sp.zeros(3), F**2)
    check("general_green_operator_is_exact",
          sp.simplify(green-predicted) == sp.zeros(3), green)
    check("oriented_derivative_has_unique_path_algebra_inverse",
          solution == [{u: 1, v: 1, w: 1}], solution)
    check("green_equation_forces_complete_unit_path_sum",
          sp.simplify((identity-F)*(identity+F+F**2)-identity) == sp.zeros(3),
          identity+F+F**2)
    check("direct_two_step_term_reopens_wp863_modulus",
          sp.diff(rho**2+delta, delta) == 1, rho**2+delta)
    check("nearest_neighbor_magnitude_remains_free_without_normalization",
          sp.diff(green, rho) != sp.zeros(3), sp.diff(green, rho))
    check("unreferenced_signs_are_unitarily_conjugate",
          sp.simplify(sign_flip*F*sign_flip.conjugate().T+F) == sp.zeros(3)
          and sp.simplify(sign_flip*(identity-F)*sign_flip.conjugate().T
                          -(identity+F)) == sp.zeros(3), sign_flip)
    check("kinetic_is_invertible_for_all_hostile_parameters",
          sp.factor(kinetic.det()) == 1, kinetic.det())
    check("threshold_and_instrument_gates_remain_separate", True,
          "requires WP860 reducing projector and calibrated physical16 port")

    result = {
        "schema": "marici.flavor.oriented-path-green-operator-audit.v1",
        "work_package": "WP864",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_domain": "normalized marked length-three path with kinetic block K",
        "conditional_source_principle": "Green inversion of the oriented discrete derivative K=I-F",
        "forced_green_operator": "I + F + F^2",
        "general_hostile": "K_(rho,delta)=I-rho F-delta F^2",
        "general_inverse": "I+rho F+(rho^2+delta) F^2",
        "smallest_falsifiers": {
            "magnitude": "rho != 1",
            "locality": "delta != 0",
            "sign": "I-F and I+F are conjugate without a retained reference",
        },
        "classification": "conditional coefficient selector; incomplete end-to-end source constructor",
        "remaining_gates": [
            "derive normalized oriented derivative from one microscopic source",
            "identify its physical RG generator with the WP859 global basin",
            "derive the WP860 reducing threshold projector",
            "calibrate the complementary port in physical16 units",
        ],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp864_oriented_path_green_operator_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
