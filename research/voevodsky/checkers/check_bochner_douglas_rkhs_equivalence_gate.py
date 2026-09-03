from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/bochner-douglas-rkhs-equivalence-gate-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # Atoms u=(0,pi), translate labels x=(0,1): exact character evaluation matrix.
    V = sp.Matrix([[1, 1], [1, -1]])
    assert V.det() == -2
    signed_weights = sp.diag(1, sp.Rational(-1, 2))
    signed_gram = V * signed_weights * V.T
    assert signed_gram == sp.Matrix([[sp.Rational(1, 2), sp.Rational(3, 2)], [sp.Rational(3, 2), sp.Rational(1, 2)]])
    assert signed_gram.eigenvals() == {2: 1, -1: 1}

    # The negative atomic direction is isolated by a translate coefficient vector.
    coefficient = sp.Matrix([sp.Rational(1, 2), sp.Rational(-1, 2)])
    evaluations = V.T * coefficient
    assert evaluations == sp.Matrix([0, 1])
    assert (coefficient.T * signed_gram * coefficient)[0] == sp.Rational(-1, 2)

    # Every scalar heat value is positive despite the negative Gram direction.
    t = sp.symbols("t", positive=True, real=True)
    scalar_heat = 1 - sp.Rational(1, 2) * sp.exp(-sp.pi**2 * t)
    assert sp.limit(scalar_heat, t, 0, dir="+") == sp.Rational(1, 2)
    assert sp.diff(scalar_heat, t).is_positive

    # Positive atomic weights give an explicit source feature factorization.
    positive_weights = sp.diag(1, sp.Rational(1, 2))
    feature = sp.diag(1, 1 / sp.sqrt(2)) * V.T
    positive_gram = V * positive_weights * V.T
    assert sp.simplify(feature.T * feature - positive_gram) == sp.zeros(2)
    assert positive_gram.is_positive_definite

    status = contract["status"]
    assert status["source_derived_completed_positivity"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.bochner-douglas-rkhs-equivalence-gate-check.v1",
        "status":"finite_equivalence_gate_verified",
        "invertible_character_probe":True,
        "negative_atomic_weight_detected_by_gram":True,
        "positive_scalar_heat_with_negative_gram":True,
        "positive_atomic_feature_factorization":True,
        "source_derived_completed_positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
