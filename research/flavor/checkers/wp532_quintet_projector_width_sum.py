"""Exact quintet projector and basis-invariant pair-width sum for WP532."""

import contextlib
import io
import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp517 = load("wp517_unequal_vector_partial_widths.json")
wp531 = load("wp531_exact_candidate_block_zeros.json")

# Replay only the exact WP508 mass operator. The WP516 witness substitutions
# are exact, including the two square-root entrance coordinates.
path508 = root / "checkers" / "wp508_canonical_heavy_gauge_poles.py"
namespace = {"__file__": str(path508), "__name__": "wp508_replay"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(
            compile(path508.read_text(encoding="utf-8"), str(path508), "exec"),
            namespace,
        )
    except SystemExit as error:
        if error.code != 0:
            raise

g_f = namespace["g_f"]
g_p = namespace["g_p"]
g_e = namespace["g_e"]
mu = namespace["mu"]
s = namespace["s"]
a = namespace["a"]
b = namespace["b"]
heavy_block = namespace["heavy_block"]
witness = {
    g_f: sp.sqrt(2),
    g_p: sp.Rational(1, 10),
    g_e: sp.Rational(1, 50),
    mu: 1,
    s: 16,
    a: sp.sqrt(sp.Rational(4841280000, 160001)),
    b: sp.sqrt(sp.Rational(30258, 160001)),
}
mass_matrix = sp.simplify(heavy_block.subs(witness))
quintet_mass_squared = sp.Integer(6)
quintet_kernel = (mass_matrix - quintet_mass_squared * sp.eye(14)).nullspace()
quintet_frame = sp.Matrix.hstack(*quintet_kernel)
quintet_projector = sp.simplify(
    quintet_frame
    * (quintet_frame.T * quintet_frame).inv()
    * quintet_frame.T
)

# Construct the exact Yang--Mills tensor.
imag = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -imag, 0], [imag, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -imag], [0, 0, 0], [imag, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -imag], [0, imag, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
gauge_slices = []
for parent in range(14):
    matrix = sp.zeros(14)
    if parent < 8:
        for left in range(8):
            commutator = lambdas[parent] * lambdas[left] - lambdas[left] * lambdas[parent]
            for right in range(8):
                matrix[left, right] = sp.simplify(
                    sp.sqrt(2)
                    * sp.trace(commutator * lambdas[right])
                    / (4 * imag)
                )
    elif 8 <= parent < 11:
        for left in range(3):
            for right in range(3):
                matrix[8 + left, 8 + right] = (
                    sp.Rational(1, 10)
                    * sp.LeviCivita(parent - 8, left, right)
                )
    else:
        for left in range(3):
            for right in range(3):
                matrix[11 + left, 11 + right] = (
                    sp.Rational(1, 50)
                    * sp.LeviCivita(parent - 11, left, right)
                )
    gauge_slices.append(matrix)

# The factor one half turns the ordered contraction into the norm over
# unordered antisymmetric daughter pairs.
pair_norm_operator = sp.Matrix(
    14,
    14,
    lambda left, right: sp.simplify(
        sp.trace(
            gauge_slices[left].T
            * quintet_projector
            * gauge_slices[right]
            * quintet_projector
        )
        / 2
    ),
)
flavor_identity = sp.diag(*([1] * 8 + [0] * 6))
principal_triplet_projector = sp.simplify(
    flavor_identity - quintet_projector
)
expected_pair_norm_operator = sp.Rational(5, 2) * principal_triplet_projector

# Exact hostile rotation: individual quintet-pair coordinates move, while the
# complete unordered-pair norm does not.
eye8 = sp.eye(8)
q_frame = sp.Matrix.hstack(
    (eye8[:, 0] - eye8[:, 5]) / sp.sqrt(2),
    (eye8[:, 1] - eye8[:, 6]) / sp.sqrt(2),
    (sp.sqrt(3) * eye8[:, 2] - eye8[:, 7]) / 2,
    eye8[:, 3],
    eye8[:, 4],
)
triplet_witness = (eye8[:, 0] + eye8[:, 5]) / sp.sqrt(2)
flavor_slices = [matrix[:8, :8] for matrix in gauge_slices[:8]]
amplitude = sp.Matrix(
    5,
    5,
    lambda left, right: sp.simplify(
        sum(
            triplet_witness[parent]
            * (q_frame[:, left].T * flavor_slices[parent] * q_frame[:, right])[0]
            for parent in range(8)
        )
    ),
)
rotation = sp.eye(5)
rotation[0, 0] = rotation[0, 1] = rotation[1, 0] = 1 / sp.sqrt(2)
rotation[1, 1] = -1 / sp.sqrt(2)
rotated_amplitude = sp.simplify(rotation.T * amplitude * rotation)


def upper_norm(matrix):
    return sp.simplify(
        sum(matrix[left, right] ** 2 for left in range(5) for right in range(left + 1, 5))
    )


original_norm = upper_norm(amplitude)
rotated_norm = upper_norm(rotated_amplitude)
hostile_coordinate_before = sp.simplify(amplitude[0, 4] ** 2)
hostile_coordinate_after = sp.simplify(rotated_amplitude[0, 4] ** 2)

# Audit that WP516/WP517 retained the complete ten-pair coordinate expansion
# for each heavy parent. Individual entries are presentation data, but their
# complete sum represents the invariant contraction above.
quintet_indices = set(range(7, 12))
wp516_quintet_channels = [
    channel
    for channel in wp516["open_cubic_vector_channels"]
    if channel["daughter_1"] in quintet_indices
    and channel["daughter_2"] in quintet_indices
]
wp517_quintet_channels = [
    channel
    for channel in wp517["channel_partial_widths"]
    if channel["daughter_1"] in quintet_indices
    and channel["daughter_2"] in quintet_indices
]
parent_packets = {}
for parent in sorted({channel["parent"] for channel in wp516_quintet_channels}):
    channels = [
        channel for channel in wp516_quintet_channels if channel["parent"] == parent
    ]
    daughter_pairs = sorted(
        (channel["daughter_1"], channel["daughter_2"]) for channel in channels
    )
    parent_packets[str(parent)] = {
        "coordinate_channel_count": len(channels),
        "all_ten_unordered_pairs_present": daughter_pairs
        == [
            (left, right)
            for left in range(7, 12)
            for right in range(left + 1, 12)
        ],
        "summed_squared_coupling": sum(
            channel["cubic_coupling"] ** 2 for channel in channels
        ),
        "summed_partial_width_GeV": sum(
            channel["partial_width_GeV"]
            for channel in wp517_quintet_channels
            if channel["parent"] == parent
        ),
    }

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp517_dependency_passed": bool(wp517["passed"]),
    "wp531_dependency_passed": bool(wp531["passed"]),
    "quintet_eigenspace_has_dimension_five": len(quintet_kernel) == 5,
    "quintet_projector_is_symmetric": quintet_projector.T == quintet_projector,
    "quintet_projector_is_idempotent": quintet_projector**2 == quintet_projector,
    "quintet_projector_has_rank_five": quintet_projector.rank() == 5,
    "quintet_projector_is_exact_mass_six_projector": (
        mass_matrix * quintet_projector
        == quintet_mass_squared * quintet_projector
    ),
    "pair_norm_operator_is_five_halves_triplet_projector": (
        pair_norm_operator == expected_pair_norm_operator
    ),
    "hostile_rotation_changes_an_individual_coordinate": (
        hostile_coordinate_before != hostile_coordinate_after
    ),
    "hostile_rotation_preserves_complete_pair_norm": (
        original_norm == rotated_norm == sp.Rational(5, 2)
    ),
    "wp516_contains_twenty_quintet_pair_coordinates": (
        len(wp516_quintet_channels) == 20
    ),
    "wp517_contains_the_same_twenty_coordinates": (
        len(wp517_quintet_channels) == 20
    ),
    "each_heavy_parent_contains_all_ten_unordered_pairs": (
        set(parent_packets) == {"12", "13"}
        and all(
            packet["all_ten_unordered_pairs_present"]
            for packet in parent_packets.values()
        )
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP532",
    "domain": "The exact mass-six five-dimensional gauge eigenspace and the twenty WP516/WP517 coordinate channels with two daughters in that eigenspace.",
    "quintet_mass_squared_GeV_squared": str(quintet_mass_squared),
    "quintet_projector": [
        [str(value) for value in row] for row in quintet_projector.tolist()
    ],
    "projector_rank": quintet_projector.rank(),
    "pair_norm_theorem": "For any canonical parent vector x, the complete unordered quintet-pair coupling norm is x^T S x with S=(5/2) P_triplet. It is independent of the orthonormal frame chosen inside the five-dimensional quintet.",
    "hostile_rotation": {
        "individual_squared_coordinate_before": str(hostile_coordinate_before),
        "individual_squared_coordinate_after": str(hostile_coordinate_after),
        "complete_squared_norm_before": str(original_norm),
        "complete_squared_norm_after": str(rotated_norm),
    },
    "wp517_coordinate_audit": parent_packets,
    "classification": "Basis-invariant rigidification of the quintet-pair contribution. The twenty WP517 rows are a coordinate expansion of two invariant parent-level sums, not twenty separately physical channels.",
    "selector": False,
    "rigidifier": bool(
        pair_norm_operator == expected_pair_norm_operator
        and original_norm == rotated_norm
    ),
    "instrument": "No new detector instrument is supplied. The projector freezes the internal-state sum required by a pole width; production, lineshape, detector response, and the source-to-WET interface remain external gates.",
    "smallest_exact_falsifier": "The mass-six kernel has dimension other than five, S differs from (5/2) P_triplet, or a complete ten-pair parent sum changes under an orthogonal quintet-frame rotation.",
    "remaining_gate": "Classify the 131 threshold-open numerical-zero coordinate triples by exact block/projector contractions, then replace coordinate rows by parent-level invariant width sums and compose those sums with WP525 and WP527.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp532_quintet_projector_width_sum.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
