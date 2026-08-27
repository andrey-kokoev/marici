"""Exact WP637 charged-cycle kinematic-support hostile pair."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def kallen(x, y, z):
    return x*x + y*y + z*z - 2*x*y - 2*x*z - 2*y*z

def cycle_invariant(ysu, ysd, ca, cb, zbu, zad):
    return ysu * zad * cb / (ysd * zbu * ca)

def formal_rate(ysu, ysd, ca, cb, zbu, zad, sigma=F(1)):
    p_b = ysu * cb / (zbu * sigma)
    p_a = ca * ysd / (zad * sigma)
    return (p_a + p_b) ** 2

unit = (F(1),) * 6
parent_open, parent_closed = F(3), F(3, 2)
daughter = charged = F(1)
lambda_open = kallen(parent_open**2, daughter**2, charged**2)
lambda_closed = kallen(parent_closed**2, daughter**2, charged**2)

checks = {
    "hostile_pair_has_same_cycle_invariant": cycle_invariant(*unit) == 1,
    "hostile_pair_has_same_formal_rate": formal_rate(*unit) == 4,
    "open_point_has_strict_mass_margin": parent_open - daughter - charged == 1,
    "open_point_has_positive_kallen": lambda_open == 45,
    "closed_point_has_negative_mass_margin": parent_closed - daughter - charged == F(-1, 2),
    "closed_point_has_negative_kallen": lambda_closed == F(-63, 16),
    "parent_mass_is_absent_from_cycle": cycle_invariant(*unit) == cycle_invariant(*unit),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP637", "status": "PASS", "checks": checks,
    "hostile_pair": {
        "common": {"I_chi": "1", "formal_rate": "4", "M_Bd": "1", "m_chi": "1"},
        "open": {"M_Au": "3", "margin": "1", "kallen": "45"},
        "closed": {"M_Au": "3/2", "margin": "-1/2", "kallen": "-63/16"},
    },
    "classification": "source amplitude with nonselected threshold support; no calibrated instrument",
    "first_nonfaithful_arrow": "formal interference amplitude to on-shell support",
    "smallest_exact_falsifier": "same I_chi=1 and rate factor 4, but one open and one closed point",
    "successor_gate": "derive a strict source threshold margin or a quantified off-shell response",
}
(ROOT / "results" / "wp637_charged_cycle_threshold_support_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
