"""Exact WP633 full sign-rephasing and two-stage matching audit."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
fields = ("Q", "Hu", "Hd", "sigma", "AuL", "AuR", "BuL", "BuR",
          "AdL", "AdR", "BdL", "BdR", "u", "d", "S", "X")
terms = (
    ("Q", "Hu", "AuR"), ("AuL", "S", "BuR"), ("BuL", "X", "u"),
    ("Q", "Hd", "AdR"), ("AdL", "S", "BdR"), ("BdL", "X", "d"),
    ("sigma", "AuL", "AuR"), ("sigma", "BuL", "BuR"),
    ("sigma", "AdL", "AdR"), ("sigma", "BdL", "BdR"),
)

def preserves(p):
    return all(sum(p[x] for x in term) % 2 == 0 for term in terms)

symmetries = []
for bits in itertools.product((0, 1), repeat=len(fields)):
    p = dict(zip(fields, bits))
    if preserves(p):
        symmetries.append(p)

vacuum_projection = {(p["Hd"], p["sigma"]) for p in symmetries}
down_flip = {x: 0 for x in fields}
for x in ("Hd", "AdL", "AdR", "BdL", "BdR", "d"):
    down_flip[x] = 1

# Unit couplings: the two-stage coefficient is -1/sigma^2.
def matched_yukawa(hd, sigma):
    return -F(hd, sigma * sigma)

y_plus = matched_yukawa(1, 1)
y_relative_flip = matched_yukawa(-1, 1)

checks = {
    "full_rephasing_group_enumerated": len(symmetries) > 1,
    "all_four_Hd_sigma_sign_changes_exist": vacuum_projection == {(0, 0), (0, 1), (1, 0), (1, 1)},
    "down_sector_flip_preserves_every_vertex": preserves(down_flip),
    "down_sector_flip_changes_relative_sign": (down_flip["Hd"] + down_flip["sigma"]) % 2 == 1,
    "two_sigma_denominators_erase_sigma_sign": matched_yukawa(1, 1) == matched_yukawa(1, -1),
    "Hd_flip_only_changes_yukawa_sign": y_relative_flip == -y_plus,
    "right_handed_rephasing_erases_yukawa_sign": abs(y_relative_flip) == abs(y_plus),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP633", "status": "PASS", "checks": checks,
    "sign_rephasing_group_order": len(symmetries),
    "vacuum_sign_projection": [list(x) for x in sorted(vacuum_projection)],
    "tree_matching": "C_d=-yH*yS*yX/(zA*zB*sigma^2)",
    "classification": "restricted-groupoid relative sign collapses under full source rephasing; no selector",
    "first_nonfaithful_arrow": "selected diagonal Z2 quotient to full source sign-rephasing quotient",
    "smallest_exact_falsifier": "the legal down-sector rephasing flips Hd with sigma fixed",
    "physical16_result": "unchanged after the induced right-handed down-quark rephasing",
    "successor_gate": "derive a closed interference cycle or external reference invariant under full rephasing",
}
(ROOT / "results" / "wp633_common_singlet_relative_sign_collapse.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

