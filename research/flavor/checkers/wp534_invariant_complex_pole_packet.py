"""Invariant parent widths and signed-current complex-pole packet for WP534."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp517 = load("wp517_unequal_vector_partial_widths.json")
wp518 = load("wp518_common_order_residue_width_composition.json")
wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp525 = load("wp525_complex_mass_ward_completion.json")
wp527 = load("wp527_hierarchical_nonquark_closure.json")
wp532 = load("wp532_quintet_projector_width_sum.json")
wp533 = load("wp533_exact_open_zero_classification.json")

quintet_indices = set(range(7, 12))
vector_channels = wp517["channel_partial_widths"]

# Replace basis-dependent daughter coordinates inside Q by one complete
# parent-level sum. All other daughters are nondegenerate at this witness.
invariant_vector_groups = []
for parent in sorted({channel["parent"] for channel in vector_channels}):
    parent_channels = [
        channel for channel in vector_channels if channel["parent"] == parent
    ]
    quintet_pair = [
        channel
        for channel in parent_channels
        if channel["daughter_1"] in quintet_indices
        and channel["daughter_2"] in quintet_indices
    ]
    nonquintet = [
        channel for channel in parent_channels if channel not in quintet_pair
    ]
    for channel in nonquintet:
        invariant_vector_groups.append(
            {
                "parent": parent,
                "kind": "simple_daughter_pair",
                "daughter_states": [
                    channel["daughter_1"],
                    channel["daughter_2"],
                ],
                "coordinate_multiplicity": 1,
                "partial_width_GeV": channel["partial_width_GeV"],
            }
        )
    if quintet_pair:
        invariant_vector_groups.append(
            {
                "parent": parent,
                "kind": "complete_quintet_pair",
                "daughter_subspace": "Q wedge Q",
                "coordinate_multiplicity": len(quintet_pair),
                "summed_squared_coupling": sum(
                    channel["cubic_coupling"] ** 2 for channel in quintet_pair
                ),
                "partial_width_GeV": sum(
                    channel["partial_width_GeV"] for channel in quintet_pair
                ),
            }
        )

invariant_parent_vector_sums = {}
for group in invariant_vector_groups:
    key = str(group["parent"])
    invariant_parent_vector_sums[key] = (
        invariant_parent_vector_sums.get(key, 0.0)
        + group["partial_width_GeV"]
    )

# WP527 closes every declared nonquark two-body pair, while WP533 proves that
# WP517 contains every threshold-open vector channel. Thus the WP518
# quark-plus-vector lower bounds become channel-complete declared tree widths.
state_packets = []
for packet in wp518["common_mass_ordering"]:
    state = packet["state"]
    vector_width = invariant_parent_vector_sums.get(str(state), 0.0)
    total_tree_width = packet["quark_partial_width_GeV"] + vector_width
    state_packets.append(
        {
            "state": state,
            "pole_kind": packet["pole_kind"],
            "sector": packet.get("sector"),
            "mass_squared_GeV_squared": packet[
                "mass_squared_GeV_squared"
            ],
            "mass_GeV": packet["mass_GeV"],
            "flavor_current_trace_residue": packet[
                "quark_residue_trace"
            ],
            "quark_partial_width_GeV": packet[
                "quark_partial_width_GeV"
            ],
            "invariant_vector_partial_width_GeV": vector_width,
            "channel_complete_declared_tree_width_GeV": total_tree_width,
            "fractional_tree_width": total_tree_width / packet["mass_GeV"],
            "complex_mass_squared_GeV_squared": {
                "real": packet["mass_squared_GeV_squared"],
                "imaginary": -packet["mass_GeV"] * total_tree_width,
                "convention": "mu_squared=M_squared-i M Gamma_tree",
            },
        }
    )

# Collapse the five degenerate coordinates into one projector-valued pole.
quintet_packets = [
    packet for packet in state_packets if packet["pole_kind"] == "quintet"
]
quintet_pole = {
    "pole_kind": "rank_five_quintet_projector",
    "coordinate_states": [packet["state"] for packet in quintet_packets],
    "multiplicity": len(quintet_packets),
    "mass_squared_GeV_squared": 6.0,
    "mass_GeV": float(sp.sqrt(6)),
    "current_residue_operator": "2 P_Q",
    "per_coordinate_trace_residue": 2.0,
    "per_coordinate_tree_width_GeV": sum(
        packet["channel_complete_declared_tree_width_GeV"]
        for packet in quintet_packets
    )
    / len(quintet_packets),
}
quintet_pole["complex_mass_squared_GeV_squared"] = {
    "real": 6.0,
    "imaginary": -quintet_pole["mass_GeV"]
    * quintet_pole["per_coordinate_tree_width_GeV"],
    "convention": "mu_Q_squared=(M_Q_squared-i M_Q Gamma_Q) P_Q",
}
simple_poles = [
    packet for packet in state_packets if packet["pole_kind"] == "cubic"
]

# Extract the signed aligned b-s residues from WP520's exact scalar kernel.
# These, rather than positive trace residues, are the numerator data needed by
# the finite-propagator and Ward-completed bilocal experiment.
z = sp.symbols("z")
kernel = sp.sympify(
    wp520["aligned_bs_kernel"]["exact_witness_rational_function"],
    locals={"z": z},
)
numerator, denominator = sp.fraction(kernel)
root_values = sorted(
    [sp.re(value) for value in sp.nroots(denominator, n=100, maxsteps=500)],
    key=lambda value: float(value),
)
bs_states = [
    packet
    for packet in simple_poles
    if packet["sector"] in (0, 1)
]
unused_states = {packet["state"] for packet in bs_states}
signed_bs_residues = []
residue_terms = []
for root_value in root_values:
    root_value_float = float(root_value)
    state = min(
        unused_states,
        key=lambda candidate: abs(
            next(
                packet["mass_squared_GeV_squared"]
                for packet in bs_states
                if packet["state"] == candidate
            )
            - root_value_float
        ),
    )
    packet = next(
        item for item in bs_states if item["state"] == state
    )
    unused_states.remove(state)
    pole_root = sp.N(root_value, 100)
    residue = sp.N(
        numerator / sp.diff(denominator, z).subs(z, pole_root),
        90,
    )
    residue_terms.append((residue, pole_root))
    signed_bs_residues.append(
        {
            "state": state,
            "mass_squared_GeV_squared": packet[
                "mass_squared_GeV_squared"
            ],
            "root_match_error_GeV_squared": abs(
                packet["mass_squared_GeV_squared"] - root_value_float
            ),
            "signed_bs_residue": str(residue),
            "complex_mass_squared_GeV_squared": packet[
                "complex_mass_squared_GeV_squared"
            ],
        }
    )
signed_bs_residues.sort(key=lambda item: item["state"])

kernel_at_zero_from_residues = sp.N(
    sum(residue / (-pole_root) for residue, pole_root in residue_terms),
    70,
)
kernel_at_zero_exact = sp.N(kernel.subs(z, 0), 70)
kernel_at_zero_error = sp.Abs(
    kernel_at_zero_from_residues - kernel_at_zero_exact
)

# Recheck the universal complex-mass Ward identity. The same mu^2 packet must
# be inserted in transverse, longitudinal, unphysical and Goldstone terms.
t, xi, mu2, current_norm, divergence_norm = sp.symbols(
    "t xi mu2 current_norm divergence_norm"
)
vector_rxi = (
    current_norm / (t - mu2)
    - divergence_norm
    * (1 - xi)
    / ((t - mu2) * (t - xi * mu2))
)
goldstone_rxi = -divergence_norm / (
    mu2 * (t - xi * mu2)
)
ward_sum = sp.simplify(vector_rxi + goldstone_rxi)
expected_ward_sum = (
    current_norm - divergence_norm / mu2
) / (t - mu2)

wp517_parent_sums = {
    key: value["summed_vector_partial_width_GeV"]
    for key, value in wp517["parent_vector_width_sums"].items()
}
checks = {
    "wp517_dependency_passed": bool(wp517["passed"]),
    "wp518_dependency_passed": bool(wp518["passed"]),
    "wp520_dependency_passed": bool(wp520["passed"]),
    "wp525_dependency_passed": bool(wp525["passed"]),
    "wp527_dependency_passed": bool(wp527["passed"]),
    "wp532_dependency_passed": bool(wp532["passed"]),
    "wp533_dependency_passed": bool(wp533["passed"]),
    "thirty_four_rows_reduce_to_sixteen_invariant_groups": (
        len(vector_channels) == 34
        and len(invariant_vector_groups) == 16
    ),
    "two_complete_quintet_pair_groups_replace_twenty_rows": (
        sum(
            group["kind"] == "complete_quintet_pair"
            for group in invariant_vector_groups
        )
        == 2
        and sum(
            group["coordinate_multiplicity"]
            for group in invariant_vector_groups
            if group["kind"] == "complete_quintet_pair"
        )
        == 20
    ),
    "invariant_parent_sums_reproduce_wp517": all(
        abs(invariant_parent_vector_sums[key] - value) < 1e-18
        for key, value in wp517_parent_sums.items()
    ),
    "fourteen_state_width_packets_are_present": len(state_packets) == 14,
    "five_quintet_coordinates_collapse_to_one_projector_pole": (
        quintet_pole["multiplicity"] == 5
        and len(simple_poles) == 9
    ),
    "all_declared_tree_widths_are_positive": all(
        packet["channel_complete_declared_tree_width_GeV"] > 0
        for packet in state_packets
    ),
    "six_signed_bs_residues_are_matched_once": (
        len(signed_bs_residues) == 6 and len(unused_states) == 0
    ),
    "signed_bs_root_matching_is_below_tolerance": max(
        item["root_match_error_GeV_squared"]
        for item in signed_bs_residues
    )
    < 1e-10,
    "signed_residues_reconstruct_zero_momentum_kernel": (
        kernel_at_zero_error < sp.Float("1e-60")
    ),
    "complex_mass_ward_sum_is_exactly_xi_independent": (
        sp.simplify(ward_sum - expected_ward_sum) == 0
        and sp.diff(ward_sum, xi) == 0
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP534",
    "domain": "The frozen WP516 vector witness embedded in the WP527 common-source nonquark-closed domain, at declared tree level.",
    "invariant_vector_width_groups": invariant_vector_groups,
    "invariant_parent_vector_sums_GeV": invariant_parent_vector_sums,
    "state_complex_poles": state_packets,
    "projector_complex_pole": quintet_pole,
    "simple_complex_poles": simple_poles,
    "signed_bs_pole_residues": signed_bs_residues,
    "signed_bs_zero_momentum_reconstruction": {
        "from_residues": str(kernel_at_zero_from_residues),
        "exact_wp520": str(kernel_at_zero_exact),
        "absolute_error": str(kernel_at_zero_error),
    },
    "ward_rule": "For each signed b-s pole, insert the identical complex mu^2 in the transverse denominator, longitudinal normalization, unphysical R_xi denominator and Goldstone term. The exact sum is xi independent.",
    "classification": "Channel-complete declared tree-width and signed-residue complex-pole packet on the WP527 existence witness. It upgrades WP518's lower bounds only within this frozen source domain and perturbative order.",
    "selector": False,
    "rigidifier": bool(
        len(invariant_vector_groups) == 16
        and len(signed_bs_residues) == 6
        and kernel_at_zero_error == 0
    ),
    "instrument": "The source-side complex pole packet is now typed. Physical extraction still requires the WP525 vector-plus-scalar bilocal matrix elements, production and lineshape response, detector calibration and covariance.",
    "smallest_exact_falsifier": "One omitted declared tree-level two-body channel is open, one invariant group fails to reproduce the WP517 parent sum, the signed residues fail to reconstruct WP520 at zero momentum, or vector-only complexification leaves xi dependence.",
    "remaining_gate": "Evaluate the six-pole Ward-complete vector-plus-scalar B_s bilocal kernel with renormalized hadronic matrix elements and covariance, then attach a pole-production and detector-response likelihood. Higher-order and radiative widths remain a separately declared completion.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp534_invariant_complex_pole_packet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
