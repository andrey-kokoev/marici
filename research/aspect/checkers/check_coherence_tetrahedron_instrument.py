from __future__ import annotations

import json
from pathlib import Path

from sympy import I, Matrix, Rational, symbols, simplify


def main() -> None:
    # Four oriented analytical ports sewn into the Clark pair E, E*.
    X, Xp = symbols("X Xp", complex=True)
    sewing = I * Matrix([[-1, 1, 1, 1], [-1, 1, -1, -1]]) / 2
    oriented = Matrix([I * X, -I * X, Xp, Xp])
    clark = sewing * oriented
    assert simplify(clark[0] - (X + I * Xp)) == 0
    assert simplify(clark[1] - (X - I * Xp)) == 0

    # Canonical Stokes face is a calibrated dark port, not an Xi detector.
    R, E, eps = symbols("R E eps")
    canonical_ports = Matrix([-R, -2 * E, R + 2 * E])
    canonical_dark = simplify(sum(canonical_ports))
    assert canonical_dark == 0
    perturbed_dark = simplify(sum(canonical_ports + Matrix([eps, 0, 0])))
    assert perturbed_dark == eps

    # Minimal finite Grushin augmentation removes one permanent kernel line.
    D = Matrix.diag(0, 2, 3)
    psi = Matrix([1, 0, 0])
    ell = Matrix([[1, 0, 0]])
    v = psi
    grushin = D.row_join(v).col_join(ell.row_join(Matrix([[0]])))
    assert D.det() == 0
    assert grushin.det() == -6
    assert (ell * psi)[0] == 1

    # Passive finite Douglas emulator and one deliberate nonpassive hostile.
    contraction = Matrix.diag(Rational(3, 5), Rational(4, 5))
    defect = Matrix.eye(2) - contraction.T * contraction
    assert defect == Matrix.diag(Rational(16, 25), Rational(9, 25))
    hostile = Matrix.diag(Rational(6, 5), Rational(4, 5))
    hostile_defect = Matrix.eye(2) - hostile.T * hostile
    assert hostile_defect[0, 0] == Rational(-11, 25)

    result = {
        "schema": "marici.aspect.coherence-tetrahedron-instrument.v1",
        "status": "pass",
        "instrument": {
            "oriented_inputs": ["M0+", "M0-", "M1+", "M1-"],
            "sewing_matrix": "(i/2)*[[-1,1,1,1],[-1,1,-1,-1]]",
            "coherent_outputs": ["E=X+iXprime", "Estar=X-iXprime"],
        },
        "canonical_dark_port": {
            "ports": ["-R", "-2E", "R+2E"],
            "ideal_residual": "0",
            "single_port_calibration_error": "epsilon",
            "xi_detector": False,
        },
        "grushin_fixture": {
            "D_diagonal": [0, 2, 3],
            "unreduced_determinant": "0",
            "augmented_determinant": "-6",
            "normalization": "ell(Psi)=1",
        },
        "douglas_fixture": {
            "passive_singular_values": ["3/5", "4/5"],
            "defect_diagonal": ["16/25", "9/25"],
            "hostile_singular_values": ["6/5", "4/5"],
            "hostile_negative_defect": "-11/25",
        },
        "transverse_evans_import": {
            "first_zero_ordinate": "14.13472514173469379045725198356247",
            "reported_residual": "-0.150851219058739200687179708292",
            "interval_certified": False,
            "used_as_exact_checker_input": False,
        },
        "checks": {
            "clark_sewing_exact": True,
            "canonical_dark_port_exact": True,
            "calibration_leakage_exposed": True,
            "grushin_removes_fixture_kernel": True,
            "passive_douglas_network": True,
            "nonpassive_hostile_rejected": True,
        },
        "claim_boundary": "Exact finite symbolic instrument fixture. It does not realize the global coherence pyramid, certify the transverse Evans integral, prove Hardy positivity, identify a reduced determinant with Xi, or imply RH.",
    }
    out = Path(__file__).parents[1] / "results" / "coherence_tetrahedron_instrument.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
