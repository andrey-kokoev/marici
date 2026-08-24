"""Identify F_3[C_3] with the depth-two jet algebra and its residue grades."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


P = 3


def add(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((x + y) % P for x, y in zip(a, b))  # type: ignore[return-value]


def scale(c: int, a: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((c * x) % P for x in a)  # type: ignore[return-value]


def group_multiply(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[(i + j) % 3] = (out[(i + j) % 3] + left * right) % P
    return tuple(out)  # type: ignore[return-value]


def jet_multiply(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            if i + j < 3:
                out[i + j] = (out[i + j] + left * right) % P
    return tuple(out)  # type: ignore[return-value]


def to_jet(group_coordinates: tuple[int, int, int]) -> tuple[int, int, int]:
    """Substitute g=1+t in a0+a1*g+a2*g^2."""
    a0, a1, a2 = group_coordinates
    return ((a0 + a1 + a2) % P, (a1 + 2 * a2) % P, a2 % P)


def main() -> None:
    ambient = list(product(range(P), repeat=3))
    for left in ambient:
        for right in ambient:
            assert to_jet(group_multiply(left, right)) == jet_multiply(
                to_jet(left), to_jet(right)
            )

    one = (1, 0, 0)
    g = (0, 1, 0)
    g2 = group_multiply(g, g)
    t = add(g, scale(-1, one))
    t2 = group_multiply(t, t)
    t3 = group_multiply(t2, t)
    norm = add(add(one, g), g2)

    assert to_jet(t) == (0, 1, 0)
    assert to_jet(t2) == (0, 0, 1)
    assert t3 == (0, 0, 0)
    assert norm == t2

    augmentation_ideal = {value for value in ambient if to_jet(value)[0] == 0}
    ideal_square = {
        group_multiply(left, right)
        for left in augmentation_ideal
        for right in augmentation_ideal
    }
    assert len(augmentation_ideal) == 9
    assert len(ideal_square) == 3
    assert {group_multiply(value, t2) for value in augmentation_ideal} == {(0, 0, 0)}

    # Every lift of either nonzero Tate quotient class squares to the norm.
    # In jet coordinates these are a*t+b*t^2 with a in F_3^x.
    nonzero_tate_lifts = []
    for value in ambient:
        jet = to_jet(value)
        if jet[0] == 0 and jet[1] != 0:
            nonzero_tate_lifts.append(value)
            assert group_multiply(value, value) == norm
    assert len(nonzero_tate_lifts) == 6

    result = {
        "status": "PASS",
        "field": "F_3",
        "multiplication_pairs_checked": len(ambient) ** 2,
        "isomorphism": "F_3[C_3] ~= F_3[t]/(t^3), t=g-1",
        "augmentation_ideal_dimension": 2,
        "ideal_square_dimension": 1,
        "ideal_cube_dimension": 0,
        "associated_grade_dimensions": [1, 1, 1],
        "tate_grade": "I/I^2",
        "norm_identity": "1+g+g^2=t^2",
        "nonzero_tate_lifts_checked": len(nonzero_tate_lifts),
        "canonical_quadratic_map": "every nonzero class in I/I^2 squares to norm in I^2",
        "reflection_character_transition": "odd Tate grade squares to even norm grade",
        "soft_gysin_filtered_action": "identity",
        "scalar_readout": "augmentation retains A/I and kills I/I^2 and I^2",
    }

    output = Path(__file__).parents[1] / "results" / "c3-occurrence-is-depth-two-jet.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
