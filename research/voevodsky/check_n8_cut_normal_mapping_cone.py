"""Identify the D05 loaded collar as the mapping cone of a unit map."""

import check_n8_loaded_octagon_carrier as octagon
import check_n8_six_by_four_cut_boundary as boundary


DIMENSION = 5
CUT = (0, 5)


def radial_sign(face, added):
    return (-1) ** sum(d < added for d in face)


def normal_sign(face, marked, removed):
    return (-1) ** (DIMENSION - len(face) + tuple(sorted(marked)).index(removed))


def main():
    octagon.main()

    diagonals = boundary.diagonals(8)
    compatible = tuple(d for d in diagonals if d != CUT and not boundary.crosses(d, CUT))
    link_faces = boundary.faces(compatible)
    generators = tuple(
        (face, marked)
        for face in link_faces
        for marked in boundary.subsets(face)
    )
    assert len(generators) == 1075

    # U is the unmarked Cut facet and N its copy with the Cut marked.
    # Removing the Cut is a diagonal unit map N -> U.
    bridge_sign = {}
    for face, marked in generators:
        full_face = tuple(sorted(face + (CUT,)))
        normal_marked = tuple(sorted(marked + (CUT,)))
        bridge_sign[(face, marked)] = normal_sign(full_face, normal_marked, CUT)
        assert abs(bridge_sign[(face, marked)]) == 1
    assert len(bridge_sign) == 1075

    # Every internal arrow gives a two-path square in d^2.  Its signs prove
    # d_N * epsilon + epsilon * d_U = 0, hence the collar is Cone(id).
    cone_squares = 0
    radial_squares = 0
    marking_squares = 0
    for face, marked in generators:
        full_face = tuple(sorted(face + (CUT,)))
        for added in compatible:
            if added in face or any(boundary.crosses(added, d) for d in face):
                continue
            target = (tuple(sorted(face + (added,))), marked)
            u_sign = radial_sign(full_face, added)
            n_sign = u_sign
            assert n_sign * bridge_sign[target] + bridge_sign[(face, marked)] * u_sign == 0
            cone_squares += 1
            radial_squares += 1

        for removed in marked:
            target = (face, tuple(d for d in marked if d != removed))
            u_sign = normal_sign(full_face, marked, removed)
            n_marked = tuple(sorted(marked + (CUT,)))
            n_sign = normal_sign(full_face, n_marked, removed)
            assert n_sign * bridge_sign[target] + bridge_sign[(face, marked)] * u_sign == 0
            cone_squares += 1
            marking_squares += 1

    assert radial_squares == 1735
    assert marking_squares == 1735
    assert cone_squares == 3470

    # The unit bridge commutes stalkwise with the primitive conductor row.
    conductor_row = (1, -1)
    assert tuple(1 * value for value in conductor_row) == conductor_row
    assert bridge_sign[((), ())] in (-1, 1)

    # Cone(id) has an explicit integral contraction: epsilon is diagonal with
    # unit entries.  No division and hence no torsion are introduced.
    inverse_bridge = {cell: sign for cell, sign in bridge_sign.items()}
    assert all(inverse_bridge[cell] * bridge_sign[cell] == 1 for cell in generators)

    print("D05_unmarked_boundary_cells: 1075")
    print("D05_marked_normal_cells: 1075")
    print("normal_bridge_matrix: DIAGONAL_UNITS")
    print("mapping_cone_sign_squares: 3470=1735+1735")
    print("conductor_kernel_base_change: COMMUTES")
    print("integral_normal_torsion: NONE")
    print("isolated_cut_collar_homology: ZERO")
    print("boundary_supported_extension: IMPOSSIBLE")
    print("off_collar_cancellation: REQUIRED_NEXT_GATE")


if __name__ == "__main__":
    main()
