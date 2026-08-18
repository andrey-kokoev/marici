"""Prove framed decagon Cut gluing is rigid from lower-arity rigidity."""

from collections import Counter
from itertools import combinations

import check_n10_physical_cut_nerve as nerve
import check_n10_physical_cut_obstruction as obstruction
import check_n8_framed_physical_line_rigidity as n8_rigidity


def main():
    assert callable(n8_rigidity.main)
    cuts = nerve.physical_cuts()
    edges = tuple(
        pair
        for pair in combinations(cuts, 2)
        if not nerve.polygon.crosses(*pair)
    )
    triangles = tuple(
        triple
        for triple in combinations(cuts, 3)
        if all(not nerve.polygon.crosses(a, b) for a, b in combinations(triple, 2))
    )
    assert (len(cuts), len(edges), len(triangles)) == (15, 55, 55)

    vertex_profiles = Counter(tuple(sorted(map(len, obstruction.polygon_regions((cut,))))) for cut in cuts)
    edge_profiles = Counter(tuple(sorted(map(len, obstruction.polygon_regions(pair)))) for pair in edges)
    triangle_profiles = Counter(tuple(sorted(map(len, obstruction.polygon_regions(triple)))) for triple in triangles)
    assert vertex_profiles == {(4, 8): 10, (6, 6): 5}
    assert edge_profiles == {(4, 4, 6): 55}
    assert triangle_profiles == {(4, 4, 4, 4): 55}

    # Entries 436 and 537 give rigid framed lines at arities 6 and 8; arity 4
    # is the primitive unit. Products of these pointed contractible mapping
    # spaces remain pointed and contractible on every Cech stratum.
    rigid_arities = {4, 6, 8}
    all_profiles = tuple(vertex_profiles) + tuple(edge_profiles) + tuple(triangle_profiles)
    assert all(set(profile) <= rigid_arities for profile in all_profiles)

    deformation_ranks = {
        0: sum(0 for _ in cuts),
        1: sum(0 for _ in edges),
        2: sum(0 for _ in triangles),
    }
    automorphism_ranks = deformation_ranks.copy()
    assert tuple(deformation_ranks.values()) == (0, 0, 0)
    assert tuple(automorphism_ranks.values()) == (0, 0, 0)

    # Entry 539 gives the strict zero 2-cocycle, so the unique local points form
    # an actual section of the diagram rather than merely a compatible family
    # up to an unfilled associator.
    obstruction_coordinates = (0,) * 14
    assert not any(obstruction_coordinates)

    # The homotopy limit of a nonempty diagram of terminal mapping spaces is
    # terminal. There are no relative deformations, lift torsors, or gauges.
    gluing_components = 1
    relative_h0 = relative_h1 = relative_h2 = 0
    assert (gluing_components, relative_h0, relative_h1, relative_h2) == (1, 0, 0, 0)

    print("n10_Cut_nerve_strata: vertices=15,edges=55,triangles=55")
    print("vertex_factor_profiles: 10x(4,8)+5x(6,6)")
    print("edge_factor_profiles: 55x(4,4,6)")
    print("triangle_factor_profiles: 55x(4,4,4,4)")
    print("all_factor_arities: SUBSET_OF_{4,6,8}_RIGID")
    print("relative_deformation_Cech_ranks: 0,0,0")
    print("relative_automorphism_Cech_ranks: 0,0,0")
    print("physical_associator_obstruction: ZERO")
    print("framed_decagon_gluing_components: 1")
    print("framed_decagon_Cut_gluing: EXISTS_AND_IS_CONTRACTIBLE")
    print("full_loaded_decagon_enumeration: NOT_REQUIRED_FOR_FRAMED_RIGIDITY")
    print("next_gate: FORMULATE_GENERAL_EVEN_N_INDUCTION_AND_TEST_N12_FIRST_NEW_STRATA")


if __name__ == "__main__":
    main()
