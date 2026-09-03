from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/gamma-tail-elementary-enclosure-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, R = sp.symbols("t R", positive=True, real=True)
    u = (R + 2 * t) / (4 * sp.sqrt(t))
    erfc_replacement = sp.simplify(
        2 * sp.sqrt(sp.pi * t) * sp.exp(t / 4) * sp.exp(-u**2) / (sp.sqrt(sp.pi) * u)
    )
    elementary_second = 8 * t / (R + 2 * t) * sp.exp(t / 4 - (R + 2 * t) ** 2 / (16 * t))
    assert sp.simplify(erfc_replacement - elementary_second) == 0

    simplified_second = 8 * t / (R + 2 * t) * sp.exp(-R / 4 - R**2 / (16 * t))
    assert sp.simplify(elementary_second - simplified_second) == 0

    log_derivative = sp.simplify(sp.diff(sp.log(simplified_second), t))
    expected_log_derivative = 1 / t - 2 / (R + 2 * t) + R**2 / (16 * t**2)
    assert sp.simplify(log_derivative - expected_log_derivative) == 0
    assert sp.simplify(1 / t - 2 / (R + 2 * t)) == R / (t * (R + 2 * t))

    R_value = sp.Integer(40)
    t_max = sp.Rational(2, 25)
    numerator = sp.exp(-R_value) + simplified_second.subs({R: R_value, t: t_max})
    bound = numerator / (1 - sp.exp(-R_value))
    bound_value = sp.N(bound, 50)
    assert bound_value < sp.Float("4.249e-18", 50)
    assert bound_value < sp.Float("1e-15", 50)

    result = {
        "schema":"marici.voevodsky.gamma-tail-elementary-enclosure-check.v1",
        "status":"gamma_tail_elementary_reduction_verified",
        "erfc_upper_reduction":True,
        "exponent_simplification":True,
        "monotone_in_t":True,
        "R":40,
        "tmax":"2/25",
        "elementary_upper_high_precision":str(bound_value),
        "directed_rounding_interval":False,
        "finite_gamma_quadrature":False,
        "source_D2_certification":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
