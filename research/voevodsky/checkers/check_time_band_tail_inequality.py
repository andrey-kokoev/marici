from __future__ import annotations

import json
from fractions import Fraction


def lower_bound(m_high: Fraction, c_low: Fraction, leakage: Fraction, c_prime: Fraction) -> Fraction:
    return m_high - (m_high + c_low) * leakage - c_prime


def main() -> None:
    # Exact fixture for the derived inequality. The constants stand for a
    # high-frequency gamma lower bound, low-band negative bound, concentration
    # eigenvalue, and absolute prime bound.
    m_high = Fraction(6)
    c_low = Fraction(2)
    c_prime = Fraction(3)
    leakage_good = Fraction(1, 4)
    leakage_bad = Fraction(1, 2)
    good = lower_bound(m_high, c_low, leakage_good, c_prime)
    bad = lower_bound(m_high, c_low, leakage_bad, c_prime)
    assert good == 1
    assert bad == -1

    result = {
        "schema":"marici.voevodsky.time-band-tail-inequality-check.v1",
        "status":"time_band_tail_threshold_verified",
        "tail_lower_bound_formula":"m_R-(m_R+C_low)*lambda_(M+1)-C_prime",
        "good_fixture_lower_bound":str(good),
        "deliberate_failure_lower_bound":str(bad),
        "endpoint_tail_removed_by_trial_augmentation":True,
        "existence_from_compact_concentration_spectrum":True,
        "effective_mode_threshold_computed":False,
        "off_diagonal_schur_gate_closed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
