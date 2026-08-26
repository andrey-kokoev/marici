"""WP324: exact no-go for the minimal affine flavor lift of WP323 projectors."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    a_u, b_u, a_d, b_d = sp.symbols("a_u b_u a_d b_d", real=True)
    identity = sp.eye(3)
    projector = sp.diag(1, 0, 0)
    yukawa_up = a_u * identity + b_u * projector
    yukawa_down = a_d * identity + b_d * projector
    hu = sp.simplify(yukawa_up * yukawa_up.T)
    hd = sp.simplify(yukawa_down * yukawa_down.T)
    commutator = sp.simplify(hu * hd - hd * hu)
    up_characteristic = sp.factor(yukawa_up.charpoly().as_expr())
    down_characteristic = sp.factor(yukawa_down.charpoly().as_expr())
    discriminant_up = sp.factor(sp.discriminant(up_characteristic))
    discriminant_down = sp.factor(sp.discriminant(down_characteristic))
    spectral_parameter = sp.Symbol("lambda")
    checks = {
        "projector_is_rank_one": projector.rank() == 1,
        "up_characteristic_has_double_root": sp.simplify(up_characteristic - (spectral_parameter - a_u)**2 * (spectral_parameter - a_u - b_u)) == 0,
        "down_characteristic_has_double_root": sp.simplify(down_characteristic - (spectral_parameter - a_d)**2 * (spectral_parameter - a_d - b_d)) == 0,
        "up_discriminant_vanishes_identically": discriminant_up == 0,
        "down_discriminant_vanishes_identically": discriminant_down == 0,
        "sector_hermitians_commute_identically": commutator == sp.zeros(3),
        "minimal_lift_has_no_generic_mixing": hu.is_diagonal() and hd.is_diagonal(),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP324",
        "admitted_state_domain": "WP323 rank-one selected projector B and the minimal equivariant affine lifts Y_u=a_u I+b_u B, Y_d=a_d I+b_d B",
        "faithful_quotient_coordinate": "ordered Yukawa singular spectra and relative mixing on physical16; the affine image lies on its degenerate boundary",
        "source_operation": "conditional spectral-projector selection followed by the most economical polynomial flavor matching linear in I and B",
        "up_characteristic_polynomial": str(up_characteristic),
        "down_characteristic_polynomial": str(down_characteristic),
        "up_discriminant": str(discriminant_up),
        "down_discriminant": str(discriminant_down),
        "commutator": [[str(value) for value in row] for row in commutator.tolist()],
        "contextual_partition": "all coefficient choices retain a twofold eigenvalue degeneracy in each sector and zero relative commutator",
        "classification": "WP323 remains a genuine relational selector, but its minimal affine flavor lift neither reaches the nondegenerate physical16 domain nor produces generic CKM mixing",
        "smallest_exact_falsifier": "the characteristic polynomial of each affine lift contains the squared factor (a-lambda)^2 for every coefficient choice",
        "remaining_physical_instrument_gate": "add independently derived noncommuting source covariants sufficient to split both degenerate planes, then prove stable matching and an executable flavor readout without fitting their coefficients",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp324_projector_flavor_lift_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
