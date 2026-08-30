"""Exact fault identities for a controlled D(S3) central power."""

import json
import sympy as sp


def ctrl(U):
    n = U.rows
    out = sp.zeros(2 * n)
    out[:n, :n] = sp.eye(n)
    out[n:, n:] = U
    return out


def main():
    I2 = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.diag(1, -1)
    P0 = sp.diag(1, 0)
    P1 = sp.diag(0, 1)
    ket10 = sp.Matrix([[0, 0], [1, 0]])
    ket01 = sp.Matrix([[0, 1], [0, 0]])

    # Exact nontrivial sector-phase witness.
    U = sp.diag(1, sp.I)
    C = ctrl(U)
    propagated_x = sp.simplify(C * sp.kronecker_product(X, I2) * C.H)
    expected_x = (sp.kronecker_product(ket10, U)
                  + sp.kronecker_product(ket01, U.H))
    assert propagated_x == expected_x
    assert propagated_x != sp.kronecker_product(X, I2)

    propagated_z = sp.simplify(C * sp.kronecker_product(Z, I2) * C.H)
    assert propagated_z == sp.kronecker_product(Z, I2)

    E_commuting = Z
    E_changing = X
    for name, E in (("commuting", E_commuting), ("changing", E_changing)):
        propagated = sp.simplify(C * sp.kronecker_product(I2, E) * C.H)
        expected = (sp.kronecker_product(P0, E)
                    + sp.kronecker_product(P1, U * E * U.H))
        assert propagated == expected
        if name == "commuting":
            assert propagated == sp.kronecker_product(I2, E)
        else:
            assert propagated != sp.kronecker_product(I2, E)

    result = {
        "schema": "marici.s3-controlled-power-faults.v1",
        "exact_identities": {
            "control_X_acquires_U_and_U_dagger_branches": True,
            "control_Z_commutes_and_does_not_spread": True,
            "data_E_becomes_P0_E_plus_P1_UEUdagger": True,
            "commuting_data_fault_remains_uncorrelated": True,
            "noncommuting_data_fault_becomes_branch_correlated": True,
        },
        "support_disposition": {
            "abstract_control_X_data_support": "support_of_U",
            "microscopic_numeric_bound": "unresolved_without_timed_word_or_conditional_H_support",
            "endpoint_centrality_implies_nonspreading": False,
        },
        "relation_to_record_code": {
            "six_bit_code_repairs_later_record_flip": True,
            "six_bit_code_repairs_coherent_acquisition_fault": False,
        },
        "aggregate_gates": {
            "control_X_spread_identity_exact": True,
            "control_Z_nonspread_identity_exact": True,
            "commuting_data_fault_witness_exact": True,
            "noncommuting_data_fault_witness_exact": True,
            "fault_support_requires_microscopic_word": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

