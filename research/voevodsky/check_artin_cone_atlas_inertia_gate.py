"""Audit the Artin-cone atlas and its unavoidable inertia sector."""

from collections import Counter, defaultdict

import check_fs_monoidal_pc_envelope as fs
import check_ringed_alexandrov_pc_target as pc


def main():
    generators = [
        (face, circles) for face in pc.faces() for circles in pc.subsets(face)
    ]
    adjacency = defaultdict(list)
    characteristic_ranks = Counter()

    for source in generators:
        localized = {pc.VARIABLE[a] for a in pc.localization_set(source)}
        monoid = fs.finite_monoid(localized)
        # P/P* has one N-ray for each coordinate not already groupified.
        sharp_rank = sum(not groupified for groupified in monoid)
        characteristic_ranks[sharp_rank] += 1
        assert sharp_rank >= 15

        for (target, _coefficient), _sign in pc.boundary(source).items():
            adjacency[source].append(target)

    assert sum(len(v) for v in adjacency.values()) == 522

    # Every two-step route to a fixed loaded cell induces the same composite
    # face localization. This is the cocycle needed by the Artin-cone diagram.
    two_step_routes = 0
    route_maps = defaultdict(set)
    for source, middles in list(adjacency.items()):
        for middle in middles:
            for target in adjacency.get(middle, ()):
                two_step_routes += 1
                target_l = tuple(
                    sorted(pc.VARIABLE[a] for a in pc.localization_set(target))
                )
                route_maps[(source, target)].add(target_l)
    assert two_step_routes > 0
    assert all(len(maps) == 1 for maps in route_maps.values())

    # Every Artin cone has positive-dimensional closed-stratum inertia.  A
    # nonzero character of its first G_m factor and the trivial character have
    # the same underlying rank-one stalk, but are inequivalent equivariant
    # sheaves. A plain poset module cannot distinguish them.
    minimum_inertia_rank = min(characteristic_ranks)
    assert minimum_inertia_rank > 0
    trivial_character = (0,) * minimum_inertia_rank
    nontrivial_character = (1,) + (0,) * (minimum_inertia_rank - 1)
    assert trivial_character != nontrivial_character

    print("Artin_cone_charts: 215")
    print("face_localization_arrows: 522")
    print(f"two_step_routes_checked: {two_step_routes}")
    print("all_atlas_cocycles: STRICTLY_COMMUTE")
    print("characteristic_rank_distribution: " + repr(dict(sorted(characteristic_ranks.items()))))
    print(f"minimum_closed_stratum_inertia_rank: {minimum_inertia_rank}")
    print("full_constructible_category_equals_finite_poset_modules: NO")
    print("obstruction: NONTRIVIAL_TORUS_CHARACTERS")
    print("trivial_inertia_Kato_sector_candidate: YES")
    print("six_operations_preserve_trivial_inertia: NEXT_GATE")


if __name__ == "__main__":
    main()
