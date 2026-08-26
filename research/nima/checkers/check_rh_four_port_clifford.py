#!/usr/bin/env python3
"""Exact blade-action audit for the four-port Clifford formulation."""

import json
from pathlib import Path


# Basis order: tail left, tail right, seam value, seam flux.
# Reciprocal sewing swaps the tail basis and reverses seam flux.
images = {
    0: (1, 1),
    1: (1, 0),
    2: (1, 2),
    3: (-1, 3),
}


def blade_image(indices):
    coefficient = 1
    image_indices = []
    for index in indices:
        sign, image = images[index]
        coefficient *= sign
        image_indices.append(image)
    inversions = sum(
        image_indices[i] > image_indices[j]
        for i in range(len(image_indices))
        for j in range(i + 1, len(image_indices))
    )
    coefficient *= (-1) ** inversions
    return coefficient, tuple(sorted(image_indices))


tail_bivector = blade_image((0, 1))
seam_bivector = blade_image((2, 3))
total_pseudoscalar = blade_image((0, 1, 2, 3))

assert tail_bivector == (-1, (0, 1))
assert seam_bivector == (-1, (2, 3))
assert total_pseudoscalar == (1, (0, 1, 2, 3))

# Omitting seam flux leaves a three-dimensional volume element whose sign flips.
three_port_volume = blade_image((0, 1, 2))
assert three_port_volume == (-1, (0, 1, 2))

result = {
    "tail_bivector_character": tail_bivector[0],
    "seam_bivector_character": seam_bivector[0],
    "four_port_pseudoscalar_character": total_pseudoscalar[0],
    "three_port_volume_character": three_port_volume[0],
    "verdict": (
        "reciprocal sewing reverses both oriented two-planes but preserves the four-port "
        "pseudoscalar; omitting seam flux leaves an unmatched orientation reversal"
    ),
}

output = Path(__file__).parents[1] / "results" / "rh-four-port-clifford.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
