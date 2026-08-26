import json
from pathlib import Path


def index(partition):
    return {state: block_id for block_id, block in enumerate(partition) for state in block}


def preservation_defect(partition, transform):
    cls = index(partition)
    witnesses = []
    for block in partition:
        for i, left in enumerate(block):
            for right in block[i + 1:]:
                if cls[transform[left]] != cls[transform[right]]:
                    witnesses.append((left, right, transform[left], transform[right]))
    return witnesses


states = tuple(range(4))
coarse = (states,)
fine = ((0, 1), (2, 3))

safe_transform = {0: 2, 1: 3, 2: 0, 3: 1}
unsafe_transform = {0: 0, 1: 2, 2: 0, 3: 2}

assert preservation_defect(coarse, safe_transform) == []
assert preservation_defect(coarse, unsafe_transform) == []
assert preservation_defect(fine, safe_transform) == []
unsafe_witnesses = preservation_defect(fine, unsafe_transform)
assert unsafe_witnesses == [(0, 1, 0, 2), (2, 3, 0, 2)]

# The coarse quotient has one point and its identity operation. Every function
# from the two fine classes to themselves is a lift through the constant
# downgrade map. Existence therefore leaves four incompatible choices.
fine_class_count = len(fine)
abstract_lift_count = fine_class_count ** fine_class_count
assert abstract_lift_count == 4

# Adding the concrete source transformer selects one lift only if it preserves
# the fine partition.
fine_index = index(fine)
safe_lift = tuple(fine_index[safe_transform[block[0]]] for block in fine)
assert safe_lift == (1, 0)

# A redundant refinement has singleton downgrade fibers and hence a unique lift.
identity_partition = ((0,), (1,), (2,), (3,))
singleton_fiber_lifts = 1

result = {
    "schema": "marici.nima.protocol-migration-defect.v1",
    "safe_concrete_transform_defect_count": len(preservation_defect(fine, safe_transform)),
    "unsafe_concrete_transform_defect_count": len(unsafe_witnesses),
    "unsafe_witnesses": unsafe_witnesses,
    "abstract_coarse_operation_lift_count": abstract_lift_count,
    "source_selected_safe_lift": safe_lift,
    "singleton_fiber_lift_count": singleton_fiber_lifts,
    "verdict": "Protocol migration has two independent gates: preservation of the refined equivalence by concrete operations, and source authority selecting one lift among the abstract lifts."
}

out = Path(__file__).parents[1] / "results" / "protocol-migration-defect.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
