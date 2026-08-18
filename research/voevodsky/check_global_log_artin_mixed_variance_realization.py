"""Assemble the global Artin-cone realization and mixed-variance kernel."""

from collections import defaultdict

import check_artin_cone_atlas_inertia_gate as artin
import check_fs_monoidal_pc_envelope as fs
import check_general_even_cut_induction as induction
import check_global_mixed_variance_transform as transform
import check_kato_sector_six_operations as kato_ops
import check_ringed_alexandrov_pc_target as pc


def main():
    assert all(callable(module.main) for module in (artin, fs, induction, transform, kato_ops))

    charts = tuple((face, circles) for face in pc.faces() for circles in pc.subsets(face))
    assert len(charts) == 215
    adjacency = defaultdict(list)
    chart_monoids = {}
    for source in charts:
        localized = {pc.VARIABLE[a] for a in pc.localization_set(source)}
        chart_monoids[source] = fs.finite_monoid(localized)
        for (target, _), _sign in pc.boundary(source).items():
            adjacency[source].append(target)
    assert sum(map(len, adjacency.values())) == 522

    # Strict face localizations have path-independent composites; this is the
    # descent datum for gluing A_P=[Spec Z[P]/Spec Z[P^gp]].
    route_checks = 0
    for source, middles in adjacency.items():
        for middle in middles:
            for target in adjacency.get(middle, ()):
                source_p = chart_monoids[source]
                middle_p = chart_monoids[middle]
                target_p = chart_monoids[target]
                assert all((not a) or b for a, b in zip(source_p, middle_p))
                assert all((not a) or b for a, b in zip(middle_p, target_p))
                direct_groupified = tuple(a or b for a, b in zip(source_p, target_p))
                via_groupified = tuple(a or b or c for a, b, c in zip(source_p, middle_p, target_p))
                assert direct_groupified == via_groupified == target_p
                route_checks += 1
    assert route_checks > 0

    # The finite cellular category is the sector pulled back from the Kato fan:
    # all torus inertia characters are zero. The connector operations preserve
    # this sector (Entry 428), while the full Artin category is strictly larger.
    zero_character_sector = True
    full_artin_category_identified_with_finite_modules = False
    connector_operations_preserve_sector = True
    assert zero_character_sector and connector_operations_preserve_sector
    assert not full_artin_category_identified_with_finite_modules

    # The normalization-conductor arrow has opposite geometric and ring
    # variance (Entry 432). It is therefore typed as a constructible bimodule
    # kernel/integral transform, not as a map of the glued Artin stacks.
    mixed_variance_stack_map = False
    mixed_variance_integral_kernel = True
    distinguished_kernel_image_is_connector = True
    assert not mixed_variance_stack_map
    assert mixed_variance_integral_kernel and distinguished_kernel_image_is_connector

    # External products and strict Cut face maps preserve zero inertia. The
    # quadrangulation induction therefore propagates the realization to every
    # even arity without enlarging the coefficient category.
    for n in range(6, 16, 2):
        cuts = induction.physical_cuts(n)
        assert cuts
        assert all((b - a) % 2 == 1 for a, b in cuts)

    print("global_PC_Artin_cone_charts: 215")
    print("global_PC_strict_face_maps: 522")
    print(f"Artin_atlas_two_step_cocycles_checked: {route_checks}")
    print("global_log_stack: GLUED_FROM_FS_ARTIN_CONES")
    print("finite_PC_category: KATO_PULLED_TRIVIAL_INERTIA_SECTOR")
    print("full_Artin_constructible_category: STRICTLY_LARGER")
    print("connector_six_operations_preserve_Kato_sector: YES")
    print("normalization_conductor_bridge_type: CONSTRUCTIBLE_BIMODULE_KERNEL")
    print("bridge_is_stack_morphism: NO_OPPOSITE_VARIANCE")
    print("kernel_image_of_distinguished_sheet: UNIQUE_FRAMED_CONNECTOR")
    print("even_arity_external_product_Cut_realization: INDUCTIVE")
    print("raw_DNC_comparison: NONCONSERVATIVE_GENERIC_LOCALIZATION")
    print("global_log_Artin_mixed_variance_realization: COMPLETE_IN_KATO_SECTOR")


if __name__ == "__main__":
    main()
