"""Test the naive full-cell lift of the Thom-twisted Cut Cech section."""

from collections import Counter
from itertools import combinations

import check_n8_cut_naturality_after_sheet_transform as naturality
import check_n8_six_by_four_cut_boundary as polygon
import check_n8_twisted_cut_cech_totalization as scalar_cech


N = 8
DIMENSION = 4


def normalized(a, b):
    return tuple(sorted((a % N, b % N)))


def radial_sign(face, added):
    return (-1) ** sum(d < added for d in face)


def normal_sign(face, marked, removed):
    return (-1) ** (DIMENSION - len(face) + tuple(sorted(marked)).index(removed))


def loaded_cells(diagonals):
    return tuple(
        (face, marked)
        for face in polygon.faces(diagonals)
        for marked in polygon.subsets(face)
    )


def arrows(diagonals, cells):
    cell_set = set(cells)
    for face, marked in cells:
        for added in diagonals:
            if added in face or any(polygon.crosses(added, d) for d in face):
                continue
            target = (tuple(sorted(face + (added,))), marked)
            assert target in cell_set
            yield (face, marked), target, radial_sign(face, added), "radial"
        for removed in marked:
            target = (face, tuple(d for d in marked if d != removed))
            assert target in cell_set
            yield (face, marked), target, normal_sign(face, marked, removed), "normal"


def main():
    # The imported modules are the exact lower certificates of Entries
    # 441--446.  This checker tests only the new full-cell restriction gate.
    assert callable(naturality.main) and callable(scalar_cech.main)

    all_diagonals = polygon.diagonals(N)
    cuts = tuple(sorted({normalized(i, i + 3) for i in range(N)}))
    edges = tuple(
        (a, b) for a, b in combinations(cuts, 2) if not polygon.crosses(a, b)
    )
    assert (len(cuts), len(edges)) == (8, 12)

    chart_cells = {}
    chart_arrows = {}
    for cut in cuts:
        link = tuple(
            d for d in all_diagonals if d != cut and not polygon.crosses(d, cut)
        )
        cells = loaded_cells(link)
        assert len(cells) == 1075
        assert Counter(DIMENSION - len(f) + len(h) for f, h in cells) == {
            0: 28, 1: 168, 2: 375, 3: 369, 4: 135
        }
        chart_cells[cut] = cells
        chart_arrows[cut] = tuple(arrows(link, cells))
        assert Counter(kind for *_, kind in chart_arrows[cut]) == {
            "radial": 1735, "normal": 1735
        }

    # An overlap is literally the common compatible subcomplex.  Restriction
    # is the coordinate projection: a cell survives iff its face is compatible
    # with the other Cut.  This is the finite-space restriction of Entry 441.
    overlap_cells = {}
    restriction_commutation_checks = 0
    projected_zero_checks = 0
    escaping_radial_defects = []
    for left, right in edges:
        common = tuple(
            d for d in all_diagonals
            if d not in (left, right)
            and not polygon.crosses(d, left)
            and not polygon.crosses(d, right)
        )
        cells = loaded_cells(common)
        cell_set = set(cells)
        assert len(cells) == 125
        assert Counter(3 - len(f) + len(h) for f, h in cells) == {
            0: 8, 1: 36, 2: 54, 3: 27
        }
        overlap_cells[(left, right)] = cells

        overlap_arrow = {(s, t): sign for s, t, sign, _ in arrows(common, cells)}
        for chart in (left, right):
            for source, target, sign, _ in chart_arrows[chart]:
                source_survives = source in cell_set
                target_survives = target in cell_set
                # Compatibility is downward closed, so an arrow cannot enter
                # the common subcomplex from a projected-away source.  It can,
                # however, leave it by adding a diagonal crossing the other
                # Cut; those terms are the obstruction being measured.
                assert not (target_survives and not source_survives)
                if source_survives:
                    if target_survives:
                        assert overlap_arrow[(source, target)] == sign
                        restriction_commutation_checks += 1
                    else:
                        escaping_radial_defects.append((left, right, chart, source, target, sign))
                else:
                    projected_zero_checks += 1

    assert escaping_radial_defects
    assert all(target[0] != source[0] for *_, source, target, _ in escaping_radial_defects)

    # The native odd Thom line still cancels the scalar Koszul edge sign, and
    # the constant coefficient is cellwise compatible.  But this does not
    # repair the escaping radial terms: a sign twist cannot turn a non-chain
    # projection into a chain map.
    cut_index = {cut: i for i, cut in enumerate(cuts)}
    constant = [1] * len(cuts)
    cech_cell_checks = 0
    for left, right in edges:
        row = [0] * len(cuts)
        row[cut_index[left]] = -1
        row[cut_index[right]] = 1
        assert sum(a * b for a, b in zip(row, constant)) == 0
        for cell in overlap_cells[(left, right)]:
            assert cell in set(chart_cells[left])
            assert cell in set(chart_cells[right])
            cech_cell_checks += 1
    assert cech_cell_checks == 12 * 125

    # There are no triple physical-Cut intersections (Entry 443), so no higher
    # scalar Cech cell can absorb the defect.  A relative/Gysin restriction or
    # an explicit homotopy correcting these radial exits is indispensable.
    chart_generators = sum(map(len, chart_cells.values()))
    overlap_generators = sum(map(len, overlap_cells.values()))
    assert (chart_generators, overlap_generators) == (8600, 1500)

    print("full_cut_charts: 8x1075=8600_LOADED_CELLS")
    print("full_pair_overlaps: 12x125=1500_LOADED_CELLS")
    print("chart_internal_arrows: 8x3470=27760")
    print(f"restriction_commuting_arrow_checks: {restriction_commutation_checks}")
    print(f"restriction_projected_zero_checks: {projected_zero_checks}")
    print(f"escaping_radial_defects: {len(escaping_radial_defects)}")
    print("Thom_twisted_Cech_cell_checks: 1500")
    print("scalar_global_section: CONSTANT_PRIMITIVE_PLUS_ONE")
    print("naive_full_cell_coordinate_restriction: NOT_A_CHAIN_MAP")
    print("sign_twist_repairs_support_defect: NO")
    print("next_gate: CONSTRUCT_RELATIVE_GYSIN_RESTRICTION_OR_DEFECT_HOMOTOPY")


if __name__ == "__main__":
    main()
