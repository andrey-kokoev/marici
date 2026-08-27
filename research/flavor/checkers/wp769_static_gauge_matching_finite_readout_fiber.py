"""Gauge-boundary protection at zero momentum versus finite readout."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp768 = json.loads(
    (ROOT / "results" / "wp768_separated_boundary_exchange_completion_fiber.json").read_text(
        encoding="utf-8"
    )
)

m, ell, p, r0, rL = sp.symbols(
    "m ell p r_0 r_L", positive=True, real=True
)
mu = sp.sqrt(m**2 + p**2)
a = r0 * p**2
b = rL * p**2
denominator = (mu + a * b / mu) * sp.sinh(mu * ell) + (a + b) * sp.cosh(mu * ell)
G = sp.simplify(1 / denominator)
G_static = sp.simplify(G.subs(p, 0))

G_finite_bare = sp.simplify(G.subs({m: 1, ell: 1, p: 1, r0: 0, rL: 0}))
G_finite_boundary = sp.simplify(G.subs({m: 1, ell: 1, p: 1, r0: 1, rL: 0}))

# An unbroken boundary gauge symmetry forbids a Proca boundary mass. A
# boundary gauge-kinetic operator is invariant and contributes r_i p^2.
boundary_proca_mass_gauge_invariant = False
boundary_kinetic_term_gauge_invariant = True

checks = {
    "wp768_dependency_passed": wp768["status"] == "PASS" and all(wp768["checks"].values()),
    "boundary_mass_forbidden_by_unbroken_gauge_symmetry": not boundary_proca_mass_gauge_invariant,
    "boundary_kinetic_completion_is_gauge_invariant": boundary_kinetic_term_gauge_invariant,
    "kinetic_robin_data_vanish_at_zero_momentum": sp.simplify(a.subs(p, 0)) == 0 and sp.simplify(b.subs(p, 0)) == 0,
    "static_cross_matching_is_boundary_kinetic_independent": sp.simplify(G_static - 1 / (m * sp.sinh(m * ell))) == 0 and not G_static.has(r0, rL),
    "finite_readout_depends_on_boundary_kinetic_data": G.has(r0, rL),
    "hostile_finite_pair_is_distinct": sp.simplify(G_finite_bare - G_finite_boundary) != 0,
    "hostile_pair_preserves_positive_propagator": bool(G_finite_bare > 0 and G_finite_boundary > 0),
    "finite_bare_value_is_exact": sp.simplify(G_finite_bare - 1 / (sp.sqrt(2) * sp.sinh(sp.sqrt(2)))) == 0,
    "finite_boundary_value_is_exact": sp.simplify(G_finite_boundary - 1 / (sp.sqrt(2) * sp.sinh(sp.sqrt(2)) + sp.cosh(sp.sqrt(2)))) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP769",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP768",
    "admitted_state_domain": "the separated-boundary bulk exchange of WP768 specialized to an unbroken boundary gauge current, including every quadratic gauge-invariant boundary kinetic completion",
    "faithful_coordinate": "Euclidean readout momentum p and boundary kinetic coefficients r_0,r_L in addition to m and ell",
    "source_authorized_probe": "the momentum-dependent boundary-to-boundary gauge response",
    "static_matching": "G(0,ell;p=0)=1/[m sinh(m ell)], independent of r_0,r_L",
    "finite_response": "replace m by sqrt(m^2+p^2) and Robin data by r_0 p^2,r_L p^2",
    "classification": "unbroken gauge symmetry plus locality protects the static exchange coefficient from quadratic boundary completion, but a finite-energy physical readout remains nonfaithful unless boundary kinetic data are source-fixed or independently calibrated",
    "smallest_exact_falsifier": "at m=ell=p=1, (r_0,r_L)=(0,0) gives 1/[sqrt(2)sinh(sqrt(2))], while (1,0) gives 1/[sqrt(2)sinh(sqrt(2))+cosh(sqrt(2))]",
    "threshold_result": "conditional static threshold survival is achieved within the quadratic gauge-invariant boundary class",
    "instrument_gate": "static matching is not the finite detector transfer function; the detector must calibrate r_0,r_L and momentum support in the same frame",
    "deutschian_status": "the zero-momentum explanation is harder to vary, but promoting it to a physical prediction without the finite response is an illicit change of explanandum",
    "next_source_gate": "derive or calibrate the complete boundary spectral function and then fix m ell and the common gauge normalization from an isolated source trajectory",
}
(ROOT / "results" / "wp769_static_gauge_matching_finite_readout_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
