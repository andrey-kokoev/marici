from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/endpoint-rank-one-schur-gate-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # Strictly positive fixture: threshold c <= 1/(v^T L^-1 v).
    L = sp.diag(2, 1)
    v = sp.Matrix([1, 0])
    leverage = (v.T * L.inv() * v)[0]
    assert leverage == sp.Rational(1, 2)
    at_threshold = L - 2 * v * v.T
    above_threshold = L - 3 * v * v.T
    assert at_threshold.is_positive_semidefinite
    assert not above_threshold.is_positive_semidefinite
    assert len([value for value in above_threshold.eigenvals() if value < 0]) == 1

    # Singular range fixture.
    singular = sp.diag(2, 0)
    singular_pinv = singular.pinv()
    in_range = sp.Matrix([1, 0])
    outside_range = sp.Matrix([0, 1])
    assert singular * singular_pinv * in_range == in_range
    assert singular * singular_pinv * outside_range != outside_range
    assert (singular - in_range * in_range.T).is_positive_semidefinite
    assert not (singular - outside_range * outside_range.T).is_positive_semidefinite

    # Negative inertia on v-perp survives every rank-one subtraction along v.
    indefinite = sp.diag(2, -1)
    perpendicular = sp.Matrix([0, 1])
    repaired_candidate = indefinite - sp.Rational(1, 2) * v * v.T
    assert (perpendicular.T * repaired_candidate * perpendicular)[0] == -1

    # Raw endpoint localizer has negative coefficient; normalized endpoint is constant.
    t, h = sp.symbols("t h", positive=True, real=True)
    endpoint = sp.exp(t / 4)
    endpoint_difference = sp.simplify(endpoint - endpoint.subs(t, t + h))
    assert sp.simplify(endpoint_difference + endpoint * (sp.exp(h / 4) - 1)) == 0
    normalized_endpoint = sp.simplify(sp.exp(-t / 4) * endpoint)
    assert normalized_endpoint == 1
    assert normalized_endpoint - normalized_endpoint.subs(t, t + h) == 0

    status = contract["status"]
    assert status["normalization_target_identification"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.endpoint-rank-one-schur-gate-check.v1",
        "status":"rank_one_endpoint_gate_verified",
        "strict_schur_threshold_fixture":True,
        "singular_range_condition_fixture":True,
        "v_perp_negative_inertia_hostile":True,
        "raw_endpoint_negative_localizer":True,
        "normalized_endpoint_zero_localizer":True,
        "normalization_target_identification":False,
        "gamma_prime_localizer_positivity":False,
        "arithmetic_schur_bound":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
