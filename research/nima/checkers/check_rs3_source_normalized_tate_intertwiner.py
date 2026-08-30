"""Exact source-normalized D3 intertwiner into the mod-three Tate line."""

import json
from pathlib import Path

P = 3


def add(a, b):
    return tuple((x + y) % P for x, y in zip(a, b))


def sub(a, b):
    return tuple((x - y) % P for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x % P for x in a)


def g(a):
    """Left multiplication by g in the basis (1,g,g^2)."""
    return (a[2], a[0], a[1])


def r(a):
    """D3 reflection g -> g^{-1}."""
    return (a[0], a[2], a[1])


one = (1, 0, 0)
g1 = (0, 1, 0)
g2 = (0, 0, 1)
t = sub(g1, one)
t2 = sub(g(t), t)  # (g-1)t
oriented_difference = sub(g1, g2)

# I=ker(epsilon) has basis t,t^2 and (g-1)I=<t^2>.
assert sum(t) % P == 0
assert sum(t2) % P == 0
assert t2 != (0, 0, 0)
assert oriented_difference != (0, 0, 0)

# In I/(g-1)I, g-g^{-1} is -t and is therefore nonzero.
assert add(oriented_difference, t) == scale(2, t2)

# Reflection reverses the oriented source difference.
assert r(oriented_difference) == scale(-1, oriented_difference)

# Rotation acts trivially on the quotient: g*x-x lies in <t^2>.
rotation_defect = sub(g(oriented_difference), oriented_difference)
assert rotation_defect in {scale(c, t2) for c in range(P)}

# Negative controls: the even sum has the wrong reflection character and the
# unoriented augmentation has no class in I.
even_pair = add(g1, g2)
assert r(even_pair) == even_pair
assert sum(even_pair) % P != 0

result = {
    "schema": "marici.rs3.source-normalized-tate-intertwiner.v1",
    "field": "F3",
    "source_module": "F3[C3]",
    "target": "I/(g-1)I",
    "map": "d(X2-X3) -> [g-g^{-1}]",
    "oriented_difference": list(oriented_difference),
    "class_relation": "(g-g^{-1}) + (g-1) = 2(g-1)^2",
    "rotation_character": 1,
    "reflection_character": -1,
    "target_dimension": 1,
    "negative_controls": {
        "even_pair_reflection_character": 1,
        "even_pair_not_in_augmentation_ideal": True,
    },
    "verdict": (
        "The source-labelled orientation canonically normalizes the unique D3 "
        "intertwiner from the unequal-energy cotangent line to the Tate quotient. "
        "Ordinary augmentation still kills its target class."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs3-source-normalized-tate-intertwiner.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
