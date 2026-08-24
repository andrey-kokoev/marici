"""Exact GF(2) census for the periodic square-lattice toric-code chain complex."""

from collections import defaultdict
import json


def rank_gf2(rows, width):
    rows = list(rows)
    rank = 0
    for col in range(width):
        pivot = next((i for i in range(rank, len(rows)) if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> col) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def column_space(columns):
    values = {0}
    for column in columns:
        values |= {x ^ column for x in tuple(values)}
    return values


def lattice(L):
    vertex = lambda x, y: (x % L) * L + (y % L)
    horizontal = lambda x, y: (x % L) * L + (y % L)
    vertical = lambda x, y: L * L + (x % L) * L + (y % L)

    boundary_1 = []
    for x in range(L):
        for y in range(L):
            boundary_1.append((1 << vertex(x, y)) | (1 << vertex(x + 1, y)))
    for x in range(L):
        for y in range(L):
            boundary_1.append((1 << vertex(x, y)) | (1 << vertex(x, y + 1)))

    boundary_2 = []
    for x in range(L):
        for y in range(L):
            boundary_2.append(
                (1 << horizontal(x, y))
                | (1 << vertical(x + 1, y))
                | (1 << horizontal(x, y + 1))
                | (1 << vertical(x, y))
            )
    return boundary_1, boundary_2


def apply_columns(columns, vector):
    out = 0
    for i, column in enumerate(columns):
        if (vector >> i) & 1:
            out ^= column
    return out


def audit(L):
    d1, d2 = lattice(L)
    n0, n1, n2 = L * L, 2 * L * L, L * L
    assert all(apply_columns(d1, face) == 0 for face in d2), "d1 d2 != 0"
    rank_d1 = rank_gf2(d1, n0)
    rank_d2 = rank_gf2(d2, n1)
    h1_dimension = n1 - rank_d1 - rank_d2

    # Two source-labelled cocycles: a vertical cut pairs with horizontal
    # winding, and a horizontal cut pairs with vertical winding.
    probe_h = [int(i < L * L and (i // L) == 0) for i in range(n1)]
    probe_v = [int(i >= L * L and ((i - L * L) % L) == 0) for i in range(n1)]
    combined_columns = [
        d1[i] | (probe_h[i] << n0) | (probe_v[i] << (n0 + 1))
        for i in range(n1)
    ]
    combined_rank = rank_gf2(combined_columns, n0 + 2)
    assert all(
        sum(((face >> i) & 1) * probe_h[i] for i in range(n1)) % 2 == 0
        and sum(((face >> i) & 1) * probe_v[i] for i in range(n1)) % 2 == 0
        for face in d2
    ), "logical probes do not descend through local repairs"
    assert n1 - combined_rank == rank_d2
    result = {
        "L": L,
        "dimensions": [n2, n1, n0],
        "rank_d2": rank_d2,
        "rank_d1": rank_d1,
        "h1_dimension": h1_dimension,
        "d1_d2_zero": True,
        "syndrome_plus_two_loops_rank": combined_rank,
        "joint_kernel_dimension": n1 - combined_rank,
        "joint_kernel_equals_local_repair_dimension": n1 - combined_rank == rank_d2,
    }
    if L == 2:
        stabilizers = column_space(d2)
        by_syndrome = defaultdict(list)
        for error in range(1 << n1):
            by_syndrome[apply_columns(d1, error)].append(error)
        quotient_counts = []
        for errors in by_syndrome.values():
            unseen = set(errors)
            cosets = 0
            while unseen:
                representative = next(iter(unseen))
                unseen -= {representative ^ stabilizer for stabilizer in stabilizers}
                cosets += 1
            quotient_counts.append(cosets)
        result.update(
            {
                "edge_chains": 1 << n1,
                "realized_syndromes": len(by_syndrome),
                "errors_per_syndrome": sorted({len(v) for v in by_syndrome.values()}),
                "stabilizer_space_size": len(stabilizers),
                "logical_cosets_per_syndrome": sorted(set(quotient_counts)),
            }
        )
        assert result["realized_syndromes"] == 8
        assert result["errors_per_syndrome"] == [32]
        assert result["stabilizer_space_size"] == 8
        assert result["logical_cosets_per_syndrome"] == [4]
    if L == 3:
        # Two diagonal-neighbor defects admit two equally short corrections.
        # Their difference is the boundary of the intervening face.
        target_syndrome = (1 << 0) | (1 << 4)
        candidates = [
            error
            for error in range(1 << n1)
            if apply_columns(d1, error) == target_syndrome
        ]
        minimum_weight = min(error.bit_count() for error in candidates)
        minimum_decoders = [
            error for error in candidates if error.bit_count() == minimum_weight
        ]
        result.update(
            {
                "hostile_syndrome_minimum_repair_weight": minimum_weight,
                "hostile_syndrome_minimum_decoder_count": len(minimum_decoders),
                "minimum_decoders_differ_by_local_repair": (
                    minimum_decoders[0] ^ minimum_decoders[1]
                )
                in column_space(d2),
            }
        )
        assert minimum_weight == 2
        assert len(minimum_decoders) == 2
        assert result["minimum_decoders_differ_by_local_repair"]
    assert h1_dimension == 2
    return result


def main():
    payload = {
        "schema": "marici.toric-code-chain-carrier.v1",
        "audits": [audit(L) for L in range(2, 6)],
        "aggregate_gates": {
            "chain_condition": True,
            "torus_h1_dimension_two": True,
            "smallest_syndrome_fiber_has_four_logical_classes": True,
            "syndrome_plus_two_loops_jointly_faithful_mod_repairs": True,
            "syndrome_does_not_select_preferred_decoder": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
