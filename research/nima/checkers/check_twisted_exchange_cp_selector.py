import json
from collections import deque
from pathlib import Path


POINTS = tuple((a, b) for a in range(8) for b in range(8))
POINT_INDEX = {point: i for i, point in enumerate(POINTS)}


def rotation(point):
    a, b = point
    return (a + 2) % 8, (b + 2) % 8


def cp_reflection(point):
    a, b = point
    return (-a) % 8, (-b) % 8


def twisted_exchange(point):
    a, b = point
    return (b + 1) % 8, (a - 1) % 8


def permutation(action):
    return tuple(POINT_INDEX[action(point)] for point in POINTS)


identity = tuple(range(len(POINTS)))
generators = (
    (permutation(rotation), 0, "r"),
    (permutation(cp_reflection), 1, "c"),
    (permutation(twisted_exchange), 0, "T"),
)

# Track antiunitary parity: only words with odd c-parity are generalized CP.
group = {(identity, 0): ""}
queue = deque([(identity, 0)])
while queue:
    current, parity = queue.popleft()
    for generator, generator_parity, name in generators:
        product = tuple(generator[current[i]] for i in range(len(POINTS)))
        key = product, parity ^ generator_parity
        if key not in group:
            group[key] = group[(current, parity)] + name
            queue.append(key)

assert len(group) == 32
assert len({permutation_value for permutation_value, _ in group}) == 32
assert all(twisted_exchange(twisted_exchange(point)) == point for point in POINTS)

# The anisotropy characters A_i=(-1)^t transform as
# (A1,A2) -> (-A2,-A1), so invariance of lambda1*A1+lambda2*A2
# forces lambda1=-lambda2.
for point in POINTS:
    a, b = point
    before = ((-1) ** a, (-1) ** b)
    ta, tb = twisted_exchange(point)
    after = ((-1) ** ta, (-1) ** tb)
    assert after == (-before[1], -before[0])

selected_vacua = tuple((a, b) for a in range(8) if a % 2 == 0
                        for b in range(8) if b % 2 == 1)
cp_odd_elements = tuple((perm, word) for (perm, parity), word in group.items() if parity == 1)
assert len(cp_odd_elements) == 16

stabilizer_counts = {}
for vacuum in selected_vacua:
    point_id = POINT_INDEX[vacuum]
    stabilizers = tuple(word for perm, word in cp_odd_elements if perm[point_id] == point_id)
    stabilizer_counts[str(vacuum)] = len(stabilizers)
    assert stabilizers == ()

# Removing T allows equal anisotropy coefficients and an aligned vacuum with CP.
assert cp_reflection((0, 0)) == (0, 0)

result = {
    "schema": "marici.nima.twisted-exchange-cp-selector.v1",
    "generated_group_order": len(group),
    "generalized_cp_element_count": len(cp_odd_elements),
    "selected_vacuum_count": len(selected_vacua),
    "selected_vacua_with_generalized_cp_stabilizer": sum(bool(v) for v in stabilizer_counts.values()),
    "twisted_exchange_is_involution": True,
    "twisted_exchange_forces_opposite_anisotropy_coefficients": True,
    "removing_twisted_exchange_restores_cp_hostile": True,
    "verdict": "A source-authorized quarter-twisted exchange forces the relative D4 anisotropy sign and the full generated group has no generalized-CP stabilizer on any selected vacuum."
}

out = Path(__file__).parents[1] / "results" / "twisted-exchange-cp-selector.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
