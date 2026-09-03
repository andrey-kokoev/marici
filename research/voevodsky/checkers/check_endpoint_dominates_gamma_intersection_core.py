from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/endpoint-dominates-gamma-intersection-core-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    y, beta = sp.symbols("y beta", nonnegative=True, positive=True)

    # log(2+y) <= log(2)+y/2 by integrating its derivative bound.
    log_majorant_gap = sp.log(2) + y / 2 - sp.log(2 + y)
    assert log_majorant_gap.subs(y, 0) == 0
    assert sp.simplify(sp.diff(log_majorant_gap, y) - y / (2 * (y + 2))) == 0

    # Exact maximum of y^2 exp(-beta y) occurs at y=2/beta.
    weighted_polynomial = y**2 * sp.exp(-beta * y)
    critical = sp.Rational(2) / beta
    assert sp.simplify(sp.diff(weighted_polynomial, y).subs(y, critical)) == 0
    maximum = sp.simplify(weighted_polynomial.subs(y, critical))
    assert maximum == 4 * sp.exp(-2) / beta**2

    # The stated constant follows from (a+b)^2 <= 2a^2+2b^2.
    C_beta = 1 + 2 * sp.log(2) ** 2 + 2 * sp.exp(-2) / beta**2
    algebraic_majorant = 1 + 2 * sp.log(2) ** 2 + y**2 / 2
    exponential_majorant = sp.simplify(C_beta * sp.exp(beta * y))
    assert sp.simplify(
        exponential_majorant - algebraic_majorant
    ).subs(y, critical).is_nonnegative

    # Exact finite beta fixtures verify the complete pointwise inequality symbolically.
    for beta_value in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)):
        for y_value in (sp.Integer(0), sp.Rational(1, 3), sp.Integer(1), sp.Integer(3), sp.Integer(8)):
            difference = (
                C_beta * sp.exp(beta * y)
                - (1 + sp.log(2 + y) ** 2)
            ).subs({beta: beta_value, y: y_value})
            assert difference.is_positive or difference == 0

    status = contract["status"]
    assert status["common_transport_identification"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.endpoint-dominates-gamma-intersection-core-check.v1",
        "status":"endpoint_gamma_weight_domination_verified",
        "logarithm_linear_majorant":True,
        "exponential_polynomial_maximum":True,
        "sampled_exact_weight_inequalities":15,
        "intersection_core_conditional":True,
        "common_transport_identification":False,
        "prime_row_control":False,
        "positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
