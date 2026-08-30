"""Exact conditional expectation from the D(S3) ambient algebra to its center."""

import json
import sympy as sp


def main():
    labels = ("A", "B", "C", "D", "E", "F", "G", "H")
    dims = (1, 1, 2, 3, 3, 2, 2, 2)
    total = sum(dims)
    offsets = []
    cursor = 0
    for dim in dims:
        offsets.append(cursor)
        cursor += dim

    def matrix_unit(i, j):
        out = sp.zeros(total)
        out[i, j] = 1
        return out

    projectors = []
    for offset, dim in zip(offsets, dims):
        p = sp.zeros(total)
        for i in range(offset, offset + dim):
            p[i, i] = 1
        projectors.append(p)

    def dephase(x):
        return sum((p * x * p for p in projectors), sp.zeros(total))

    def center_expectation(x):
        return sum(
            ((sp.trace(p * x) / dim) * p for p, dim in zip(projectors, dims)),
            sp.zeros(total),
        )

    # Test the maps on a basis, not only on selected witnesses.
    basis = [matrix_unit(i, j) for i in range(total) for j in range(total)]
    assert all(dephase(dephase(x)) == dephase(x) for x in basis)
    assert all(center_expectation(center_expectation(x)) == center_expectation(x) for x in basis)
    assert all(center_expectation(dephase(x)) == center_expectation(x) for x in basis)
    assert all(dephase(center_expectation(x)) == center_expectation(x) for x in basis)
    assert center_expectation(sp.eye(total)) == sp.eye(total)
    assert all(sp.trace(center_expectation(x)) == sp.trace(x) for x in basis)

    # Hilbert--Schmidt self-adjointness on the full matrix-unit basis.
    assert all(
        sp.trace(x.T * center_expectation(y)) == sp.trace(center_expectation(x).T * y)
        for x in basis
        for y in basis
    )

    # Measure sector weight, then prepare the maximally mixed state in that block.
    symbolic_weights = sp.symbols("p0:8")
    prepared = sum(
        ((weight / dim) * p for weight, dim, p in zip(symbolic_weights, dims, projectors)),
        sp.zeros(total),
    )
    assert [sp.trace(p * prepared) for p in projectors] == list(symbolic_weights)

    # A Kraus family K_(a,i,j)=|a,i><a,j|/sqrt(d_a) realizes the same channel.
    kraus = []
    for offset, dim in zip(offsets, dims):
        for i in range(offset, offset + dim):
            for j in range(offset, offset + dim):
                kraus.append(matrix_unit(i, j) / sp.sqrt(dim))
    assert sum((k.T * k for k in kraus), sp.zeros(total)) == sp.eye(total)
    assert all(
        sum((k * x * k.T for k in kraus), sp.zeros(total)) == center_expectation(x)
        for x in basis
    )

    # Deliberate failures distinguish the three maps.
    c0 = offsets[2]
    traceless_c = matrix_unit(c0, c0) - matrix_unit(c0 + 1, c0 + 1)
    assert dephase(traceless_c) == traceless_c
    assert center_expectation(traceless_c) == sp.zeros(total)
    assert dephase(traceless_c) != center_expectation(traceless_c)
    noncentral_probe = traceless_c
    state_pairing_before = sp.trace(noncentral_probe * traceless_c)
    state_pairing_after = sp.trace(noncentral_probe * center_expectation(traceless_c))
    assert state_pairing_before == 2 and state_pairing_after == 0

    result = {
        "schema": "marici.s3-center-conditional-expectation.v1",
        "ambient_matrix_algebra_dimension": total * total,
        "block_dephasing_image_dimension": sum(dim * dim for dim in dims),
        "block_dephasing_kernel_dimension": total * total - sum(dim * dim for dim in dims),
        "center_expectation_image_dimension": len(dims),
        "center_expectation_kernel_dimension": total * total - len(dims),
        "kraus_rank": len(kraus),
        "factorization": "measure_sector_weights_then_prepare_blockwise_maximally_mixed_state",
        "deliberate_failure": {
            "claim": "block_dephasing_equals_center_expectation",
            "witness": "traceless_diagonal_inside_C",
            "dephasing_output_nonzero": True,
            "center_expectation_output_zero": True,
            "noncentral_pairing_residual": str(state_pairing_before - state_pairing_after),
        },
        "aggregate_gates": {
            "dephasing_is_idempotent": True,
            "center_expectation_is_idempotent": True,
            "center_expectation_is_unital": True,
            "center_expectation_is_trace_preserving": True,
            "center_expectation_is_hilbert_schmidt_self_adjoint": True,
            "center_expectation_has_explicit_cptp_kraus_realization": True,
            "center_expectation_is_measure_prepare_and_entanglement_breaking": True,
            "center_expectation_factors_through_sector_weights": True,
            "dephasing_and_center_expectation_are_distinct": True,
            "only_central_expectations_are_preserved_in_general": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
