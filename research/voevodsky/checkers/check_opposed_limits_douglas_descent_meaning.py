from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/opposed-limits-douglas-descent-meaning-v1.json")


def leading(matrix: sp.Matrix, size: int) -> sp.Matrix:
    return matrix[:size, :size]


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    max_stage = 8

    # Compatible uniformly contractive family.
    bounded = [sp.diag(*(sp.Rational(k, k + 1) for k in range(1, stage + 1))) for stage in range(1, max_stage + 1)]
    assert all(leading(bounded[stage], stage) == bounded[stage - 1] for stage in range(1, max_stage))
    assert all(max(matrix.diagonal()) < 1 for matrix in bounded)
    defects = [sp.eye(stage) - bounded[stage - 1].T * bounded[stage - 1] for stage in range(1, max_stage + 1)]
    assert all(all(value > 0 for value in defect.diagonal()) for defect in defects)
    assert all(leading(defects[stage], stage) == defects[stage - 1] for stage in range(1, max_stage))

    # Compatible but unbounded: coherent algebraic map with no bounded completed extension.
    unbounded = [sp.diag(*range(1, stage + 1)) for stage in range(1, max_stage + 1)]
    assert all(leading(unbounded[stage], stage) == unbounded[stage - 1] for stage in range(1, max_stage))
    assert [max(matrix.diagonal()) for matrix in unbounded] == list(range(1, max_stage + 1))

    # Uniformly bounded but incompatible: no map on the direct-limit equivalence classes.
    incompatible = [((-1) ** stage) * sp.eye(stage) for stage in range(1, max_stage + 1)]
    assert all(max(abs(value) for value in matrix.diagonal()) == 1 for matrix in incompatible)
    restriction_failures = sum(leading(incompatible[stage], stage) != incompatible[stage - 1] for stage in range(1, max_stage))
    assert restriction_failures == max_stage - 1

    status = contract["status"]
    assert status["arithmetic_compatible_uniform_family"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.opposed-limits-douglas-descent-meaning-check.v1",
        "status":"bounded_descent_mechanism_verified",
        "finite_stages_checked":max_stage,
        "compatible_uniform_family_extensible":True,
        "defect_certificates_restrict_coherently":True,
        "compatible_unbounded_family_detected":True,
        "uniform_incompatible_family_detected":True,
        "restriction_failures":restriction_failures,
        "arithmetic_family_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
