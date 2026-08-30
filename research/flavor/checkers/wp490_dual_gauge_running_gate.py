"""Exact one-loop dual-gauge running gate for the WP489 field content."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp483 = load("wp483_connector_frame_architecture.json")
wp489 = load("wp489_common_source_threshold_constructor.json")

# SU(3)_F coefficient is independently reconstructed in WP483.
b0_f = sp.Rational(-37, 2)

# SO(3)_P is locally SU(2), with C_A=2 and T(vector)=2. Only the second-stage
# B messengers carry the port vector index. Their multiplicity for the port
# trace is two SM charge sectors times three colors times dim(3_F).
ca_p = sp.Integer(2)
t_vector = sp.Integer(2)
b_dirac_vector_multiplicity = sp.Integer(2) * sp.Integer(3) * sp.Integer(3)
s2_f_p = b_dirac_vector_multiplicity * t_vector

# Real port-vector scalars: eight SU(3)_F-adjoint components of X_i and three
# connector rows S_alpha_i.
real_scalar_vector_multiplicity = sp.Integer(8) + sp.Integer(3)
s2_s_p = real_scalar_vector_multiplicity * t_vector
b0_p = sp.factor(
    sp.Rational(11, 3) * ca_p
    - sp.Rational(4, 3) * s2_f_p
    - sp.Rational(1, 6) * s2_s_p
)

# In beta_g=-b0*g^3/(16 pi^2), both negative b0 values give positive cubic
# running. The exact simultaneous one-loop ray fixes only a coupling ratio.
c_f = -b0_f
c_p = -b0_p
ray_g_p2_over_g_f2 = sp.factor(c_f / c_p)
wp489_witness_ratio = sp.Rational(1, 68)

g_f2, g_p2 = sp.symbols("g_F_squared g_P_squared", positive=True)
log_ratio_beta_numerator = sp.factor(c_p * g_p2 - c_f * g_f2)

checks = {
    "wp483_dependency_passed": wp483["passed"],
    "wp489_dependency_passed": wp489["passed"],
    "port_dirac_vector_multiplicity_is_eighteen": b_dirac_vector_multiplicity == 18,
    "port_real_scalar_vector_multiplicity_is_eleven": real_scalar_vector_multiplicity == 11,
    "port_fermion_dynkin_sum_is_thirty_six": s2_f_p == 36,
    "port_scalar_dynkin_sum_is_twenty_two": s2_s_p == 22,
    "flavor_one_loop_coefficient_is_negative": b0_f == -sp.Rational(37, 2),
    "port_one_loop_coefficient_is_negative": b0_p == -sp.Rational(133, 3),
    "no_positive_nonzero_one_loop_fixed_point_for_either_factor": b0_f < 0 and b0_p < 0,
    "dual_gauge_ray_ratio_is_exact": ray_g_p2_over_g_f2 == sp.Rational(111, 266),
    "ray_annihilates_ratio_beta": sp.simplify(
        log_ratio_beta_numerator.subs(g_p2, ray_g_p2_over_g_f2 * g_f2)
    ) == 0,
    "wp489_existence_witness_is_not_on_gauge_ray": wp489_witness_ratio != ray_g_p2_over_g_f2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP490",
    "domain": "unbroken high-scale WP489 field content above both messenger thresholds, in the WP483 one-loop convention",
    "charged_matter_census": {
        "SU(3)_F": "WP483: 42 Dirac fundamentals and three real adjoint triplet labels",
        "SO(3)_P_dirac_vectors": int(b_dirac_vector_multiplicity),
        "SO(3)_P_real_scalar_vectors": int(real_scalar_vector_multiplicity),
        "SO(3)_P_S2_fermions": str(s2_f_p),
        "SO(3)_P_S2_scalars": str(s2_s_p),
    },
    "one_loop_coefficients": {"b0_F": str(b0_f), "b0_P": str(b0_p)},
    "gauge_only_fixed_points": "only the Gaussian point at one loop; neither factor has a positive finite nonzero zero",
    "dual_gauge_fixed_ray": {
        "g_P_squared_over_g_F_squared": str(ray_g_p2_over_g_f2),
        "meaning": "an exact ratio trajectory and asymptotic Gaussian-IR ratio, not a finite nonzero coupling selector",
        "WP489_witness_ratio": str(wp489_witness_ratio),
    },
    "classification": "Gauge running supplies a conditional coupling-ratio ray but cannot select the finite g_F needed for a nonzero physical clock prediction.",
    "selector": "ratio-only asymptotic ray; no finite gauge-coupling selector",
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "Both exact one-loop coefficients are negative, so beta_g is positive for every nonzero positive coupling and has no finite gauge-only zero.",
    "remaining_gate": "Derive the complete gauge-Yukawa beta system with threshold matching. A finite selector requires Yukawa contributions that create a controlled interacting fixed point or another independently declared boundary operation.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp490_dual_gauge_running_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
