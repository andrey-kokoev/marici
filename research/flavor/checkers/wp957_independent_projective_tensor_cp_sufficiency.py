import json
from pathlib import Path

import sympy as sp


def gram(y: sp.Matrix) -> sp.Matrix:
    return sp.simplify(y * y.conjugate().T)


def main() -> None:
    identity = sp.eye(3)
    p = sp.diag(1, 0, 0)
    q = sp.Matrix([
        [sp.Rational(1, 2), sp.Rational(1, 2), 0],
        [sp.Rational(1, 2), sp.Rational(1, 2), 0],
        [0, 0, 0],
    ])
    vector_r = sp.Matrix([1, sp.I, 1])
    r = sp.simplify(vector_r * vector_r.conjugate().T / 3)
    b = sp.simplify(p - q)
    b_squared = sp.simplify(b**2)

    w = sp.Matrix([1, 2, sp.I])
    w_projector = sp.simplify(w * w.conjugate().T / (w.conjugate().T * w)[0])

    yukawa_up = sp.simplify(identity + p + q + r)
    yukawa_down = sp.simplify(2 * identity + b_squared + w_projector)
    yukawa_down_control = sp.simplify(2 * identity + b_squared + r)

    hu = gram(yukawa_up)
    hd = gram(yukawa_down)
    hd_control = gram(yukawa_down_control)
    commutator = sp.simplify(hu * hd - hd * hu)
    commutator_control = sp.simplify(hu * hd_control - hd_control * hu)

    down_discriminant = sp.factor(sp.discriminant(yukawa_down.charpoly().as_expr()))
    control_discriminant = sp.factor(sp.discriminant(yukawa_down_control.charpoly().as_expr()))
    cp_cubic = sp.factor(sp.trace(commutator**3))
    control_cp_cubic = sp.factor(sp.trace(commutator_control**3))

    scaled_w = (3 + 2 * sp.I) * w
    scaled_projector = sp.simplify(
        scaled_w * scaled_w.conjugate().T / (scaled_w.conjugate().T * scaled_w)[0]
    )

    checks = {
        "b_square_sign_blind": (-b) ** 2 == b_squared,
        "w_is_rank_one_projector": w_projector.rank() == 1 and sp.simplify(w_projector**2) == w_projector,
        "w_projector_ray_invariant": scaled_projector == w_projector,
        "down_spectrum_simple": down_discriminant == sp.Rational(575, 1728),
        "gram_commutator_rank_three": commutator.rank() == 3,
        "cp_cubic_nonzero": cp_cubic == -sp.Rational(12866425, 3456) * sp.I,
        "reused_r_control_spectrum_simple": control_discriminant == sp.Rational(19, 108),
        "reused_r_control_cp_zero": control_cp_cubic == 0,
        "spectral_splitting_not_sufficient": control_discriminant != 0 and control_cp_cubic == 0,
        "algebraic_projective_repair_exists": down_discriminant != 0 and cp_cubic != 0,
        "source_authority_remains_open": True,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP957",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_witness": {
            "w": [str(entry) for entry in w],
            "down_discriminant": str(down_discriminant),
            "gram_commutator_rank": commutator.rank(),
            "cp_cubic": str(cp_cubic),
        },
        "hostile_control": {
            "second_tensor": "R reused from up operator",
            "down_discriminant": str(control_discriminant),
            "cp_cubic": str(control_cp_cubic),
        },
        "classification": "a second independent projective tensor is algebraically sufficient for simple spectrum and nonzero three-family CP, but is not yet source-authorized",
        "smallest_exact_falsifier": "reusing R gives simple down spectrum with zero CP cubic",
        "remaining_gate": "derive the second projective tensor from an admitted source rule independently of flavor readout, then test completion, descent, and instrument authority",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp957_independent_projective_tensor_cp_sufficiency.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
