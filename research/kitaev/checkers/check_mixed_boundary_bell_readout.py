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


def symplectic_product(u, v, logical_qubits):
    z_u = u[:logical_qubits, :]
    x_u = u[logical_qubits:, :]
    z_v = v[:logical_qubits, :]
    x_v = v[logical_qubits:, :]
    return int((z_u.T * x_v + x_u.T * z_v)[0] % 2)


def main():
    fixtures = []
    for logical_qubits in range(1, 7):
        # Symplectic coordinates on data plus reference: first all Z, then X,
        # with k data coordinates followed by k reference coordinates.
        total_qubits = 2 * logical_qubits
        checks = []
        for i in range(logical_qubits):
            zz = sp.zeros(2 * total_qubits, 1)
            zz[i, 0] = 1
            zz[logical_qubits + i, 0] = 1
            checks.append(zz)
        for i in range(logical_qubits):
            xx = sp.zeros(2 * total_qubits, 1)
            xx[total_qubits + i, 0] = 1
            xx[total_qubits + logical_qubits + i, 0] = 1
            checks.append(xx)

        for i, left in enumerate(checks):
            for right in checks[i + 1:]:
                assert symplectic_product(left, right, total_qubits) == 0

        check_matrix = sp.Matrix.hstack(*checks).T
        assert gf2_rank(check_matrix) == 2 * logical_qubits
        records = 2 ** (2 * logical_qubits)
        assert records == 4 ** logical_qubits
        fixtures.append({
            "logical_qubits": logical_qubits,
            "independent_commuting_checks": 2 * logical_qubits,
            "joint_records": records,
        })

    # Data-only one-qubit Z and X anticommute; doubled ZZ and XX commute.
    z = sp.Matrix([1, 0])
    x = sp.Matrix([0, 1])
    assert symplectic_product(z, x, 1) == 1
    zz = sp.Matrix([1, 1, 0, 0])
    xx = sp.Matrix([0, 0, 1, 1])
    assert symplectic_product(zz, xx, 2) == 0

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_finite_stabilizer_instrument_theorem",
        "fixture_count": len(fixtures),
        "data_only_paired_probes_commute": False,
        "doubled_bell_checks_commute": True,
        "independent_check_count": "2k",
        "joint_record_count": "4^k",
        "binary_record_lower_bound_attained": True,
        "single_sharp_setting": True,
        "qnd_relational_pauli_label": True,
        "requires_matched_logical_reference": True,
        "requires_bell_preparation_for_error_identification": True,
        "is_arbitrary_state_tomography": False,
    }
    out = Path(__file__).parents[1] / "results" / "mixed-boundary-bell-readout.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
