"""Exact WP609 stabilizer audit for an anchored two-matching carrier."""

import itertools
import json
from pathlib import Path

import sympy as sp


def permutation_matrix(permutation):
    matrix = sp.zeros(3)
    for source, target in enumerate(permutation):
        matrix[target, source] = 1
    return matrix


permutations = list(itertools.permutations(range(3)))
matrices = {permutation: permutation_matrix(permutation) for permutation in permutations}

anchor = sp.eye(3)
forward = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
reverse = forward.T
reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])


def stabilizers(*relations):
    result = []
    for left_name, left in matrices.items():
        for right_name, right in matrices.items():
            if all(left.T * relation * right == relation for relation in relations):
                result.append((left_name, right_name))
    return result


anchor_only = stabilizers(anchor)
forward_only = stabilizers(forward)
joint = stabilizers(anchor, forward)

joint_matrices = [(matrices[left], matrices[right]) for left, right in joint]
joint_is_simultaneous = all(left == right for left, right in joint_matrices)
joint_orders = []
for left, _ in joint_matrices:
    if left == sp.eye(3):
        joint_orders.append(1)
    elif left**3 == sp.eye(3):
        joint_orders.append(3)
    else:
        joint_orders.append(None)

shifted_reflection = forward.T * reflection * forward

# A detector projection that forgets which source relation generated an edge.
uncolored_record = anchor + forward
uncolored_stabilizers = []
for name, matrix in matrices.items():
    if matrix.T * uncolored_record * matrix == uncolored_record:
        uncolored_stabilizers.append(name)

checks = {
    "anchor_only_has_six_simultaneous_relabellings": len(anchor_only) == 6
    and all(left == right for left, right in anchor_only),
    "forward_only_has_six_independent_pair_relabellings": len(forward_only) == 6,
    "forward_only_contains_shifted_reflection": any(
        matrices[left] == reflection and matrices[right] == shifted_reflection
        for left, right in forward_only
    ),
    "joint_stabilizer_has_three_elements": len(joint) == 3,
    "joint_stabilizer_is_simultaneous": joint_is_simultaneous,
    "joint_stabilizer_is_c3": sorted(joint_orders) == [1, 3, 3],
    "no_common_reflection_stabilizes_both": all(
        left != reflection or right != reflection for left, right in joint_matrices
    ),
    "reflection_reverses_forward_relation": reflection.T * forward * reflection
    == reverse,
    "anchor_is_unchanged_by_reflection": reflection.T * anchor * reflection
    == anchor,
    "uncolored_join_still_has_only_c3": len(uncolored_stabilizers) == 3,
    "deleting_either_relation_restores_sixfold_stabilizer": len(anchor_only) == 6
    and len(forward_only) == 6,
}

if not all(checks.values()):
    raise SystemExit(f"WP609 check failed: {checks}")

result = {
    "work_package": "WP609",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "source_object": "two source-derived relations on the same physical A and B port families: diagonal anchor D=I and forward matching K=P_forward",
    "full_contextual_partition": "the joined relational object has automorphism group C3; either one-relation deletion has a six-element stabilizer containing a reflection",
    "hard_to_vary_content": "reflection removal is combinatorial and survives arbitrary nonzero coefficients that keep the two support relations distinct",
    "classification": "source-defined relational carrier and presentation rigidifier; neither a numerical flavor selector nor a physical16 readout",
    "smallest_exact_falsifier": "delete or physically fail either the diagonal anchor or the forward matching; the stabilizer enlarges from C3 to six elements",
    "instrument": "measure both support relations on the same physically tagged A/B ports; a detector-only alignment port defines a new relational experiment",
    "instrument_kernel": "forgetting the shared physical port identity restores independent A/B relabelling and erases the reflection obstruction",
    "physical16_gate": "derive weak-basis-invariant A/B port identities and a source action whose joint support selects a proper physical16 family",
    "numerical_gate": "no mass ratio, mixing angle, or CP invariant is fixed by the two support relations alone",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp609_anchored_two_matching_relational_carrier.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
