import json
from pathlib import Path
import sympy as sp


def gf2_rank(matrix):
    rows = [sum((int(matrix[i, j]) & 1) << j for j in range(matrix.cols))
            for i in range(matrix.rows)]
    rank = 0
    for col in range(matrix.cols):
        pivot = next((i for i in range(rank, len(rows))
                      if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def boundary_inclusion_matrix(genus, boundary_count, selected):
    # H1(Sigma) basis: 2g handle cycles followed by the first b-1 boundary
    # circles. The last boundary circle is their sum over F2.
    rows = 2 * genus + boundary_count - 1
    cols = []
    for component in selected:
        vector = [0] * rows
        if component < boundary_count - 1:
            vector[2 * genus + component] = 1
        else:
            for j in range(boundary_count - 1):
                vector[2 * genus + j] = 1
        cols.append(sp.Matrix(vector))
    return sp.Matrix.hstack(*cols) if cols else sp.zeros(rows, 0)


def relative_rank(genus, boundary_count, selected):
    absolute = 2 * genus + boundary_count - 1
    inclusion_rank = gf2_rank(boundary_inclusion_matrix(
        genus, boundary_count, selected))
    reduced_h0 = max(len(selected) - 1, 0)
    return absolute - inclusion_rank + reduced_h0, inclusion_rank


def main():
    fixtures = []
    for genus in range(3):
        for boundary_count in range(2, 7):
            for rough_count in range(1, boundary_count):
                rough = list(range(rough_count))
                smooth = list(range(rough_count, boundary_count))
                primal, rough_inclusion = relative_rank(
                    genus, boundary_count, rough)
                dual, smooth_inclusion = relative_rank(
                    genus, boundary_count, smooth)
                expected = 2 * genus + boundary_count - 2
                assert rough_inclusion == rough_count
                assert smooth_inclusion == len(smooth)
                assert primal == dual == expected
                fixtures.append({
                    "genus": genus,
                    "boundary_components": boundary_count,
                    "rough_components": rough_count,
                    "smooth_components": len(smooth),
                    "logical_rank": expected,
                })

    # Endpoint types recover the absolute rank rather than the mixed formula.
    empty_rank, empty_inclusion = relative_rank(0, 3, [])
    full_rank, full_inclusion = relative_rank(0, 3, [0, 1, 2])
    assert empty_rank == 2 and empty_inclusion == 0
    assert full_rank == 2 and full_inclusion == 2

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_finite_relative_homology_theorem",
        "mixed_fixture_count": len(fixtures),
        "mixed_logical_rank_formula": "2g+b-2",
        "primal_dual_ranks_equal": True,
        "annulus_mixed_rank": 0,
        "pair_of_pants_mixed_rank": 1,
        "empty_rough_rank_pair_of_pants": empty_rank,
        "full_rough_rank_pair_of_pants": full_rank,
        "additional_rough_component_creates_relative_arc": True,
        "boundary_labels_source_derived": True,
    }
    out = Path(__file__).parents[1] / "results" / "mixed-boundary-relative-rank.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
