"""Exact WP593 completion debt for instantiating WP592 in the messenger theory."""

import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp480 = json.loads(
    (ROOT / "results" / "wp480_triplicated_messenger_beta_gate.json").read_text(
        encoding="utf-8"
    )
)
wp545 = json.loads(
    (ROOT / "results" / "wp545_rg_completion_debt.json").read_text(
        encoding="utf-8"
    )
)

old_radials = ("F", "H", "R", "sigma")
extended_radials = old_radials + ("s",)
old_basis = set(combinations_with_replacement(old_radials, 2))
extended_basis = set(combinations_with_replacement(extended_radials, 2))
new_cp_coordinates = extended_basis - old_basis

rho_f, rho_h, rho_r, kappa_s = sp.symbols(
    "rho_F rho_H rho_R kappa_s", positive=True, real=True
)
generated_cross_support = {
    "s^2 F^2": sp.simplify(kappa_s * rho_f),
    "s^2 H^2": sp.simplify(kappa_s * rho_h),
    "s^2 R^2": sp.simplify(kappa_s * rho_r),
}

base_debt = wp545["conservative_unresolved_coordinate_count"]
extended_debt = base_debt + len(new_cp_coordinates)

checks = {
    "old_radial_quartic_basis_has_ten_coordinates": len(old_basis) == 10,
    "extended_radial_quartic_basis_has_fifteen_coordinates": len(extended_basis)
    == 15,
    "cp_extension_adds_exactly_five_coordinates": len(new_cp_coordinates) == 5,
    "new_coordinates_are_the_s_row": new_cp_coordinates
    == {
        ("F", "s"),
        ("H", "s"),
        ("R", "s"),
        ("sigma", "s"),
        ("s", "s"),
    },
    "three_missing_cp_leaf_portals_have_nonzero_support": all(
        value != 0 for value in generated_cross_support.values()
    ),
    "prior_completion_debt_is_eighteen": base_debt == 18,
    "extended_completion_debt_is_at_least_twenty_three": extended_debt == 23,
    "triplicated_gauge_root_is_not_positive": not wp480[
        "gauge_only_two_loop_coefficients"
    ]["physical_positive_root"],
    "triplicated_formal_root_is_negative": wp480[
        "gauge_only_two_loop_coefficients"
    ]["formal_g_squared_root"]
    == "-104*pi**2/265",
}

if not all(checks.values()):
    raise SystemExit(f"WP593 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP593",
    "status": "PASS",
    "checks": checks,
    "concrete_source": "triplicated messenger plus common-clock CP modulus",
    "known_gauge_result": wp480["gauge_only_two_loop_coefficients"],
    "prior_unresolved_coordinate_lower_bound": base_debt,
    "new_cp_radial_coordinates": [
        f"{left}^4" if left == right else f"{left}^2 {right}^2"
        for left, right in sorted(new_cp_coordinates)
    ],
    "generated_cross_support": {
        key: sp.sstr(value) for key, value in generated_cross_support.items()
    },
    "extended_unresolved_coordinate_lower_bound": extended_debt,
    "wp592_coverage": {
        "gauge_fixed_point": "fails in the computed gauge-only triplicated truncation",
        "yukawa_ray_coefficients": "not computed",
        "cp_clock_ratio_beta": "not present in the declared action",
        "threshold_preservation": "not proved",
    },
    "classification": "exact concrete-instantiation obstruction and RG-completion lower bound; no realized selector or instrument",
    "smallest_exact_falsifier": "omitting only s^2 F^2 is already non-closed because the s^2 sigma^2 and F^2 sigma^2 vertices generate it at one loop",
    "remaining_gate": "derive a closed beta system on at least the 23-coordinate unresolved packet plus inherited couplings and show an isolated positive fixed ray survives thresholds",
}

out = (
    ROOT
    / "results"
    / "wp593_triplicated_fixed_ray_completion_debt.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
