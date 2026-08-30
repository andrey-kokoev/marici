"""Exact WP636 two-path charged messenger interference audit."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def paths(ysu, cb, zbu, ca, ysd, zad, sigma=F(1)):
    p_b = ysu * cb / (zbu * sigma)
    p_a = ca * ysd / (zad * sigma)
    return p_a, p_b

def rate(p_a, p_b):
    return (p_a + p_b) ** 2

p_a_plus, p_b_plus = paths(F(1), F(1), F(1), F(1), F(1), F(1))
p_a_minus, p_b_minus = paths(F(1), F(-1), F(1), F(1), F(1), F(1))
ratio_plus = p_b_plus / p_a_plus
ratio_minus = p_b_minus / p_a_minus

# A common endpoint sign is the residual transformation of the full amplitude.
endpoint_sign = F(-1)
checks = {
    "two_finite_mass_paths_exist": p_a_plus != 0 and p_b_plus != 0,
    "path_ratio_equals_cycle_invariant_on_unit_slice": ratio_plus == 1,
    "opposite_cycle_sign_is_exact": ratio_minus == -1,
    "constructive_rate_is_four": rate(p_a_plus, p_b_plus) == 4,
    "destructive_rate_is_zero": rate(p_a_minus, p_b_minus) == 0,
    "common_endpoint_rephasing_preserves_rate": (
        rate(endpoint_sign * p_a_plus, endpoint_sign * p_b_plus)
        == rate(p_a_plus, p_b_plus)),
    "common_sigma_sign_cancels_from_ratio": (
        paths(F(2), F(3), F(5), F(7), F(11), F(13), F(-1))[1]
        / paths(F(2), F(3), F(5), F(7), F(11), F(13), F(-1))[0]
        == F(2 * 3 * 13, 5 * 7 * 11)),
    "electric_charge_is_conserved": F(2, 3) - F(-1, 3) == 1,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP636", "status": "PASS", "checks": checks,
    "amplitudes": ["P_A=CA*YSd/(ZAd*sigma)",
                   "P_B=YSu*CB/(ZBu*sigma)"],
    "relative_invariant": "P_B/P_A=I_chi",
    "hostile_rates": {"I_chi=+1": "4", "I_chi=-1": "0"},
    "classification": "conditional source-generated threshold probe; not a selector or calibrated instrument",
    "smallest_exact_falsifier": "equal-magnitude opposite paths cancel exactly",
    "instrument_gate": "open mass-eigenstate transition with finite widths, competing decays, production, resolution, and likelihood",
}
(ROOT / "results" / "wp636_charged_cycle_tree_interference.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

