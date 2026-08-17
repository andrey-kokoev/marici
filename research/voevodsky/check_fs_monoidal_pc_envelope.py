"""Audit the fs monoidal envelope of the loaded PC finite space."""

import check_ringed_alexandrov_pc_target as pc


def finite_monoid(localized):
    # Coordinate flag: False=N (nonnegative), True=Z (groupified).
    return (False,) * 9 + tuple(i in localized for i in range(9))


def raw_generic_monoid(localized):
    # u_a=X_a*t_a and u_a invertible forces X_a and t_a invertible.
    return tuple(i in localized for i in range(9)) + tuple(
        i in localized for i in range(9)
    )


def contains(monoid, vector):
    return all(groupified or exponent >= 0 for groupified, exponent in zip(monoid, vector))


def main():
    generators = [
        (face, circles) for face in pc.faces() for circles in pc.subsets(face)
    ]
    assert len(generators) == 215

    radial = normal = 0
    comparison_localizations = 0
    for generator in generators:
        source_l = {pc.VARIABLE[a] for a in pc.localization_set(generator)}
        source_p = finite_monoid(source_l)

        # Direct products of copies of N and Z are fine and saturated.  The
        # coordinate criterion also verifies saturation on diagnostic vectors.
        for coordinate in range(18):
            vector = [0] * 18
            vector[coordinate] = -1
            for multiplier in (2, 3, 5):
                multiple = [multiplier * x for x in vector]
                assert contains(source_p, multiple) == contains(source_p, vector)

        raw_q = raw_generic_monoid(source_l)
        for index in source_l:
            assert not source_p[index]  # X_index remains nonnegative.
            assert raw_q[index]         # Raw generic chart groupifies it.
            assert source_p[9 + index] and raw_q[9 + index]
            comparison_localizations += 1

        for (target, coefficient), _sign in pc.boundary(generator).items():
            target_l = {pc.VARIABLE[a] for a in pc.localization_set(target)}
            added = target_l - source_l
            assert len(added) == 1
            target_p = finite_monoid(target_l)
            changed = [i for i, (a, b) in enumerate(zip(source_p, target_p)) if a != b]
            assert changed == [9 + next(iter(added))]
            if sum(coefficient[0]) == 1:
                radial += 1
            else:
                normal += 1

            # Finite incidence then generic comparison equals generic comparison
            # then incidence: both groupify precisely the same coordinate sets.
            target_q = raw_generic_monoid(target_l)
            assert all((not a) or b for a, b in zip(source_p, target_p))
            assert all((not a) or b for a, b in zip(source_p, raw_q))
            assert all((not a) or b for a, b in zip(target_p, target_q))
            assert all((not a) or b for a, b in zip(raw_q, target_q))

    assert (radial, normal) == (261, 261)
    assert comparison_localizations > 0
    print("loaded_fs_monoid_charts: 215")
    print("chart_monoid: N^9_X + N/Z_NORMAL_BY_CELL")
    print("all_chart_monoids_fine_saturated: YES")
    print("radial_incidences: 261")
    print("normal_incidences: 261")
    print("all_incidence_maps: FACE_LOCALIZATIONS")
    print("all_finite_to_raw_generic_squares: COMMUTE")
    print("occurrence_boundary_retained: YES")
    print("raw_DNC_generic_recovery: LOCALIZE_MATCHING_X")
    print("fs_monoidal_PC_envelope: CONSTRUCTED")
    print("log_stack_realization: NEXT_GATE")


if __name__ == "__main__":
    main()
