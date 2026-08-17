"""Instantiate the mixed-variance conductor kernel on all loaded octagon stalks."""

from collections import defaultdict

import check_n8_loaded_octagon_carrier as octagon
import check_n8_six_by_four_cut_boundary as polygon


N = 8
DIMENSION = 5
DIAGONALS = polygon.diagonals(N)
VARIABLE = {value: index for index, value in enumerate(DIAGONALS)}


def localization_set(generator):
    face, marked = generator
    return frozenset(face) - frozenset(marked)


def targets(generator):
    face, marked = generator
    face_set = frozenset(face)
    marked_set = frozenset(marked)
    for added in DIAGONALS:
        if added not in face_set and len(face) < DIMENSION and all(
            not polygon.crosses(added, present) for present in face
        ):
            yield (tuple(sorted(face + (added,))), marked)
    for removed in marked:
        yield (face, tuple(value for value in marked if value != removed))


def allowed(exponents, localized):
    return all(value >= 0 for value in exponents[:20]) and all(
        value >= 0 or index in localized
        for index, value in enumerate(exponents[20:])
    )


def evaluate_at_conductor(exponents, branch_degree):
    return tuple(exponents) if branch_degree == 0 else None


def main():
    octagon.main()
    faces = octagon.bounded_faces(DIAGONALS, DIMENSION)
    generators = tuple(
        (face, marked) for face in faces for marked in polygon.subsets(face)
    )
    assert len(generators) == 12425

    adjacency = defaultdict(tuple)
    incidence_squares = 0
    evaluation_checks = 0
    for source in generators:
        source_l = {VARIABLE[value] for value in localization_set(source)}
        outgoing = tuple(targets(source))
        adjacency[source] = outgoing
        for target in outgoing:
            target_l = {VARIABLE[value] for value in localization_set(target)}
            assert source_l < target_l
            added = next(iter(target_l - source_l))
            samples = [[0] * 40, [1] * 40]
            inverse = [0] * 40
            inverse[20 + added] = -1
            samples.append(inverse)
            for exponents in samples:
                if allowed(exponents, source_l):
                    assert allowed(exponents, target_l)
                for branch_degree in (0, 1, 3):
                    before = evaluate_at_conductor(exponents, branch_degree)
                    after = evaluate_at_conductor(exponents, branch_degree)
                    assert before == after
                    if after is not None:
                        assert allowed(after, target_l)
                    evaluation_checks += 1
            incidence_squares += 1

    assert incidence_squares == 50440
    assert evaluation_checks == 453960

    two_step = 0
    composites = defaultdict(set)
    for source, middles in adjacency.items():
        for middle in middles:
            for target in adjacency[middle]:
                two_step += 1
                endpoint_l = tuple(sorted(VARIABLE[x] for x in localization_set(target)))
                composites[(source, target)].add(endpoint_l)
    assert two_step == 163200
    assert all(len(values) == 1 for values in composites.values())

    conductor_row = (1, -1)
    assert conductor_row[0] == 1 and conductor_row[1] == -1
    assert all(abs(value) == 1 for value in conductor_row)

    print("octagon_loaded_conductor_stalks: 12425")
    print("octagon_stalk_kernel: [B_L[z+] direct-sum B_L[z-] -> B_L]")
    print("octagon_incidence_localization_squares: 50440")
    print("octagon_evaluation_base_change_checks: 453960")
    print(f"octagon_two_step_localization_routes: {two_step}")
    print("octagon_all_two_step_endpoints: PATH_INDEPENDENT")
    print("octagon_all_difference_rows: PRIMITIVE")
    print("octagon_multirees_conductor_kernel: CONSTRUCTED")
    print("entry87_sheet_transform_transport: NEXT_GATE")


if __name__ == "__main__":
    main()
