from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/endpoint-toeplitz-deficit-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    sigma, d = sp.symbols("sigma d", positive=True, real=True)
    e0 = sp.exp(sigma / 2)
    ed = e0 * sp.cosh(d / 2)
    matrix = sp.Matrix([[e0, ed], [ed, e0]])
    determinant = sp.factor(matrix.det())
    expected = -sp.exp(sigma) * sp.sinh(d / 2) ** 2
    assert sp.simplify(determinant - expected) == 0

    symmetric = sp.simplify(e0 + ed)
    antisymmetric = sp.simplify(e0 - ed)
    assert symmetric.subs(d, 2).is_positive
    assert antisymmetric.subs(d, 2).is_negative

    deficit = sp.simplify(ed - e0)
    assert deficit.subs(d, 2).is_positive
    assert sp.simplify(antisymmetric + deficit) == 0
    local_coefficient = sp.limit(deficit / d**2, d, 0)
    assert local_coefficient == sp.exp(sigma / 2) / 8
    endpoint_second_derivative = sp.diff(e0 * sp.cosh(d / 2), d, 2).subs(d, 0)
    assert endpoint_second_derivative == sp.exp(sigma / 2) / 4

    status = contract["status"]
    assert status["completed_compensation_inequality"] == "not proved"
    result = {
        "schema":"marici.voevodsky.endpoint-toeplitz-deficit-check.v1",
        "status":"endpoint_antisymmetric_gram_failure_verified",
        "determinant_identity":True,
        "symmetric_channel_positive":True,
        "antisymmetric_channel_negative":True,
        "quadratic_deficit_coefficient":str(local_coefficient),
        "necessary_remainder_curvature":"R_second(0)<=-exp(sigma/2)/4",
        "sectorwise_positive_anchor":False,
        "completed_compensation_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
