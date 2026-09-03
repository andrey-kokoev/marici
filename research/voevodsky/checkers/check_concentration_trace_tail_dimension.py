from __future__ import annotations

import json
from fractions import Fraction


def certified_delta(m_high: Fraction, c_low: Fraction, c_prime: Fraction, trace_bound: Fraction, modes_plus_one: int) -> Fraction:
    leakage_bound = trace_bound / modes_plus_one
    return m_high - (m_high + c_low) * leakage_bound - c_prime


def main() -> None:
    m_high = Fraction(6)
    c_low = Fraction(2)
    c_prime = Fraction(3)
    trace_bound = Fraction(10)
    good_modes_plus_one = 27
    bad_modes_plus_one = 26
    good = certified_delta(m_high, c_low, c_prime, trace_bound, good_modes_plus_one)
    bad = certified_delta(m_high, c_low, c_prime, trace_bound, bad_modes_plus_one)
    assert good == Fraction(1, 27)
    assert bad == Fraction(-1, 13)

    result = {
        "schema":"marici.voevodsky.concentration-trace-tail-dimension-check.v1",
        "status":"explicit_tail_dimension_from_trace_bound",
        "concentration_trace":"2*L*R/pi",
        "eigenvalue_bound":"lambda_(M+1)<=2*L*R/(pi*(M+1))",
        "dimension_condition":"M+1 > [2*L*R/pi]*(m_R+C_low)/(m_R-C_prime)",
        "good_fixture_delta":str(good),
        "deliberate_failure_delta":str(bad),
        "gamma_constants_enclosed":False,
        "prime_constant_exact":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
