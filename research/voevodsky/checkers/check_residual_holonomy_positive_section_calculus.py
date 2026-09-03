from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/residual-holonomy-positive-section-calculus-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # Directed category: a:0->1, b:1->2, c:0->2; relation b a = c.
    omega_a, omega_b, omega_c = map(sp.Integer, (2, 3, 5))
    composed = omega_b + omega_a
    assert composed == omega_c
    flat_period = omega_c - composed
    assert flat_period == 0

    anomalous_c = sp.Integer(6)
    nonflat_period = anomalous_c - composed
    assert nonflat_period == 1

    # Omega defined from global vertex data is a formal coboundary.
    K0, K1, K2 = map(sp.Integer, (7, 9, 12))
    assert omega_a == K1 - K0
    assert omega_b == K2 - K1
    assert omega_c == K2 - K0

    # A substantive defect section can be positive and nonzero.
    D = sp.diag(sp.Rational(1, 2), sp.Rational(2, 3))
    R = D.T * D
    assert R == sp.diag(sp.Rational(1, 4), sp.Rational(4, 9))
    assert R.is_positive_definite and R != sp.zeros(2)

    # Observer kernel modulo declared presentation relations.
    observer_2 = sp.Matrix([[1, 0]])
    assert observer_2.nullspace() == [sp.Matrix([0, 1])]
    presentation_2 = [sp.Matrix([0, 1])]
    assert observer_2.nullspace() == presentation_2

    observer_3 = sp.Matrix([[1, 0, 0]])
    presentation_3 = [sp.Matrix([0, 1, 0])]
    invisible = sp.Matrix([0, 0, 1])
    assert observer_3 * invisible == sp.zeros(1, 1)
    assert invisible not in presentation_3

    status = contract["status"]
    assert status["arithmetic_all_generator_relations"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.residual-holonomy-positive-section-calculus-check.v1",
        "status":"residual_type_separation_verified",
        "flat_directed_period":True,
        "nonflat_period_detected":True,
        "global_assignment_coboundary":True,
        "positive_nonzero_substantive_residual":True,
        "presentation_kernel_quotiented":True,
        "invisible_nonpresentation_kernel_detected":True,
        "arithmetic_generator_relations_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
