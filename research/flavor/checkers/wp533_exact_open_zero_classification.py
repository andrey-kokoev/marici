"""Exact representation-support classification of all WP529 open triples."""

import contextlib
import io
import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp529 = load("wp529_lightweight_vector_census.json")
wp531 = load("wp531_exact_candidate_block_zeros.json")
wp532 = load("wp532_quintet_projector_width_sum.json")

# Replay the lightweight census to recover all 173 open triples. The generated
# WP529 result stores aggregates but deliberately does not serialize 131 zeros.
path529 = root / "checkers" / "wp529_lightweight_vector_census.py"
namespace = {"__file__": str(path529), "__name__": "wp529_replay"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(
            compile(path529.read_text(encoding="utf-8"), str(path529), "exec"),
            namespace,
        )
    except SystemExit as error:
        if error.code != 0:
            raise

all_open = namespace["all_open"]
numerical_zeros = namespace["numerical_zeros"]
resolved = namespace["resolved"]
subcutoff_candidates = namespace["subcutoff_candidates"]

# Exact orthonormal frames. Q is the principal-SU(2) quintet. Each C_i is the
# rank-three complement of the embedded quintet line in one WP508 four-block.
eye = sp.eye(14)
frames = {
    "Q": sp.Matrix.hstack(
        (eye[:, 0] - eye[:, 5]) / sp.sqrt(2),
        (eye[:, 1] - eye[:, 6]) / sp.sqrt(2),
        (sp.sqrt(3) * eye[:, 2] - eye[:, 7]) / 2,
        eye[:, 3],
        eye[:, 4],
    ),
    "C0": sp.Matrix.hstack(
        (eye[:, 0] + eye[:, 5]) / sp.sqrt(2),
        eye[:, 8],
        eye[:, 11],
    ),
    "C1": sp.Matrix.hstack(
        (eye[:, 1] + eye[:, 6]) / sp.sqrt(2),
        eye[:, 9],
        eye[:, 12],
    ),
    "C2": sp.Matrix.hstack(
        (eye[:, 2] + sp.sqrt(3) * eye[:, 7]) / 2,
        eye[:, 10],
        eye[:, 13],
    ),
}
projectors = {
    name: sp.simplify(frame * frame.T) for name, frame in frames.items()
}

# Exact canonical cubic tensor.
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
gauge_tensor = sp.MutableDenseNDimArray.zeros(14, 14, 14)
for left in range(8):
    for middle in range(8):
        commutator = lambdas[left] * lambdas[middle] - lambdas[middle] * lambdas[left]
        for right in range(8):
            gauge_tensor[left, middle, right] = sp.simplify(
                sp.sqrt(2)
                * sp.trace(commutator * lambdas[right])
                / (4 * imag)
            )
for offset, coupling in ((8, sp.Rational(1, 10)), (11, sp.Rational(1, 50))):
    for left in range(3):
        for middle in range(3):
            for right in range(3):
                gauge_tensor[offset + left, offset + middle, offset + right] = (
                    coupling * sp.LeviCivita(left, middle, right)
                )


def nonzero_support(column):
    return [(index, value) for index, value in enumerate(column) if value != 0]


frame_supports = {
    name: [
        nonzero_support(frame[:, column])
        for column in range(frame.cols)
    ]
    for name, frame in frames.items()
}


def restricted_norm(signature):
    total = sp.Integer(0)
    for left_support in frame_supports[signature[0]]:
        for middle_support in frame_supports[signature[1]]:
            for right_support in frame_supports[signature[2]]:
                coefficient = sp.simplify(
                    sum(
                        left_value
                        * middle_value
                        * right_value
                        * gauge_tensor[left, middle, right]
                        for left, left_value in left_support
                        for middle, middle_value in middle_support
                        for right, right_value in right_support
                    )
                )
                total += coefficient**2
    return sp.simplify(total)


class_names = ["Q", "C0", "C1", "C2"]
restriction_norms = {
    (left, middle, right): restricted_norm((left, middle, right))
    for left in class_names
    for middle in class_names
    for right in class_names
}
zero_signatures = {
    signature for signature, norm in restriction_norms.items() if norm == 0
}

# State ordering from the frozen WP516 eigenvalue list. The five exactly
# degenerate coordinates are Q; the other states are roots inside C_i.
state_class = {
    0: "C2",
    1: "C0",
    2: "C1",
    3: "C2",
    4: "C0",
    5: "C1",
    6: "C2",
    7: "Q",
    8: "Q",
    9: "Q",
    10: "Q",
    11: "Q",
    12: "C0",
    13: "C1",
}


def signature(item):
    return (
        state_class[item["parent"]],
        state_class[item["daughter_1"]],
        state_class[item["daughter_2"]],
    )


def compact(item):
    return {
        "parent": item["parent"],
        "daughter_1": item["daughter_1"],
        "daughter_2": item["daughter_2"],
        "signature": list(signature(item)),
        "absolute_coupling": item["absolute_coupling"],
    }


structural_zeros = [item for item in all_open if signature(item) in zero_signatures]
certified_numerical_zeros = [
    item for item in numerical_zeros if signature(item) in zero_signatures
]
unresolved_zeros = [
    item for item in numerical_zeros if signature(item) not in zero_signatures
]
resolved_in_zero_class = [
    item for item in resolved if signature(item) in zero_signatures
]
candidates_in_zero_class = [
    item for item in subcutoff_candidates if signature(item) in zero_signatures
]

signature_census = {}
for item in all_open:
    key = " x ".join(signature(item))
    packet = signature_census.setdefault(
        key,
        {
            "exact_restriction_norm": str(restriction_norms[signature(item)]),
            "open_coordinate_count": 0,
            "resolved_coordinate_count": 0,
            "numerical_zero_coordinate_count": 0,
        },
    )
    packet["open_coordinate_count"] += 1
    if item["absolute_coupling"] > 1e-12:
        packet["resolved_coordinate_count"] += 1
    else:
        packet["numerical_zero_coordinate_count"] += 1

frame_resolution = sp.simplify(sum(projectors.values(), sp.zeros(14)))
checks = {
    "wp529_dependency_passed": bool(wp529["passed"]),
    "wp531_dependency_passed": bool(wp531["passed"]),
    "wp532_dependency_passed": bool(wp532["passed"]),
    "frames_are_orthonormal": all(
        frame.T * frame == sp.eye(frame.cols) for frame in frames.values()
    ),
    "four_projectors_are_pairwise_orthogonal": all(
        projectors[left] * projectors[right] == sp.zeros(14)
        for left in class_names
        for right in class_names
        if left != right
    ),
    "four_projectors_resolve_the_gauge_space": frame_resolution == sp.eye(14),
    "replay_recovers_173_open_coordinates": len(all_open) == 173,
    "replay_recovers_131_numerical_zeros": len(numerical_zeros) == 131,
    "replay_recovers_42_resolved_coordinates": len(resolved) == 42,
    "all_eight_wp529_candidates_are_in_exact_zero_classes": (
        len(candidates_in_zero_class) == 8
    ),
    "the_only_resolved_coordinates_in_zero_classes_are_the_eight_candidates": (
        len(resolved_in_zero_class) == 8
        and {
            (item["parent"], item["daughter_1"], item["daughter_2"])
            for item in resolved_in_zero_class
        }
        == {
            (item["parent"], item["daughter_1"], item["daughter_2"])
            for item in subcutoff_candidates
        }
    ),
    "all_131_numerical_zeros_receive_exact_support_certificates": (
        len(certified_numerical_zeros) == 131
    ),
    "exact_support_partition_leaves_the_34_wp516_channels": (
        len(structural_zeros) == 139
        and len(all_open) - len(structural_zeros) == 34
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP533",
    "domain": "All 173 threshold-open coordinate triples in the frozen WP516 fourteen-vector witness, partitioned by the exact Q, C0, C1 and C2 representation subspaces.",
    "exact_subspaces": {
        name: {
            "dimension": frame.cols,
            "projector_rank": projectors[name].rank(),
        }
        for name, frame in frames.items()
    },
    "zero_restriction_signature_count": len(zero_signatures),
    "nonzero_restriction_signature_count": len(restriction_norms)
    - len(zero_signatures),
    "open_signature_census": signature_census,
    "classification_counts": {
        "open_coordinate_count": len(all_open),
        "resolved_coordinate_count": len(resolved),
        "numerical_zero_coordinate_count": len(numerical_zeros),
        "exact_structural_zero_coordinate_count": len(structural_zeros),
        "of_which_wp529_candidates": len(candidates_in_zero_class),
        "of_which_numerical_zeros": len(certified_numerical_zeros),
        "exact_nonzero_support_coordinate_count": len(all_open)
        - len(structural_zeros),
        "unresolved_numerical_zero_coordinate_count": len(unresolved_zeros),
    },
    "unresolved_numerical_zeros": [compact(item) for item in unresolved_zeros],
    "theorem": "Every coordinate triple whose Q/C_i signature has zero exact restricted tensor norm vanishes for all within-subspace basis choices. All 131 numerical zeros and the eight WP529 candidates lie in those classes. The complement contains exactly the 34 WP516 channels.",
    "classification": "Complete exact representation-support partition of the WP529 open census: 139 forbidden coordinates and 34 allowed coordinates. It supersedes numerical cutoff authority for channel presence on this witness.",
    "selector": False,
    "rigidifier": bool(
        len(structural_zeros) == 139
        and len(certified_numerical_zeros) == 131
    ),
    "instrument": "No instrument is added. This audit determines which internal vector channels are absent before physical pole production, lineshape and detector response are applied.",
    "smallest_exact_falsifier": "A numerically resolved coupling appears in an exactly zero restriction class, or an allegedly structural-zero coordinate has a signature with nonzero restricted norm.",
    "remaining_gate": "Replace the 34 coordinate rows by invariant parent-level sums, freeze the quark and vector self-energy in the common WP527 source domain, and compose it through the WP525 complex-mass Ward completion without assigning detector authority.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp533_exact_open_zero_classification.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
