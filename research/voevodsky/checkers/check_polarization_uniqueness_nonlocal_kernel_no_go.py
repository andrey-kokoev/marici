from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/polarization-uniqueness-nonlocal-kernel-no-go-v1.json")


def quadratic(matrix: sp.Matrix, vector: sp.Matrix) -> sp.Expr:
    return sp.expand((sp.conjugate(vector).T * matrix * vector)[0])


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    # Polarization recovers every matrix coefficient from quadratic values.
    H = sp.Matrix([[2, 1 + sp.I], [1 - sp.I, 3]])
    f = sp.Matrix([1 + 2 * sp.I, 2 - sp.I])
    g = sp.Matrix([3 - sp.I, -1 + sp.I])
    recovered = sum(
        sp.I**k * quadratic(H, f + sp.I**k * g)
        for k in range(4)
    ) / 4
    expected = (sp.conjugate(f).T * H * g)[0]
    # This convention recovers <g,Hf>; compare its conjugate orientation explicitly.
    assert sp.simplify(recovered - sp.conjugate(expected)) == 0

    # An indefinite full-space form cannot equal R*R.
    D = sp.diag(1, -1, 2)
    negative_vector = sp.Matrix([0, 1, 0])
    assert quadratic(D, negative_vector) == -1

    # Restriction can remove the negative direction: B* D B is positive.
    B = sp.Matrix([[1, 0], [0, 0], [0, 1]])
    compressed = B.T * D * B
    assert compressed == sp.diag(1, 2)
    assert compressed.is_positive_definite
    assert B.rank() < D.rows

    # A restriction that still reaches the negative coordinate fails.
    bad_B = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    bad_compressed = bad_B.T * D * bad_B
    assert bad_compressed.det() < 0

    result = {
        "schema":"marici.voevodsky.polarization-uniqueness-nonlocal-kernel-no-go-check.v1",
        "status":"polarization_and_compression_no_go_verified",
        "polarization_recovery":True,
        "full_space_indefinite_no_positive_factor":True,
        "proper_restriction_positive_fixture":True,
        "restriction_reaching_negative_direction_fails":True,
        "weil_form_core_faithfulness":False,
        "positive_source_compression":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
