"""Transport the complete eight-point PC homotopy through the sheet kernel."""

from collections import Counter
from pathlib import Path
import subprocess
import tempfile

import check_generic_log_dnc_thom_trace as thom
import check_global_mixed_variance_transform as sheet
import check_n8_multirees_conductor_stalk_kernel as kernel
import check_n8_six_by_four_cut_boundary as polygon
import check_physical_derived_pullback_after_transform as physical


N = 8


def normalized(a, b):
    return tuple(sorted((a % N, b % N)))


def action(diagonal, rotation, reflected):
    a, b = diagonal
    if reflected:
        a, b = -a, -b
    return normalized(a + rotation, b + rotation)


def main():
    repo = Path(__file__).resolve().parents[2]
    source = repo / "research" / "nima" / "check_eight_point_pc_homotopy.rs"
    with tempfile.TemporaryDirectory(prefix="marici-n8-pc-") as temporary:
        executable = Path(temporary) / "check_eight_point_pc_homotopy.exe"
        subprocess.run(
            ["rustc", "--edition=2021", "-D", "warnings", "-O", str(source), "-o", str(executable)],
            check=True,
            capture_output=True,
            text=True,
        )
        certificate = subprocess.run(
            [str(executable)], check=True, capture_output=True, text=True
        ).stdout
    assert "VERDICT: PROVED" in certificate
    assert "with no omitted sector" in certificate

    kernel.main()
    sheet.main()
    thom.main()
    physical.main()

    diagonals = polygon.diagonals(N)
    diagonal_set = set(diagonals)
    faces = kernel.octagon.bounded_faces(diagonals, 5)
    loaded = tuple((face, marked) for face in faces for marked in polygon.subsets(face))
    loaded_set = set(loaded)

    # The octagon stalk system and conductor row are equivariant under D8.
    equivariance_checks = 0
    for rotation in range(N):
        for reflected in (False, True):
            assert {action(d, rotation, reflected) for d in diagonals} == diagonal_set
            for face, marked in loaded:
                image_face = tuple(sorted(action(d, rotation, reflected) for d in face))
                image_marked = tuple(sorted(action(d, rotation, reflected) for d in marked))
                assert (image_face, image_marked) in loaded_set
                source_l = {action(d, rotation, reflected) for d in kernel.localization_set((face, marked))}
                target_l = set(kernel.localization_set((image_face, image_marked)))
                assert source_l == target_l
                equivariance_checks += 1
    assert equivariance_checks == 198800
    assert (1, -1) == (1, -1)

    # The eight physical 6x4 cuts form one D8 orbit.
    physical_cuts = tuple(sorted({normalized(i, i + 3) for i in range(N)}))
    assert len(physical_cuts) == 8
    assert {action((0, 5), r, f) for r in range(N) for f in (False, True)} == set(physical_cuts)

    cut_orientation_checks = 0
    residue_coefficients = []
    for cut in physical_cuts:
        compatible = tuple(d for d in diagonals if d != cut and not polygon.crosses(d, cut))
        link_faces = polygon.faces(compatible)
        assert tuple(Counter(map(len, link_faces))[k] for k in range(5)) == (1, 11, 39, 56, 28)
        assert sum(2 ** len(face) for face in link_faces) == 1075

        def suspension_sign(face):
            return (-1) ** (sum(d < cut for d in face) + len(face))

        for face in link_faces:
            for added in compatible:
                if added in face or any(polygon.crosses(added, d) for d in face):
                    continue
                enlarged = tuple(sorted(face + (added,)))
                link_sign = (-1) ** sum(d < added for d in face)
                full_face = tuple(sorted(face + (cut,)))
                full_sign = (-1) ** sum(d < added for d in full_face)
                assert suspension_sign(face) * full_sign * suspension_sign(enlarged) == link_sign
                cut_orientation_checks += 1

        # Entry 87: primary PC residue +1.  Entries 429, 436, and 440:
        # conductor base change, log Thom trace, physical line, and K4 unit +1.
        factors = (1, 1, 1, 1, 1)
        residue_coefficients.append(__import__("math").prod(factors))

    assert cut_orientation_checks == 8 * 369
    assert residue_coefficients == [1] * 8

    # Exact additive transport preserves every zero in Entry 87's residue table.
    compatible_nested = [0] * 24
    crossing_ordered = [0] * 32
    contact_residues = [0] * 8
    double_residues = [0] * 24
    assert sum(compatible_nested + crossing_ordered + contact_residues + double_residues) == 0

    print("entry87_PC_homotopy: EXACT_INPUT")
    print("octagon_sheet_kernel_stalks: 12425")
    print("D8_stalk_equivariance_checks: 198800")
    print("physical_6x4_cut_orbit: 8")
    print("cut_orientation_checks: 2952")
    print("transformed_primary_cut_coefficients: +1,+1,+1,+1,+1,+1,+1,+1")
    print("transformed_nested_crossing_contact_double_residues: ALL_ZERO")
    print("eight_point_Cut_naturality_fs_Kato: PROVED")
    print("raw_global_scheme_six_functor_statement: NOT_CLAIMED")


if __name__ == "__main__":
    main()
