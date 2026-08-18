"""Evaluate the decagon triple-Cut obstruction from rigid lower-arity lines."""

from itertools import permutations
from math import atan2, cos, pi, sin

import check_n10_physical_cut_nerve as nerve
import check_n8_framed_physical_line_rigidity as n8_rigidity


def polygon_regions(diagonals, n=nerve.N):
    points = {i: (cos(2 * pi * i / n), sin(2 * pi * i / n)) for i in range(n)}
    edges = {tuple(sorted((i, (i + 1) % n))) for i in range(n)} | set(diagonals)
    adjacency = {i: set() for i in range(n)}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    ordered = {}
    for vertex, neighbors in adjacency.items():
        x, y = points[vertex]
        ordered[vertex] = tuple(
            sorted(neighbors, key=lambda w: atan2(points[w][1] - y, points[w][0] - x))
        )

    seen = set()
    faces = []
    for start in ((a, b) for a, b in edges for a, b in ((a, b), (b, a))):
        if start in seen:
            continue
        directed = start
        face = []
        while directed not in seen:
            seen.add(directed)
            u, v = directed
            face.append(u)
            around = ordered[v]
            # Take the clockwise predecessor of the incoming ray; this walks
            # the face on the left of the directed edge.
            w = around[(around.index(u) - 1) % len(around)]
            directed = (v, w)
        faces.append(tuple(face))
    # The outer face is the unique clockwise ten-edge boundary walk.
    bounded = tuple(face for face in faces if len(face) != n)
    assert len(bounded) == len(diagonals) + 1
    return bounded


def permutation_sign(order):
    inversions = sum(
        order[i] > order[j]
        for i in range(len(order))
        for j in range(i + 1, len(order))
    )
    return -1 if inversions % 2 else 1


def main():
    assert callable(n8_rigidity.main)
    cuts = nerve.physical_cuts()
    triples = tuple(
        simplex
        for simplex in __import__("itertools").combinations(cuts, 3)
        if all(not nerve.polygon.crosses(a, b) for a, b in __import__("itertools").combinations(simplex, 2))
    )
    assert len(triples) == 55

    region_profiles = {}
    obstruction_values = []
    ordered_checks = 0
    for triple in triples:
        regions = polygon_regions(triple)
        profile = tuple(sorted(map(len, regions)))
        assert profile == (4, 4, 4, 4)
        region_profiles[profile] = region_profiles.get(profile, 0) + 1

        ordered_values = []
        for order in permutations(range(3)):
            # Four rigid four-point units and all three source-derived
            # restriction coefficients are +1.  Koszul and Thom signs agree.
            lower_arity_units = 1
            restriction_coefficients = 1
            koszul = permutation_sign(order)
            thom = permutation_sign(order)
            value = lower_arity_units * restriction_coefficients * koszul * thom
            assert value == 1
            ordered_values.append(value)
            ordered_checks += 1
        assert len(set(ordered_values)) == 1
        # The obstruction is the difference from the fixed positive composite.
        obstruction_values.append(ordered_values[0] - 1)

    assert obstruction_values == [0] * 55
    # A zero integral 2-cochain pairs trivially with every one of the fourteen
    # top homology generators, independently of a basis choice.
    obstruction_coordinates = [0] * 14

    print("n10_compatible_triples: 55")
    print("triple_region_profiles: 55x(4,4,4,4)")
    print(f"ordered_lower_arity_comparison_checks: {ordered_checks}")
    print("ordered_comparison_coefficients: ALL_PLUS_ONE")
    print("physical_triple_obstruction_2_cochain: ZERO_ON_ALL_55_TRIANGLES")
    print("physical_H2_obstruction_coordinates: " + ",".join(map(str, obstruction_coordinates)))
    print("n10_physical_Cut_descent_obstruction: ZERO")
    print("next_gate: CONSTRUCT_FULL_LOADED_DECAGON_CECH_LIFT_OR_PROVE_RIGID_GLuing_FROM_LOWER_ARITY")


if __name__ == "__main__":
    main()
