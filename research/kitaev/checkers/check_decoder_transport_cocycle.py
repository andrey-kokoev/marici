import hashlib
import itertools
import json
from pathlib import Path


def transformed(labels, frames, edges):
    return tuple(
        (label + frames[tail] - frames[head]) % 2
        for label, (tail, head) in zip(labels, edges)
    )


triangle_edges = ((0, 1), (1, 2), (2, 0))
frames = list(itertools.product(range(2), repeat=3))

obstructed = (1, 0, 0)
trivial = (1, 1, 0)
obstructed_solutions = [frame for frame in frames if transformed(obstructed, frame, triangle_edges) == (0, 0, 0)]
trivial_solutions = [frame for frame in frames if transformed(trivial, frame, triangle_edges) == (0, 0, 0)]
assert sum(obstructed) % 2 == 1
assert obstructed_solutions == []
assert sum(trivial) % 2 == 0
assert len(trivial_solutions) == 2

# Every cochain on a tree is removable; two solutions differ by global shift.
tree_edges = ((0, 1), (1, 2))
for labels in itertools.product(range(2), repeat=2):
    solutions = [frame for frame in frames if transformed(labels, frame, tree_edges) == (0, 0)]
    assert len(solutions) == 2

payload = {
    "status": "pass",
    "theorem": "local_decoder_origins_glue_only_when_the_transport_cocycle_is_trivial",
    "logical_group": "C2",
    "obstructed_triangle_displacements": list(obstructed),
    "obstructed_cycle_holonomy": 1,
    "obstructed_global_frames": len(obstructed_solutions),
    "trivial_triangle_displacements": list(trivial),
    "trivial_cycle_holonomy": 0,
    "trivial_global_frames": len(trivial_solutions),
    "every_tree_transport_trivializable": True,
    "completion_uniformity_additional": True,
    "theta_transport_instantiated": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "decoder-transport-cocycle.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
