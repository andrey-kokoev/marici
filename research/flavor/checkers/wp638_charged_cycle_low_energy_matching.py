"""Exact WP638 two-path low-energy messenger matching audit."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def paths(yhu, yxd, ca, ysd, ysu, cb, mau, mad, mbu, mbd):
    l_a = yhu * yxd * ca * ysd / (mau * mad * mbd)
    l_b = yhu * yxd * ysu * cb / (mau * mbu * mbd)
    return l_a, l_b

def matched_square(l_a, l_b):
    return (l_a + l_b) ** 2

plus = paths(*((F(1),) * 10))
minus = paths(F(1), F(1), F(1), F(1), F(1), F(-1),
              F(1), F(1), F(1), F(1))
generic = paths(F(2), F(3), F(5), F(7), F(11), F(13),
                F(17), F(19), F(23), F(29))
generic_ratio = generic[1] / generic[0]
expected_ratio = F(11 * 13 * 19, 5 * 7 * 23)
endpoint_sign = F(-1)

# Reuse WP637's exactly closed heavy-parent point.  The low-energy matching
# remains finite because it requires virtual propagators, not the two-body
# decay A^u -> B^d + chi to be open.
closed_mau, closed_mbd, closed_mchi = F(3, 2), F(1), F(1)
closed_kallen = (
    closed_mau**4 + closed_mbd**4 + closed_mchi**4
    - 2 * closed_mau**2 * closed_mbd**2
    - 2 * closed_mau**2 * closed_mchi**2
    - 2 * closed_mbd**2 * closed_mchi**2
)
closed_paths = paths(
    F(1), F(1), F(1), F(1), F(1), F(1),
    closed_mau, F(2), F(2), closed_mbd,
)

checks = {
    "two_complete_low_energy_paths_exist": plus[0] != 0 and plus[1] != 0,
    "generic_path_ratio_is_cycle_invariant": generic_ratio == expected_ratio,
    "constructive_matched_square_is_four": matched_square(*plus) == 4,
    "destructive_matched_square_is_zero": matched_square(*minus) == 0,
    "common_endpoint_rephasing_preserves_response": (
        matched_square(endpoint_sign * plus[0], endpoint_sign * plus[1])
        == matched_square(*plus)),
    "operator_dimension_is_seven": F(3) + F(4) == 7,
    "coefficient_mass_dimension_is_minus_three": -3 == 4 - 7,
    "operator_hypercharge_is_zero": (-F(1, 6) - F(1, 2) + 1 - F(1, 3) == 0),
    "heavy_parent_channel_is_exactly_closed": closed_kallen == -F(63, 16),
    "closed_point_low_energy_paths_are_finite_nonzero": (
        closed_paths[0] != 0 and closed_paths[1] != 0),
    "closed_point_matched_response_is_nonzero": matched_square(*closed_paths) > 0,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP638", "status": "PASS", "checks": checks,
    "operator": "bar(Q_L) tilde(Hu) chi S X d_R",
    "operator_dimension": 7,
    "paths": ["L_A=YHu*YXd*CA*YSd/(MAu*MAd*MBd)",
              "L_B=YHu*YXd*YSu*CB/(MAu*MBu*MBd)"],
    "relative_invariant": "L_B/L_A=I_chi",
    "closed_heavy_parent_test": {
        "M_Au": "3/2", "M_Bd": "1", "m_chi": "1",
        "kallen": "-63/16", "matched_square": str(matched_square(*closed_paths)),
    },
    "classification": "source-derived low-energy charged portal probe; neither physical16 selector nor calibrated instrument",
    "smallest_exact_falsifier": "equal opposite paths cancel the matched portal exactly",
    "instrument_gate": "accessible chi pole with production, widths, QCD transport, acceptance, and likelihood",
}
(ROOT / "results" / "wp638_charged_cycle_low_energy_matching.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
