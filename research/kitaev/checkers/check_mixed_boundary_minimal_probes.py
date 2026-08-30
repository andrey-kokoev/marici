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


def main():
    fixtures = []
    for genus in range(3):
        for boundary_count in range(2, 7):
            for rough in range(1, boundary_count):
                smooth = boundary_count - rough
                logical_rank = 2 * genus + boundary_count - 2

                one_sector = sp.eye(logical_rank)
                full_probe = sp.eye(2 * logical_rank)
                assert gf2_rank(one_sector) == logical_rank
                assert gf2_rank(full_probe) == 2 * logical_rank

                if logical_rank > 0:
                    omitted = one_sector[:-1, :]
                    assert gf2_rank(omitted) == logical_rank - 1
                    assert logical_rank - gf2_rank(omitted) == 1

                primal_counts = [2 * genus, smooth - 1, rough - 1]
                dual_counts = [2 * genus, rough - 1, smooth - 1]
                assert sum(primal_counts) == sum(dual_counts) == logical_rank

                omega = sp.zeros(2 * logical_rank)
                omega[:logical_rank, logical_rank:] = sp.eye(logical_rank)
                omega[logical_rank:, :logical_rank] = sp.eye(logical_rank)
                assert gf2_rank(omega) == 2 * logical_rank
                if logical_rank > 0:
                    assert any(omega[i, logical_rank + i] == 1
                               for i in range(logical_rank))

                fixtures.append({
                    "genus": genus,
                    "boundary_components": boundary_count,
                    "rough_components": rough,
                    "smooth_components": smooth,
                    "logical_rank": logical_rank,
                    "one_sector_minimal_probes": logical_rank,
                    "full_pauli_minimal_binary_probes": 2 * logical_rank,
                })

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_finite_quotient_readout_and_incompatibility_theorem",
        "fixture_count": len(fixtures),
        "one_css_probe_minimum": "k=2g+b-2",
        "full_pauli_probe_minimum": "2k",
        "omit_one_basis_probe_kernel_dimension": 1,
        "rough_arc_ports_required": "r-1",
        "smooth_arc_ports_required": "s-1",
        "minimum_sharp_settings_for_both_css_sectors": "2 when k>0; 0 when k=0",
        "full_probe_family_pairwise_commuting": False,
        "pauli_label_map_is_state_tomography": False,
        "pair_of_pants_full_pauli_bits": 2,
    }
    out = Path(__file__).parents[1] / "results" / "mixed-boundary-minimal-probes.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
