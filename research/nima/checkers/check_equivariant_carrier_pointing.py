import json
from pathlib import Path


ORDER = 4


def rotate(pair, group_element):
    x, y = pair
    return ((x + group_element) % ORDER, (y + group_element) % ORDER)


def relative(pair):
    x, y = pair
    return (x - y) % ORDER


pairs = [(x, y) for x in range(ORDER) for y in range(ORDER)]

for pair in pairs:
    for group_element in range(ORDER):
        assert relative(rotate(pair, group_element)) == relative(pair)

# Relative value classifies diagonal orbits exactly.
for left in pairs:
    for right in pairs:
        same_relative = relative(left) == relative(right)
        same_orbit = any(rotate(left, g) == right for g in range(ORDER))
        assert same_relative == same_orbit

# Absolute target coordinates vary inside every diagonal orbit.
absolute_ambiguity = {}
for value in range(ORDER):
    orbit = [rotate((value, 0), g) for g in range(ORDER)]
    targets = sorted({x for x, _ in orbit})
    assert targets == list(range(ORDER))
    absolute_ambiguity[str(value)] = targets

# A prepared reference basepoint y=0 makes relative phase equal target phase.
prepared = [(x, 0) for x in range(ORDER)]
assert all(relative(pair) == pair[0] for pair in prepared)

result = {
    "schema": "marici.equivariant-carrier-pointing.v1",
    "group": "C4",
    "pair_count": len(pairs),
    "diagonal_orbit_count": ORDER,
    "relative_coordinate_complete": True,
    "absolute_target_ambiguous_without_pointing": True,
    "absolute_ambiguity": absolute_ambiguity,
    "prepared_basepoint_recovers_target": True,
    "verdict": "equivariant transport needs a source pointing or yields only a relative coordinate",
}

output = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "equivariant-carrier-pointing.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
