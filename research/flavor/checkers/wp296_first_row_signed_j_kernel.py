"""WP296: exact physical16 kernel after first-row CKM plus signed-J probes."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def ckm_packet(s23, c23):
    s12, c12 = sp.Rational(3, 5), sp.Rational(4, 5)
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
    readout = masses + squared_moduli[:3] + [signed_j]
    physical = masses + squared_moduli + [signed_j]
    return matrix, squared_moduli, signed_j, readout, physical


def main():
    first = ckm_packet(sp.Rational(5, 13), sp.Rational(12, 13))
    second = ckm_packet(sp.Rational(12, 13), sp.Rational(5, 13))
    first_matrix, first_moduli, first_j, first_readout, first_physical = first
    second_matrix, second_moduli, second_j, second_readout, second_physical = second
    difference = [sp.simplify(a - b) for a, b in zip(first_physical, second_physical)]

    checks = {
        "first_ckm_is_exactly_unitary": sp.simplify(first_matrix * first_matrix.conjugate().T) == sp.eye(3),
        "second_ckm_is_exactly_unitary": sp.simplify(second_matrix * second_matrix.conjugate().T) == sp.eye(3),
        "six_masses_first_row_and_signed_j_match": first_readout == second_readout,
        "full_physical16_embeddings_differ": any(value != 0 for value in difference),
        "lower_two_ckm_rows_differ": first_moduli[3:] != second_moduli[3:],
        "signed_j_is_nonzero": first_j == second_j and first_j > 0,
        "row_and_column_normalization_hold": all(
            sum(moduli[3 * row : 3 * row + 3]) == 1 and sum(moduli[row::3]) == 1
            for moduli in (first_moduli, second_moduli)
            for row in range(3)
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP296",
        "admitted_state_domain": "nondegenerate ordered masses and exact unitary CKM packets at fixed first row and signed J",
        "faithful_quotient_coordinate": "physical16 represented by six masses, nine squared CKM moduli, and signed J",
        "probe_family": "six ordered masses, complete first-row CKM moduli, and signed J",
        "shared_probe_readout": [str(value) for value in first_readout],
        "hostile_pair": {
            "first_physical16_squared_embedding": [str(value) for value in first_physical],
            "second_physical16_squared_embedding": [str(value) for value in second_physical],
            "difference": [str(value) for value in difference],
        },
        "contextual_partition": "mass, first-row, and signed-J probes collapse packets related by exchanging s23 and c23 while the remaining CKM moduli separate them",
        "descent": "all admitted readouts are weak-basis invariants after ordered mass conventions",
        "classification": "physical readout family and partial separator; neither selector nor rigidifier, and nonfaithful on physical16",
        "smallest_exact_falsifier": "s23=5/13,c23=12/13 and its interchange preserve the first row and signed J but change the lower CKM rows",
        "first_nonfaithful_arrow": "physical16 -> (six masses, first-row moduli, signed J)",
        "remaining_physical_instrument_gate": "add independently calibrated lower-row or lower-column probes and distinguish their readout role from a source operation that would actually select their values",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp296_first_row_signed_j_kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
