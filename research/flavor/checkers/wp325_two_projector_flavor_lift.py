"""WP325: exact capability and residual no-go for a two-projector flavor lift."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    identity = sp.eye(3)
    p = sp.diag(1, 0, 0)
    q = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [0, 0, 0]])
    common_line = sp.Matrix([0, 0, 1])
    yukawa_up = identity + p + 2 * q
    yukawa_down = 2 * identity + 3 * p + q
    hu = sp.simplify(yukawa_up * yukawa_up.T)
    hd = sp.simplify(yukawa_down * yukawa_down.T)
    commutator = sp.simplify(hu * hd - hd * hu)
    cp_odd = sp.simplify(sp.trace(commutator**3))
    up_charpoly = sp.factor(yukawa_up.charpoly().as_expr())
    down_charpoly = sp.factor(yukawa_down.charpoly().as_expr())
    up_discriminant = sp.factor(sp.discriminant(up_charpoly))
    down_discriminant = sp.factor(sp.discriminant(down_charpoly))
    checks = {
        "p_is_rank_one_projector": p.rank() == 1 and p**2 == p,
        "q_is_rank_one_projector": q.rank() == 1 and q**2 == q,
        "projectors_do_not_commute": p * q != q * p,
        "both_projectors_annihilate_common_line": p * common_line == sp.zeros(3, 1) and q * common_line == sp.zeros(3, 1),
        "up_spectrum_is_nondegenerate": up_discriminant != 0,
        "down_spectrum_is_nondegenerate": down_discriminant != 0,
        "sector_hermitians_do_not_commute": commutator != sp.zeros(3),
        "three_family_cp_odd_invariant_vanishes": cp_odd == 0,
        "common_line_remains_sector_eigenvector": hu * common_line == common_line and hd * common_line == 4 * common_line,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP325",
        "admitted_state_domain": "two nonorthogonal rank-one relational projectors P,Q in three dimensions and affine sector lifts in span{I,P,Q}",
        "faithful_quotient_coordinate": "nondegenerate sector spectra plus relative mixing invariants; the example reaches a two-family stratum but not generic CP-violating physical16",
        "source_operation": "conditional selection of P and Q followed by fixed affine Yukawa lifts Y_u=I+P+2Q and Y_d=2I+3P+Q",
        "up_characteristic_polynomial": str(up_charpoly),
        "down_characteristic_polynomial": str(down_charpoly),
        "up_discriminant": str(up_discriminant),
        "down_discriminant": str(down_discriminant),
        "commutator": [[str(value) for value in row] for row in commutator.tolist()],
        "cp_odd_trace_commutator_cubed": str(cp_odd),
        "contextual_partition": "P and Q generate a noncommuting two-dimensional block and leave their common orthogonal line invariant",
        "classification": "two projectors repair spectral degeneracy and generate two-family mixing, but cannot generate generic three-family CP violation; selector authority also remains conditional on their source and coefficients",
        "smallest_exact_falsifier": "the nonzero vector (0,0,1) is annihilated by both projectors, so it is a common eigenvector of every affine lift and Tr([H_u,H_d]^3)=0",
        "remaining_physical_instrument_gate": "derive at least one further covariant that breaks the common invariant line, together with source-fixed coefficients, stable matching, and a typed CP-sensitive instrument",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp325_two_projector_flavor_lift.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
