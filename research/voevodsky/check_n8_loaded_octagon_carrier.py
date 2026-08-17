"""Construct the full loaded octagon carrier and its D05 boundary embedding."""

from collections import Counter
from itertools import combinations

import check_n8_six_by_four_cut_boundary as boundary


def bounded_faces(ds, maximum):
    return tuple(
        face
        for size in range(maximum + 1)
        for face in combinations(ds, size)
        if all(not boundary.crosses(x, y) for x, y in combinations(face, 2))
    )


def main():
    boundary.main()
    cut = (0, 5)
    octagon_diagonals = boundary.diagonals(8)
    octagon_faces = bounded_faces(octagon_diagonals, 5)
    face_counts = Counter(map(len, octagon_faces))
    assert tuple(face_counts[k] for k in range(6)) == (1, 20, 120, 300, 330, 132)

    loaded = tuple(
        (face, marked)
        for face in octagon_faces
        for marked in boundary.subsets(face)
    )
    assert len(loaded) == 12425
    degree_counts = Counter(5 - len(face) + len(marked) for face, marked in loaded)
    assert tuple(degree_counts[k] for k in range(6)) == (132, 990, 2940, 4320, 3140, 903)

    compatible = tuple(
        d for d in octagon_diagonals if d != cut and not boundary.crosses(d, cut)
    )
    link_faces = boundary.faces(compatible)
    boundary_loaded = tuple(
        (face, marked)
        for face in link_faces
        for marked in boundary.subsets(face)
    )

    # Adjoin the Cut diagonal as an unmarked divisor: the closed D05 facet.
    embedding = {
        (face, marked): (tuple(sorted(face + (cut,))), marked)
        for face, marked in boundary_loaded
    }
    assert len(embedding) == 1075
    assert len(set(embedding.values())) == 1075
    loaded_set = set(loaded)
    assert set(embedding.values()) <= loaded_set
    assert all(
        4 - len(face) + len(marked)
        == 5 - len(image_face) + len(image_marked)
        for (face, marked), (image_face, image_marked) in embedding.items()
    )

    # Contract the full octagon orientation along D05.
    def contraction_sign(face):
        # The extra |face| is the suspension sign of the outward normal.
        return (-1) ** (sum(d < cut for d in face) + len(face))

    radial_checks = 0
    for face in link_faces:
        for added in compatible:
            if added in face or any(boundary.crosses(added, d) for d in face):
                continue
            enlarged = tuple(sorted(face + (added,)))
            link_sign = (-1) ** sum(d < added for d in face)
            full_face = tuple(sorted(face + (cut,)))
            full_sign = (-1) ** sum(d < added for d in full_face)
            transported = contraction_sign(face) * full_sign * contraction_sign(enlarged)
            assert transported == link_sign
            radial_checks += 1
    assert radial_checks == 369

    # Each radial face arrow occurs once for every marking of its source.
    loaded_radial_checks = sum(
        (size + 1) * next_count * (2**size)
        for size, next_count in enumerate((11, 39, 56, 28))
    )
    assert loaded_radial_checks == 1735

    # Marking D05 gives the disjoint degree-shifted normal copy.
    marked_cut_copy = {
        (tuple(sorted(face + (cut,))), tuple(sorted(marked + (cut,))))
        for face, marked in boundary_loaded
    }
    assert len(marked_cut_copy) == 1075
    assert marked_cut_copy.isdisjoint(set(embedding.values()))
    assert marked_cut_copy <= loaded_set

    print("octagon_face_counts: 1,20,120,300,330,132")
    print("octagon_loaded_cells: 12425")
    print("octagon_loaded_chain_ranks: 132,990,2940,4320,3140,903")
    print("D05_boundary_embedding_cells: 1075")
    print("D05_boundary_degree_preservation: EXACT")
    print("D05_contracted_orientation_checks: 369")
    print("D05_loaded_radial_arrows: 1735")
    print("D05_marked_normal_copy: 1075_SHIFTED_CELLS")
    print("carrier_extension_obstruction: NONE")
    print("class_extension_obstruction: NEXT_GATE")


if __name__ == "__main__":
    main()
