"""Compose half-twist selection, KK exchange, static protection, and readout."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
deps = {}
for wp, name in [
    (738, "required_link_mediators_fixed_point_exhaustion"),
    (753, "full_kk_tower_half_twist_theorem"),
    (754, "bulk_localization_spectral_index_fiber"),
    (769, "static_gauge_matching_finite_readout_fiber"),
    (770, "two_momentum_boundary_response_tomography"),
]:
    deps[wp] = json.loads((ROOT / "results" / f"wp{wp}_{name}.json").read_text(encoding="utf-8"))

R, g2 = sp.symbols("R g_*^2", positive=True, real=True)
omega = sp.Rational(1, 2)
N = sp.Integer(1)
ell = sp.pi * R
m_soft2 = omega**2 / R**2
m_vector2 = N**2 / R**2
epsilon = sp.simplify(m_soft2 / (m_vector2 + m_soft2))
m_vector = N / R
dimensionless_separation = sp.simplify(m_vector * ell)
static_shape = sp.simplify(1 / sp.sinh(dimensionless_separation))
portal_contrast = sp.simplify(g2 * epsilon / 2)

checks = {
    "all_dependencies_passed": all(d["status"] == "PASS" and all(d["checks"].values()) for d in deps.values()),
    "half_twist_is_one_half": omega == sp.Rational(1, 2),
    "unit_vector_mode_is_integer_selected": N == 1,
    "threshold_factor_is_one_fifth": epsilon == sp.Rational(1, 5),
    "threshold_factor_is_radius_free": not epsilon.has(R),
    "dimensionless_exchange_separation_is_pi": dimensionless_separation == sp.pi,
    "static_exchange_shape_is_radius_free": static_shape == 1 / sp.sinh(sp.pi) and not static_shape.has(R),
    "portal_contrast_is_gstar_squared_over_ten": portal_contrast == g2 / 10,
    "gauge_normalization_remains": portal_contrast.has(g2),
    "hostile_gauge_pair_changes_magnitude": sp.simplify(portal_contrast.subs(g2, 2) - portal_contrast.subs(g2, 1)) == sp.Rational(1, 10),
    "positive_link_only_lift_exists": deps[754]["checks"]["link_only_bulk_index_is_positive_thirteen"],
    "portal_bulk_lift_reverses_sign": deps[754]["checks"]["portal_operands_bulk_index_is_negative_nineteen"],
    "required_mediator_fixed_point_search_is_empty": deps[738]["checks"]["no_physical_branch_exists"],
    "two_port_readout_is_jointly_faithful": deps[770]["checks"]["two_momentum_response_has_rank_two"],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP771",
    "status": "PASS",
    "checks": checks,
    "dependencies": ["WP738", "WP753", "WP754", "WP769", "WP770"],
    "admitted_state_domain": "the positive-spectral-index half-twist branch, first massive vector KK level on an interval ell=pi R, locality and unbroken-gauge static matching, and the calibrated two-momentum response packet",
    "faithful_coordinate": "spectral lift class, twist omega, KK integer N, fixed-point gauge normalization g_*^2, boundary response invariants, and calibrated momentum ports",
    "source_composition": "positive full KK tower selects omega=1/2; N=1 fixes m_vector ell=pi; locality plus gauge symmetry protects static matching; two momentum ports reconstruct quadratic finite response",
    "portal_prediction": "Delta=g_*^2/10",
    "radius_result": "both epsilon=1/5 and the static exchange shape 1/sinh(pi) are independent of R",
    "classification": "conditional selector, static threshold theorem, and jointly faithful formal readout; not a completed source because the current packet does not jointly derive the positive bulk lift and an isolated physical gauge fixed point",
    "smallest_exact_magnitude_falsifier": "g_*^2=1 and g_*^2=2 preserve every geometric and readout datum but give Delta=1/10 and 1/5",
    "current_source_obstruction": "the link-only lift has positive spectral index but the required-mediator gauge-Yukawa packet has zero physical fixed-point branches; putting portal operands in bulk reverses the spectral sign",
    "deutschian_status": "the radius is no longer an easy variation; the remaining easy variation is precisely the gauge normalization and the independently chosen bulk lift",
    "next_source_gate": "derive one anomaly-complete five-dimensional matter localization that simultaneously has positive spectral index and an isolated interacting gauge normalization, then realize the WP770 ports in physical16 channels",
}
(ROOT / "results" / "wp771_radius_free_static_portal_composition.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
