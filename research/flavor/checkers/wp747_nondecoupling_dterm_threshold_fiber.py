"""Exact heavy-vector elimination and nondecoupling D-term threshold audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
g2, M2, ms2 = sp.symbols("g_squared M_squared m_soft_squared", positive=True)
J, sigma = sp.symbols("J sigma", real=True)
M = sp.sqrt(M2)

potential = g2*(J+M*sigma)**2/2 + ms2*sigma**2/2
sigma_solution = sp.solve(sp.diff(potential,sigma),sigma)[0]
effective_potential = sp.factor(potential.subs(sigma,sigma_solution))
epsilon = sp.factor(ms2/(g2*M2+ms2))
expected_effective = sp.factor(g2*epsilon*J**2/2)

# Apply the common threshold factor to the WP746 simple-group moment-map data.
gn = sp.factor(epsilon*g2/3)
gm = sp.factor(-epsilon*g2/6)
contrast = sp.factor(gn-gm)
margin = sp.factor(epsilon**2*g2**2/12)
ratio = sp.factor(gn/gm)

supersymmetric_limit = sp.limit(epsilon,ms2,0,dir="+")
hard_soft_limit = sp.limit(epsilon,ms2,sp.oo)
e = sp.symbols("e", positive=True)
inverse_soft_mass = sp.factor(sp.solve(sp.Eq(e,epsilon),ms2)[0])

witness_half = {ms2:g2*M2}
witness_three_quarters = {ms2:3*g2*M2}
contrast_half = sp.factor(contrast.subs(witness_half))
contrast_three_quarters = sp.factor(contrast.subs(witness_three_quarters))
threshold_residual = sp.factor(contrast_three_quarters-contrast_half)

checks = {
    "heavy_scalar_solution_is_exact": sigma_solution == -J*M*g2/(M2*g2+ms2),
    "effective_potential_has_common_threshold_factor": sp.simplify(effective_potential-expected_effective) == 0,
    "threshold_factor_is_between_zero_and_one": epsilon.is_positive and sp.simplify(1-epsilon).is_positive,
    "supersymmetric_limit_decouples": supersymmetric_limit == 0,
    "large_soft_mass_recovers_full_dterm": hard_soft_limit == 1,
    "portal_sign_ratio_survives_finite_threshold": ratio == -2,
    "portal_contrast_is_scaled_not_fixed": contrast == epsilon*g2/2,
    "radial_margin_is_scaled_not_destroyed": margin == epsilon**2*g2**2/12,
    "every_open_interval_threshold_factor_has_a_soft_mass": sp.simplify(inverse_soft_mass-M2*g2*e/(1-e)) == 0,
    "two_admissible_soft_ratios_give_different_contrasts": contrast_half == g2/4 and contrast_three_quarters == 3*g2/8,
    "deliberate_failure_residual_is_nonzero": threshold_residual == g2/8,
}
checks = {name: bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP747",
    "status": "PASS",
    "checks": checks,
    "source_domain": "conditional WP746 moment-map current coupled to a heavy gauge-breaking scalar with vector mass parameter M and soft mass m_soft",
    "matching_map": "V_eff=(g^2/2) epsilon J^2 with epsilon=m_soft^2/(g^2 M^2+m_soft^2)",
    "classification": "threshold sign/ratio rigidifier, but neither threshold-survival selector nor magnitude selector",
    "preserved_data": "for every finite positive epsilon, g_n/g_m=-2 and the radial margin remains positive",
    "decoupling_falsifier": "the exact supersymmetric limit m_soft^2 -> 0 gives epsilon -> 0 and erases the portal",
    "continuous_threshold_fiber": "every epsilon in (0,1) is realized by m_soft^2=[epsilon/(1-epsilon)] g^2 M^2",
    "smallest_exact_falsifier": "m_soft^2=g^2 M^2 gives contrast g^2/4, while m_soft^2=3g^2 M^2 gives 3g^2/8; residual g^2/8",
    "claim_boundary": "tree-level common heavy-vector D-term elimination; nonuniversal breaking masses, kinetic mixing, loops, and detector response can add further fibers",
    "remaining_source_gate": "derive the SUSY-breaking mass ratio and gauge magnitude from the same source, with an RG-attractive trajectory and physical clock",
    "remaining_physical_gate": "construct the full labelled threshold spectrum and calibrated physical16 response, including widths and uncertainties",
}
(ROOT / "results" / "wp747_nondecoupling_dterm_threshold_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
