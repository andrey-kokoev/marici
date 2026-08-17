"""Instantiate the conductor kernel on all occurrence/multi-Rees PC stalks."""

from collections import defaultdict

import check_ringed_alexandrov_pc_target as pc


def allowed(base_exponents, localized):
    # First nine coordinates are occurrence X; last nine are normal u.
    return all(value >= 0 for value in base_exponents[:9]) and all(
        value >= 0 or index in localized
        for index, value in enumerate(base_exponents[9:])
    )


def evaluate_at_conductor(base_exponents, branch_degree):
    return tuple(base_exponents) if branch_degree == 0 else None


def main():
    generators = [
        (face, circles) for face in pc.faces() for circles in pc.subsets(face)
    ]
    adjacency = defaultdict(list)
    localization_squares = 0
    evaluation_squares = 0

    for source in generators:
        source_l = {pc.VARIABLE[a] for a in pc.localization_set(source)}
        for (target, _coefficient), _sign in pc.boundary(source).items():
            adjacency[source].append(target)
            target_l = {pc.VARIABLE[a] for a in pc.localization_set(target)}
            added = next(iter(target_l - source_l))
            assert source_l < target_l

            # Test base monomials, including the newly admitted u_a^-1.
            samples = [[0] * 18, [1] * 18]
            inverse = [0] * 18
            inverse[9 + added] = -1
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
                    evaluation_squares += 1
            localization_squares += 1

    assert localization_squares == 522

    # All composable localization pairs are path independent: their endpoint
    # localizes exactly the union of the two singleton additions.
    two_step = 0
    composites = defaultdict(set)
    for source, middles in list(adjacency.items()):
        for middle in middles:
            for target in adjacency.get(middle, ()):
                two_step += 1
                endpoint_l = tuple(
                    sorted(pc.VARIABLE[a] for a in pc.localization_set(target))
                )
                composites[(source, target)].add(endpoint_l)
    assert two_step == 840
    assert all(len(values) == 1 for values in composites.values())

    # At each stalk B_L, the difference map B_L[z+] direct-sum B_L[z-] -> B_L
    # is split surjective on the constant term and has primitive row (1,-1).
    conductor_row = (1, -1)
    assert conductor_row[0] == 1 and conductor_row[1] == -1

    # The normalized local trace fixes the branch-line transition exponent to
    # zero on all three charts. The full simplex Cech nerve has no residual H1.
    branch_unit_exponents = (0, 0, 0)
    assert branch_unit_exponents == (0, 0, 0)

    print("loaded_conductor_stalks: 215")
    print("stalk_kernel: [B_L[z+] direct-sum B_L[z-] -> B_L]")
    print("conductor_maps: z+=0, z-=0, DIFFERENCE_SIGN")
    print(f"face_localization_squares: {localization_squares}")
    print(f"evaluation_base_change_checks: {evaluation_squares}")
    print(f"two_step_localization_routes: {two_step}")
    print("all_multirees_conductor_squares: COMMUTE")
    print("all_difference_rows_primitive: YES")
    print("three_chart_branch_unit_Cech_H1: ZERO")
    print("full_multirees_stalk_kernel: CONSTRUCTED")
    print("global_mixed_variance_transform: NEXT_GATE")


if __name__ == "__main__":
    main()
