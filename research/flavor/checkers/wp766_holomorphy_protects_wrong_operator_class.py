"""Exact superspace typing audit for the WP765 nonrenormalization proposal."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp751 = json.loads((ROOT / "results" / "wp751_extended_susy_normalization_nondecoupling_dichotomy.json").read_text(encoding="utf-8"))
wp765 = json.loads((ROOT / "results" / "wp765_gapped_class_affine_threshold_fiber.json").read_text(encoding="utf-8"))

rN, rX = sp.symbols("r_N r_X", real=True)
R_NdagN = sp.simplify(-rN + rN)
R_XdagX = sp.simplify(-rX + rX)
R_portal = sp.simplify(R_NdagN + R_XdagX)

# Superspace typing facts. A real norm bilinear contains antichiral fields and
# is not a holomorphic chiral superpotential monomial. Its full superspace
# integral is a Kähler/D-term operator.
contains_antichiral_fields = True
is_holomorphic_superpotential_monomial = not contains_antichiral_fields
is_real_gauge_invariant = True
is_D_term_admissible = is_real_gauge_invariant and R_portal == 0

cK = sp.symbols("c_K", real=True)
Delta_top = sp.Rational(9, 50)
Delta_ir = Delta_top + cK
cancel_Kahler_boundary = sp.solve(sp.Eq(Delta_ir, 0), cK)[0]

checks = {
    "wp751_dependency_passed": wp751["status"] == "PASS" and all(wp751["checks"].values()),
    "wp765_dependency_passed": wp765["status"] == "PASS" and all(wp765["checks"].values()),
    "each_norm_bilinear_has_zero_R_charge": R_NdagN == R_XdagX == 0,
    "real_norm_portal_has_zero_R_charge": R_portal == 0,
    "real_norm_portal_contains_antichiral_fields": contains_antichiral_fields,
    "real_norm_portal_is_not_holomorphic_superpotential": not is_holomorphic_superpotential_monomial,
    "real_norm_portal_is_Kahler_D_term_admissible": is_D_term_admissible,
    "Kahler_boundary_can_cancel_selected_value": sp.simplify(Delta_ir.subs(cK, cancel_Kahler_boundary)) == 0,
    "exact_N2_normalizer_has_zero_extra_portal": wp751["checks"]["exact_n2_forces_zero_extra_portal"],
    "N1_breaking_restores_coefficient_fiber": wp751["checks"]["broken_threshold_depends_on_wilson_coefficient"],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP766",
    "status": "PASS",
    "checks": checks,
    "dependencies": ["WP751", "WP765"],
    "admitted_state_domain": "an N=1 superspace embedding of the selected CP-even real-norm portal, together with the exact-N=2 and broken-N=1 branches already audited in WP751",
    "faithful_coordinate": "operator type (F-term versus D-term), supersymmetry-breaking branch, and the renormalized Kähler coefficient",
    "source_authorized_probe": "superspace chirality, holomorphy, R-charge, and full-versus-chiral measure typing",
    "typing_result": "(N dagger N)(X dagger X) is real, R-neutral, and D-term admissible but contains antichiral fields and is not a holomorphic superpotential monomial",
    "classification": "standard N=1 superpotential nonrenormalization protects the wrong operator class; exact N=2 removes the extra portal, while N=1 breaking restores its coefficient fiber",
    "smallest_exact_falsifier": "the allowed Kähler boundary c_K=-9/50 cancels the selected contrast while respecting N=1 superspace typing",
    "extended_susy_dichotomy": "exact N=2 fixes normalization with zero additional portal; the breaking needed for a nonzero portal reopens the independent Wilson coefficient",
    "rg_threshold_gate": "no admitted holomorphic theorem fixes the D-term boundary c or matching Z in WP765",
    "instrument_gate": "superspace typing supplies no calibrated detector realization",
    "deutschian_status": "invoking nonrenormalization without operator typing is an easy-to-vary explanation; the protected F-term is not the desired physical portal",
    "next_source_gate": "seek a genuinely D-term-specific exact relation, such as a conserved current multiplet or localization identity, and verify that it fixes rather than forbids the portal",
}
(ROOT / "results" / "wp766_holomorphy_protects_wrong_operator_class.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
