"""WP311: exact left-right representation completion and vacuum-selector gate."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def hierarchy(diagonal_matrix):
    diagonal = list(diagonal_matrix.diagonal())
    return sp.simplify(diagonal[-1] / diagonal[0])


def main():
    t3_right = sp.diag(sp.Rational(1, 2), sp.Rational(-1, 2))
    half_b_minus_l = sp.eye(2) * sp.Rational(1, 6)
    hypercharge = t3_right + half_b_minus_l
    weyl = sp.Matrix([[0, 1], [-1, 0]])
    conjugated_t3 = sp.simplify(weyl * t3_right * weyl.inv())
    conjugated_hypercharge = sp.simplify(weyl * hypercharge * weyl.inv())

    yukawa_y = sp.diag(1, 2, 4)
    yukawa_z = sp.diag(1, 3, 9)
    vev_one, vev_two = sp.Rational(2), sp.Rational(1)
    mass_up = vev_one * yukawa_y + vev_two * yukawa_z
    mass_down = vev_two * yukawa_y + vev_one * yukawa_z
    exchanged_mass_up = vev_two * yukawa_y + vev_one * yukawa_z
    exchanged_mass_down = vev_one * yukawa_y + vev_two * yukawa_z
    hierarchy_ratio = sp.simplify(hierarchy(mass_up) / hierarchy(mass_down))

    symmetric_vev = sp.Rational(1)
    symmetric_up = symmetric_vev * yukawa_y + symmetric_vev * yukawa_z
    symmetric_down = symmetric_vev * yukawa_y + symmetric_vev * yukawa_z

    checks = {
        "hypercharge_embedding_recovers_up_and_down_values": list(hypercharge.diagonal()) == [sp.Rational(2, 3), sp.Rational(-1, 3)],
        "weyl_conjugation_flips_t3_right": conjugated_t3 == -t3_right,
        "weyl_square_is_central_minus_identity": weyl**2 == -sp.eye(2),
        "weyl_conjugation_swaps_hypercharge_eigenvalues": list(conjugated_hypercharge.diagonal()) == [sp.Rational(-1, 3), sp.Rational(2, 3)],
        "matching_is_equivariant_under_vev_exchange": exchanged_mass_up == mass_down and exchanged_mass_down == mass_up,
        "generic_breaking_vacuum_has_unequal_hierarchies": hierarchy_ratio == sp.Rational(17, 22) and hierarchy_ratio != 1,
        "symmetric_breaking_vacuum_gives_equal_mass_packets": symmetric_up == symmetric_down,
        "symmetric_breaking_vacuum_gives_equal_hierarchy_ratio": hierarchy(symmetric_up) / hierarchy(symmetric_down) == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP311",
        "source_extension": "right-handed SU(2)_R doublet with Y=T3_R+(B-L)/2 and B-L=1/3 for quarks",
        "representation_repair": {
            "T3_R": [[str(value) for value in t3_right.row(i)] for i in range(2)],
            "half_B_minus_L": "1/6",
            "hypercharge_eigenvalues": [str(value) for value in hypercharge.diagonal()],
            "weyl_action_is_legal_upstream": True,
        },
        "equivariant_matching": "M_u=v1*Y+v2*Z, M_d=v2*Y+v1*Z",
        "generic_vacuum_packet": {
            "v1": str(vev_one),
            "v2": str(vev_two),
            "M_u_diagonal": [str(value) for value in mass_up.diagonal()],
            "M_d_diagonal": [str(value) for value in mass_down.diagonal()],
            "hierarchy_ratio": str(hierarchy_ratio),
        },
        "fixed_vacuum_condition": "v1=v2 makes M_u=M_d and realizes the reciprocal fixed locus",
        "descent": "the exchange is legal in the enlarged unbroken source, but matching to Standard Model hypercharge requires a breaking vacuum whose orbit and selection must be declared",
        "classification": "representation completion and equivariant source architecture; not yet a numerical hierarchy selector because generic symmetry-breaking vacua leave r!=1",
        "smallest_exact_falsifier": "with v1=2,v2=1, Y=diag(1,2,4), and Z=diag(1,3,9), the legal equivariant matching gives hierarchy ratio 17/22",
        "remaining_physical_instrument_gate": "derive a stable source potential selecting the v1=v2 orbit without answer-coded coefficients, then obtain realistic gauge breaking, anomalies, thresholds, CKM mixing, and calibrated physical16 readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp311_left_right_exchange_completion.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
