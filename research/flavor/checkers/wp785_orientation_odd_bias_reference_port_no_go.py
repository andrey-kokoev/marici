"""Exact audit of the smallest orientation-odd flux bias."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp784 = json.loads(
    (ROOT / "results" / "wp784_flux_energy_metric_rigidifier_orientation_doublet.json")
    .read_text(encoding="utf-8")
)

u, v, t, mu, theta = sp.symbols("u v t mu theta", real=True)
k, c = sp.symbols("k c", nonzero=True, real=True)
I = sp.I

J = sp.diag(1, -1)
R = sp.Matrix([[0, -1], [-1, 0]])
f_plus = sp.Matrix([2, -1])
f_minus = sp.Matrix([1, -2])
b = sp.Matrix([1, 1])

q = lambda f: sp.expand((f.T * J * f)[0])
pairing = lambda f: sp.expand((b.T * J * f)[0])

base = sp.Rational(1, 2) * (sp.exp(t) * u**2 + sp.exp(-t) * v**2)
real_bias = sp.expand(base + mu * u * v)
gram = sp.Matrix([[sp.exp(t), mu], [mu, sp.exp(-t)]])

e_plus = sp.simplify(real_bias.subs({t: sp.log(3), u: 1, v: 3}))
e_minus = sp.simplify(real_bias.subs({t: sp.log(3), u: -1, v: 3}))
splitting = sp.simplify(e_plus - e_minus)

w_plus = sp.exp(-3 + I * theta * q(f_plus))
w_minus = sp.exp(-3 + I * theta * q(f_minus))
modulus_ratio = sp.simplify(
    (w_plus * sp.conjugate(w_plus)) / (w_minus * sp.conjugate(w_minus))
)

relational_descent = sp.simplify(
    real_bias.subs({u: -u, mu: -mu}, simultaneous=True) - real_bias
)
fixed_reference_failure = sp.simplify(real_bias.subs(u, -u) - real_bias)

lam, mu0 = sp.symbols("lambda mu0", positive=True)
reference_potential = lam * (mu**2 - mu0**2) ** 2
paired_plus = sp.simplify(e_plus.subs(mu, -mu0) + reference_potential.subs(mu, -mu0))
paired_minus = sp.simplify(e_minus.subs(mu, mu0) + reference_potential.subs(mu, mu0))

gs_tangent_constant_bias = sp.simplify(
    k * sp.diff(splitting, k) - c * sp.diff(splitting, c)
)

checks = {
    "wp784_dependency_passed": wp784["status"] == "PASS"
    and all(wp784["checks"].values()),
    "reflection_exchanges_the_two_minimizers": R * f_plus == f_minus,
    "pairing_three_is_preserved_by_reflection": pairing(f_plus)
    == pairing(f_minus)
    == 3,
    "lattice_norm_is_the_smallest_odd_discriminator": (q(f_plus), q(f_minus))
    == (3, -3),
    "reflection_is_anti_isometric": R.T * J * R == -J,
    "topological_phase_does_not_split_probability_weights": modulus_ratio == 1,
    "real_orientation_bias_splits_by_six_mu": splitting == 6 * mu,
    "real_bias_is_positive_only_inside_open_unit_interval": sp.det(gram)
    == 1 - mu**2,
    "fixed_reference_fails_reflection_descent": fixed_reference_failure
    == -2 * mu * u * v,
    "pseudoscalar_reference_restores_relational_descent": relational_descent == 0,
    "symmetric_dynamic_reference_leaves_paired_vacua": sp.simplify(
        paired_plus - paired_minus
    )
    == 0,
    "constant_bias_is_green_schwarz_tangent_blind": gs_tangent_constant_bias == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP785",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP784",
    "admitted_state_domain": (
        "the WP784 orientation doublet, its compatible positive quadratic flux "
        "energy, a possible topological phase theta*q, and the smallest real "
        "orientation bias mu*q"
    ),
    "faithful_coordinate": (
        "pairing b.f=3, lattice norm q=f^2, metric ratio t, Green-Schwarz "
        "coordinates (k,c), and an explicitly typed pseudoscalar reference mu"
    ),
    "source_authorized_probe": (
        "WP784 quadratic energy plus only the standard reference-free "
        "topological phase; the real mu*q bias is audited as a candidate, not "
        "admitted as source-derived"
    ),
    "contextual_partition": (
        "q separates the two physical flux states algebraically, but the "
        "reference-free topological phase leaves their probability weights equal"
    ),
    "candidate_result": (
        "a real mu*q term selects a branch and preserves positivity for |mu|<1, "
        "but fixed mu fails orientation-reversal descent; treating mu as a "
        "pseudoscalar reference restores descent only in a new relational "
        "experiment"
    ),
    "dynamic_reference_result": (
        "a reflection-symmetric dynamical reference has paired equal-energy "
        "vacua and therefore correlates orientation without predicting an "
        "absolute branch"
    ),
    "green_schwarz_result": (
        "constant mu is blind to the product-preserving tangent (k,-c); making "
        "mu transverse requires a new k,c-dependent source law not supplied by "
        "anomaly cancellation"
    ),
    "classification": (
        "the lattice norm is a discriminator, not yet a selector; theta is "
        "neither, a fixed real bias is an undeclared selector, and a "
        "pseudoscalar port is a relational selector with a changed groupoid"
    ),
    "smallest_exact_falsifier": (
        "f+=(2,-1) and f-=(1,-2) have q=+3 and q=-3, while their Euclidean "
        "topological weights exp(-3+i*theta*q) have exactly equal modulus"
    ),
    "deutschian_status": (
        "adding mu*q makes the desired answer easy to fit but does not explain "
        "mu; a satisfactory explanation must derive the reference orientation, "
        "its magnitude, and its coupling to the Green-Schwarz scale"
    ),
    "remaining_gate": (
        "derive a symmetry-breaking boundary/source state with calibrated "
        "orientation, prove a nonzero Green-Schwarz-transverse response, and "
        "transport it through RG, thresholds, and a physical16 instrument"
    ),
}
(ROOT / "results" / "wp785_orientation_odd_bias_reference_port_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
