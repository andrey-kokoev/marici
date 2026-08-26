"""Exact Ward completion and width-authority gate for one flavor-vector pole."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp509 = load("wp509_spectral_residue_width_sum_rules.json")
wp518 = load("wp518_common_order_residue_width_composition.json")
wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp524 = load("wp524_euclidean_h0_estimator.json")

t, mu2, m2, xi, j2, d2 = sp.symbols("t mu2 m2 xi J2 d2", nonzero=True)

# R_xi vector exchange and the Ward-fixed Goldstone exchange. The pole mass
# may be real or complex; gauge cancellation requires the same mu2 everywhere.
vector_consistent = j2 / (t - mu2) - (1 - xi) * d2 / (
    (t - mu2) * (t - xi * mu2)
)
goldstone_consistent = -d2 / (mu2 * (t - xi * mu2))
unitary_consistent = (j2 - d2 / mu2) / (t - mu2)
ward_residual = sp.factor(
    vector_consistent + goldstone_consistent - unitary_consistent
)

# Hostile partial resummation: put a shifted pole only in the transverse
# denominator while retaining the real mass in longitudinal and Goldstone
# factors. Its xi derivative is the exact gauge-dependence obstruction.
vector_naive = j2 / (t - mu2) - (1 - xi) * d2 / (
    (t - mu2) * (t - xi * m2)
)
goldstone_naive = -d2 / (m2 * (t - xi * m2))
naive_total = sp.factor(vector_naive + goldstone_naive)
naive_xi_derivative = sp.factor(sp.diff(naive_total, xi))
hostile_naive_residual = sp.factor(
    naive_xi_derivative.subs({t: 7, mu2: 3, m2: 4, xi: 2, d2: 5, j2: 11})
)

states = wp518["common_mass_ordering"]
lower_bound_only = all(
    "quark_plus_resolved_vector_width_lower_bound_GeV" in state
    for state in states
)
has_total_width = all("total_width_GeV" in state for state in states)

checks = {
    "wp518_dependency_passed": bool(wp518["passed"]),
    "wp509_dependency_passed": bool(wp509["passed"]),
    "wp520_dependency_passed": bool(wp520["passed"]),
    "wp524_dependency_passed": bool(wp524["passed"]),
    "consistent_complex_mass_ward_sum_is_xi_independent": ward_residual == 0,
    "naive_partial_width_insertion_is_gauge_dependent": naive_xi_derivative != 0,
    "hostile_naive_width_witness_is_nonzero": hostile_naive_residual != 0,
    "wp518_widths_are_explicit_lower_bounds": lower_bound_only,
    "wp518_does_not_supply_channel_complete_total_widths": not has_total_width,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP525",
    "domain": "One pole of the WP520 flavor-current resolvent, with the WP524 nonconserved b-to-s current and a possibly complex pole mass.",
    "ward_completion": {
        "vector_Rxi": sp.sstr(vector_consistent),
        "goldstone_Rxi": sp.sstr(goldstone_consistent),
        "gauge_independent_sum": sp.sstr(unitary_consistent),
        "exact_residual": sp.sstr(ward_residual),
        "rule": "The identical pole parameter mu^2 must occur in the transverse denominator, longitudinal numerator normalization, unphysical R_xi pole, and Goldstone coupling.",
    },
    "finite_width_attack": {
        "naive_xi_derivative": sp.sstr(naive_xi_derivative),
        "hostile_exact_value": sp.sstr(hostile_naive_residual),
        "consequence": "Inserting a width only into the visible vector denominator violates the Ward cancellation. A complex-mass or pole scheme derived consistently across vector and Goldstone sectors is required.",
    },
    "residue_width_authority": {
        "residue_rule": "Each pole's longitudinal and Goldstone term inherits the same signed b-s current residue as its transverse term, divided by the same pole mass squared where required by the Ward identity.",
        "current_status": "WP509 freezes exact matrix-residue functionals and WP520 fixes their aligned scalar b-s combination. WP518 joins trace residues to resolved widths in one ordering, but its widths are explicit lower bounds rather than channel-complete totals.",
        "physical_consequence": "The signed b-s residue algebra exists, but it has not been joined pole by pole to channel-complete complex masses in one gauge-consistent scheme.",
    },
    "induced_operator_family": [
        "left-left vector bilocal from J_mu J^mu",
        "right-right scalar bilocal proportional to m_b^2 S_R S_R",
        "left-left scalar bilocal proportional to m_s^2 S_L S_L",
        "mixed scalar bilocal proportional to m_b m_s S_R S_L",
    ],
    "classification": "A universal gauge-independent pole completion is fixed conditionally by the Ward identity. The current source packet cannot instantiate its finite-width version because channel-complete pole widths and the existing signed b-s residue algebra are not joined in one complex-pole scheme.",
    "selector": False,
    "rigidifier": bool(ward_residual == 0),
    "instrument": "The operator family is now source-typed, but the lattice instrument awaits the complete complex pole packet and renormalized vector-plus-scalar bilocal matrix elements.",
    "smallest_exact_falsifier": "A partial width insertion mu^2!=m^2 produces a nonzero derivative with respect to xi; the frozen hostile witness evaluates that derivative away from every pole.",
    "remaining_gate": "Complete every pole width in a gauge-consistent pole scheme, transport the WP509/WP520 signed b-s residues into that same pole ordering, and evaluate the enlarged vector-plus-scalar B_s bilocal basis with covariance.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp525_complex_mass_ward_completion.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
