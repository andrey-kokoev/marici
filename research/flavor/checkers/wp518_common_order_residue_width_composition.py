"""Common-order quark residues plus resolved vector-width lower bounds."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp509 = load("wp509_spectral_residue_width_sum_rules.json")
wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp517 = load("wp517_unequal_vector_partial_widths.json")

z = sp.symbols("z")
g_f, g_p, g_e, mu, s, a, b = sp.symbols(
    "g_F g_P g_E mu s a b", positive=True
)
symbols = {
    "z": z,
    "g_F": g_f,
    "g_P": g_p,
    "g_E": g_e,
    "mu": mu,
    "s": s,
    "a": a,
    "b": b,
}

v_squared = sp.Integer(246) ** 2
ratio = sp.Integer(400)
b_squared = sp.factor(v_squared / (2 * (ratio**2 + 1)))
a_squared = sp.factor(ratio**2 * b_squared)
substitution = {
    g_f: sp.sqrt(2),
    g_p: sp.Rational(1, 10),
    g_e: sp.Rational(1, 50),
    mu: 1,
    s: 16,
    a: sp.sqrt(a_squared),
    b: sp.sqrt(b_squared),
}
quintet_mass_squared = sp.factor((3 * g_f**2 * mu**2).subs(substitution))
ordered_mass_squared = wp516["mass_basis"]["ordered_mass_squared_GeV_squared"]
ordered_masses = wp516["mass_basis"]["ordered_masses_GeV"]


def nearest_unused_index(value, unused):
    return min(unused, key=lambda index: abs(ordered_mass_squared[index] - value))


# First reserve the exactly fivefold quintet pole.  Cubic roots are separated
# from Q at this witness, so the matching is unambiguous despite the arbitrary
# basis inside the degenerate quintet subspace.
quintet_indices = [
    index
    for index, value in enumerate(ordered_mass_squared)
    if abs(value - float(quintet_mass_squared)) < 1e-10
]
unused_indices = set(range(14)) - set(quintet_indices)
state_packets = {}
sector_packets = []
root_match_errors = []
sector_completeness_errors = []

for sector_index, component in enumerate(
    item for item in wp508["heavy_gauge_poles"]["components"] if item["size"] == 4
):
    cubic = sp.Poly(
        sp.sympify(component["cubic_characteristic_polynomial"], locals=symbols).subs(substitution),
        z,
    )
    numerator = sp.Matrix(
        [
            [sp.sympify(value, locals=symbols).subs(substitution) for value in row]
            for row in component["flavor_current_resolvent"]["numerator_matrix"]
        ]
    )
    roots = sorted(
        [float(sp.re(root_value)) for root_value in sp.nroots(cubic.as_expr(), n=50, maxsteps=200)]
    )
    sector_residue_sum = 0.0
    matched_states = []
    for root_value in roots:
        index = nearest_unused_index(root_value, unused_indices)
        error = abs(ordered_mass_squared[index] - root_value)
        unused_indices.remove(index)
        derivative = sp.diff(cubic.as_expr(), z).subs(z, sp.Float(root_value, 50))
        trace_residue = sp.N(
            sp.trace(numerator.subs(z, sp.Float(root_value, 50)))
            / ((sp.Float(root_value, 50) - quintet_mass_squared) * derivative),
            40,
        )
        trace_residue_float = float(trace_residue)
        quark_fraction = trace_residue_float / (4 * sp.pi.evalf(40))
        quark_fraction_float = float(quark_fraction)
        quark_width = ordered_masses[index] * quark_fraction_float
        state_packets[index] = {
            "state": index,
            "pole_kind": "cubic",
            "sector": sector_index,
            "mass_squared_GeV_squared": ordered_mass_squared[index],
            "mass_GeV": ordered_masses[index],
            "root_match_error_GeV_squared": error,
            "quark_residue_trace": trace_residue_float,
            "quark_fractional_width": quark_fraction_float,
            "quark_partial_width_GeV": quark_width,
        }
        sector_residue_sum += trace_residue_float
        matched_states.append(index)
        root_match_errors.append(error)
    sector_completeness_error = abs(sector_residue_sum - float(substitution[g_f] ** 2))
    sector_completeness_errors.append(sector_completeness_error)
    sector_packets.append(
        {
            "sector": sector_index,
            "generators": component["generators"],
            "matched_cubic_states": matched_states,
            "cubic_residue_trace_sum": sector_residue_sum,
            "expected_cubic_residue_trace_sum": float(substitution[g_f] ** 2),
            "completeness_error": sector_completeness_error,
        }
    )

# Each of the five principal-SU(2) quintet coordinates has scalar current
# residue g_F^2.  Degenerate rotations alter labels but not this identity.
quintet_residue_trace = float(substitution[g_f] ** 2)
for index in quintet_indices:
    quark_fraction = quintet_residue_trace / float(4 * sp.pi.evalf(40))
    state_packets[index] = {
        "state": index,
        "pole_kind": "quintet",
        "mass_squared_GeV_squared": ordered_mass_squared[index],
        "mass_GeV": ordered_masses[index],
        "root_match_error_GeV_squared": abs(
            ordered_mass_squared[index] - float(quintet_mass_squared)
        ),
        "quark_residue_trace": quintet_residue_trace,
        "quark_fractional_width": quark_fraction,
        "quark_partial_width_GeV": ordered_masses[index] * quark_fraction,
    }

resolved_vector_sums = {
    int(index): packet
    for index, packet in wp517["parent_vector_width_sums"].items()
}
ordered_packets = []
for index in range(14):
    packet = state_packets[index]
    vector_width = resolved_vector_sums.get(index, {}).get(
        "summed_vector_partial_width_GeV", 0.0
    )
    lower_bound = packet["quark_partial_width_GeV"] + vector_width
    ordered_packets.append(
        {
            **packet,
            "resolved_vector_partial_width_sum_GeV": vector_width,
            "quark_plus_resolved_vector_width_lower_bound_GeV": lower_bound,
            "lower_bound_fractional_width": lower_bound / packet["mass_GeV"],
        }
    )

global_residue_trace = sum(packet["quark_residue_trace"] for packet in ordered_packets)
expected_global_residue_trace = float(8 * substitution[g_f] ** 2)
states_with_vector_addition = [
    packet["state"]
    for packet in ordered_packets
    if packet["resolved_vector_partial_width_sum_GeV"] > 0
]

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp509_dependency_passed": bool(wp509["passed"]),
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp517_dependency_passed": bool(wp517["passed"]),
    "five_quintet_states_are_matched": len(quintet_indices) == 5,
    "all_nine_cubic_roots_are_matched_once": bool(len(unused_indices) == 0),
    "root_matching_is_below_tolerance": bool(max(root_match_errors) < 1e-10),
    "every_cubic_residue_trace_is_positive": bool(
        all(packet["quark_residue_trace"] > 0 for packet in ordered_packets if packet["pole_kind"] == "cubic")
    ),
    "each_cubic_sector_saturates_its_wp509_trace_sum": bool(
        max(sector_completeness_errors) < 1e-10
    ),
    "global_eight_current_residue_sum_is_saturated": bool(
        abs(global_residue_trace - expected_global_residue_trace) < 1e-10
    ),
    "vector_additions_match_wp517_parent_set": bool(
        states_with_vector_addition == sorted(resolved_vector_sums)
    ),
    "all_composed_lower_bounds_exceed_or_equal_quark_widths": bool(
        all(
            packet["quark_plus_resolved_vector_width_lower_bound_GeV"]
            >= packet["quark_partial_width_GeV"]
            for packet in ordered_packets
        )
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP518",
    "admitted_state_domain": wp516["admitted_state_domain"],
    "common_mass_ordering": ordered_packets,
    "sector_residue_completeness": sector_packets,
    "global_residue_trace_sum": global_residue_trace,
    "expected_global_residue_trace_sum": expected_global_residue_trace,
    "states_with_resolved_vector_width_addition": states_with_vector_addition,
    "classification": "Common-order composition of independently frozen quark residues and resolved vector partial widths. Each sum is a rigorous channel-explicit lower bound, not a total width.",
    "selector": False,
    "rigidifier": bool(len(ordered_packets) == 14 and len(states_with_vector_addition) == 4),
    "instrument": "WP511 constrains the entrance ratio. Quark and vector partial widths are source-normalized, but no pole-resolved production, lineshape, or detector likelihood is attached.",
    "smallest_exact_falsifier": "A cubic root cannot be matched uniquely to the WP516 ordering, a residue trace is nonpositive, or a sector fails the exact WP509 completeness sum.",
    "remaining_gate": "Add scalar and sub-resolution channels and attach a pole-resolved production plus detector-response likelihood. Only the resulting channel-complete sums may be called total widths or experimentally identified residues.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp518_common_order_residue_width_composition.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
