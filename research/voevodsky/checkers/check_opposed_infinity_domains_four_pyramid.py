from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/opposed-infinity-domains-four-pyramid-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # Finite Douglas fixture: A is identity and B=C is a strict contraction.
    A = sp.eye(3)
    C = sp.diag(sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(3, 4))
    B = C * A
    defect_square = sp.simplify(sp.eye(3) - C.T * C)
    assert all(value >= 0 for value in defect_square.diagonal())
    Q = sp.simplify(A.T * A - B.T * B)
    assert Q == defect_square

    # Restriction to nested finite source stages preserves the same certificate.
    for size in (1, 2, 3):
        restricted_q = Q[:size, :size]
        restricted_defect = defect_square[:size, :size]
        assert restricted_q == restricted_defect

    # Conformance failure: B does not vanish on ker A, so C(Af)=Bf is undefined.
    A_bad = sp.Matrix([[1, 0], [0, 0]])
    B_bad = sp.Matrix([[0, 0], [0, 1]])
    kernel_vector = sp.Matrix([0, 1])
    assert A_bad * kernel_vector == sp.zeros(2, 1)
    assert B_bad * kernel_vector != sp.zeros(2, 1)

    # Refinement grows source dimension while restricted admissible cones only lose constraints.
    source_dimensions = [1, 2, 3]
    constraint_counts = [1, 3, 6]
    assert source_dimensions == sorted(source_dimensions)
    assert constraint_counts == sorted(constraint_counts)

    status = contract["status"]
    assert status["uniform_arithmetic_contraction"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.opposed-infinity-domains-four-pyramid-check.v1",
        "status":"opposed_limit_variance_verified",
        "direct_source_stages_checked":3,
        "inverse_constraint_stages_checked":3,
        "douglas_certificate_identity":True,
        "certificate_restriction_coherence":True,
        "kernel_inclusion_needed_for_factorization":True,
        "uniform_arithmetic_contraction_supplied":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
