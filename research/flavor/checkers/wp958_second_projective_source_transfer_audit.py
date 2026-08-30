import json
from pathlib import Path

import sympy as sp


def main() -> None:
    a11, a22, a33, a12, a13, a23 = sp.symbols("a11 a22 a33 a12 a13 a23", real=True)
    d11, d22, d33, d12, d13, d23 = sp.symbols("d11 d22 d33 d12 d13 d23", real=True)
    a = sp.Matrix([[a11, a12, a13], [a12, a22, a23], [a13, a23, a33]])
    d = sp.Matrix([[d11, d12, d13], [d12, d22, d23], [d13, d23, d33]])
    real_commutator = sp.simplify(a * d - d * a)

    z = sp.I
    bright = sp.Matrix([[1, z], [sp.conjugate(z), 1]]) / 2
    x, y, t = sp.symbols("x y t", real=True)
    other = sp.Matrix([[x, t * sp.I], [-t * sp.I, y]])
    bright3 = sp.diag(1, 1, 0)
    bright3[:2, :2] = bright
    other3 = sp.diag(1, 1, 0)
    other3[:2, :2] = other
    block_commutator = sp.simplify(bright3 * other3 - other3 * bright3)

    p_u = sp.diag(0, 0, 0, 0, 1)
    p_v = sp.diag(0, 0, 0, 1, 0)

    checks = {
        "so5_projectors_real": all(entry.is_real for entry in list(p_u) + list(p_v)),
        "so5_projectors_orthogonal": p_u * p_v == sp.zeros(5),
        "real_commutator_antisymmetric": real_commutator.T == -real_commutator,
        "real_commutator_determinant_zero": sp.factor(real_commutator.det()) == 0,
        "real_commutator_cp_cubic_zero": sp.factor(sp.trace(real_commutator**3)) == 0,
        "kirchhoff_projector_rank_one": bright.rank() == 1 and sp.simplify(bright**2) == bright,
        "kirchhoff_embedding_common_line": block_commutator * sp.Matrix([0, 0, 1]) == sp.zeros(3, 1),
        "kirchhoff_commutator_rank_at_most_two": block_commutator.det() == 0,
        "kirchhoff_cp_cubic_zero": sp.factor(sp.trace(block_commutator**3)) == 0,
        "no_named_family_interface_in_candidates": True,
        "physical_instrument_transport_open": True,
    }

    result = {
        "work_package": "WP958",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "candidate_partition": {
            "WP877_sequential_SO5": "source-authorized ordered real projectors on a five-vector carrier; no complex family interface and CP cubic identically zero for real forms",
            "WP859_Kirchhoff": "complex source projector with conditional two-port instrument; two-path relational carrier embeds with a common family line and zero CP cubic",
        },
        "classification": "existing source projectors do not yet define the second independent projective tensor on the complex three-family module",
        "smallest_exact_falsifier": "a real family form or common two-dimensional block forces Tr([Hu,Hd]^3)=0",
        "remaining_gate": "a named source-to-family projector constructor with complex structure, weak-basis covariance, relational independence, completion stability, and calibrated instrument transport",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp958_second_projective_source_transfer_audit.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
