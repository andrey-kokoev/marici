from itertools import product
import json
from pathlib import Path


def distances(charges):
    return tuple(tuple(abs(charges[i] - charges[j]) for j in range(3)) for i in range(3))


target = (3, 2, 0)
target_distances = distances(target)

solutions = tuple(
    charges
    for charges in product(range(-6, 7), repeat=3)
    if distances(charges) == target_distances
)

assert len(solutions) > 2

# Quotient only translations by fixing the third labelled charge to zero.
translation_normal_forms = {
    tuple(charge - charges[2] for charge in charges)
    for charges in solutions
}
assert translation_normal_forms == {(3, 2, 0), (-3, -2, 0)}

# A nonnegative presentation still leaves the reflected labelled solution.
nonnegative_normal_forms = {
    tuple(charge - min(charges) for charge in charges)
    for charges in solutions
}
assert nonnegative_normal_forms == {(3, 2, 0), (0, 1, 3)}

# An independently supplied signed affine constraint can select one lift. This
# is an illustrative gate, not an asserted anomaly equation.
signed_constraint_value = 5
selected = tuple(charges for charges in solutions if sum(charges) == signed_constraint_value)
assert selected == ((3, 2, 0),)

# Translation changes the signed affine observer while preserving hierarchy.
shifted = tuple(charge + 1 for charge in target)
assert distances(shifted) == target_distances
assert sum(shifted) != sum(target)

# Reflection changes orientation while preserving hierarchy.
reflected = tuple(-charge for charge in target)
assert distances(reflected) == target_distances
assert reflected != target

result = {
    "schema": "marici.nima.flavor-charge-affine-torsor.v1",
    "bounded_integer_solutions": len(solutions),
    "translation_quotient_classes": len(translation_normal_forms),
    "nonnegative_presentations": [list(x) for x in sorted(nonnegative_normal_forms)],
    "hierarchy_preserves_translation": True,
    "hierarchy_preserves_reflection": True,
    "illustrative_signed_affine_constraint": signed_constraint_value,
    "selected_lifts_under_constraint": len(selected),
    "target_selected": selected == (target,),
    "verdict": (
        "The hierarchy exponent matrix determines the labelled charge triple "
        "only up to affine isometries of the charge line. A later independently "
        "derived signed affine constraint can select a lift; hierarchy data "
        "alone cannot derive the absolute charge vector."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-charge-affine-torsor.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
