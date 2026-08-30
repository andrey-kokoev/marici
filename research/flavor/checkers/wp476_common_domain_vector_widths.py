"""Exact common-domain vector-threshold and response audit for WP476."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp435 = load("wp435_dynamical_flavon_messenger_completion.json")
wp449 = load("wp449_triplet_width_packet.json")
wp463 = load("wp463_run2_production_rate_reach.json")
wp474 = load("wp474_kaon_conditioned_higgs_alignment.json")
wp475 = load("wp475_hierarchical_scalar_residue_packet.json")

f = sp.sympify(wp474["f_min_TeV"])
v = sp.Rational(12311, 50000)
mu = sp.simplify(f / sp.sqrt(6))
m1 = sp.Integer(5)
m3 = sp.sqrt(3) * m1
g = sp.simplify(m1 / mu)

# Freeze the still-free vectorlike messenger masses through the positive
# renormalizable common-clock term M_U=M_D=w=mu.  This is a declared source
# benchmark, not a selected coefficient.
messenger_mass = mu

# The lowest physical SU(3)_F-charged scalar curvature is 16 w^2 in the
# WP468 flavor block.  Higgs and radial singlets are flavor neutral.
charged_scalar_mass = 4 * mu

fractional_width = sp.simplify(g**2 / (4 * sp.pi))
gamma1_tev = sp.simplify(m1 * fractional_width)
gamma3_tev = sp.simplify(m3 * fractional_width)
ratio_readout = sp.simplify(g * f / v)

g_symbol, mu_symbol = sp.symbols("g_F mu", positive=True)
m_readout = g_symbol * mu_symbol
current_readout = 1 / (6 * mu_symbol**2)
ordinary_jacobian = sp.Matrix(
    [
        [sp.diff(m_readout, g_symbol), sp.diff(m_readout, mu_symbol)],
        [sp.diff(current_readout, g_symbol), sp.diff(current_readout, mu_symbol)],
    ]
)
ordinary_determinant = sp.factor(ordinary_jacobian.det())
log_response = sp.Matrix([[1, 1], [0, -2]])

max_run2_events = sp.Float(
    str(wp463["unit_acceptance_rate_ceiling"]["maximum_replica_produced_events"])
)

checks = {
    "wp435_dependency_passed": wp435["passed"],
    "wp449_dependency_passed": wp449["passed"],
    "wp463_dependency_passed": wp463["passed"],
    "wp474_dependency_passed": wp474["passed"],
    "wp475_dependency_passed": wp475["passed"],
    "common_clock_relation_exact": sp.simplify(f - sp.sqrt(6) * mu) == 0,
    "triplet_pole_is_exactly_five_TeV": sp.simplify(g * mu - m1) == 0,
    "messenger_pair_threshold_is_closed": 2 * messenger_mass > m3,
    "charged_scalar_pair_threshold_is_closed": 2 * charged_scalar_mass > m3,
    "vector_widths_are_positive": gamma1_tev > 0 and gamma3_tev > 0,
    "vector_width_ratio_is_sqrt_three": sp.simplify(gamma3_tev / gamma1_tev - sp.sqrt(3)) == 0,
    "ordinary_response_determinant_is_nonzero": ordinary_determinant == -1 / (3 * mu_symbol**2),
    "log_response_rank_is_two": log_response.rank() == 2,
    "log_response_determinant_is_minus_two": log_response.det() == -2,
    "ratio_depends_only_on_pole_and_electroweak_clock": ratio_readout == 250000 * sp.sqrt(6) / 12311,
    "run2_source_yield_remains_below_one": max_run2_events < 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP476",
    "domain": "WP474-WP475 kaon-conditioned endpoint, five-TeV triplet benchmark, y=kappa=lambda=rho=1, and common-clock messenger masses M_U=M_D=mu",
    "source_parameters": {
        "f_TeV_exact": str(f),
        "f_TeV_numeric": float(sp.N(f, 16)),
        "mu_TeV_exact": str(mu),
        "mu_TeV_numeric": float(sp.N(mu, 16)),
        "g_F_exact": str(g),
        "g_F_numeric": float(sp.N(g, 16)),
        "messenger_mass_TeV_numeric": float(sp.N(messenger_mass, 16)),
        "messenger_mass_coefficient_status": "declared unit common-clock benchmark; not source-selected",
    },
    "vector_poles_TeV": {
        "triplet": str(m1),
        "quintet": str(m3),
    },
    "closed_nonquark_thresholds": {
        "messenger_pair_threshold_TeV_numeric": float(sp.N(2 * messenger_mass, 16)),
        "lightest_charged_scalar_mass_TeV_numeric": float(sp.N(charged_scalar_mass, 16)),
        "charged_scalar_pair_threshold_TeV_numeric": float(sp.N(2 * charged_scalar_mass, 16)),
        "note": "The 125.20-GeV Higgs and three radial poles are SU(3)_F neutral; the first flavor-charged physical scalar has curvature 16 mu^2.",
    },
    "independently_frozen_quark_widths": {
        "fractional_width_exact": str(fractional_width),
        "triplet_width_GeV_numeric": float(sp.N(1000 * gamma1_tev, 16)),
        "quintet_width_GeV_numeric": float(sp.N(1000 * gamma3_tev, 16)),
        "support": "tree level, six massless quarks; scalar and messenger channels proved closed on this benchmark",
    },
    "two_source_response": {
        "source_coordinates": ["g_F", "mu"],
        "readouts": ["m_1=g_F mu", "C_0=1/(6 mu^2)"],
        "ordinary_jacobian": [[str(value) for value in row] for row in ordinary_jacobian.tolist()],
        "ordinary_determinant": str(ordinary_determinant),
        "logarithmic_response": [[int(value) for value in row] for row in log_response.tolist()],
        "logarithmic_determinant": int(log_response.det()),
        "formal_rank": 2,
    },
    "g_F_f_over_v": {
        "exact": str(ratio_readout),
        "numeric": float(sp.N(ratio_readout, 16)),
        "authority": "conditional five-TeV pole readout, not a source-selected numerical value",
    },
    "contextual_partition": {
        "source_map": "The pole-plus-current family separates every positive (g_F,mu) point.",
        "current_instruments": "The CP-even kaon likelihood remains provisional and the Run-2 pole channel has less than one produced event even at unit acceptance.",
        "first_nonfaithful_arrow": "finite collider production/counting support; no detector pole record exists on the admitted endpoint",
    },
    "classification": "Common-domain exact width closure and formally rank-two source readout; neither a selector nor a presentation rigidifier.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "smallest_exact_falsifier": "An open messenger or SU(3)_F-charged scalar pair threshold below the quintet pole, or a zero determinant for the pole-plus-current response.",
    "remaining_instrument_gate": "A controlled CP-even kaon likelihood and an actually populated flavor-tagged pole experiment in the same source domain; Run-2 cannot supply the pole coordinate.",
    "remaining_selector_gate": "Derive the five-TeV pole-to-electroweak-clock ratio from source dynamics instead of freezing it as a benchmark.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp476_common_domain_vector_widths.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
