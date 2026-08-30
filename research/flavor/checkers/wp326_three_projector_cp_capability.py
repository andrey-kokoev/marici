"""WP326: exact three-projector capability witness for generic flavor and CP."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def cp_trace(yukawa_up, yukawa_down):
    hu = sp.simplify(yukawa_up * yukawa_up.conjugate().T)
    hd = sp.simplify(yukawa_down * yukawa_down.conjugate().T)
    commutator = sp.simplify(hu * hd - hd * hu)
    return sp.simplify(sp.trace(commutator**3)), commutator


def main():
    identity = sp.eye(3)
    p = sp.diag(1, 0, 0)
    q = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [0, 0, 0]])
    vector_r = sp.Matrix([1, sp.I, 1])
    r = sp.simplify(vector_r * vector_r.conjugate().T / 3)
    spanning_vectors = sp.Matrix.hstack(sp.Matrix([1, 0, 0]), sp.Matrix([1, 1, 0]), vector_r)
    yukawa_up = identity + p + 2 * q + 3 * r
    yukawa_down = 2 * identity + 4 * p + q + 5 * r
    cp_odd, commutator = cp_trace(yukawa_up, yukawa_down)
    conjugate_cp_odd, _ = cp_trace(yukawa_up.conjugate(), yukawa_down.conjugate())
    up_charpoly = sp.factor(yukawa_up.charpoly().as_expr())
    down_charpoly = sp.factor(yukawa_down.charpoly().as_expr())
    up_discriminant = sp.factor(sp.discriminant(up_charpoly))
    down_discriminant = sp.factor(sp.discriminant(down_charpoly))
    checks = {
        "all_three_objects_are_rank_one_projectors": all(x.rank() == 1 and x**2 == x for x in (p, q, r)),
        "projector_rays_span_three_dimensions": spanning_vectors.rank() == 3,
        "no_common_annihilated_line_exists": spanning_vectors.det() != 0,
        "up_spectrum_is_nondegenerate": up_discriminant != 0,
        "down_spectrum_is_nondegenerate": down_discriminant != 0,
        "sector_commutator_is_nonsingular": commutator.det() != 0,
        "cp_odd_invariant_is_nonzero": cp_odd == -10900883 * sp.I,
        "complex_conjugation_flips_cp_sign": conjugate_cp_odd == -cp_odd,
        "cp_even_characteristic_polynomials_survive_conjugation": yukawa_up.conjugate().charpoly().as_expr() == yukawa_up.charpoly().as_expr() and yukawa_down.conjugate().charpoly().as_expr() == yukawa_down.charpoly().as_expr(),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP326",
        "admitted_state_domain": "three rank-one relational projectors with rays e1, (1,1,0), and (1,i,1), plus fixed affine sector lifts",
        "faithful_quotient_coordinate": "nondegenerate sector spectra and the CP-odd invariant Tr([H_u,H_d]^3) on a generic physical16 stratum",
        "source_operation": "conditional selection of three spanning projectors followed by Y_u=I+P+2Q+3R and Y_d=2I+4P+Q+5R",
        "up_characteristic_polynomial": str(up_charpoly),
        "down_characteristic_polynomial": str(down_charpoly),
        "up_discriminant": str(up_discriminant),
        "down_discriminant": str(down_discriminant),
        "commutator_determinant": str(sp.factor(commutator.det())),
        "cp_odd_trace_commutator_cubed": str(cp_odd),
        "conjugate_cp_odd_value": str(conjugate_cp_odd),
        "contextual_partition": "the three rays span the full space and remove the common-line kernel; complex-conjugate source packets retain CP-even spectra but occupy opposite CP branches",
        "classification": "three complex relational projectors have generic physical16 and CP capability, but this witness is not a selector prediction because its rays and affine coefficients are stipulated",
        "smallest_exact_falsifier": "complex conjugation preserves both sector characteristic polynomials and flips the nonzero CP-odd invariant, so CP-even source data cannot select the CP orientation",
        "remaining_physical_instrument_gate": "derive all three projector rays, their complex orientation, and affine coefficients from an admitted source action, then implement a calibrated CP-sensitive readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp326_three_projector_cp_capability.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
