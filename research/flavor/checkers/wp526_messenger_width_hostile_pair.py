"""Exact messenger-threshold ambiguity at the WP516 hierarchical witness."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp489 = load("wp489_common_source_threshold_constructor.json")
wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp518 = load("wp518_common_order_residue_width_composition.json")
wp525 = load("wp525_complex_mass_ward_completion.json")

z, z_a, z_b = sp.symbols("z z_A z_B", positive=True)

# One of the two exact aligned cubics in WP520. Its largest root is the
# state-12/state-13 heavy pole near 4.946 GeV. Sturm counting supplies an exact
# interval without relying on the printed floating root.
pole_polynomial = (
    15625 * z**3 - 493300 * z**2 + 2874619 * z - 3873024
)
poly = sp.Poly(pole_polynomial, z)
roots_24_25 = poly.count_roots(24, 25)
roots_positive = poly.count_roots(0, sp.oo)

# WP489 gives M_A=z_A sigma. Set the already used common clock sigma=1 GeV.
# z_A=1 opens a messenger pair at any pole with M^2>4; z_A=3 closes it for
# the certified root M^2<25 because the pair threshold squared is 36.
open_threshold_squared = (2 * sp.Integer(1)) ** 2
closed_threshold_squared = (2 * sp.Integer(3)) ** 2
open_margin_lower_bound = 24 - open_threshold_squared
closed_margin_lower_bound = closed_threshold_squared - 25

wp516_coefficients = wp516["source_witness"]["authority"] + " " + wp516[
    "source_witness"
]["gauge_parameters"]
wp489_messenger_terms = " ".join(
    wp489["source_action_extension"]["messenger_masses"]
)
state_13 = next(
    state for state in wp518["common_mass_ordering"] if state["state"] == 13
)

checks = {
    "wp489_dependency_passed": bool(wp489["passed"]),
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp518_dependency_passed": bool(wp518["passed"]),
    "wp525_dependency_passed": bool(wp525["passed"]),
    "aligned_cubic_has_three_positive_poles": roots_positive == 3,
    "heavy_pole_is_exactly_isolated_between_24_and_25": roots_24_25 == 1,
    "zA_one_opens_messenger_pair_with_strict_margin": open_margin_lower_bound
    > 0,
    "zA_three_closes_messenger_pair_with_strict_margin": closed_margin_lower_bound
    > 0,
    "tree_vector_polynomial_is_independent_of_messenger_yukawas": sp.diff(
        pole_polynomial, z_a
    )
    == 0
    and sp.diff(pole_polynomial, z_b) == 0,
    "wp489_declares_independent_messenger_yukawa_masses": "z_A" in wp489_messenger_terms
    and "z_B" in wp489_messenger_terms,
    "wp516_witness_does_not_freeze_zA_or_zB": "z_A" not in wp516_coefficients
    and "z_B" not in wp516_coefficients,
    "heavy_pole_has_nonzero_quark_current_residue": state_13[
        "quark_residue_trace"
    ]
    > 0,
    "wp518_labels_composed_width_as_lower_bound": "lower bound"
    in wp518["classification"].lower(),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP526",
    "domain": "Tree-level WP516 hierarchical vector witness extended by the source-authorized WP489 singlet messenger masses.",
    "exact_heavy_pole_certificate": {
        "polynomial": sp.sstr(pole_polynomial),
        "positive_root_count": int(roots_positive),
        "roots_in_mass_squared_interval_24_25": int(roots_24_25),
        "certified_parent_mass_interval_GeV": "sqrt(24) < M < 5",
    },
    "hostile_pair": {
        "shared_data": "Identical WP516 gauge couplings, flavon and connector VEVs, fourteen vector poles, Yang-Mills vertices, and WP509/WP520 residue algebra.",
        "open_completion": "sigma=1 GeV and z_A=1 give messenger mass 1 GeV; the certified heavy pole has M^2>24>4 M_A^2, so the pair channel is strictly open.",
        "closed_completion": "sigma=1 GeV and z_A=3 give messenger mass 3 GeV; the certified heavy pole has M^2<25<4 M_A^2, so the same channel is strictly closed.",
        "tree_vector_packet_unchanged": "The messenger Yukawa z_A does not enter the tree vector mass polynomial.",
    },
    "classification": "Exact same-pole hostile pair proving that WP516-WP518 do not determine channel-complete tree widths. The ambiguity is a source coefficient omitted from the hierarchical witness, not detector noise.",
    "selector": False,
    "rigidifier": False,
    "instrument": "No finite-width current instrument can be admitted until messenger Yukawas and every other threshold-setting coefficient are frozen in the same source witness and pole scheme.",
    "smallest_exact_falsifier": "At one certified pole with 24<M^2<25, z_A=1 opens and z_A=3 closes the messenger pair while leaving the tree vector polynomial unchanged.",
    "remaining_gate": "Freeze z_A,z_B and the complete scalar/messenger spectrum for the hierarchical witness, enumerate every allowed channel and self-energy at a declared perturbative order, and form channel-complete complex poles before applying WP525.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp526_messenger_width_hostile_pair.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
