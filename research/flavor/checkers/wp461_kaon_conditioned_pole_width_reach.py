"""Exact conditional reach and detector-resolution audit for WP457."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp449 = json.loads(
    (root / "results" / "wp449_triplet_width_packet.json").read_text(
        encoding="utf-8"
    )
)
wp456 = json.loads(
    (root / "results" / "wp456_pole_resolved_current_complement.json").read_text(
        encoding="utf-8"
    )
)
wp457 = json.loads(
    (root / "results" / "wp457_pole_clock_parameter_identifiability.json").read_text(
        encoding="utf-8"
    )
)
wp460 = json.loads(
    (root / "results" / "wp460_provisional_deltamk_likelihood.json").read_text(
        encoding="utf-8"
    )
)

# Atlas response factors for a physical vectorlike coefficient A:
# F_5=(Pqq+Pdd+2 Pqd)*(5 TeV)^2 and similarly at 100 TeV.
f_5 = sp.Integer(263_200_000)
f_100 = sp.Integer(338_330_000)
m1_tev = sp.Integer(5)
v_tev = sp.Rational(123, 500)

# The worst declared threshold envelope uses F(m3)=F_100.
minimum_response_per_g_squared = sp.simplify(
    (3 * f_5 - f_100) / (24 * m1_tev**2)
)
x_upper = sp.sympify(wp460["working_95_percent_interval"]["exact_upper"])
g_squared_max = sp.simplify(x_upper / minimum_response_per_g_squared)
g_max = sp.sqrt(g_squared_max)
mu_min_tev = sp.simplify(m1_tev / g_max)
f_min_tev = sp.simplify(sp.sqrt(6) * mu_min_tev)
target_benchmark = sp.simplify(sp.sqrt(6) * m1_tev / v_tev)

gamma1_max_gev = sp.simplify(
    (1000 * m1_tev) * g_squared_max / (4 * sp.pi)
)
detector_fractional_resolution = sp.Rational(3, 100)
detector_resolution_gev = sp.simplify(
    1000 * m1_tev * detector_fractional_resolution
)
resolution_to_width = sp.simplify(detector_resolution_gev / gamma1_max_gev)

checks = {
    "wp449_dependency_passed": wp449["passed"],
    "wp456_dependency_passed": wp456["passed"],
    "wp457_dependency_passed": wp457["passed"],
    "wp460_dependency_passed": wp460["passed"],
    "atlas_endpoint_ratio_exact": f_100 / f_5
    == sp.Rational(33_833, 26_320),
    "envelope_minimum_response_positive": minimum_response_per_g_squared
    == sp.Rational(2_256_350, 3),
    "provisional_endpoint_bounds_coupling": g_squared_max > 0,
    "conditional_scale_reconstruction_exact": sp.simplify(g_max * mu_min_tev)
    == m1_tev,
    "benchmark_target_is_pole_readout": target_benchmark
    == 2500 * sp.sqrt(6) / 123,
    "detector_resolution_is_150_GeV": detector_resolution_gev == 150,
    "intrinsic_width_is_below_resolution": gamma1_max_gev
    < detector_resolution_gev,
    "width_resolution_gap_exceeds_five_orders": resolution_to_width > 100_000,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP461",
    "benchmark": {
        "m_triplet_TeV": int(m1_tev),
        "m_quintet_TeV": str(sp.sqrt(3) * m1_tev),
        "not_source_selected": "The triplet pole mass is frozen as a reach benchmark.",
    },
    "transport_envelope": {
        "F_5_TeV_squared": int(f_5),
        "F_100_TeV_squared": int(f_100),
        "endpoint_ratio": str(f_100 / f_5),
        "assumption": "F_5 <= F(m_quintet) <= F_100; no interpolation is claimed.",
        "minimum_x_per_g_F_squared": str(minimum_response_per_g_squared),
    },
    "conditional_working_limits": {
        "g_F_max": str(g_max),
        "g_F_max_decimal": float(g_max.evalf()),
        "mu_min_TeV": str(mu_min_tev),
        "mu_min_TeV_decimal": float(mu_min_tev.evalf()),
        "f_min_TeV": str(f_min_tev),
        "f_min_TeV_decimal": float(f_min_tev.evalf()),
        "g_F_f_over_v_benchmark": str(target_benchmark),
        "g_F_f_over_v_benchmark_decimal": float(target_benchmark.evalf()),
    },
    "width_and_detector": {
        "Gamma_triplet_max_GeV": str(gamma1_max_gev),
        "Gamma_triplet_max_GeV_decimal": float(gamma1_max_gev.evalf()),
        "ATLAS_fractional_dijet_resolution": str(detector_fractional_resolution),
        "resolution_at_5_TeV_GeV": int(detector_resolution_gev),
        "resolution_to_width_ratio": str(resolution_to_width),
        "resolution_to_width_ratio_decimal": float(resolution_to_width.evalf()),
    },
    "detector_response_rank": "At most one for the proposed mass-plus-width coordinates because all allowed widths map to the zero-width template.",
    "classification": "Conditional current constraint and negative detector-width audit; neither selector nor rigidifier.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "smallest_exact_falsifier": "The allowed intrinsic width reaches 3 percent of the pole mass or the envelope-minimum kaon response is nonpositive.",
    "remaining_gate": "Freeze a flavor-tagged production-rate likelihood or a line-shape instrument capable of resolving the sub-MeV width at multi-TeV mass.",
    "sources": [
        "https://arxiv.org/abs/2009.07276",
        "https://arxiv.org/abs/1910.08447",
    ],
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp461_kaon_conditioned_pole_width_reach.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
