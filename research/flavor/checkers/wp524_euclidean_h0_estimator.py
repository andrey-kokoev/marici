"""Exact consistency checks for the WP522 Euclidean H_0 estimator contract."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp522 = load("wp522_six_resolvent_bilocal_basis.json")
wp523 = load("wp523_h0_instrument_census.json")

x, a, s4 = sp.symbols("x a s4", nonnegative=True)
mb, ms, scalar_r, scalar_l = sp.symbols("m_b m_s S_R S_L")
f6 = 15625 * x**3 + 493300 * x**2 + 2874619 * x + 3873024
f7 = (
    2500015625 * x**3
    + 78928115075 * x**2
    + 459939206528 * x
    + 619683840000
)
D = sp.expand(f6 * f7)
n0 = sp.Integer(2400050384732160000)
F = sp.cancel(n0 / D)
wp520_F = sp.sympify(
    wp520["aligned_bs_kernel"]["normalized_spacelike_form_factor"],
    locals={"q_squared": x},
)

# For the standard nearest-neighbor lattice momentum,
# qhat^2 = q^2 - a^2 sum_mu q_mu^4/12 + O(a^4).
delta = -a**2 * s4 / 12
kernel_through_a2 = sp.series(1 / D.subs(x, x + delta), a, 0, 4).removeO()
expected_through_a2 = 1 / D + a**2 * s4 * sp.diff(D, x) / (12 * D**2)
continuum_residual = sp.cancel(kernel_through_a2 - expected_through_a2)

contact = sp.Integer(1)
source_slope = sp.diff(F, x).subs(x, 0)
contact_slope = sp.diff(contact, x).subs(x, 0)

# The left-handed flavor-changing current is not conserved. On shell,
# q_mu bar{s} gamma^mu P_L b = m_b bar{s} P_R b - m_s bar{s} P_L b.
current_divergence = mb * scalar_r - ms * scalar_l
hostile_divergence = current_divergence.subs(
    {mb: sp.Integer(5), ms: sp.Integer(1), scalar_r: 1, scalar_l: 0}
)

# Exact Euclidean pole audit. Each cubic must have three negative real roots;
# hence D(Q^2) has no pole for Q^2 >= 0.
negative_roots_f6 = sp.Poly(f6, x).count_roots(-sp.oo, 0)
negative_roots_f7 = sp.Poly(f7, x).count_roots(-sp.oo, 0)
common_factor = sp.gcd(sp.Poly(f6, x), sp.Poly(f7, x)).as_expr()

checks = {
    "wp520_dependency_passed": bool(wp520["passed"]),
    "wp522_dependency_passed": bool(wp522["passed"]),
    "wp523_dependency_passed": bool(wp523["passed"]),
    "frozen_kernel_matches_wp520": sp.cancel(F - wp520_F) == 0,
    "frozen_h0_coefficient_matches_wp522": str(n0)
    == wp522["frozen_source_probe"]["wp520_coefficient"],
    "cubics_are_coprime": common_factor == 1,
    "all_six_euclidean_poles_are_timelike": negative_roots_f6 == 3
    and negative_roots_f7 == 3,
    "lattice_kernel_has_exact_continuum_limit_through_a2": continuum_residual == 0,
    "contact_substitution_is_deliberately_falsified_by_slope": source_slope
    != contact_slope,
    "flavor_changing_left_current_is_not_identically_conserved": current_divergence
    != 0,
    "smallest_longitudinal_hostile_witness_is_nonzero": hostile_divergence != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP524",
    "source_domain": "Frozen WP520 aligned finite-propagator B_s kernel and the WP522 direct H_0 functional.",
    "euclidean_estimator_contract": {
        "current": "J_mu_bs(x)=bar{s}_L(x) gamma_mu b_L(x)",
        "kernel_momentum_space": sp.sstr(1 / D),
        "weighted_correlator": "Sum_{x,y} <O_Bsbar(T) J_mu_bs(x) K_a,munu(x-y) J_nu_bs(y) O_Bsbar_dagger(0)>, with the standard integrated-correlator slope extracted after declared subtractions.",
        "lattice_momentum": "qhat^2=sum_mu 4 sin^2(a q_mu/2)/a^2",
        "continuum_expansion": sp.sstr(expected_through_a2),
        "physical_readout": "Multiply the renormalized continuum H_0 matrix element by the frozen source coefficient n_0 and the independently declared current normalization before entering M_12^s.",
        "authority_limit": "This estimator covers only the scalar J_mu J_mu contraction encoded by WP520. It is not the full gauge-invariant massive-vector exchange amplitude.",
    },
    "tensor_completion_obstruction": {
        "on_shell_current_divergence": sp.sstr(current_divergence),
        "hostile_witness": sp.sstr(hostile_divergence),
        "consequence": "The longitudinal q_mu q_nu part of a massive-vector propagator does not vanish for the b-to-s left current. Goldstone and scalar-operator terms cannot be inferred from the scalar WP520 form factor alone.",
    },
    "pole_certificate": {
        "negative_real_roots_first_cubic": int(negative_roots_f6),
        "negative_real_roots_second_cubic": int(negative_roots_f7),
        "common_factor": sp.sstr(common_factor),
        "consequence": "The Euclidean kernel is nonsingular on Q^2 >= 0; its six poles lie on the timelike continuation.",
    },
    "required_calibrations": [
        "nonperturbative current renormalization in a declared scheme",
        "coincident-point contact subtraction and mixing counterterms",
        "finite-volume and continuum extrapolations",
        "heavy-quark discretization and tuning systematics",
        "matching across every light-mediator threshold",
        "normalization and covariance in the DeltaM_s likelihood",
    ],
    "classification": "Exact scalar-kernel estimator contract plus a tensor-completion obstruction. It preserves WP522 H_0 and has a controlled continuum limit, but it is not yet a gauge-invariant physical instrument because the flavor-changing current is nonconserved.",
    "selector": False,
    "rigidifier": False,
    "instrument": "The scalar lattice integrated-correlator architecture is typed. Physical-instrument authority is withheld until the full transverse, longitudinal, Goldstone, and counterterm packet is derived from the same broken flavor-gauge action and then evaluated on calibrated B_s ensembles.",
    "smallest_exact_falsifier": "At unequal b and s masses, q_mu J_L^mu=m_b S_R-m_s S_L is not identically zero. Therefore a scalar H_0 convolution alone cannot certify the full massive-vector exchange amplitude.",
    "remaining_gate": "Derive the gauge-parameter-independent tensor plus Goldstone bilocal kernel from the admitted flavon action, enlarge the operator basis by the induced scalar channels, and only then execute the renormalized B_s estimator and publish its covariance.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp524_euclidean_h0_estimator.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
