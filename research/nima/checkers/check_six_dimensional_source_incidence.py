from itertools import permutations
import json
from pathlib import Path


POINTS = tuple(range(6))
LEFT = frozenset(range(3))
RIGHT = frozenset(range(3, 6))
PAIRS = frozenset(frozenset((i, i + 3)) for i in range(3))


def image_set(perm, values):
    return frozenset(perm[i] for i in values)


def image_pairs(perm):
    return frozenset(frozenset((perm[i], perm[i + 3])) for i in range(3))


all_perms = list(permutations(POINTS))
matching = [p for p in all_perms if image_pairs(p) == PAIRS]
unordered_summands = [
    p
    for p in matching
    if {image_set(p, LEFT), image_set(p, RIGHT)} == {LEFT, RIGHT}
]
ordered_summands = [
    p for p in matching if image_set(p, LEFT) == LEFT and image_set(p, RIGHT) == RIGHT
]

assert len(all_perms) == 720
assert len(matching) == 48
assert len(unordered_summands) == 12
assert len(ordered_summands) == 6

identity = POINTS
nontrivial = next(p for p in ordered_summands if p != identity)
assert image_pairs(nontrivial) == PAIRS
assert image_set(nontrivial, LEFT) == LEFT

result = {
    "schema": "marici.nima.six-dimensional-source-incidence.v1",
    "verdict": "dual typing reduces but does not resolve source incidence",
    "counts": {
        "untyped": len(all_perms),
        "perfect_matching_only": len(matching),
        "matching_with_unordered_summands": len(unordered_summands),
        "matching_with_ordered_summands": len(ordered_summands),
    },
    "finite_falsifier": list(nontrivial),
}

out = Path(__file__).parents[1] / "results" / "six-dimensional-source-incidence.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
