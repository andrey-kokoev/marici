"""Lightweight reconstruction of the complete WP516 pre-cutoff vector tensor."""

import json
import math
from pathlib import Path

import numpy as np


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp517 = load("wp517_unequal_vector_partial_widths.json")
wp527 = load("wp527_hierarchical_nonquark_closure.json")
wp528 = load("wp528_vector_cutoff_width_envelope.json")

sqrt = np.sqrt
i_unit = 1j
lambdas = [
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex),
    np.array([[0, -i_unit, 0], [i_unit, 0, 0], [0, 0, 0]], complex),
    np.diag([1, -1, 0]).astype(complex),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex),
    np.array([[0, 0, -i_unit], [0, 0, 0], [i_unit, 0, 0]], complex),
    np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex),
    np.array([[0, 0, 0], [0, 0, -i_unit], [0, i_unit, 0]], complex),
    np.diag([1, 1, -2]).astype(complex) / sqrt(3),
]
spin_one = [
    np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], complex) / sqrt(2),
    np.array([[0, -i_unit, 0], [i_unit, 0, -i_unit], [0, i_unit, 0]], complex)
    / sqrt(2),
    np.diag([1, 0, -1]).astype(complex),
]
row_generators = [
    np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]], float),
    np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]], float),
    np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]], float),
]

g_f = sqrt(2)
g_p = 0.1
g_e = 0.02
mu = 1.0
s = 16.0
b_squared = 30258 / 160001
a_squared = 160000 * b_squared
a = sqrt(a_squared)
b = sqrt(b_squared)
S0 = s * np.eye(3)
U0 = np.zeros((3, 2), complex)
D0 = np.zeros((3, 2), complex)
U0[2, 1] = a
D0[0, 1] = b


def adjoint_coordinates(matrix):
    return np.array([np.trace(matrix @ basis).real / 2 for basis in lambdas])


def complex_coordinates(matrix):
    return np.concatenate([matrix.real.ravel(), matrix.imag.ravel()])


def field_vector(delta_s, delta_x, delta_u, delta_d):
    return np.concatenate(
        [
            np.asarray(delta_s).real.ravel(),
            *(adjoint_coordinates(matrix) for matrix in delta_x),
            complex_coordinates(delta_u),
            complex_coordinates(delta_d),
        ]
    )


zero_s = np.zeros((3, 3))
zero_x = [np.zeros((3, 3), complex) for _ in range(3)]
zero_u = np.zeros((3, 2), complex)
zero_d = np.zeros((3, 2), complex)
tangents = []
for generator in lambdas:
    delta_x = [
        i_unit * g_f * mu * (generator @ matrix - matrix @ generator)
        for matrix in spin_one
    ]
    tangents.append(field_vector(zero_s, delta_x, zero_u, zero_d))
for generator in row_generators:
    delta_x = [
        g_p
        * mu
        * sum(
            (generator[left, right] * spin_one[right] for right in range(3)),
            np.zeros((3, 3), complex),
        )
        for left in range(3)
    ]
    tangents.append(
        field_vector(-g_p * S0 @ generator, delta_x, zero_u, zero_d)
    )
for generator in row_generators:
    tangents.append(
        field_vector(
            g_e * generator @ S0,
            zero_x,
            g_e * generator @ U0,
            g_e * generator @ D0,
        )
    )

tangent_matrix = np.column_stack(tangents)
tangent_matrix[:, :8] *= 0.5
kinetic_weights = np.array([1.0] * 9 + [2.0] * 24 + [2.0] * 24)
mass_matrix = tangent_matrix.T @ (kinetic_weights[:, None] * tangent_matrix)
mass_squared, rotation = np.linalg.eigh(mass_matrix)
masses = np.sqrt(np.maximum(mass_squared, 0))


def levi_civita(left, middle, right):
    if len({left, middle, right}) < 3:
        return 0.0
    permutation = [left, middle, right]
    inversions = sum(
        permutation[i] > permutation[j] for i in range(3) for j in range(i + 1, 3)
    )
    return -1.0 if inversions % 2 else 1.0


flavor_structure = np.zeros((8, 8, 8))
for left in range(8):
    for middle in range(8):
        commutator = lambdas[left] @ lambdas[middle] - lambdas[middle] @ lambdas[left]
        for right in range(8):
            flavor_structure[left, middle, right] = (
                np.trace(commutator @ lambdas[right]) / (4j)
            ).real
gauge_tensor = np.zeros((14, 14, 14))
gauge_tensor[:8, :8, :8] = g_f * flavor_structure
for offset, coupling in ((8, g_p), (11, g_e)):
    for left in range(3):
        for middle in range(3):
            for right in range(3):
                gauge_tensor[offset + left, offset + middle, offset + right] = (
                    coupling * levi_civita(left, middle, right)
                )
mass_tensor = np.einsum(
    "abc,ai,bj,ck->ijk", gauge_tensor, rotation, rotation, rotation
)

all_open = []
for parent in range(14):
    for daughter_1 in range(14):
        for daughter_2 in range(daughter_1 + 1, 14):
            margin = masses[parent] - masses[daughter_1] - masses[daughter_2]
            if margin > 1e-9:
                all_open.append(
                    {
                        "parent": parent,
                        "daughter_1": daughter_1,
                        "daughter_2": daughter_2,
                        "margin_GeV": float(margin),
                        "coupling": float(mass_tensor[parent, daughter_1, daughter_2]),
                        "absolute_coupling": abs(
                            float(mass_tensor[parent, daughter_1, daughter_2])
                        ),
                    }
                )

nonzero_floor = 1e-12
resolved = [item for item in all_open if item["absolute_coupling"] > nonzero_floor]
numerical_zeros = [
    item for item in all_open if item["absolute_coupling"] <= nonzero_floor
]
resolved.sort(key=lambda item: item["absolute_coupling"])
maximum_zero = max(
    (item["absolute_coupling"] for item in numerical_zeros), default=0.0
)
minimum_nonzero = min(item["absolute_coupling"] for item in resolved)
wp516_channels = wp516["open_cubic_vector_channels"]
subcutoff_candidates = [
    item for item in resolved if item["absolute_coupling"] <= 1e-7
]


def partial_width(item):
    parent_mass = masses[item["parent"]]
    daughter_1_mass = masses[item["daughter_1"]]
    daughter_2_mass = masses[item["daughter_2"]]
    coupling = item["absolute_coupling"]
    kallen = (
        parent_mass**4
        + daughter_1_mass**4
        + daughter_2_mass**4
        - 2 * parent_mass**2 * daughter_1_mass**2
        - 2 * parent_mass**2 * daughter_2_mass**2
        - 2 * daughter_1_mass**2 * daughter_2_mass**2
    )
    polynomial = (
        parent_mass**4
        + daughter_1_mass**4
        + daughter_2_mass**4
        + 10 * parent_mass**2 * daughter_1_mass**2
        + 10 * parent_mass**2 * daughter_2_mass**2
        + 10 * daughter_1_mass**2 * daughter_2_mass**2
    )
    polarization_sum = (
        kallen
        * polynomial
        / (
            12
            * parent_mass**2
            * daughter_1_mass**2
            * daughter_2_mass**2
        )
    )
    momentum = math.sqrt(kallen) / (2 * parent_mass)
    return (
        momentum
        * coupling**2
        * polarization_sum
        / (8 * math.pi * parent_mass**2)
    )


for item in subcutoff_candidates:
    item["candidate_partial_width_GeV"] = partial_width(item)
subcutoff_width_sum = sum(
    item["candidate_partial_width_GeV"] for item in subcutoff_candidates
)

mass_residual = float(
    np.max(np.abs(mass_matrix @ rotation - rotation @ np.diag(mass_squared)))
)
orthogonality_residual = float(
    np.max(np.abs(rotation.T @ rotation - np.eye(14)))
)
stored_masses = np.array(wp516["mass_basis"]["ordered_masses_GeV"])
mass_reproduction_error = float(np.max(np.abs(masses - stored_masses)))

checks = {
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp517_dependency_passed": bool(wp517["passed"]),
    "wp527_dependency_passed": bool(wp527["passed"]),
    "wp528_dependency_passed": bool(wp528["passed"]),
    "mass_spectrum_reproduces_wp516": mass_reproduction_error < 1e-12,
    "eigendecomposition_residual_is_below_1e_12": mass_residual < 1e-12,
    "orthogonality_residual_is_below_1e_12": orthogonality_residual < 1e-12,
    "wp516_retained_exactly_34_channels": len(wp516_channels) == 34,
    "lightweight_census_finds_42_entries_above_1e_12": len(resolved) == 42,
    "eight_candidates_were_removed_by_original_cutoff": len(
        subcutoff_candidates
    )
    == 8,
    "every_candidate_is_below_original_cutoff": all(
        item["absolute_coupling"] <= 1e-7 for item in subcutoff_candidates
    ),
    "every_remaining_entry_is_below_numerical_zero_floor": maximum_zero
    <= nonzero_floor,
    "candidate_to_zero_gap_exceeds_fifty": minimum_nonzero
    > 50 * maximum_zero,
    "candidate_width_sum_is_positive": subcutoff_width_sum > 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP529",
    "domain": "All threshold-open unordered daughter pairs for every parent in the frozen WP516 fourteen-vector witness.",
    "lightweight_reconstruction": {
        "method": "Direct numerical evaluation of WP507's explicit gauge tangents, followed by WP508 canonical generator and field-metric normalizations; no symbolic replay.",
        "mass_reproduction_error_GeV": mass_reproduction_error,
        "eigendecomposition_residual": mass_residual,
        "orthogonality_residual": orthogonality_residual,
    },
    "precutoff_census": {
        "threshold_open_candidate_count": len(all_open),
        "nonzero_above_1e_12_count": len(resolved),
        "numerical_zero_at_or_below_1e_12_count": len(numerical_zeros),
        "minimum_nonzero_coupling": minimum_nonzero,
        "maximum_numerical_zero": maximum_zero,
        "smallest_nonzero_channels": resolved[:10],
        "subcutoff_candidate_channels": subcutoff_candidates,
        "subcutoff_candidate_width_sum_GeV": subcutoff_width_sum,
    },
    "classification": "Corrective lightweight census. Eight threshold-open candidate couplings occur below WP516's cutoff and above the numerical-zero cluster. Their widths are computable candidates, not admitted exact channels, because near-degenerate eigenvector sensitivity has not been bounded.",
    "selector": False,
    "rigidifier": False,
    "instrument": "WP517's 34-channel list is not numerically complete under its own pre-cutoff tensor reconstruction. Exact width correction awaits high-precision interval certification of the eight candidates and the numerical-zero class.",
    "smallest_exact_falsifier": "A high-precision interval for any candidate contains zero, showing it is a near-degenerate basis artifact rather than a physical nonzero coupling.",
    "remaining_gate": "Reconstruct the small-gap eigenspaces at high precision, certify basis-invariant summed couplings by intervals, then add every certified candidate width before applying WP525.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp529_lightweight_vector_census.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
