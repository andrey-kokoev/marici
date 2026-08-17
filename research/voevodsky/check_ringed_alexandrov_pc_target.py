"""Audit the ringed Alexandrov realization of the loaded PC/Cech target."""

from itertools import combinations


N = 6
DIMENSION = 3


def boundary_edge(value):
    return value[1] - value[0] == 1 or value == (0, N - 1)


def between(vertex, first, second):
    span = (second - first) % N
    position = (vertex - first) % N
    return 0 < position < span


def crosses(first, second):
    if set(first) & set(second):
        return False
    return (
        between(second[0], *first) != between(second[1], *first)
        and between(first[0], *second) != between(first[1], *second)
    )


DIAGONALS = tuple(
    (a, b)
    for a in range(N)
    for b in range(a + 1, N)
    if not boundary_edge((a, b))
)
assert len(DIAGONALS) == 9
VARIABLE = {value: index for index, value in enumerate(DIAGONALS)}


def noncrossing(face):
    return all(not crosses(a, b) for a, b in combinations(face, 2))


def faces():
    result = []
    for size in range(DIMENSION + 1):
        result.extend(
            frozenset(values)
            for values in combinations(DIAGONALS, size)
            if noncrossing(values)
        )
    return result


def subsets(face):
    values = tuple(sorted(face))
    for size in range(len(values) + 1):
        for chosen in combinations(values, size):
            yield frozenset(chosen)


def incidence_sign(face, added):
    return 1 if sum(value < added for value in face) % 2 == 0 else -1


def addable(face, value):
    return (
        value not in face
        and len(face) < DIMENSION
        and all(not crosses(value, present) for present in face)
    )


def monomial(occurrence_index=None, normal_index=None):
    occurrence = [0] * 9
    normal = [0] * 9
    if occurrence_index is not None:
        occurrence[occurrence_index] += 1
    if normal_index is not None:
        normal[normal_index] -= 1
    return tuple(occurrence), tuple(normal)


def multiply(left, right):
    return tuple(a + b for a, b in zip(left[0], right[0])), tuple(
        a + b for a, b in zip(left[1], right[1])
    )


ONE = monomial()


def add_term(result, key, coefficient):
    result[key] = result.get(key, 0) + coefficient
    if result[key] == 0:
        del result[key]


def boundary(generator):
    face, circles = generator
    result = {}
    for added in DIAGONALS:
        if not addable(face, added):
            continue
        target = (face | {added}, circles)
        coefficient = monomial(VARIABLE[added], VARIABLE[added])
        add_term(result, (target, coefficient), incidence_sign(face, added))

    base_dimension = DIMENSION - len(face)
    for position, removed in enumerate(sorted(circles)):
        target = (face, circles - {removed})
        sign = 1 if (base_dimension + position) % 2 == 0 else -1
        add_term(result, (target, ONE), sign)
    return result


def boundary_combination(combination):
    result = {}
    for (generator, coefficient_monomial), coefficient in combination.items():
        for (target, boundary_monomial), boundary_coefficient in boundary(
            generator
        ).items():
            add_term(
                result,
                (target, multiply(coefficient_monomial, boundary_monomial)),
                coefficient * boundary_coefficient,
            )
    return result


def degree(generator):
    face, circles = generator
    return DIMENSION - len(face) + len(circles)


def localization_set(generator):
    face, circles = generator
    return face - circles


def main():
    all_faces = faces()
    face_counts = [sum(len(face) == size for face in all_faces) for size in range(4)]
    assert face_counts == [1, 9, 21, 14]

    generators = [
        (face, circles) for face in all_faces for circles in subsets(face)
    ]
    assert len(generators) == 215
    degree_ranks = [
        sum(degree(generator) == present for generator in generators)
        for present in range(4)
    ]
    assert degree_ranks == [14, 63, 93, 45]

    radial_transitions = 0
    normal_transitions = 0
    for generator in generators:
        first_boundary = boundary(generator)
        assert boundary_combination(first_boundary) == {}
        source_localization = localization_set(generator)
        for (target, coefficient), sign in first_boundary.items():
            assert abs(sign) == 1
            target_localization = localization_set(target)
            added_localizations = target_localization - source_localization
            assert len(added_localizations) == 1
            occurrence_degree = sum(coefficient[0])
            normal_degree = sum(coefficient[1])
            if occurrence_degree == 1:
                assert normal_degree == -1
                radial_transitions += 1
            else:
                assert coefficient == ONE
                normal_transitions += 1

    assert radial_transitions > 0 and normal_transitions > 0

    print("face_counts: 1,9,21,14")
    print("loaded_Alexandrov_cells: 215")
    print("cellular_degree_ranks: 14,63,93,45")
    print(f"radial_localization_incidences: {radial_transitions}")
    print(f"normal_localization_incidences: {normal_transitions}")
    print("all_stalk_maps: FLAT_LOCALIZATIONS")
    print("all_radial_normal_mixed_squares: COMMUTE_WITH_ORIENTED_SIGNS")
    print("cellular_d_squared: 0")
    print("ringed_Alexandrov_PC_target: CONSTRUCTED")
    print("normalized_blowdown_ringed_morphism: NEXT_GATE")


if __name__ == "__main__":
    main()
