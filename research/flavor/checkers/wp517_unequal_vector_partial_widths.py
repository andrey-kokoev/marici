"""Unequal-mass Yang--Mills partial widths for the WP516 open channels."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp509 = load("wp509_spectral_residue_width_sum_rules.json")
wp511 = load("wp511_neutral_b_current_instrument.json")
wp516 = load("wp516_hierarchical_mass_basis_vertices.json")

# Derive the polarization-summed kinematic functional rather than importing a
# fitted width formula.  Metric convention is (+,-,-,-), all vertex momenta
# are outgoing, and the parent is at rest.  Daughter labels are distinct, as
# required by the antisymmetric gauge tensor, so there is no symmetry factor.
M, m_1, m_2, p = sp.symbols("M m_1 m_2 p", positive=True)
E_1 = (M**2 + m_1**2 - m_2**2) / (2 * M)
E_2 = (M**2 - m_1**2 + m_2**2) / (2 * M)
metric = sp.diag(1, -1, -1, -1)
k_0 = sp.Matrix([-M, 0, 0, 0])
k_1 = sp.Matrix([E_1, 0, 0, p])
k_2 = sp.Matrix([E_2, 0, 0, -p])


def dot(left, right):
    return (left.T * metric * right)[0]


parent_polarizations = [
    sp.Matrix([0, 1, 0, 0]),
    sp.Matrix([0, 0, 1, 0]),
    sp.Matrix([0, 0, 0, 1]),
]
daughter_1_polarizations = [
    sp.Matrix([0, 1, 0, 0]),
    sp.Matrix([0, 0, 1, 0]),
    sp.Matrix([p / m_1, 0, 0, E_1 / m_1]),
]
daughter_2_polarizations = [
    sp.Matrix([0, 1, 0, 0]),
    sp.Matrix([0, 0, 1, 0]),
    sp.Matrix([p / m_2, 0, 0, -E_2 / m_2]),
]


def unit_vertex_amplitude(e_0, e_1, e_2):
    # Contract the standard three-gauge-boson vertex with physical
    # polarizations.  This dot-product form is algebraically equivalent to the
    # indexed Lorentz tensor and avoids any hidden polarization convention.
    return sp.expand(
        dot(e_0, e_1) * dot(k_0 - k_1, e_2)
        + dot(e_1, e_2) * dot(k_1 - k_2, e_0)
        + dot(e_2, e_0) * dot(k_2 - k_0, e_1)
    )


polarization_sum = sp.expand(
    sum(
        unit_vertex_amplitude(e_0, e_1, e_2) ** 2
        for e_0 in parent_polarizations
        for e_1 in daughter_1_polarizations
        for e_2 in daughter_2_polarizations
    )
    / 3
)
lambda_polynomial = sp.expand(
    M**4 + m_1**4 + m_2**4
    - 2 * M**2 * m_1**2
    - 2 * M**2 * m_2**2
    - 2 * m_1**2 * m_2**2
)
p_squared = lambda_polynomial / (4 * M**2)
polarization_sum_on_shell = sp.factor(polarization_sum.subs(p**2, p_squared))
expected_polarization_sum = sp.factor(
    lambda_polynomial
    * (
        M**4 + m_1**4 + m_2**4
        + 10 * M**2 * m_1**2
        + 10 * M**2 * m_2**2
        + 10 * m_1**2 * m_2**2
    )
    / (12 * M**2 * m_1**2 * m_2**2)
)


def partial_width(parent_mass, daughter_1_mass, daughter_2_mass, coupling):
    substitutions = {
        M: sp.Float(parent_mass, 40),
        m_1: sp.Float(daughter_1_mass, 40),
        m_2: sp.Float(daughter_2_mass, 40),
    }
    lam = sp.N(lambda_polynomial.subs(substitutions), 40)
    momentum = sp.sqrt(lam) / (2 * substitutions[M])
    amplitude_squared = sp.N(
        coupling**2 * polarization_sum_on_shell.subs(substitutions), 40
    )
    width = momentum * amplitude_squared / (8 * sp.pi * substitutions[M] ** 2)
    return float(width), float(amplitude_squared), float(momentum)


channel_widths = []
for channel in wp516["open_cubic_vector_channels"]:
    width, amplitude_squared, momentum = partial_width(
        channel["parent_mass_GeV"],
        channel["daughter_masses_GeV"][0],
        channel["daughter_masses_GeV"][1],
        channel["cubic_coupling"],
    )
    channel_widths.append(
        {
            **channel,
            "center_of_mass_momentum_GeV": momentum,
            "polarization_averaged_amplitude_squared_GeV_squared": amplitude_squared,
            "partial_width_GeV": width,
            "fractional_partial_width": width / channel["parent_mass_GeV"],
        }
    )

parent_sums = {}
for channel in channel_widths:
    key = str(channel["parent"])
    packet = parent_sums.setdefault(
        key,
        {
            "parent_mass_GeV": channel["parent_mass_GeV"],
            "open_vector_channel_count": 0,
            "summed_vector_partial_width_GeV": 0.0,
        },
    )
    packet["open_vector_channel_count"] += 1
    packet["summed_vector_partial_width_GeV"] += channel["partial_width_GeV"]
for packet in parent_sums.values():
    packet["summed_vector_fractional_width"] = (
        packet["summed_vector_partial_width_GeV"] / packet["parent_mass_GeV"]
    )

# Orthogonal changes of basis inside an exactly degenerate daughter subspace
# preserve the summed squared coupling.  Verify the algebraic two-coordinate
# identity used for every such complete degenerate sum.
c_1, c_2, theta = sp.symbols("c_1 c_2 theta", real=True)
rotated_1 = sp.cos(theta) * c_1 + sp.sin(theta) * c_2
rotated_2 = -sp.sin(theta) * c_1 + sp.cos(theta) * c_2
degenerate_norm_difference = sp.trigsimp(
    rotated_1**2 + rotated_2**2 - c_1**2 - c_2**2
)

width_values = [channel["partial_width_GeV"] for channel in channel_widths]
largest_channel = max(channel_widths, key=lambda item: item["partial_width_GeV"])
largest_parent = max(
    parent_sums.items(), key=lambda item: item[1]["summed_vector_partial_width_GeV"]
)

checks = {
    "wp509_dependency_passed": bool(wp509["passed"]),
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp516_dependency_passed": bool(wp516["passed"]),
    "all_external_polarizations_are_unit_spacelike": bool(
        all(dot(vector, vector) == -1 for vector in parent_polarizations)
        and all(dot(vector, vector).subs(p**2, E_1**2 - m_1**2).simplify() == -1 for vector in daughter_1_polarizations)
        and all(dot(vector, vector).subs(p**2, E_2**2 - m_2**2).simplify() == -1 for vector in daughter_2_polarizations)
    ),
    "all_external_polarizations_are_transverse": bool(
        all(dot(-k_0, vector) == 0 for vector in parent_polarizations)
        and all(sp.simplify(dot(k_1, vector)) == 0 for vector in daughter_1_polarizations)
        and all(sp.simplify(dot(k_2, vector)) == 0 for vector in daughter_2_polarizations)
    ),
    "polarization_sum_matches_closed_unequal_mass_formula": sp.simplify(
        polarization_sum_on_shell - expected_polarization_sum
    ) == 0,
    "all_wp516_channels_receive_positive_partial_widths": bool(
        len(width_values) == len(wp516["open_cubic_vector_channels"])
        and min(width_values) > 0
    ),
    "parent_sums_are_positive": bool(
        len(parent_sums) > 0
        and all(packet["summed_vector_partial_width_GeV"] > 0 for packet in parent_sums.values())
    ),
    "degenerate_subspace_coupling_norm_is_rotation_invariant": degenerate_norm_difference == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP517",
    "width_functional": {
        "metric": "(+,-,-,-)",
        "vertex": "standard Yang-Mills three-vector vertex with all momenta outgoing",
        "daughter_typing": "distinct gauge mass eigenstates; no identical-particle factor",
        "phase_space": "Gamma=|p| times averaged |M|^2 divided by (8 pi M^2)",
        "kallen_polynomial": str(lambda_polynomial),
        "polarization_averaged_unit_coupling_amplitude_squared": str(expected_polarization_sum),
        "normalization_authority": "Derived from the canonical kinetic action and explicit physical-polarization sum; no width datum is fitted.",
    },
    "channel_partial_widths": channel_widths,
    "parent_vector_width_sums": parent_sums,
    "largest_channel": largest_channel,
    "largest_parent_sum": {"parent": int(largest_parent[0]), **largest_parent[1]},
    "classification": "Independently normalized tree-level vector partial widths at the frozen WP516 existence witness. These are additions to, not replacements for, WP509 quark partial widths.",
    "selector": False,
    "rigidifier": bool(len(parent_sums) > 0),
    "instrument": "WP511 constrains the entrance ratio; no pole-resolved production/decay likelihood or detector resolution is attached.",
    "smallest_exact_falsifier": "The explicit polarization contraction differs from the closed unequal-mass functional, or any WP516 strict-threshold nonzero vertex yields a nonpositive partial width.",
    "remaining_gate": "Recover each parent's WP509 quark residue in the same mass ordering, add scalar and off-shell channels, and attach pole-resolved production, lineshape, and detector response before calling the sums total widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp517_unequal_vector_partial_widths.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
