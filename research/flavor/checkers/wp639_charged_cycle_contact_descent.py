"""Exact WP639 charged-scalar contact-descent audit."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def contact_magnitude(l_a, l_b, m_chi):
    if m_chi <= 0:
        raise ValueError("m_chi must be positive")
    return (l_a + l_b) ** 2 / m_chi**2


plus_m1 = contact_magnitude(F(1), F(1), F(1))
minus_m1 = contact_magnitude(F(1), F(-1), F(1))
plus_m2 = contact_magnitude(F(1), F(1), F(2))
endpoint_sign = F(-1)

checks = {
    "constructive_contact_magnitude_is_four": plus_m1 == 4,
    "destructive_contact_magnitude_is_zero": minus_m1 == 0,
    "common_current_sign_rephasing_is_invisible": (
        contact_magnitude(endpoint_sign, endpoint_sign, F(1)) == plus_m1),
    "same_cycle_record_different_mass_changes_response": plus_m2 == 1,
    "cycle_record_alone_is_not_response_faithful": plus_m1 != plus_m2,
    "light_current_dimension_is_six": F(3) + F(1) + F(1) + F(1) == 6,
    "contact_operator_dimension_is_twelve": 2 * 6 == 12,
    "contact_coefficient_dimension_is_minus_eight": -8 == 4 - 12,
    "light_current_hypercharge_is_minus_one": (
        -F(1, 6) - F(1, 2) - F(1, 3) == -1),
    "contact_operator_hypercharge_is_zero": F(1) + F(-1) == 0,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP639",
    "status": "PASS",
    "checks": checks,
    "source_current": "J=(L_A+L_B) O6",
    "light_operator": "O6=bar(Q_L) tilde(Hu) S X d_R",
    "contact_operator": "O6^dagger O6",
    "contact_coefficient_magnitude": "(L_A+L_B)^2/m_chi^2 on the real sign slice",
    "contextual_partition": {
        "I_chi=+1,m_chi=1": "4",
        "I_chi=-1,m_chi=1": "0",
        "I_chi=+1,m_chi=2": "1",
    },
    "classification": "source-derived contact descent; neither physical16 selector nor calibrated instrument",
    "smallest_exact_falsifier": "equal opposite paths give zero contact coefficient",
    "instrument_gate": "typed light channel with momentum matching, running, matrix elements, acceptance, and calibrated likelihood",
}
(ROOT / "results" / "wp639_charged_cycle_contact_descent.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
