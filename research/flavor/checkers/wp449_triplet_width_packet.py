"""Exact WP449 leading-width packet in the frozen quark-only decay domain."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp448 = json.loads((root / "results" / "wp448_triplet_pole_residue_packet.json").read_text(encoding="utf-8"))
g_f, mu = sp.symbols("g_F mu", positive=True, real=True)
pi = sp.pi
N_c = sp.Integer(3)
quark_types = sp.Integer(2)
generator_trace = sp.Rational(1, 2)

m_triplet = g_f*mu
m_quintet = sp.sqrt(3)*g_f*mu

# For one Dirac quark type with vectorlike coupling, summed over its three
# generations: Gamma=N_c g^2 M Tr(T^2)/(12 pi).
width_coefficient = sp.simplify(N_c*quark_types*generator_trace/(12*pi))
gamma_triplet = sp.simplify(width_coefficient*g_f**2*m_triplet)
gamma_quintet = sp.simplify(width_coefficient*g_f**2*m_quintet)

checks = {
    "wp448_dependency_passed": wp448["passed"],
    "inclusive_quark_width_coefficient": width_coefficient == 1/(4*pi),
    "triplet_width_is_exact_in_declared_approximation": gamma_triplet == g_f**3*mu/(4*pi),
    "quintet_width_is_exact_in_declared_approximation": gamma_quintet == sp.sqrt(3)*g_f**3*mu/(4*pi),
    "common_width_to_mass_ratio": sp.simplify(gamma_triplet/m_triplet-gamma_quintet/m_quintet) == 0,
    "width_ratio_tracks_mass_ratio": sp.simplify(gamma_quintet/gamma_triplet-sp.sqrt(3)) == 0,
    "gauge_cascade_is_kinematically_closed": sp.sqrt(3) < 2,
    "hostile_zero_coupling_limit_closes_widths": sp.limit(gamma_triplet, g_f, 0) == 0 and sp.limit(gamma_quintet, g_f, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP449",
    "approximation": "Leading order, massless six-quark limit, fixed-width pole model.",
    "frozen_support_assumptions": [
        "m_triplet>2 m_top",
        "all vectorlike messenger pair thresholds lie above m_quintet",
        "all physical flavon-containing decay thresholds lie above m_quintet",
        "no additional light SU(3)_F-charged states",
        "g_F^2/(4 pi) is perturbative",
    ],
    "partial_trace_rule": "For each of up-type and down-type Dirac quarks, sum over generations gives Tr(T^2)=1/2 and over color gives N_c=3.",
    "total_widths": {"triplet": "g_F^3 mu/(4 pi)", "quintet": "sqrt(3) g_F^3 mu/(4 pi)"},
    "common_width_to_mass_ratio": "g_F^2/(4 pi)",
    "pole_residues": wp448["residue_operators"],
    "instrument": None,
    "classification": "Independently frozen conditional leading widths and residues; not detector-calibrated and not valid when a declared threshold opens.",
    "smallest_exact_falsifier": "One open messenger/flavon channel in the declared mass range, m_triplet below 2m_top, or a nonperturbative width ratio.",
    "remaining_gate": "Freeze a viable messenger-to-physical16 map and detector resolution, then replace the massless inclusive width by threshold-resolved partial widths with uncertainties.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp449_triplet_width_packet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
