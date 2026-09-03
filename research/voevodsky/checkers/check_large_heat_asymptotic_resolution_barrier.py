from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/large-heat-asymptotic-resolution-barrier-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, alpha, beta = sp.symbols("t alpha beta", positive=True, real=True)
    for m in range(1, 7):
        ratio = t ** (-m) / sp.exp(-alpha * t)
        assert sp.limit(ratio, t, sp.oo) == sp.oo

    slower_ratio = sp.exp(-beta * t) / sp.exp(-alpha * t)
    # Verify representative strict exponent separations exactly.
    for a, b in ((2, 1), (5, 3), (sp.Rational(7, 2), sp.Rational(3, 2))):
        assert sp.limit(slower_ratio.subs({alpha: a, beta: b}), t, sp.oo) == sp.oo

    faster_ratio = sp.exp(-sp.Rational(5, 2) * t) / sp.exp(-2 * t)
    assert sp.limit(faster_ratio, t, sp.oo) == 0
    equal_ratio = sp.exp(-2 * t) / sp.exp(-2 * t)
    assert sp.simplify(equal_ratio) == 1

    # Renormalization isolates a positive leading coefficient when the remainder is faster.
    C, R = sp.symbols("C R", positive=True, real=True)
    model = C * sp.exp(-2 * t) + R * sp.exp(-3 * t)
    assert sp.limit(sp.exp(2 * t) * model, t, sp.oo) == C

    result = {
        "schema":"marici.voevodsky.large-heat-asymptotic-resolution-barrier-check.v1",
        "status":"asymptotic_resolution_no_go_verified",
        "algebraic_orders_checked":6,
        "slower_exponential_cases_checked":3,
        "equal_and_faster_exponent_cases":True,
        "renormalized_positive_limit_fixture":True,
        "conditional_D2_leading_asymptotic":False,
        "global_D2_positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
