"""WP295: exact physical16 kernel remaining after full signed-J readout."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def ckm_packet(s12, c12):
    s23, c23 = sp.Rational(5, 13), sp.Rational(12, 13)
    s13, c13 = sp.Rational(5, 13), sp.Rational(12, 13)
    matrix = sp.Matrix(
        [
            [c12 * c13, s12 * c13, -sp.I * s13],
            [-s12 * c23 - sp.I * c12 * s23 * s13, c12 * c23 - sp.I * s12 * s23 * s13, s23 * c13],
            [s12 * s23 - sp.I * c12 * c23 * s13, -c12 * s23 - sp.I * s12 * c23 * s13, c23 * c13],
        ]
    )
    squared_moduli = [sp.simplify(sp.expand_complex(value * sp.conjugate(value))) for value in matrix]
    signed_j = sp.simplify(c12 * c23 * c13**2 * s12 * s23 * s13)
    masses = [sp.Rational(value) for value in (1, 2, 3, 5, 7, 11)]
    return matrix, squared_moduli, signed_j, masses + squared_moduli + [signed_j]


def main():
    first = ckm_packet(sp.Rational(3, 5), sp.Rational(4, 5))
    second = ckm_packet(sp.Rational(4, 5), sp.Rational(3, 5))
    first_matrix, first_moduli, first_j, first_physical = first
    second_matrix, second_moduli, second_j, second_physical = second
    difference = [sp.simplify(a - b) for a, b in zip(first_physical, second_physical)]

    checks = {
        "first_matrix_is_exactly_unitary": sp.simplify(first_matrix * first_matrix.conjugate().T) == sp.eye(3),
        "second_matrix_is_exactly_unitary": sp.simplify(second_matrix * second_matrix.conjugate().T) == sp.eye(3),
        "ordered_masses_are_identical": first_physical[:6] == second_physical[:6],
        "signed_j_readouts_are_exactly_equal": first_j == second_j,
        "shared_signed_j_is_nonzero_positive": first_j > 0,
        "ckm_modulus_packets_are_distinct": first_moduli != second_moduli,
        "physical16_embeddings_are_distinct": any(value != 0 for value in difference),
        "sign_plus_magnitude_readout_collapses_pair": (sp.sign(first_j), abs(first_j)) == (sp.sign(second_j), abs(second_j)),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP295",
        "admitted_state_domain": "nondegenerate ordered quark masses and exact unitary CKM matrices at fixed positive signed J",
        "faithful_quotient_coordinate": "physical16, represented exactly by six masses, nine squared CKM moduli, and signed J",
        "probe_family": "binary CP branch plus exact J magnitude, equivalently full signed-J readout",
        "shared_signed_j": str(first_j),
        "hostile_pair": {
            "first_physical16_squared_embedding": [str(value) for value in first_physical],
            "second_physical16_squared_embedding": [str(value) for value in second_physical],
            "difference": [str(value) for value in difference],
        },
        "contextual_partition": "full signed-J probes place physically inequivalent packets with different CP-even CKM moduli in one class",
        "descent": "signed J is a declared weak-basis invariant and descends to physical16",
        "classification": "CP-odd scalar readout and possible orientation selector; neither a faithful physical16 separator nor a point selector",
        "smallest_exact_falsifier": "interchanging s12=3/5,c12=4/5 with s12=4/5,c12=3/5 preserves their product and signed J but changes CKM moduli",
        "first_nonfaithful_arrow": "physical16 -> signed J",
        "remaining_physical_instrument_gate": "derive source-authorized CP-even operations that constrain masses and CKM moduli, rather than inferring them from the selected CP branch",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp295_signed_j_physical16_kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
