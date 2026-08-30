import json
from pathlib import Path

import sympy as sp


def main() -> None:
    identity = sp.eye(3)
    p = sp.diag(1, 1, -1)
    v = sp.Matrix([1, 2, 2]) / 3
    q = sp.simplify(identity - 2 * v * v.T)
    commutator = sp.simplify(p * q - q * p)

    hu = 3 * identity + p
    hd = 4 * identity + 2 * q
    gram_commutator = sp.simplify(hu * hd - hd * hu)
    hu_minors = [hu[:n, :n].det() for n in (1, 2, 3)]
    hd_minors = [sp.simplify(hd[:n, :n].det()) for n in (1, 2, 3)]
    kernel = commutator.nullspace()

    checks = {
        "p_hermitian": p == p.conjugate().T,
        "q_hermitian": q == q.conjugate().T,
        "p_involution": p**2 == identity,
        "q_involution": sp.simplify(q**2) == identity,
        "source_decompositions_noncommuting": commutator != sp.zeros(3),
        "commutator_rank_two": commutator.rank() == 2,
        "commutator_has_common_kernel_line": len(kernel) == 1 and kernel[0] == sp.Matrix([-2, 1, 0]),
        "involution_commutator_cubic_zero": sp.trace(commutator**3) == 0,
        "up_gram_positive": hu_minors == [4, 16, 32],
        "down_gram_positive": hd_minors == [sp.Rational(50, 9), sp.Rational(68, 3), 72],
        "gram_pair_noncommuting": gram_commutator.rank() == 2,
        "gram_cp_cubic_zero": sp.trace(gram_commutator**3) == 0,
        "each_involution_has_only_two_eigenvalues": len(p.eigenvals()) == len(q.eigenvals()) == 2,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP952",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_witness": {
            "q": str(q.tolist()),
            "commutator_rank": commutator.rank(),
            "commutator_kernel_generator": [str(value) for value in kernel[0]],
            "involution_cp_cubic": str(sp.trace(commutator**3)),
            "gram_cp_cubic": str(sp.trace(gram_commutator**3)),
            "up_gram_leading_principal_minors": [str(value) for value in hu_minors],
            "down_gram_leading_principal_minors": [str(value) for value in hd_minors],
        },
        "classification": "two source involutions can force a mixing plane but retain a common line, two-level degeneracy, and zero three-family CP cubic",
        "smallest_exact_falsifier": "noncommuting rank-two involution commutator has kernel (-2,1,0) and cubic trace 0",
        "remaining_gate": "at least three source-related decompositions or a simple-spectrum operator with independently fixed noncommuting partner and calibrated instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp952_two_boundary_involutions_cp_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
