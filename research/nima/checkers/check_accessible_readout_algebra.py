"""Exact logical-Pauli census for accessible readout algebras."""

import json


def rank_gf2(vectors, width=4):
    rows = list(vectors)
    rank = 0
    for bit in range(width):
        pivot = next((i for i in range(rank, len(rows)) if (rows[i] >> bit) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> bit) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def symplectic(a, b):
    # labels are x1,x2,z1,z2 in bits 0,1,2,3
    ax, az = a & 0b0011, (a >> 2) & 0b0011
    bx, bz = b & 0b0011, (b >> 2) & 0b0011
    return ((ax & bz).bit_count() + (az & bx).bit_count()) % 2


def audit(name, generators):
    label_rank = rank_gf2(generators)
    all_commute = all(symplectic(a, b) == 0 for a in generators for b in generators)
    return {
        "name": name,
        "generator_count": len(generators),
        "logical_pauli_span_rank": label_rank,
        "projective_pauli_basis_size": 1 << label_rank,
        "all_generators_commute": all_commute,
        "full_logical_operator_basis": label_rank == 4,
    }


def main():
    # Z1=0100, Z2=1000, X1=0001, X2=0010.
    cases = [
        audit("local_stabilizers_only", []),
        audit("one_logical_port", [0b0100]),
        audit("two_commuting_loop_ports", [0b0100, 0b1000]),
        audit("full_primal_dual_loop_ports", [0b0100, 0b1000, 0b0001, 0b0010]),
    ]
    by_name = {case["name"]: case for case in cases}
    assert by_name["local_stabilizers_only"]["projective_pauli_basis_size"] == 1
    assert by_name["one_logical_port"]["projective_pauli_basis_size"] == 2
    assert by_name["two_commuting_loop_ports"]["projective_pauli_basis_size"] == 4
    assert by_name["two_commuting_loop_ports"]["all_generators_commute"]
    assert by_name["full_primal_dual_loop_ports"]["projective_pauli_basis_size"] == 16
    assert not by_name["full_primal_dual_loop_ports"]["all_generators_commute"]
    assert by_name["full_primal_dual_loop_ports"]["full_logical_operator_basis"]
    print(
        json.dumps(
            {
                "schema": "marici.accessible-readout-algebra.v1",
                "logical_qubits": 2,
                "cases": cases,
                "gates": {
                    "one_port_only_detects_one_binary_grade": True,
                    "commuting_ports_separate_a_basis_but_not_coherences": True,
                    "full_primal_dual_ports_generate_operator_basis": True,
                },
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
