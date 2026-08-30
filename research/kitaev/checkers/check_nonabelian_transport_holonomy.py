import hashlib
import itertools
import json
from pathlib import Path


IDENTITY = (0, 1, 2)


def compose(left, right):
    """Return left after right."""
    return tuple(left[right[i]] for i in range(3))


def inverse(permutation):
    result = [0, 0, 0]
    for index, image in enumerate(permutation):
        result[image] = index
    return tuple(result)


S3 = list(itertools.permutations(range(3)))
t12 = (1, 0, 2)
t23 = (0, 2, 1)


def transform_edges(labels, frames):
    edges = ((0, 1), (1, 2), (2, 0))
    return tuple(
        compose(frames[head], compose(label, inverse(frames[tail])))
        for label, (tail, head) in zip(labels, edges)
    )


def holonomy(labels):
    g01, g12, g20 = labels
    return compose(g20, compose(g12, g01))


obstructed = (t12, t23, IDENTITY)
trivial = (t12, t12, IDENTITY)
obstructed_holonomy = holonomy(obstructed)
trivial_holonomy = holonomy(trivial)
assert obstructed_holonomy in {(1, 2, 0), (2, 0, 1)}
assert trivial_holonomy == IDENTITY

all_frames = itertools.product(S3, repeat=3)
obstructed_solutions = 0
trivial_solutions = 0
for frames in all_frames:
    if transform_edges(obstructed, frames) == (IDENTITY,) * 3:
        obstructed_solutions += 1
    if transform_edges(trivial, frames) == (IDENTITY,) * 3:
        trivial_solutions += 1
assert obstructed_solutions == 0
assert trivial_solutions == 6

# Holonomy transforms by conjugation at the base vertex.
sample_frames = (t12, t23, obstructed_holonomy)
transformed = transform_edges(obstructed, sample_frames)
expected = compose(sample_frames[0], compose(obstructed_holonomy, inverse(sample_frames[0])))
assert holonomy(transformed) == expected

payload = {
    "status": "pass",
    "theorem": "nonabelian_frame_transport_is_classified_by_ordered_holonomy",
    "frame_group": "S3",
    "obstructed_edge_classes": ["transposition_12", "transposition_23", "identity"],
    "obstructed_holonomy_class": "three_cycle",
    "obstructed_trivializing_frames": obstructed_solutions,
    "trivial_edge_classes": ["transposition_12", "transposition_12", "identity"],
    "trivial_holonomy_class": "identity",
    "trivializing_frames": trivial_solutions,
    "holonomy_conjugation_law_verified": True,
    "central_readout_recovers_based_frame": False,
    "physical_endpoint_ports_constructed": False,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "nonabelian-transport-holonomy.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
