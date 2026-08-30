from fractions import Fraction
import json
from pathlib import Path


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix)))


def add(left, right):
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


def subtract(left, right):
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left)))
        for i in range(len(left))
    )


P = (
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
)
PT = transpose(P)

# One-family reciprocal elimination retains only a symmetric orientation-even
# channel. The two directed presentations collapse there.
one_family_plus = add(P, PT)
one_family_minus = add(PT, P)
assert one_family_plus == one_family_minus

# Two inequivalent families admit a reciprocal full block with a directed
# cross-block. The full six-dimensional kernel remains symmetric.
def full_block(K):
    KT = transpose(K)
    zero = (0, 0, 0)
    top = tuple(K[i] for i in range(3))
    bottom = tuple(KT[i] for i in range(3))
    return tuple(zero + top[i] for i in range(3)) + tuple(bottom[i] + zero for i in range(3))


full_plus = full_block(P)
full_minus = full_block(PT)
assert transpose(full_plus) == full_plus
assert transpose(full_minus) == full_minus
assert full_plus != full_minus
assert subtract(P, PT) != ((0, 0, 0),) * 3

# Two coherence processes have the same one-time outage marginal 1/10.
outage = Fraction(1, 10)
iid_all_outage = outage**4
persistent_outage_given_outage = Fraction(91, 100)
persistent_outage_given_coherent = Fraction(1, 100)
stationary_outage = persistent_outage_given_coherent / (
    1 - persistent_outage_given_outage + persistent_outage_given_coherent
)
persistent_all_outage = stationary_outage * persistent_outage_given_outage**3
assert stationary_outage == outage
assert iid_all_outage == Fraction(1, 10000)
assert persistent_all_outage == Fraction(753571, 10000000)
assert iid_all_outage != persistent_all_outage

states = tuple(
    (orientation, process)
    for orientation in ("clockwise", "counterclockwise")
    for process in ("iid", "persistent")
)


def static_record(_state):
    return one_family_plus, Fraction(9, 10)


def spatial_record(state):
    orientation, _ = state
    return full_plus if orientation == "clockwise" else full_minus


def temporal_record(state):
    _, process = state
    return iid_all_outage if process == "iid" else persistent_all_outage


assert len({static_record(s) for s in states}) == 1
assert len({spatial_record(s) for s in states}) == 2
assert len({temporal_record(s) for s in states}) == 2
assert len({(spatial_record(s), temporal_record(s)) for s in states}) == 4

result = {
    "schema": "marici.nima.flavor-bipartite-temporal-correspondence.v1",
    "source_classes": len(states),
    "static_record_classes": len({static_record(s) for s in states}),
    "spatial_only_classes": len({spatial_record(s) for s in states}),
    "temporal_only_classes": len({temporal_record(s) for s in states}),
    "joined_classes": len({(spatial_record(s), temporal_record(s)) for s in states}),
    "one_family_reciprocal_channel_erases_orientation": True,
    "bipartite_full_kernel_reciprocal_and_orientation_sensitive": True,
    "same_one_time_marginal": True,
    "iid_four_block_failure": str(iid_all_outage),
    "persistent_four_block_failure": str(persistent_all_outage),
    "verdict": (
        "Family orientation and temporal coherence are independent missing "
        "coordinates. The joined bipartite-process correspondence is faithful "
        "on the four-class hostile; either projection leaves a two-sheet fiber."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-bipartite-temporal-correspondence.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
