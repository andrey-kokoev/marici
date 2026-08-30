"""Exact D3-set audit for the global eight-cone/literal-row comparison.

This intentionally forgets occurrence monomials and stalk maps.  It tests
whether cardinality plus D3 covariance alone can identify the two certified
24-element row sets.  A positive uniqueness result here would authorize a
symmetry-derived assignment; failure proves that actual conductor-stalk
maps are indispensable.
"""

from itertools import product
import json


Signs = tuple[int, int, int]
Pair = tuple[int, int]


def sorted_pair(a: int, b: int) -> Pair:
    return (a, b) if a < b else (b, a)


def rotate_signs(s: Signs) -> Signs:
    return (s[2], s[0], s[1])


def reflect_signs(s: Signs) -> Signs:
    return (-s[0], -s[2], -s[1])


def rotate_pair(p: Pair) -> Pair:
    return sorted_pair((p[0] + 1) % 3, (p[1] + 1) % 3)


def reflect_axis(a: int) -> int:
    return (0, 2, 1)[a]


def reflect_pair(p: Pair) -> Pair:
    return sorted_pair(reflect_axis(p[0]), reflect_axis(p[1]))


Source = tuple[Signs, Pair]
Target = tuple[int, int, int]  # road, sheet sign, decoration in {0,1,2,3}


SOURCE: tuple[Source, ...] = tuple(
    (s, p)
    for s in product((1, -1), repeat=3)
    for p in ((0, 1), (0, 2), (1, 2))
)
TARGET: tuple[Target, ...] = tuple(
    (road, sheet, decoration)
    for road in range(3)
    for sheet in (1, -1)
    for decoration in range(4)
)


def source_r(x: Source) -> Source:
    return (rotate_signs(x[0]), rotate_pair(x[1]))


def source_s(x: Source) -> Source:
    return (reflect_signs(x[0]), reflect_pair(x[1]))


def target_r(x: Target) -> Target:
    road, sheet, decoration = x
    return ((road + 1) % 3, sheet, decoration)


def target_s(x: Target) -> Target:
    road, sheet, decoration = x
    return ((-road) % 3, -sheet, decoration)


def compose(f, g):
    return lambda x: f(g(x))


def group_actions(r, s):
    identity = lambda x: x
    r2 = compose(r, r)
    return (identity, r, r2, s, compose(r, s), compose(r2, s))


def fixed_counts(points, actions):
    return tuple(sum(action(x) == x for x in points) for action in actions)


def orbits(points, actions):
    unseen = set(points)
    result = []
    while unseen:
        seed = min(unseen)
        orbit = {action(seed) for action in actions}
        assert len(orbit) == 6
        unseen -= orbit
        result.append(tuple(sorted(orbit)))
    return tuple(result)


def source_orbit_fingerprint(x: Source) -> str:
    signs, pair = x
    complement = next(axis for axis in range(3) if axis not in pair)
    if signs[0] == signs[1] == signs[2]:
        return "uniform"
    if signs[pair[0]] == signs[pair[1]]:
        return "pair_equal_complement_opposite"
    cyclic_first = (complement + 1) % 3
    cyclic_second = (complement + 2) % 3
    if (signs[cyclic_first], signs[cyclic_second]) == (1, -1):
        return "pair_mixed_cyclic_forward"
    assert (signs[cyclic_first], signs[cyclic_second]) == (-1, 1)
    return "pair_mixed_cyclic_backward"


def main() -> None:
    source_actions = group_actions(source_r, source_s)
    target_actions = group_actions(target_r, target_s)

    assert len(SOURCE) == len(set(SOURCE)) == 24
    assert len(TARGET) == len(set(TARGET)) == 24

    # Exact permutation characters: four copies of the regular D3 action.
    source_character = fixed_counts(SOURCE, source_actions)
    target_character = fixed_counts(TARGET, target_actions)
    assert source_character == target_character == (24, 0, 0, 0, 0, 0)

    source_orbits = orbits(SOURCE, source_actions)
    target_orbits = orbits(TARGET, target_actions)
    assert len(source_orbits) == len(target_orbits) == 4

    fingerprints = tuple(source_orbit_fingerprint(orbit[0]) for orbit in source_orbits)
    assert all(
        {source_orbit_fingerprint(point) for point in orbit} == {fingerprints[index]}
        for index, orbit in enumerate(source_orbits)
    )
    assert set(fingerprints) == {
        "uniform",
        "pair_equal_complement_opposite",
        "pair_mixed_cyclic_forward",
        "pair_mixed_cyclic_backward",
    }

    # An equivariant bijection between free G-sets with k orbits chooses a
    # permutation of the k target orbits and one image for the basepoint in
    # each target G-orbit: k! * |G|^k.
    group_order = 6
    orbit_count = 4
    equivariant_bijections = 24 * group_order**orbit_count
    assert equivariant_bijections == 31_104
    assert equivariant_bijections > 1

    packet = {
        "claim": (
            "The certified 24 source BC rows and 24 literal replacement rows "
            "have identical D3 permutation characters, each four copies of "
            "the regular representation, but D3 covariance and cardinality "
            "leave 31,104 equivariant bijections."
        ),
        "status": "proved_scoped_negative_control",
        "source_character": source_character,
        "target_character": target_character,
        "source_free_orbits": len(source_orbits),
        "target_free_orbits": len(target_orbits),
        "equivariant_bijections": equivariant_bijections,
        "source_orbit_fingerprints": sorted(fingerprints),
        "consequence": (
            "The global row assignment cannot be derived from rank and D3 "
            "symmetry alone; actual normalization-conductor stalk maps must "
            "select the orbit correspondence and four within-orbit phases."
        ),
        "negative_control_scope": (
            "Occurrence monomials, normal lines, Tor typing, and Cech stalk "
            "maps are deliberately forgotten; those are precisely the data "
            "the next conductor-kernel instantiation must use.  In particular "
            "it must derive a bijection from the four source fingerprints to "
            "the four (Boolean replacement type, Tor grade) target decorations."
        ),
    }
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
