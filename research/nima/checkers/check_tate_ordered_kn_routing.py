"""Exact candidate routing from full-log cone rows to literal KN/Tor rows.

The construction uses only the cyclic axis order, the remaining-ray sheet,
Entry 210's moving-then-persistent order, and Entry 328's augmented KN wall.
"""

from itertools import combinations, product
import json


AXES = (0, 1, 2)


def cyclic_order(pair: tuple[int, int]) -> tuple[int, int]:
    """Orient an unordered pair in the positive 0->1->2->0 direction."""
    a, b = pair
    return (a, b) if (a + 1) % 3 == b else (b, a)


def route(signs: tuple[int, int, int], pair: tuple[int, int]):
    road = next(axis for axis in AXES if axis not in pair)
    positive = signs[road] == 1
    ordered = cyclic_order(pair)
    if not positive:
        ordered = ordered[::-1]
    moving, persistent = ordered
    # Entry 324's forced axis dictionary sends the conductor-Tor axis tau to
    # the persistent corridor label and the chart-normal axes to the moving
    # labels.  Hence the earlier intuitive assignment must be reversed.
    boolean_extra = int(signs[moving] == -1)
    tor = int(signs[persistent] == -1)
    return road, positive, boolean_extra, tor


def rotate_signs(signs):
    return signs[2], signs[0], signs[1]


def rotate_pair(pair):
    return tuple(sorted(((pair[0] + 1) % 3, (pair[1] + 1) % 3)))


def reflect_signs(signs):
    return -signs[0], -signs[2], -signs[1]


def reflect_pair(pair):
    permutation = (0, 2, 1)
    return tuple(sorted((permutation[pair[0]], permutation[pair[1]])))


def main() -> None:
    rows = [
        (signs, pair)
        for signs in product((1, -1), repeat=3)
        for pair in combinations(AXES, 2)
    ]
    images = {route(signs, pair) for signs, pair in rows}
    expected = set(product(AXES, (False, True), (0, 1), (0, 1)))
    assert len(rows) == len(images) == len(expected) == 24
    assert images == expected

    # Rotation is literal on roads and preserves all three decorations.
    for signs, pair in rows:
        road, half, boolean_extra, tor = route(signs, pair)
        assert route(rotate_signs(signs), rotate_pair(pair)) == (
            (road + 1) % 3,
            half,
            boolean_extra,
            tor,
        )

    # Reflection is computed rather than assumed.  It fixes road 0, swaps
    # roads 1/2, reverses the half, and complements both square coordinates.
    road_reflection = (0, 2, 1)
    for signs, pair in rows:
        road, half, boolean_extra, tor = route(signs, pair)
        assert route(reflect_signs(signs), reflect_pair(pair)) == (
            road_reflection[road],
            not half,
            1 - boolean_extra,
            1 - tor,
        )

    print(json.dumps({
        "status": "proved_scoped_cyclic_ordered_KN_routing",
        "source_rows": 24,
        "target_rows": 24,
        "bijection": True,
        "routing": {
            "remaining_ray_sign": "corridor_half",
            "first_cyclic_contracted_sign": "moving_chart_normal_Boolean_extra",
            "second_cyclic_contracted_sign": "persistent_tau_Tor",
        },
        "rotation_exact": True,
        "internally_induced_reflection": {
            "road_permutation": [0, 2, 1],
            "half_complemented": True,
            "boolean_extra_complemented": True,
            "tor_complemented": True,
        },
        "scope_boundary": (
            "This proves a labelled bijection and cyclic transport.  The "
            "induced reflection law is not yet compared with the independently "
            "frozen literal short-facet incidence; that comparison fails in "
            "the separate decorated-facet checker."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
